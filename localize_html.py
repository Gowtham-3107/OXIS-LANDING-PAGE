import os
import re

html_path = "cloned_site/index_original.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace framerusercontent asset URLs with relative local paths where downloaded
# Pattern 1: https://framerusercontent.com/images/<filename> -> assets/framerusercontent.com/images/<filename>
# Pattern 2: https://framerusercontent.com/assets/<filename> -> assets/framerusercontent.com/assets/<filename>
# Pattern 3: https://framerusercontent.com/sites/<filename> -> assets/framerusercontent.com/sites/<filename>

def replace_framer_urls(match):
    full_url = match.group(0)
    # clean backslash escapes if in JSON/script strings
    clean_url = full_url.replace('\\/', '/')
    
    # Check if we have this file downloaded locally
    parsed_path = clean_url.replace("https://framerusercontent.com/", "")
    local_target = os.path.join("cloned_site", "assets", "framerusercontent.com", parsed_path.split("?")[0].replace("/", os.sep))
    
    if os.path.exists(local_target):
        return f"/cloned_site/assets/framerusercontent.com/{parsed_path.split('?')[0]}"
    return full_url

# Match framerusercontent links
modified = re.sub(r'https:\\?/\\?/framerusercontent\.com/[^\s"\'<>`,\)]+', replace_framer_urls, content)

offline_html_path = "cloned_site/index_offline.html"
with open(offline_html_path, "w", encoding="utf-8") as f:
    f.write(modified)

print(f"Offline HTML created: {offline_html_path}")

