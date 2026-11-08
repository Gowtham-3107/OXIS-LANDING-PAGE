target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect imports at the top of rg3Gd...
idx = c.find("from\"./react")
if idx == -1:
    idx = c.find("react")
print(c[max(0, idx-50):idx+200])
