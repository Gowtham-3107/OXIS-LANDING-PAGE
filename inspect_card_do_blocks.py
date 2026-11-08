target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect all Do({...}, h, S) for Card 1, 2, 3, 4
idx1 = c.find("id:`MEs6fvKPJ`")
idx2 = c.find("id:`Ys4cgfOdI`")
idx3 = c.find("id:`AZBbY2FPH`")
idx4 = c.find("id:`jixniDTfU`")

print("Card 1 Do block:")
print(c[idx1+150:c.find("},h,S)", idx1)+6])
print("\nCard 2 Do block:")
print(c[idx2+150:c.find("},h,S)", idx2)+6])
print("\nCard 3 Do block:")
print(c[idx3+150:c.find("},h,S)", idx3)+6])
print("\nCard 4 Do block:")
print(c[idx4+150:c.find("},h,S)", idx4)+6])
