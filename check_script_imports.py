import os
import re

main_mjs = 'cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/script_main.Dvcfic8j.mjs'
with open(main_mjs, 'r', encoding='utf-8') as f:
    code = f.read()

imports = re.findall(r'from\s*["\']([^"\']+)["\']', code)
imports += re.findall(r'import\s*\(\s*["\']([^"\']+)["\']\s*\)', code)

mjs_dir = os.path.dirname(main_mjs)
missing = []
for imp in imports:
    target = os.path.normpath(os.path.join(mjs_dir, imp))
    exists = os.path.exists(target)
    if not exists:
        missing.append((imp, target))
    print(f"  {imp} -> Exists: {exists}")

print(f"\nTotal imports: {len(imports)}, Missing: {len(missing)}")
for imp, t in missing:
    print(f"  MISSING: {imp}")

