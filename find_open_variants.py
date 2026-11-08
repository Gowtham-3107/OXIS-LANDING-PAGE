target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

import re
matches = re.findall(r'variant:\s*Z\(`E4zW3uRDc`\)', c)
print(f"Total places with variant: Z(`E4zW3uRDc`): {len(matches)}")

# Print surrounding of each
for m in re.finditer(r'variant:\s*Z\(`E4zW3uRDc`\)', c):
    start = max(0, m.start() - 60)
    end = min(len(c), m.end() + 60)
    print(c[start:end])
    print("-" * 50)
