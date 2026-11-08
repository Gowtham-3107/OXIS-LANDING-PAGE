import os

target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

old_callbacks = "k=D(async(...e)=>{C({isPressed:!1}),w(`P3R3KKP8c`)}),j=D(async(...e)=>{C({isPressed:!1}),w(`VGTB2Hl4I`)}),N=D(async(...e)=>{C({isPressed:!1}),w(`YEirLylRn`)}),te=D(async(...e)=>{C({isPressed:!1}),w(`sY87UdMrX`)}),re=D(async(...e)=>{w(`fhjWX54rY`)}),ie=D(async(...e)=>{w(`sY87UdMrX`)}),ae=D(async(...e)=>{w(`q9_mroeNK`)}),P=D(async(...e)=>{w(`uIHRARi0D`)}),oe=D(async(...e)=>{w(`x0h1i3LQK`)}),F=D(async(...e)=>{w(`P3R3KKP8c`)}),I=D(async(...e)=>{w(`Kd3eWdvd_`)}),se=D(async(...e)=>{w(`ebUSgHhHF`)}),L=D(async(...e)=>{w(`ZCrTK8zdE`)}),ce=D(async(...e)=>{w(`VGTB2Hl4I`)}),le=D(async(...e)=>{w(`N4EYEMTDA`)}),ue=D(async(...e)=>{w(`k7BjyTGUH`)}),de=D(async(...e)=>{w(`VrAkDQYUs`)}),fe=D(async(...e)=>{w(`YEirLylRn`)}),pe=D(async(...e)=>{w(`M7DTDgCQU`)}),me=D(async(...e)=>{w(`OQjlpokW9`)}),"

# If current open variant is clicked, toggle it to the closed state variant:
# For Desktop:
# Card 1 open is `fhjWX54rY`, clicking its close button (P) -> switches to `uIHRARi0D` (all closed)
# If already in `fhjWX54rY` and re-clicked, or when clicked to close, stay closed!
# Specifically:
# re: opens card 1 -> if currently `fhjWX54rY`, toggle to `uIHRARi0D` (closed) else `fhjWX54rY`
# P: closes card 1 -> `uIHRARi0D`
# oe: opens card 2 -> if currently `x0h1i3LQK`, toggle to `ebUSgHhHF` else `x0h1i3LQK`
# se: closes card 2 -> `ebUSgHhHF`
# L: opens card 3 -> if currently `ZCrTK8zdE`, toggle to `k7BjyTGUH` else `ZCrTK8zdE`
# ue: closes card 3 -> `k7BjyTGUH`
# de: opens card 4 -> if currently `VrAkDQYUs`, toggle to `OQjlpokW9` else `VrAkDQYUs`
# me: closes card 4 -> `OQjlpokW9`

# Let's inspect how P, se, ue, me work:
# Notice in Framer's original code:
# When Card 1 is OPEN (`fhjWX54rY`), Card 1's kcWMI5FgV is `re`.
# When Card 1 is in variant `ebUSgHhHF`, Card 1's kcWMI5FgV is `P` (which set variant to `uIHRARi0D` -> meaning Card 1 closed!).
# BUT in `fhjWX54rY`, Card 1's kcWMI5FgV was `re`! And clicking `re` set `w('fhjWX54rY')`!
# So clicking an open card didn't close it, it just re-opened it, or switched to another.
# With toggle logic:
# When card 1 is clicked: if h === 'fhjWX54rY', close to 'uIHRARi0D', else open to 'fhjWX54rY'.
# When card 2 is clicked: if h === 'x0h1i3LQK', close to 'ebUSgHhHF', else open to 'x0h1i3LQK'.
# When card 3 is clicked: if h === 'ZCrTK8zdE', close to 'k7BjyTGUH', else open to 'ZCrTK8zdE'.
# When card 4 is clicked: if h === 'VrAkDQYUs', close to 'OQjlpokW9', else open to 'VrAkDQYUs'.

new_callbacks = """k=D(async(...e)=>{C({isPressed:!1}),w(h===`P3R3KKP8c`?`sY87UdMrX`:`P3R3KKP8c`)}),j=D(async(...e)=>{C({isPressed:!1}),w(h===`VGTB2Hl4I`?`sY87UdMrX`:`VGTB2Hl4I`)}),N=D(async(...e)=>{C({isPressed:!1}),w(h===`YEirLylRn`?`sY87UdMrX`:`YEirLylRn`)}),te=D(async(...e)=>{C({isPressed:!1}),w(`sY87UdMrX`)}),re=D(async(...e)=>{w(h===`fhjWX54rY`?`uIHRARi0D`:`fhjWX54rY`)}),ie=D(async(...e)=>{w(h===`sY87UdMrX`?`P3R3KKP8c`:`sY87UdMrX`)}),ae=D(async(...e)=>{w(h===`q9_mroeNK`?`Kd3eWdvd_`:`q9_mroeNK`)}),P=D(async(...e)=>{w(`uIHRARi0D`)}),oe=D(async(...e)=>{w(h===`x0h1i3LQK`?`uIHRARi0D`:`x0h1i3LQK`)}),F=D(async(...e)=>{w(h===`P3R3KKP8c`?`sY87UdMrX`:`P3R3KKP8c`)}),I=D(async(...e)=>{w(h===`Kd3eWdvd_`?`q9_mroeNK`:`Kd3eWdvd_`)}),se=D(async(...e)=>{w(`uIHRARi0D`)}),L=D(async(...e)=>{w(h===`ZCrTK8zdE`?`uIHRARi0D`:`ZCrTK8zdE`)}),ce=D(async(...e)=>{w(h===`VGTB2Hl4I`?`sY87UdMrX`:`VGTB2Hl4I`)}),le=D(async(...e)=>{w(h===`N4EYEMTDA`?`q9_mroeNK`:`N4EYEMTDA`)}),ue=D(async(...e)=>{w(`uIHRARi0D`)}),de=D(async(...e)=>{w(h===`VrAkDQYUs`?`uIHRARi0D`:`VrAkDQYUs`)}),fe=D(async(...e)=>{w(h===`YEirLylRn`?`sY87UdMrX`:`YEirLylRn`)}),pe=D(async(...e)=>{w(h===`M7DTDgCQU`?`q9_mroeNK`:`M7DTDgCQU`)}),me=D(async(...e)=>{w(`uIHRARi0D`)}),"""

assert old_callbacks in c, "Could not find old_callbacks"
c_new = c.replace(old_callbacks, new_callbacks)

with open(target, "w", encoding="utf-8") as f:
    f.write(c_new)

print("Successfully replaced accordion callbacks with true toggle & close behavior!")

