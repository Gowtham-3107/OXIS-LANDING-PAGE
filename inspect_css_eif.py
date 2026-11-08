target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect CSS for framer-eif0sx:
idx = c.find(".framer-eif0sx")
if idx != -1:
    print(c[idx:idx+400])
else:
    print("Not in this file")
