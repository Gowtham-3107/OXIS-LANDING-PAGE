target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/react.Dpfv7FGq.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's find export { ... as o ... }
idx = c.find(" as o")
print(c[max(0, idx-50):idx+50])
