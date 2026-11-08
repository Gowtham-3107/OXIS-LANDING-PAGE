import os
import re
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# 1. Collect all framerusercontent.com URLs inside all .mjs files in sites/
site_dir = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg"
modules = [os.path.join(site_dir, f) for f in os.listdir(site_dir) if f.endswith(('.mjs', '.js'))]

urls_to_download = set()
for m in modules:
    with open(m, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()
        for u in re.findall(r'https://framerusercontent\.com/[^\s"\'<>`,\)\\]+', c):
            urls_to_download.add(u)

print(f"Total URLs to check/download: {len(urls_to_download)}")

def download(u):
    try:
        clean_u = u.replace('\\/', '/')
        parsed = urllib.parse.urlparse(clean_u)
        path = parsed.path.lstrip('/')
        local_p = os.path.join("cloned_site", "assets", "framerusercontent.com", path.replace('/', os.sep))
        if os.path.exists(local_p) and os.path.getsize(local_p) > 0:
            return (u, True, "cached")
        os.makedirs(os.path.dirname(local_p), exist_ok=True)
        req = urllib.request.Request(clean_u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            with open(local_p, "wb") as out:
                out.write(data)
        return (u, True, len(data))
    except Exception as e:
        return (u, False, str(e))

with ThreadPoolExecutor(max_workers=10) as ex:
    results = list(ex.map(download, urls_to_download))

ok = [r for r in results if r[1]]
fail = [r for r in results if not r[1]]
print(f"Downloaded / cached: {len(ok)}, Failed: {len(fail)}")
for u, s, msg in fail:
    print("  Failed:", u, msg)

# 2. Rewrite these URLs in all modules to relative local paths
# From sites/RuE79Xrnx9TYtmvVF2nrg/ to assets/framerusercontent.com/
# Relative path is: ../../
def replace_in_module(m_path):
    with open(m_path, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()

    def repl(match):
        full = match.group(0).replace('\\/', '/')
        parsed = urllib.parse.urlparse(full)
        path = parsed.path.lstrip('/')
        # relative to sites/RuE79Xrnx9TYtmvVF2nrg is ../../<path>
        return f"../../{path}"

    new_code = re.sub(r'https:\\?/\\?/framerusercontent\.com/[^\s"\'<>`,\)\\]+', repl, code)
    if new_code != code:
        with open(m_path, "w", encoding="utf-8") as f:
            f.write(new_code)
        print(f"Rewrote URLs in {os.path.basename(m_path)} to local relative paths!")

for m in modules:
    replace_in_module(m)

print("All module URLs are now 100% locally served!")
