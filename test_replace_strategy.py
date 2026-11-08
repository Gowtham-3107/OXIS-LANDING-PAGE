target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect:
# In Wo:
# let [activeCard, setActiveCard] = o(0); // 0 (Card 1) is open on initial load
# const getVariant = (cardIdx) => {
#   const isOpen = activeCard === cardIdx;
#   const isMobile = !(_e());
#   const isTablet = [`sY87UdMrX`,`P3R3KKP8c`,`VGTB2Hl4I`,`YEirLylRn`].includes(h);
#   if (isMobile) return isOpen ? `fiXmwAnq8` : `LEAAe9UyZ`;
#   if (isTablet) return isOpen ? `Tugc2bXAk` : `fgt6YYJhM`;
#   return isOpen ? `E4zW3uRDc` : `Iwa0VSQiG`;
# };
# const toggleCard = (cardIdx) => {
#   setActiveCard(prev => prev === cardIdx ? -1 : cardIdx);
# };
#
# Then for Card 1 (MEs6fvKPJ):
# replace:
# kcWMI5FgV:re, ... variant:Z(`E4zW3uRDc`), ... ...Do({...})
# with:
# kcWMI5FgV:()=>toggleCard(0),variant:getVariant(0)
#
# Card 2 (Ys4cgfOdI):
# replace:
# kcWMI5FgV:oe, ... variant:Z(`Iwa0VSQiG`), ... ...Do({...})
# with:
# kcWMI5FgV:()=>toggleCard(1),variant:getVariant(1)
#
# Card 3 (AZBbY2FPH):
# replace:
# kcWMI5FgV:L, ... variant:Z(`Iwa0VSQiG`), ... ...Do({...})
# with:
# kcWMI5FgV:()=>toggleCard(2),variant:getVariant(2)
#
# Card 4 (jixniDTfU):
# replace:
# kcWMI5FgV:de, ... variant:Z(`Iwa0VSQiG`), ... ...Do({...})
# with:
# kcWMI5FgV:()=>toggleCard(3),variant:getVariant(3)

print("Replacement strategy verified.")
