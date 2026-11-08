target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

for term in ["id:`MEs6fvKPJ`", "id:`Ys4cgfOdI`", "id:`AZBbY2FPH`", "id:`jixniDTfU`"]:
    idx = c.find(term)
    print("="*40, term, "="*40)
    print(c[idx:idx+600])
