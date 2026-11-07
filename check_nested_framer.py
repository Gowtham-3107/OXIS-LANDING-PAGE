import os
import re

# Check inside all downloaded files in cloned_site/assets/framerusercontent.com
all_text_files = []
for root, dirs, files in os.walk("cloned_site/assets/framerusercontent.com"):
    for f in files:
        if f.endswith(('.js', '.mjs', '.css', '.html')):
            all_text_files.append(os.path.join(root, f))

print(f"Total downloaded JS/CSS files: {len(all_text_files)}")

referenced_framer_urls = set()
for path in all_text_files:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            matches = re.findall(r'https://[a-zA-Z0-9.\-_/]*framerusercontent\.com/[^\s"\'<>`,\)\\]+', content)
            for m in matches:
                referenced_framer_urls.add(m)
    except Exception as e:
        pass

print(f"Found {len(referenced_framer_urls)} framerusercontent URLs inside JS/CSS files.")

missing_nested = []
for u in referenced_framer_urls:
    from urllib.parse import urlparse
    p = urlparse(u).path.lstrip("/")
    local_path = os.path.join("cloned_site", "assets", "framerusercontent.com", p.replace("/", os.sep))
    if not os.path.exists(local_path):
        missing_nested.append(u)

print(f"Missing nested Framer assets: {len(missing_nested)}")
for m in missing_nested[:10]:
    print(" ", m)

