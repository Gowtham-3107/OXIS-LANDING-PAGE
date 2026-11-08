target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

idx = c.find("de=le(async(...e)=>{if(I({isPressed:!1}),T&&await T(...e)===!1)return!1;se(`E4zW3uRDc`)})")
print(c[idx:idx+800])
