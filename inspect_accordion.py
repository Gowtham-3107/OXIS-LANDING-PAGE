with open("cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/Z8MROexOS.rj7ghI2W.mjs", "r", encoding="utf-8") as f:
    c = f.read()

print("File size:", len(c))
# Look for variants, click handlers, state hooks like useState
import re
print("useState occurrences:")
for m in re.finditer(r'[a-zA-Z0-9_$]+\s*=\s*(?:useState|o)\([^)]*\)', c):
    start = max(0, m.start() - 50)
    end = min(len(c), m.end() + 100)
    print(c[start:end])
    print("-" * 50)

