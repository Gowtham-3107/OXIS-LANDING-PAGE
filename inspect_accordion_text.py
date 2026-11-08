with open("cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/Z8MROexOS.rj7ghI2W.mjs", "r", encoding="utf-8") as f:
    c = f.read()

import re
idx = c.find("AI Strategy & Mapping")
print("Position of AI Strategy:", idx)
if idx != -1:
    snippet = c[max(0, idx - 500):min(len(c), idx + 1000)]
    print("Snippet around AI Strategy:")
    print(snippet)

idx2 = c.find("rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ")
print("Position of rg3Gd... import:", idx2)

