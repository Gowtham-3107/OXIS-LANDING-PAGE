target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect where Card 1 variant is passed:
# id:`MEs6fvKPJ`,kcWMI5FgV:re,KDEMzn5iv:`(01)`,l55IL4lO3:`Data readiness assessment`,layoutId:`MEs6fvKPJ`,style:{width:`100%`},variant:Z(`E4zW3uRDc`), ...
# Card 2:
# id:`Ys4cgfOdI`,kcWMI5FgV:oe,KDEMzn5iv:`(02)`, ... variant:Z(`Iwa0VSQiG`), ...
# Card 3:
# id:`AZBbY2FPH`,kcWMI5FgV:L,KDEMzn5iv:`(03)`, ... variant:Z(`Iwa0VSQiG`), ...
# Card 4:
# id:`jixniDTfU`,kcWMI5FgV:de,KDEMzn5iv:`(04)`, ... variant:Z(`Iwa0VSQiG`), ...

# If we give parent component a real activeCard state:
# In Wo:
# let [activeCard, setActiveCard] = o(0); // 0 = Card 1, 1 = Card 2, 2 = Card 3, 3 = Card 4, null = None open!
# Then:
# Card 1 variant is: activeCard === 0 ? "E4zW3uRDc" : "Iwa0VSQiG"
# Card 1 click (kcWMI5FgV): () => setActiveCard(a => a === 0 ? null : 0)
#
# Card 2 variant is: activeCard === 1 ? "E4zW3uRDc" : "Iwa0VSQiG"
# Card 2 click (kcWMI5FgV): () => setActiveCard(a => a === 1 ? null : 1)
#
# Card 3 variant is: activeCard === 2 ? "E4zW3uRDc" : "Iwa0VSQiG"
# Card 3 click (kcWMI5FgV): () => setActiveCard(a => a === 2 ? null : 2)
#
# Card 4 variant is: activeCard === 3 ? "E4zW3uRDc" : "Iwa0VSQiG"
# Card 4 click (kcWMI5FgV): () => setActiveCard(a => a === 3 ? null : 3)
#
# AND WHAT ABOUT CARD HEIGHTS / POSITIONS?
# Let's check how the 4 cards are positioned in V:
# V({height: 128, ... y: (c?.y||0)+0+0+0, ... children: Card 1})
# V({height: 128, ... y: (c?.y||0)+0+0+136, ... children: Card 2})
# V({height: 128, ... y: (c?.y||0)+0+0+272, ... children: Card 3})
# V({height: 128, ... y: (c?.y||0)+0+0+408, ... children: Card 4})
# Let's inspect the container V for the 4 cards!
idx = c.find("id:`MEs6fvKPJ`")
print(c[idx-500:idx])
