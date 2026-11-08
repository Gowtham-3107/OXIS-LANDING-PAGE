import os
import re
import urllib.request
import urllib.parse

base_cdn = "https://framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/"
site_dir = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

visited = set()

def scan_and_download(filename):
    if filename in visited:
        return
    visited.add(filename)
    
    local_path = os.path.join(site_dir, filename)
    if not os.path.exists(local_path):
        url = base_cdn + filename
        print(f"Downloading {url} ...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                content = resp.read()
                with open(local_path, "wb") as f:
                    f.write(content)
            print(f"Saved {filename}")
        except Exception as e:
            print(f"Failed {filename}: {e}")
            return
            
    # Read and find sub-imports
    try:
        with open(local_path, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()
    except Exception:
        return

    # Pattern: import / from ./<file>.mjs
    imps = re.findall(r'from\s*["\']\./([^"\']+)["\']', code)
    imps += re.findall(r'import\s*\(\s*["\']\./([^"\']+)["\']\s*\)', code)
    imps += re.findall(r'import\(`\./([^`]+)`\)', code)
    
    for sub in imps:
        scan_and_download(sub)

# Seed with all current files
files = [f for f in os.listdir(site_dir) if f.endswith(('.mjs', '.js'))]
for f in files:
    scan_and_download(f)

print(f"Completed recursive crawl. Total modules visited: {len(visited)}")

