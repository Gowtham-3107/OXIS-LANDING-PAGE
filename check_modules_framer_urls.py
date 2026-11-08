import os
import re

site_dir = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg"
modules = [os.path.join(site_dir, f) for f in os.listdir(site_dir) if f.endswith(('.mjs', '.js'))]

urls = set()
for m in modules:
    with open(m, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()
        for u in re.findall(r'https://framerusercontent\.com/[^\s"\'<>`,\)\\]+', c):
            urls.add((u, os.path.basename(m)))

print(f"Total framerusercontent.com URLs inside sites/ modules: {len(urls)}")
for u, f in urls:
    print(f"  [{f}] -> {u}")
