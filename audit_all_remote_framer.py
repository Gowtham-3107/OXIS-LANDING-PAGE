import os
import re

remote_urls = set()

# Scan all files in cloned_site
for root, dirs, files in os.walk("cloned_site"):
    for f in files:
        if f.endswith(('.html', '.js', '.mjs', '.css', '.json')):
            p = os.path.join(root, f)
            try:
                with open(p, "r", encoding="utf-8", errors="ignore") as fl:
                    c = fl.read()
                    # Look for https://framerusercontent.com or https://events.framer.com or https://framer.com
                    for m in re.findall(r'https?://[a-zA-Z0-9.\-_/]*framerusercontent\.com/[^\s"\'<>`,\)\\]+', c):
                        clean = m.rstrip('\\"\'').replace('\\/', '/')
                        remote_urls.add((clean, p))
                    for m in re.findall(r'https?://[a-zA-Z0-9.\-_/]*framer\.com/[^\s"\'<>`,\)\\]+', c):
                        clean = m.rstrip('\\"\'').replace('\\/', '/')
                        remote_urls.add((clean, p))
            except:
                pass

print(f"Total remote Framer references found: {len(remote_urls)}")
unique_urls = set(u[0] for u in remote_urls)
print(f"Unique URLs: {len(unique_urls)}")

# Check how many are missing locally vs downloaded
from urllib.parse import urlparse
missing = []
present = []

for u in unique_urls:
    parsed = urlparse(u)
    domain = parsed.netloc
    path = parsed.path.lstrip("/")
    local_p = os.path.join("cloned_site", "assets", domain, path.replace("/", os.sep))
    if os.path.exists(local_p):
        present.append((u, local_p))
    else:
        missing.append((u, local_p))

print(f"Already downloaded locally: {len(present)}")
print(f"Not yet on local disk: {len(missing)}")
if missing:
    print("Sample missing URLs:")
    for u, lp in missing[:15]:
        print("  ", u)

