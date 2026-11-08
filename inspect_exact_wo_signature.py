target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect where Wo starts:
idx_wo = c.find("Wo=W(f(function(e,t){let n=_(null),r=t??n,i=p(),{activeLocale:o,setLocale:s}=he(),c=Oe()")
print("Wo start index:", idx_wo)
print(c[idx_wo:idx_wo+350])
