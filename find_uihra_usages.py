target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

import re
matches = [m.start() for m in re.finditer(r'uIHRARi0D', c)]
print(f"Total uIHRARi0D occurrences: {len(matches)}")
for idx in matches:
    print(c[max(0, idx - 50):min(len(c), idx + 80)])
    print("-" * 40)
