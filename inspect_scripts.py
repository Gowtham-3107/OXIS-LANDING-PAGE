with open("cloned_site/index_original.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
scripts = re.findall(r'<script\b[^>]*>.*?</script>', text, flags=re.DOTALL)
print(f"Total script tags: {len(scripts)}")
for i, s in enumerate(scripts):
    open_tag = s[:s.find('>')+1]
    body = s[s.find('>')+1:-9].strip()
    print(f"Script #{i}: {open_tag}")
    if len(body) < 300:
        print(f"   Body: {body}")
    else:
        print(f"   Body (truncated): {body[:150]}... [len {len(body)}]")

