target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect:
# In wo component (which is single card component):
# wo=W(f(function(e,t){ ...
# let {style:l,className:u,layoutId:d,variant:f, ... kcWMI5FgV:T,...E}=So(e)
# ...
# de=le(async(...e)=>{if(I({isPressed:!1}),T&&await T(...e)===!1)return!1;se(`E4zW3uRDc`)})
# fe=le(async(...e)=>{if(I({isPressed:!1}),T&&await T(...e)===!1)return!1;se(`Iwa0VSQiG`)})
#
# Look closely at `de` and `fe`:
# de is called when the card is Closed (onTap: de). It calls T(...e) (kcWMI5FgV), and then se(`E4zW3uRDc`)!
# fe is called when the card is Open (onTap: fe). It calls T(...e) (kcWMI5FgV), and then se(`Iwa0VSQiG`)!
#
# In the original code:
# When Card 1 was OPEN (Desktop variant `fhjWX54rY`), Card 1 was rendered with:
# kcWMI5FgV: re
# And in Card 1 Open, tapping it called `fe`, which executed:
# `T(...e)` -> `re(...e)`!
# And what did `re` do?
# `re = D(async(...e) => { w('fhjWX54rY') })`!
# `re` set the parent to `fhjWX54rY` (which kept Card 1 open)!
# AND what was Card 1's `kcWMI5FgV` when Card 2 was clicked?
# Card 2 had `kcWMI5FgV: oe` -> `oe` set parent to `x0h1i3LQK` (which opened Card 2 and closed Card 1)!
#
# BUT if the user tapped on Card 1 while it was OPEN, why did Card 2 open in the user's video?
# Let's check what is rendered on Card 1 when it is OPEN!
idx = c.find("id:`MEs6fvKPJ`")
print(c[idx:idx+800])
