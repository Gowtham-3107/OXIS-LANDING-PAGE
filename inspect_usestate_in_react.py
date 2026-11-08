target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/react.Dpfv7FGq.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

idx = c.find("useState")
print("useState position:", idx)
if idx != -1:
    print(c[idx-50:idx+150])
