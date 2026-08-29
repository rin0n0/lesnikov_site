import os, json
from PIL import Image

uploads_dir = r"C:\Users\artem\Documents\lesnikov_site\backend\uploads"
with open(r"C:\Users\artem\Documents\lesnikov_site\backend\data\data.json", encoding="utf-8") as f:
    data = json.load(f)

for cat in ['kindergarten', 'grade_4', 'grade_11']:
    print(f"=== ALBUM: {cat} ===")
    for img in data['albums'][cat]['images']:
        p = os.path.join(uploads_dir, img)
        im = Image.open(p)
        print(f"{img}: {im.size} (aspect={im.width/im.height:.2f})")
