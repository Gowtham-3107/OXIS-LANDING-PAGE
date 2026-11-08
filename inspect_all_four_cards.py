target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect each card's base definition and variant overrides
# Card 1:
idx1 = c.find("id:`MEs6fvKPJ`")
print("=== Card 1 ===")
print(c[idx1:idx1+350])

# Card 2:
idx2 = c.find("id:`Ys4cgfOdI`")
print("=== Card 2 ===")
print(c[idx2:idx2+350])

# Card 3:
idx3 = c.find("id:`AZBbY2FPH`")
print("=== Card 3 ===")
print(c[idx3:idx3+350])

# Card 4:
idx4 = c.find("id:`jixniDTfU`")
print("=== Card 4 ===")
print(c[idx4:idx4+350])
