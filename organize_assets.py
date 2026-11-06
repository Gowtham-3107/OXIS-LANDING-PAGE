import os
import shutil

ASSETS_SRC = "cloned_site/assets/framerusercontent.com"
EXPORT_DIR = "extracted_assets"

os.makedirs(f"{EXPORT_DIR}/images", exist_ok=True)
os.makedirs(f"{EXPORT_DIR}/icons_svg", exist_ok=True)
os.makedirs(f"{EXPORT_DIR}/fonts", exist_ok=True)

copied = 0
for root, dirs, files in os.walk(ASSETS_SRC):
    for f in files:
        ext = os.path.splitext(f)[1].lower()
        src_path = os.path.join(root, f)
        if ext in ['.png', '.jpg', '.jpeg', '.webp', '.gif']:
            shutil.copy2(src_path, os.path.join(f"{EXPORT_DIR}/images", f))
            copied += 1
        elif ext == '.svg':
            shutil.copy2(src_path, os.path.join(f"{EXPORT_DIR}/icons_svg", f))
            copied += 1
        elif ext in ['.woff2', '.woff', '.ttf', '.otf']:
            shutil.copy2(src_path, os.path.join(f"{EXPORT_DIR}/fonts", f))
            copied += 1

print(f"Organized {copied} assets into {EXPORT_DIR}/")

