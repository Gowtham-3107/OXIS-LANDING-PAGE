target = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs"
with open(target, "r", encoding="utf-8") as f:
    c = f.read()

# Let's inspect each card's Do call:
# Card 1:
# children:v(To,{CLs9GwB8X:`Identify high-ROI use cases and define a realistic, measurable AI roadmap.`,ge1PTFTPQ:`Value model & KPI definition`,height:`100%`,hMkpbcu1u:`AI Strategy & Mapping`,id:`MEs6fvKPJ`,kcWMI5FgV:re,KDEMzn5iv:`(01)`,l55IL4lO3:`Data readiness assessment`,layoutId:`MEs6fvKPJ`,style:{width:`100%`},variant:Z(`E4zW3uRDc`),W7wkfakxg:`Stakeholder discovery`,width:`100%`,...Do({ebUSgHhHF:{kcWMI5FgV:P,variant:Z(`Iwa0VSQiG`)},k7BjyTGUH:{kcWMI5FgV:P,variant:Z(`Iwa0VSQiG`)},Kd3eWdvd_:{kcWMI5FgV:ae,variant:Z(`LEAAe9UyZ`)},M7DTDgCQU:{kcWMI5FgV:ae,variant:Z(`LEAAe9UyZ`)},N4EYEMTDA:{kcWMI5FgV:ae,variant:Z(`LEAAe9UyZ`)},OQjlpokW9:{kcWMI5FgV:P,variant:Z(`Iwa0VSQiG`)},P3R3KKP8c:{kcWMI5FgV:ie,variant:Z(`fgt6YYJhM`)},q9_mroeNK:{kcWMI5FgV:ae,variant:Z(`fiXmwAnq8`)},sY87UdMrX:{kcWMI5FgV:ie,variant:Z(`Tugc2bXAk`)},uIHRARi0D:{kcWMI5FgV:P},VGTB2Hl4I:{variant:Z(`fgt6YYJhM`)},VrAkDQYUs:{variant:Z(`Iwa0VSQiG`)},x0h1i3LQK:{variant:Z(`Iwa0VSQiG`)},YEirLylRn:{variant:Z(`fgt6YYJhM`)},ZCrTK8zdE:{variant:Z(`Iwa0VSQiG`)}},h,S)})

# Look at what is inside Do:
# ONLY kcWMI5FgV and variant!
# None of the other props (like title, description, key points) are changed inside Do (except on Tablet for Card 4 where title is `Data Engineering `)!
# That means if we replace `variant` and `kcWMI5FgV` directly with our clean state controller:
# Every card will have 100% independent open/close toggle!
print("Do content check verified.")
