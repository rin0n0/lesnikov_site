import os
from PIL import Image

uploads_dir = r"C:\Users\artem\Documents\lesnikov_site\backend\uploads"
thumbs_dir = os.path.join(uploads_dir, "thumbs")

# List of images that are rotated 90 degrees clockwise and need 270 deg rotation (or rotate counter-clockwise by 90 = rotate(90, expand=True))
# In PIL: img.rotate(270, expand=True) rotates clockwise, img.rotate(90, expand=True) rotates counter-clockwise.
# If an image is lying on its right side, we need to rotate it 270 degrees (or -90).
# Let's check: 'home_d8515c01.jpg', 'home_74f514bf.jpg', 'home_34491c3d.jpg', 'home_23440735.jpg', 'home_7852c0cd.jpg', 'home_c65c26b8.jpg', 'home_48cc7d75.jpg'
# On these photos, the top of the album is on the right side. To bring top to top, we rotate 90 degrees counter-clockwise (PIL: rotate(90, expand=True)).

images_to_rotate_ccw_90 = [
    'home_d8515c01.jpg',
    'home_74f514bf.jpg',
    'home_34491c3d.jpg',
    'home_23440735.jpg',
    'home_7852c0cd.jpg',
    'home_c65c26b8.jpg',
    'home_48cc7d75.jpg',
    'home_784eb815.jpg',
    'home_93294382.jpg',
    'kindergarten_413f7f0d.jpg',
    'kindergarten_d57e1998.jpg',
    'grade_4_b44fc966.jpg',
    'grade_11_6ce10271.jpg',
    'grade_11_29d6527e.jpg'
]

def apply_rotations():
    for fname in images_to_rotate_ccw_90:
        fpath = os.path.join(uploads_dir, fname)
        thumbpath = os.path.join(thumbs_dir, fname)
        if os.path.exists(fpath):
            with Image.open(fpath) as img:
                # Rotate 90 degrees CCW (or 270 CW)
                rotated = img.rotate(90, expand=True)
                rotated.save(fpath, quality=92, optimize=True)
                print(f"Rotated {fname}")
            
            # Recreate thumb
            with Image.open(fpath) as img:
                if img.mode in ('RGBA', 'LA', 'P'):
                    img = img.convert('RGB')
                img.thumbnail((600, 600), Image.Resampling.LANCZOS)
                img.save(thumbpath, "JPEG", quality=80, optimize=True)

if __name__ == "__main__":
    apply_rotations()
