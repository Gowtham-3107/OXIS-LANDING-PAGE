import os
import re

with open("cloned_site/index_fresh_original.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace https://framerusercontent.com/ with /cloned_site/assets/framerusercontent.com/
# or relative paths ./assets/framerusercontent.com/
# Let's use relative "./assets/..." so it works from anywhere

# 1. Update <script type="module" ... src="...">
html = re.sub(
    r'src="https://framerusercontent\.com/sites/RuE79Xrnx9TYtmvVF2nrg/script_main\.Dvcfic8j\.mjs"',
    r'src="./assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/script_main.Dvcfic8j.mjs"',
    html
)

# 2. Localize all framerusercontent.com asset urls in images, links, styles
# Keep the exact query parameters or strip them if already saved locally
def replace_asset(m):
    full = m.group(0)
    # clean backslashes
    clean = full.replace('\\/', '/')
    # Check if local file exists
    rel = clean.replace("https://framerusercontent.com/", "")
    clean_rel = rel.split("?")[0]
    local_f = os.path.join("cloned_site", "assets", "framerusercontent.com", clean_rel.replace("/", os.sep))
    if os.path.exists(local_f):
        return f"./assets/framerusercontent.com/{clean_rel}"
    return full

html = re.sub(r'https:\\?/\\?/framerusercontent\.com/[^\s"\'<>`,\)\\]+', replace_asset, html)

# 3. Localize gstatic fonts
def replace_gstatic(m):
    full = m.group(0).replace('\\/', '/')
    rel = full.replace("https://fonts.gstatic.com/", "")
    local_f = os.path.join("cloned_site", "assets", "fonts.gstatic.com", rel.replace("/", os.sep))
    if os.path.exists(local_f):
        return f"./assets/fonts.gstatic.com/{rel}"
    return full

html = re.sub(r'https:\\?/\\?/fonts\.gstatic\.com/[^\s"\'<>`,\)\\]+', replace_gstatic, html)

# 4. Save to index_live.html and index_offline.html
with open("cloned_site/index_live.html", "w", encoding="utf-8") as f:
    f.write(html)
with open("cloned_site/index_offline.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Created cloned_site/index_live.html and updated index_offline.html with complete hydration pipeline!")

