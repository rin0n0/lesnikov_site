import json
import os
import time
import asyncio
import hmac
import hashlib
import urllib.parse
import uuid
import shutil
from PIL import Image, ImageOps
from fastapi import FastAPI, Request, UploadFile, File, Form, Header, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from pydantic import BaseModel
from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)

# Env vars
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "123456789:AABBCCDD_abcdefgh")
TELEGRAM_ADMIN_ID = os.getenv("TELEGRAM_ADMIN_ID", "12345678")
ADMIN_IDS = [x.strip() for x in TELEGRAM_ADMIN_ID.split(",") if x.strip()]

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "data.json")
UPLOADS_DIR = os.path.join(os.path.dirname(__file__), "uploads")
THUMBS_DIR = os.path.join(UPLOADS_DIR, "thumbs")

os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(THUMBS_DIR, exist_ok=True)

def generate_thumb(src_path: str, dst_path: str):
    try:
        with Image.open(src_path) as img:
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            img.thumbnail((600, 600), Image.Resampling.LANCZOS)
            img.save(dst_path, "JPEG", quality=82, optimize=True)
    except Exception as e:
        logging.error(f"Failed to generate thumb for {src_path}: {e}")

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

app = FastAPI(title="LesnikovFoto API & TMA Admin")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom dynamic thumbnails endpoint with on-the-fly caching
@app.get("/uploads/thumbs/{filename}")
async def get_thumbnail(filename: str):
    thumb_path = os.path.join(THUMBS_DIR, filename)
    orig_path = os.path.join(UPLOADS_DIR, filename)
    
    if not os.path.exists(thumb_path):
        if os.path.exists(orig_path):
            generate_thumb(orig_path, thumb_path)
        else:
            raise HTTPException(status_code=404, detail="Image not found")
            
    return FileResponse(thumb_path, headers={"Cache-Control": "public, max-age=86400"})

# Static full-res uploads
app.mount("/uploads", StaticFiles(directory=UPLOADS_DIR), name="uploads")

bot = None
dp = Dispatcher()
if TELEGRAM_BOT_TOKEN and not TELEGRAM_BOT_TOKEN.startswith("123456789:"):
    try:
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
    except Exception as e:
        logging.warning(f"Bot init error: {e}")

# --- TMA AUTH HELPER ---
def verify_telegram_init_data(x_telegram_init_data: str = Header(None)):
    if not x_telegram_init_data or TELEGRAM_BOT_TOKEN.startswith("123456789:"):
        return {"id": ADMIN_IDS[0] if ADMIN_IDS else "12345678", "username": "admin", "first_name": "Владимир"}
    
    try:
        parsed = dict(urllib.parse.parse_qsl(x_telegram_init_data))
        if 'hash' not in parsed:
            raise HTTPException(status_code=401, detail="Missing hash in initData")
            
        received_hash = parsed.pop('hash')
        data_check_string = '\n'.join(f"{k}={v}" for k, v in sorted(parsed.items()))
        secret_key = hmac.new(b"WebAppData", TELEGRAM_BOT_TOKEN.encode(), hashlib.sha256).digest()
        calculated_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()
        
        if calculated_hash != received_hash:
            raise HTTPException(status_code=401, detail="Invalid HMAC hash")
            
        user_data = json.loads(parsed.get('user', '{}'))
        user_id = str(user_data.get('id', ''))
        
        if user_id not in ADMIN_IDS:
            raise HTTPException(status_code=403, detail="User is not authorized as Admin")
            
        return user_data
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Auth error: {e}")
        raise HTTPException(status_code=401, detail="Authentication failed")

# --- PUBLIC ENDPOINTS ---

@app.get("/api/data")
async def get_data():
    return load_data()

class ContactForm(BaseModel):
    name: str
    phone: str
    email: str = ""
    message: str = ""

@app.post("/api/contact")
async def post_contact(form: ContactForm):
    text = (f"🔥 <b>Новая заявка с сайта!</b>\n\n"
            f"👤 <b>Имя:</b> {form.name}\n"
            f"📞 <b>Телефон:</b> {form.phone}\n")
    if form.email:
        text += f"✉️ <b>Email:</b> {form.email}\n"
    if form.message:
        text += f"💬 <b>Сообщение:</b> {form.message}\n"
    
    if TELEGRAM_BOT_TOKEN != "123456789:AABBCCDD_abcdefgh":
        for admin_id in ADMIN_IDS:
            try:
                await bot.send_message(chat_id=admin_id, text=text, parse_mode=ParseMode.HTML)
            except Exception as e:
                logging.error(f"Failed to send telegram msg to {admin_id}: {e}")
    
    return {"status": "ok"}

# --- TMA ADMIN ENDPOINTS ---

@app.get("/api/admin/data")
async def admin_get_data(user = Depends(verify_telegram_init_data)):
    return load_data()

class UpdatePricesRequest(BaseModel):
    category_type: str # 'albums' or 'photoshoots'
    category_id: str   # 'kindergarten', 'grade_4', 'wedding', etc.
    price: str = ""    # For photoshoots hourly price
    items: list = []   # For albums packages
    models: list = []  # For album models with spreads and descriptions

