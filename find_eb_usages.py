target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect all places where `ebUSgHhHF` has variant: Z(`E4zW3uRDc`)
import re
for m in re.finditer(r'ebUSgHhHF:\s*\{[^}]*variant:\s*Z\(`E4zW3uRDc`\)[^}]*\}', c):
    print("Found match:", m.group(0))
