import os
import re

main_mjs = 'cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/script_main.Dvcfic8j.mjs'
with open(main_mjs, 'r', encoding='utf-8') as f:
    code = f.read()

# Find all import("./...") or import('...')
dynamic_imports = re.findall(r'import\s*\(\s*["\']([^"\']+)["\']\s*\)', code)
print(f"Dynamic imports in script_main: {len(dynamic_imports)}")
mjs_dir = os.path.dirname(main_mjs)
for d in dynamic_imports:
    path = os.path.normpath(os.path.join(mjs_dir, d))
    print(f"  {d} -> exists? {os.path.exists(path)}")

