with open("cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/script_main.Dvcfic8j.mjs", "r", encoding="utf-8") as f:
    orig = f.read()
with open("cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/script_main.Dvcfic8j.mjs", "r", encoding="utf-8") as f:
    c = f.read()

import re
print("Matches for https://framer.com:", len(re.findall(r'https://framer\.com', c)))
print("Matches for https://framerusercontent.com:", len(re.findall(r'https://framerusercontent\.com', c)))
print("Matches for framerusercontent:", len(re.findall(r'framerusercontent', c)))
for line in c.split(';'):
    if 'document' in line or 'window' in line or 'hydrate' in line or 'render' in line or 'catch' in line:
        if len(line) < 300:
            print("Line:", line.strip())

