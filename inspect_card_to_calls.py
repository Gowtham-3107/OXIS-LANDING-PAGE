target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect each card's full v(To, { ... }) call:
for i in [1, 2, 3, 4]:
    card_ids = ["MEs6fvKPJ", "Ys4cgfOdI", "AZBbY2FPH", "jixniDTfU"]
    cid = card_ids[i-1]
    start = c.find(f"children:v(To,")
    # find occurrence with cid
    idx = c.find(f"id:`{cid}`")
    to_start = c.rfind("v(To,{", 0, idx)
    to_end = c.find("})})})", idx) + 2
    print(f"=== Card {i} ({cid}) ===")
    print(c[to_start:to_end])
