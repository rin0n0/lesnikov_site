import os
from PIL import Image

uploads_dir = r"C:\Users\artem\Documents\lesnikov_site\backend\uploads"
thumbs_dir = os.path.join(uploads_dir, "thumbs")

all_files = [f for f in os.listdir(uploads_dir) if f.lower().endswith(('.jpg', '.jpeg'))]

# Let's inspect all files and check which ones have horizontal orientation (width > height) but are photos of books or portraits taken sideways
# Look at the list from data.json:
# home_09353c7c.jpeg, home_0bf30e53.jpeg, home_c8f623e8.jpeg, home_4f5e0e12.jpeg, home_c7312d59.jpeg, home_f8ddd814.jpeg, home_177dbd37.jpeg
# Let's check which ones have .jpeg extension!
jpeg_candidates = [
    'home_09353c7c.jpeg', # book on table with girl
    'home_0bf30e53.jpeg', # open book
    'home_c8f623e8.jpeg',
    'home_4f5e0e12.jpeg',
    'home_c7312d59.jpeg',
    'home_f8ddd814.jpeg',
    'home_177dbd37.jpeg',
    'home_7344db06.jpg',
    'home_48cc7d75.jpg',
    'home_39a6585a.jpg'
]

for fname in all_files:
    for cand in jpeg_candidates:
        if cand in fname:
            print(f"Found: {fname}")
