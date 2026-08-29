import os
from PIL import Image

uploads_dir = os.path.join(os.path.dirname(__file__), "uploads")
thumbs_dir = os.path.join(uploads_dir, "thumbs")
os.makedirs(thumbs_dir, exist_ok=True)

def create_thumbnails():
    files = [f for f in os.listdir(uploads_dir) if os.path.isfile(os.path.join(uploads_dir, f))]
    print(f"Processing {len(files)} images for thumbnails...")
    
    count = 0
    for filename in files:
        if filename.startswith('.'):
            continue
            
        src_path = os.path.join(uploads_dir, filename)
        dst_path = os.path.join(thumbs_dir, filename)
        
        if not os.path.exists(dst_path):
            try:
                with Image.open(src_path) as img:
                    # Convert RGBA to RGB if needed
                    if img.mode in ('RGBA', 'LA', 'P'):
                        img = img.convert('RGB')
                    
                    # Resize preserving aspect ratio (max width 600px)
                    img.thumbnail((600, 600), Image.Resampling.LANCZOS)
                    img.save(dst_path, "JPEG", quality=80, optimize=True)
                    count += 1
            except Exception as e:
                print(f"Failed {filename}: {e}")
                
    print(f"Done! Generated {count} new thumbnails in {thumbs_dir}.")

if __name__ == "__main__":
    create_thumbnails()
