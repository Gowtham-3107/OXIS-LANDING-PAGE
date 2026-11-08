target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

import re
matches = [m.start() for m in re.finditer(r'wo\b', c)]
print(f"Occurrences of wo: {len(matches)}")
for idx in matches:
    print(c[max(0, idx - 100):min(len(c), idx + 200)])
    print("="*60)