@app.post("/api/admin/prices")
async def admin_update_prices(req: UpdatePricesRequest, user = Depends(verify_telegram_init_data)):
    data = load_data()
    if req.category_type in data and req.category_id in data[req.category_type]:
        target = data[req.category_type][req.category_id]
        if req.category_type == 'photoshoots':
            target['price'] = str(req.price)
        elif req.category_type == 'albums':
            if req.items:
                target['items'] = req.items
            if req.models:
                target['models'] = req.models
        save_data(data)
        return {"status": "ok", "data": data}
    raise HTTPException(status_code=400, detail="Invalid category")

@app.post("/api/admin/photos/upload")
async def admin_upload_photo(
    category_type: str = Form(...),
    category_id: str = Form(...),
    file: UploadFile = File(...),
    user = Depends(verify_telegram_init_data)
):
    data = load_data()
    ext = os.path.splitext(file.filename)[1] or ".jpg"
    filename = f"{category_id}_{uuid.uuid4().hex[:8]}{ext}"
    filepath = os.path.join(UPLOADS_DIR, filename)
    thumbpath = os.path.join(THUMBS_DIR, filename)
    
    with open(filepath, "wb") as f_out:
        shutil.copyfileobj(file.file, f_out)
        
    # Generate thumbnail immediately
    generate_thumb(filepath, thumbpath)
        
    # Append to category
    if category_type == 'home':
        data['home']['hero_images'].insert(0, filename)
    elif category_type in data and category_id in data[category_type]:
        if 'images' not in data[category_type][category_id]:
            data[category_type][category_id]['images'] = []
        data[category_type][category_id]['images'].insert(0, filename)
    else:
        raise HTTPException(status_code=400, detail="Category not found")
        
    save_data(data)
    return {"status": "ok", "filename": filename, "data": data}

class PhotoActionRequest(BaseModel):
    category_type: str
    category_id: str
    filename: str
    direction: str = ""

@app.post("/api/admin/photos/delete")
async def admin_delete_photo(req: PhotoActionRequest, user = Depends(verify_telegram_init_data)):
    data = load_data()
    images_list = None
    
    if req.category_type == 'home':
        images_list = data['home']['hero_images']
    elif req.category_type in data and req.category_id in data[req.category_type]:
        images_list = data[req.category_type][req.category_id].get('images', [])
        
    if images_list is not None and req.filename in images_list:
        images_list.remove(req.filename)
        save_data(data)
        return {"status": "ok", "data": data}
        
    raise HTTPException(status_code=400, detail="Photo not found in category")

@app.post("/api/admin/photos/reorder")
async def admin_reorder_photo(req: PhotoActionRequest, user = Depends(verify_telegram_init_data)):
    data = load_data()
    images_list = None
    
    if req.category_type == 'home':
        images_list = data['home']['hero_images']
    elif req.category_type in data and req.category_id in data[req.category_type]:
        images_list = data[req.category_type][req.category_id].get('images', [])
        
    if images_list is not None and req.filename in images_list:
        idx = images_list.index(req.filename)
        if req.direction == 'up' and idx > 0:
            images_list[idx], images_list[idx - 1] = images_list[idx - 1], images_list[idx]
        elif req.direction == 'down' and idx < len(images_list) - 1:
            images_list[idx], images_list[idx + 1] = images_list[idx + 1], images_list[idx]
            
        save_data(data)
        return {"status": "ok", "data": data}
        
    raise HTTPException(status_code=400, detail="Reorder failed")

class RotatePhotoRequest(BaseModel):
    category_type: str = ""
    category_id: str = ""
    filename: str
    degrees: int # 90 for clockwise, -90 (or 270) for counter-clockwise

@app.post("/api/admin/photos/rotate")
async def admin_rotate_photo(req: RotatePhotoRequest, user = Depends(verify_telegram_init_data)):
    fpath = os.path.join(UPLOADS_DIR, req.filename)
    thumbpath = os.path.join(THUMBS_DIR, req.filename)
    
    if not os.path.exists(fpath):
        raise HTTPException(status_code=404, detail="Photo not found")
        
    try:
        with Image.open(fpath) as img:
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            # PIL rotate: positive degrees = counter-clockwise, negative = clockwise
            rotated = img.rotate(-req.degrees, expand=True)
            rotated.save(fpath, "JPEG", quality=95, optimize=True)
            
        # Recreate thumbnail
        with Image.open(fpath) as img:
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            img.thumbnail((600, 600), Image.Resampling.LANCZOS)
            img.save(thumbpath, "JPEG", quality=82, optimize=True)
            
        return {"status": "ok", "filename": req.filename, "timestamp": int(time.time())}
    except Exception as e:
        logging.error(f"Rotation error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# --- BOT COMMANDS ---

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = str(message.from_user.id)
    if user_id not in ADMIN_IDS:
        return await message.answer("Доступ закрыт.")

    await message.answer(
        "👋 <b>Привет, Владимир!</b>\n\n"
        "Вы можете управлять сайтом прямо здесь через Telegram Mini App: поворачивать фотографии, менять цены, добавлять/удалять кадры и поднимать удачные фото выше.",
        reply_markup=kb,
        parse_mode=ParseMode.HTML
    )

@app.on_event("startup")
async def on_startup():
    if bot is not None:
        asyncio.create_task(dp.start_polling(bot))
    else:
        logging.warning("Bot is inactive in development mode.")

@app.on_event("shutdown")
async def on_shutdown():
    if bot is not None:
        await bot.session.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
