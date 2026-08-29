import os, json
from PIL import Image

uploads_dir = r"C:\Users\artem\Documents\lesnikov_site\backend\uploads"
with open(r"C:\Users\artem\Documents\lesnikov_site\backend\data\data.json", encoding="utf-8") as f:
    data = json.load(f)

print("=== HOME IMAGES ===")
for img in data['home']['hero_images'][:15]:
    p = os.path.join(uploads_dir, img)
    if os.path.exists(p):
        im = Image.open(p)
        print(f"{img}: {im.size}")
