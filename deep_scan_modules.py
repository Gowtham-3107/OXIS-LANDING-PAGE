import os
import re

site_dir = 'cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg'
all_mjs = [os.path.join(site_dir, f) for f in os.listdir(site_dir) if f.endswith(('.mjs', '.js'))]

visited = set()
missing_overall = set()

def scan_file(fpath):
    if fpath in visited:
        return
    visited.add(fpath)
    try:
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
    except Exception:
        return

    cur_dir = os.path.dirname(fpath)
    imps = re.findall(r'from\s*["\']([^"\']+)["\']', c)
    imps += re.findall(r'import\s*\(\s*["\']([^"\']+)["\']\s*\)', c)
    for imp in imps:
        if imp.startswith('http'):
            # Remote URL remaining?
            print(f"Remote URL in {os.path.basename(fpath)}: {imp}")
            missing_overall.add(imp)
        elif imp.startswith('.'):
            target = os.path.normpath(os.path.join(cur_dir, imp))
            if not os.path.exists(target):
                print(f"Missing local file referenced in {os.path.basename(fpath)}: {imp} -> {target}")
                missing_overall.add(target)
            else:
                scan_file(target)

for m in all_mjs:
    scan_file(m)

print(f"\nScanned {len(visited)} JS modules.")
print(f"Total missing dependencies: {len(missing_overall)}")

