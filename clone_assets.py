import os
import re
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://agen-ai.framer.website/"
OUT_DIR = "cloned_site"
ASSETS_DIR = os.path.join(OUT_DIR, "assets")

os.makedirs(ASSETS_DIR, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

print(f"Fetching main page: {BASE_URL}")
req = urllib.request.Request(BASE_URL, headers=headers)
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode("utf-8", errors="ignore")

with open(os.path.join(OUT_DIR, "index_original.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Original HTML saved.")

# Collect raw URLs
discovered = set()

# Pattern 1: framerusercontent URLs (images, scripts, styles, fonts, videos)
for match in re.findall(r'https://[a-zA-Z0-9.\-_/]*framerusercontent\.com/[^\s"\'<>`,\)]+', html):
    # Clean trailing characters
    clean_url = match.rstrip('\\"\'')
    discovered.add(clean_url)

# Pattern 2: Framer app or CDN scripts / assets
for match in re.findall(r'https://[a-zA-Z0-9.\-_/]*framer\.com/[^\s"\'<>`,\)]+', html):
    clean_url = match.rstrip('\\"\'')
    discovered.add(clean_url)

# Pattern 3: standard src/href relative or absolute
for attr in ["src", "href", "data-src"]:
    for match in re.findall(rf'{attr}=["\']([^"\']+)["\']', html):
        full = urllib.parse.urljoin(BASE_URL, match)
        if full.startswith("http"):
            discovered.add(full)

# Pattern 4: any image, font, media or script url
for match in re.findall(r'https://[^\s"\'<>`,\)]+\.(?:png|jpg|jpeg|webp|svg|gif|mp4|webm|woff2|woff|ttf|css|js)', html):
    discovered.add(match)

print(f"Total discovered raw candidate URLs: {len(discovered)}")

# Filter out non-asset or tracking URLs if any
valid_urls = []
for u in discovered:
    # clean backslashes from JSON escapes if present
    u = u.replace('\\/', '/')
    # remove framing quotes
    u = u.strip('"\'')
    if u.startswith("http"):
        valid_urls.append(u)

valid_urls = sorted(list(set(valid_urls)))

with open(os.path.join(OUT_DIR, "asset_manifest.txt"), "w", encoding="utf-8") as f:
    for u in valid_urls:
        f.write(u + "\n")

print(f"Cleaned unique URLs to fetch: {len(valid_urls)}")

# Download assets
def download_asset(url):
    try:
        parsed = urllib.parse.urlparse(url)
        # build a safe relative path
        domain = parsed.netloc
        path = parsed.path.lstrip("/")
        if not path:
            path = "index.html"
        
        # Determine local filepath
        # keep query parameter hash if needed for unique naming
        filename = os.path.basename(path)
        subdir = os.path.dirname(path)
        
        target_dir = os.path.join(ASSETS_DIR, domain, subdir)
        os.makedirs(target_dir, exist_ok=True)
        
        target_file = os.path.join(target_dir, filename)
        if os.path.exists(target_file) and os.path.getsize(target_file) > 0:
            return (url, True, "Already cached")

        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            with open(target_file, "wb") as f_out:
                f_out.write(content)
        return (url, True, len(content))
    except Exception as e:
        return (url, False, str(e))

print("Starting concurrent asset download...")
success_count = 0
fail_count = 0

with ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(download_asset, valid_urls)
    for url, success, msg in results:
        if success:
            success_count += 1
        else:
            fail_count += 1
            # print(f"Failed {url}: {msg}")

print(f"\nDownload finished!\nSuccessfully downloaded: {success_count}\nFailed/Skipped: {fail_count}")

