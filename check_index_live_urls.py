import os
import re

with open("cloned_site/index_live.html", "r", encoding="utf-8") as f:
    c = f.read()

# Find any remaining http / https URLs in index_live.html
all_urls = re.findall(r'https?://[^\s"\'<>`,\)\\]+', c)
framer_cdn = [u for u in all_urls if "framerusercontent.com" in u]
print(f"Total URLs in index_live.html: {len(all_urls)}")
print(f"framerusercontent.com URLs in index_live.html: {len(framer_cdn)}")
for u in set(framer_cdn):
    print(" ", u)
