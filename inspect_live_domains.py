with open("cloned_site/index_live.html", "r", encoding="utf-8") as f:
    c = f.read()

import re
all_urls = re.findall(r'https?://[^\s"\'<>`,\)\\]+', c)
from collections import Counter
domains = Counter()
for u in all_urls:
    from urllib.parse import urlparse
    domains[urlparse(u).netloc] += 1

print("Domains in index_live.html:")
for d, count in domains.most_common():
    print(f"  {d}: {count}")
