import os
from PIL import Image

uploads_dir = os.path.join(os.path.dirname(__file__), "uploads")
thumbs_dir = os.path.join(uploads_dir, "thumbs")

# Check all images in uploads
for fname in os.listdir(uploads_dir):
    if fname.startswith('.') or not os.path.isfile(os.path.join(uploads_dir, fname)):
        continue
    fpath = os.path.join(uploads_dir, fname)
    try:
        with Image.open(fpath) as img:
            w, h = img.size
            # If width > height and filename contains specific rotated ones
            # Let's inspect images in grade_11
            if 'grade_11' in fname or 'individual' in fname:
                print(f"{fname}: {w}x{h}")
    except:
        pass
