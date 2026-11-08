target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect each card's children: v(To, { ... })
for card_id in ["MEs6fvKPJ", "Ys4cgfOdI", "AZBbY2FPH", "jixniDTfU"]:
    idx = c.find(f"id:`{card_id}`")
    print(f"=== {card_id} ===")
    print(c[idx-30:idx+250])
