target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect what happens if each Card (To) manages its OWN open/closed variant independently!
# Look at component `wo` (which is `To`):
# wo is the single accordion card!
# Does wo receive `variant` as prop?
# Let's check wo props:
# So=({click:e,description:t,height:n,id:r,keyPt1:i,keyPt2:a,keyPt3:o,serialNo:s,title:c,width:l,...u})=>({...u, ... variant:yo[u.variant]??u.variant??`Iwa0VSQiG`})
# wo component:
# {baseVariant:re,classNames:ie,clearLoadingGesture:ae,gestureHandlers:P,gestureVariant:oe,isLoading:F,setGestureState:I,setVariant:se,variants:L}=ne({cycleOrder:fo,defaultVariant:`Iwa0VSQiG`,ref:r,variant:f,variantClassNames:mo})
# de is the onTap handler for Closed variant (`Iwa0VSQiG`):
# de=le(async(...e)=>{if(I({isPressed:!1}),T&&await T(...e)===!1)return!1;se(`E4zW3uRDc`)})
# fe is the onTap handler for Open variant (`E4zW3uRDc`):
# fe=le(async(...e)=>{if(I({isPressed:!1}),T&&await T(...e)===!1)return!1;se(`Iwa0VSQiG`)})
print("de and fe in wo:")
idx = c.find("de=le(async(...e)=>{if(I({isPressed:!1}),T&&await T(...e)===!1)return!1;se(`E4zW3uRDc`)})")
print(c[idx:idx+350])
