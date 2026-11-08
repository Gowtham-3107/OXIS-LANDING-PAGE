import urllib.request
import re

req = urllib.request.Request("https://agen-ai.framer.website/", headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
})
with urllib.request.urlopen(req) as resp:
    fresh_html = resp.read().decode('utf-8', errors='ignore')

# Save fresh original for comparison
with open("cloned_site/index_fresh_original.html", "w", encoding="utf-8") as f:
    f.write(fresh_html)

print("Fresh HTML downloaded, length:", len(fresh_html))

# Compare script #7 or script #4 appear animator
scripts = re.findall(r'<script\b[^>]*>.*?</script>', fresh_html, flags=re.DOTALL)
print(f"Scripts in fresh live site: {len(scripts)}")
for i, s in enumerate(scripts):
    open_tag = s[:s.find('>')+1]
    print(f"#{i}: {open_tag}")

