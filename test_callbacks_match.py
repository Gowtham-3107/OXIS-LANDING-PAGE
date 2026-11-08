target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

idx = c.find("k=D(async(...e)=>{C({isPressed:!1}),w(`P3R3KKP8c`)}),")
old_callbacks = "k=D(async(...e)=>{C({isPressed:!1}),w(`P3R3KKP8c`)}),j=D(async(...e)=>{C({isPressed:!1}),w(`VGTB2Hl4I`)}),N=D(async(...e)=>{C({isPressed:!1}),w(`YEirLylRn`)}),te=D(async(...e)=>{C({isPressed:!1}),w(`sY87UdMrX`)}),re=D(async(...e)=>{w(`fhjWX54rY`)}),ie=D(async(...e)=>{w(`sY87UdMrX`)}),ae=D(async(...e)=>{w(`q9_mroeNK`)}),P=D(async(...e)=>{w(`uIHRARi0D`)}),oe=D(async(...e)=>{w(`x0h1i3LQK`)}),F=D(async(...e)=>{w(`P3R3KKP8c`)}),I=D(async(...e)=>{w(`Kd3eWdvd_`)}),se=D(async(...e)=>{w(`ebUSgHhHF`)}),L=D(async(...e)=>{w(`ZCrTK8zdE`)}),ce=D(async(...e)=>{w(`VGTB2Hl4I`)}),le=D(async(...e)=>{w(`N4EYEMTDA`)}),ue=D(async(...e)=>{w(`k7BjyTGUH`)}),de=D(async(...e)=>{w(`VrAkDQYUs`)}),fe=D(async(...e)=>{w(`YEirLylRn`)}),pe=D(async(...e)=>{w(`M7DTDgCQU`)}),me=D(async(...e)=>{w(`OQjlpokW9`)}),"

print("Found exact block?", old_callbacks in c)

