target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect:
# In Wo:
# let [activeCard, setActiveCard] = o(0);
# Let's check card click handlers:
# const toggleCard = (idx) => {
#   setActiveCard(prev => prev === idx ? -1 : idx);
# };
#
# Now for each Card:
# Card 0:
# kcWMI5FgV: () => toggleCard(0)
# variant: activeCard === 0 ? (_e() ? (h.startsWith("s") || h.startsWith("P") || h.startsWith("V") || h.startsWith("Y") ? "Tugc2bXAk" : "E4zW3uRDc") : "fiXmwAnq8") : (_e() ? (h.startsWith("s") || h.startsWith("P") || h.startsWith("V") || h.startsWith("Y") ? "fgt6YYJhM" : "Iwa0VSQiG") : "LEAAe9UyZ")
#
# Wait, can we simplify getCardVariant?
# const getVariant = (cardIdx) => {
#   const isOpen = activeCard === cardIdx;
#   const isMobile = !(_e());
#   const isTablet = [`sY87UdMrX`,`P3R3KKP8c`,`VGTB2Hl4I`,`YEirLylRn`].includes(h);
#   if (isMobile) return isOpen ? `fiXmwAnq8` : `LEAAe9UyZ`;
#   if (isTablet) return isOpen ? `Tugc2bXAk` : `fgt6YYJhM`;
#   return isOpen ? `E4zW3uRDc` : `Iwa0VSQiG`;
# };
#
# AND crucially:
# We do NOT pass `...Do({ ... }, h, S)` for `variant` and `kcWMI5FgV` to the 4 cards!
# Because the `...Do({...})` was what was overwriting Card 2 to be open when Card 1 closed!
print("Do overrides analysis:")
for card_name in ["Card 1", "Card 2", "Card 3", "Card 4"]:
    print(card_name)
