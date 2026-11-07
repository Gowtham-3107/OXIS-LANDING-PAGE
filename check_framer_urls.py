import re
import os

with open("cloned_site/index_original.html", "r", encoding="utf-8") as f:
    html = f.read()

urls = set()
# Match all framerusercontent URLs
matches = re.findall(r'https://[a-zA-Z0-9.\-_/]*framerusercontent\.com/[^\s"\'<>`,\)]+', html)
for m in matches:
    clean = m.rstrip('\\"\'')
    clean = clean.replace('\\/', '/')
    urls.add(clean)

print(f"Total unique framerusercontent URLs found in HTML: {len(urls)}")

# Check downloaded files
downloaded = 0
missing = []
for u in urls:
    # URL path
    from urllib.parse import urlparse
    p = urlparse(u).path.lstrip("/")
    local_path = os.path.join("cloned_site", "assets", "framerusercontent.com", p.replace("/", os.sep))
    if os.path.exists(local_path):
        downloaded += 1
    else:
        missing.append(u)

print(f"Already downloaded: {downloaded}")
print(f"Missing: {len(missing)}")
if missing:
    print("Sample missing:")
    for m in missing[:10]:
        print(" ", m)

