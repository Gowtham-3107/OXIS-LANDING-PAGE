with open("cloned_site/index_fresh_original.html", "r", encoding="utf-8") as f:
    orig = f.read()
with open("cloned_site/index_offline.html", "r", encoding="utf-8") as f:
    offline = f.read()

import re
orig_scripts = re.findall(r'<script\b[^>]*>.*?</script>', orig, flags=re.DOTALL)
offline_scripts = re.findall(r'<script\b[^>]*>.*?</script>', offline, flags=re.DOTALL)

for i in range(min(len(orig_scripts), len(offline_scripts))):
    s_orig = orig_scripts[i]
    s_off = offline_scripts[i]
    print(f"Script #{i} same? {s_orig == s_off}")
    if s_orig != s_off:
        print(f"  Orig: {s_orig[:100]} ... len={len(s_orig)}")
        print(f"  Off : {s_off[:100]} ... len={len(s_off)}")

