import os
from PIL import Image, ImageOps

uploads_dir = os.path.join(os.path.dirname(__file__), "uploads")
thumbs_dir = os.path.join(uploads_dir, "thumbs")

def fix_all_rotations():
    for root_dir in [uploads_dir, thumbs_dir]:
        if not os.path.exists(root_dir): continue
        for fname in os.listdir(root_dir):
            if not os.path.isfile(os.path.join(root_dir, fname)): continue
            if fname.startswith('.'): continue
            
            fpath = os.path.join(root_dir, fname)
            try:
                with Image.open(fpath) as img:
                    transposed = ImageOps.exif_transpose(img)
                    if transposed:
                        transposed.save(fpath, quality=90, optimize=True)
            except Exception as e:
                pass
    print("Rotations fixed via EXIF transpose.")

if __name__ == "__main__":
    fix_all_rotations()
