import os
import re
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# 1. Gather all files in cloned_site
files_to_scan = ["cloned_site/index_original.html"]
for root, dirs, files in os.walk("cloned_site"):
    for f in files:
        if f.endswith(('.html', '.js', '.mjs', '.css', '.json')):
            files_to_scan.append(os.path.join(root, f))

all_urls = set()
for path in files_to_scan:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
            for m in re.findall(r'https://[a-zA-Z0-9.\-_/]*framerusercontent\.com/[^\s"\'<>`,\)\\]+', c):
                clean = m.rstrip('\\"\'').replace('\\/', '/')
                all_urls.add(clean)
            for m in re.findall(r'https://fonts\.gstatic\.com/[^\s"\'<>`,\)\\]+', c):
                clean = m.rstrip('\\"\'').replace('\\/', '/')
                all_urls.add(clean)
            for m in re.findall(r'https://events\.framer\.com/[^\s"\'<>`,\)\\]+', c):
                clean = m.rstrip('\\"\'').replace('\\/', '/')
                all_urls.add(clean)
    except Exception:
        pass

print(f"Total discovered CDN/Framer URLs across entire project: {len(all_urls)}")

# Download any that are missing
def download(url):
    try:
        parsed = urllib.parse.urlparse(url)
        domain = parsed.netloc
        path = parsed.path.lstrip("/")
        if not path:
            path = "index.html"
        target_path = os.path.join("cloned_site", "assets", domain, path.replace("/", os.sep))
        
        if os.path.exists(target_path) and os.path.getsize(target_path) > 0:
            return (url, True, "Already local")
            
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            with open(target_path, "wb") as out:
                out.write(data)
        return (url, True, "Downloaded")
    except Exception as e:
        return (url, False, str(e))

with ThreadPoolExecutor(max_workers=10) as ex:
    results = list(ex.map(download, all_urls))

success = [r for r in results if r[1]]
failed = [r for r in results if not r[1]]
print(f"Downloaded/Cached: {len(success)}, Failed: {len(failed)}")

# Now rewrite all references in HTML and JS/CSS to point directly to ./assets/...
# Make relative paths so it works whether opened from file:// or any server
def make_local_relative(text, current_file_path):
    # current dir relative to cloned_site
    rel_depth = os.path.relpath("cloned_site/assets", os.path.dirname(current_file_path)).replace("\\", "/")
    
    # Replace https://framerusercontent.com/... with {rel_depth}/framerusercontent.com/...
    def repl_framer(m):
        full = m.group(0).replace('\\/', '/')
        parsed = urllib.parse.urlparse(full)
        path = parsed.path.lstrip("/")
        return f"{rel_depth}/framerusercontent.com/{path}"

    text = re.sub(r'https:\\?/\\?/framerusercontent\.com/[^\s"\'<>`,\)\\]+', repl_framer, text)
    
    def repl_gstatic(m):
        full = m.group(0).replace('\\/', '/')
        parsed = urllib.parse.urlparse(full)
        path = parsed.path.lstrip("/")
        return f"{rel_depth}/fonts.gstatic.com/{path}"

    text = re.sub(r'https:\\?/\\?/fonts\.gstatic\.com/[^\s"\'<>`,\)\\]+', repl_gstatic, text)

    return text

print("Converting references inside downloaded files to local relative paths...")
count_rewritten = 0
for root, dirs, files in os.walk("cloned_site"):
    for f in files:
        if f.endswith(('.html', '.js', '.mjs', '.css')):
            fp = os.path.join(root, f)
            try:
                with open(fp, "r", encoding="utf-8", errors="ignore") as file_in:
                    original = file_in.read()
                modified = make_local_relative(original, fp)
                if modified != original:
                    with open(fp, "w", encoding="utf-8") as file_out:
                        file_out.write(modified)
                    count_rewritten += 1
            except Exception as e:
                print(f"Error rewriting {fp}: {e}")

print(f"Rewrote references in {count_rewritten} files to be 100% local!")

