import re
import urllib.request
import os
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

with open("cloned_site/index_original.html", "r", encoding="utf-8") as f:
    content = f.read()

# Collect all JS / module urls referenced in the HTML
urls = set()
for m in re.findall(r'https://framerusercontent\.com/sites/[^"\'\s<>]+', content):
    clean = m.rstrip('\\"\'')
    urls.add(clean)

for m in re.findall(r'https://framerusercontent\.com/modules/[^"\'\s<>]+', content):
    clean = m.rstrip('\\"\'')
    urls.add(clean)

print(f"Found {len(urls)} initial Framer JS modules/chunks")

# Recursive discovery from JS files
visited = set(urls)
to_fetch = list(urls)
all_discovered_js = set(urls)

def fetch_and_find_imports(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            text = resp.read().decode("utf-8", errors="ignore")
            # Save chunk
            parsed = urllib.parse.urlparse(url)
            rel_path = parsed.path.lstrip("/")
            local_path = os.path.join("cloned_site/assets/framerusercontent.com", rel_path)
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            with open(local_path, "w", encoding="utf-8") as out:
                out.write(text)
            
            # Find sub-imports
            found = set()
            for imp in re.findall(r'from\s*["\']([^"\']+)["\']', text):
                full = urllib.parse.urljoin(url, imp)
                if "framerusercontent.com" in full:
                    found.add(full)
            for imp in re.findall(r'import\s*\(?["\']([^"\']+)["\']\)?', text):
                full = urllib.parse.urljoin(url, imp)
                if "framerusercontent.com" in full:
                    found.add(full)
            for imp in re.findall(r'https://framerusercontent\.com/[a-zA-Z0-9_\-\./]+\.m?js', text):
                found.add(imp)
            return url, found, True
    except Exception as e:
        return url, set(), False

print("Crawling all dependent JS modules and Framer components...")
depth = 0
while to_fetch and depth < 4:
    depth += 1
    next_batch = []
    with ThreadPoolExecutor(max_workers=10) as ex:
        results = ex.map(fetch_and_find_imports, to_fetch)
        for u, found, ok in results:
            for new_url in found:
                if new_url not in visited:
                    visited.add(new_url)
                    next_batch.append(new_url)
                    all_discovered_js.add(new_url)
    print(f"Depth {depth}: downloaded {len(to_fetch)} scripts, found {len(next_batch)} new modules.")
    to_fetch = next_batch

print(f"Total Framer JS component modules downloaded: {len(all_discovered_js)}")

