import os
import shutil
from PIL import Image, ImageOps

uploads_dir = r"C:\Users\artem\Documents\lesnikov_site\backend\uploads"
thumbs_dir = os.path.join(uploads_dir, "thumbs")

def normalize_all_images():
    print("Normalizing all images with ImageOps.exif_transpose...")
    files = [f for f in os.listdir(uploads_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png')) and os.path.isfile(os.path.join(uploads_dir, f))]
    
    for f in files:
        fpath = os.path.join(uploads_dir, f)
        try:
            with Image.open(fpath) as img:
                # Transpose according to EXIF
                transposed = ImageOps.exif_transpose(img)
                # If transposed or has EXIF, save clean image with correct orientation
                if transposed.mode in ('RGBA', 'LA', 'P'):
                    transposed = transposed.convert('RGB')
                transposed.save(fpath, "JPEG", quality=95, optimize=True)
        except Exception as e:
            print(f"Error normalizing {f}: {e}")

    # Re-generate all thumbnails cleanly from the transposed originals
    print("Recreating all thumbnails...")
    shutil.rmtree(thumbs_dir, ignore_errors=True)
    os.makedirs(thumbs_dir, exist_ok=True)
    
    for f in files:
        fpath = os.path.join(uploads_dir, f)
        thumbpath = os.path.join(thumbs_dir, f)
        try:
            with Image.open(fpath) as img:
                if img.mode in ('RGBA', 'LA', 'P'):
                    img = img.convert('RGB')
                img.thumbnail((600, 600), Image.Resampling.LANCZOS)
                img.save(thumbpath, "JPEG", quality=82, optimize=True)
        except Exception as e:
            print(f"Error thumbnail {f}: {e}")
            
    print("All images and thumbnails normalized and regenerated!")

if __name__ == "__main__":
    normalize_all_images()
