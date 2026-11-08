target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect right after `E=Uo(e,T),`:
idx = c.find("E=Uo(e,T),{activeVariantCallback:D,delay:O}=Se(h),")
print("Found E=Uo...", idx != -1)
print(c[idx:idx+150])
