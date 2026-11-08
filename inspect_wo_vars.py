target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect where Wo defines its top variables:
idx = c.find("Wo=W(f(function(e,t){let n=_(null),r=t??n,i=p(),{activeLocale:o,setLocale:s}=he(),c=Oe()")
print(c[idx:idx+450])
