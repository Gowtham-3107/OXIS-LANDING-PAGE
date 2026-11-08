import os
import re
import urllib.request

base_cdn = "https://framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg/"
target_dir = "cloned_site/assets/framerusercontent.com/sites/RuE79Xrnx9TYtmvVF2nrg"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

needed = [
    "KF7LKg6reUoK1qTKt0eKXi_94Gm-6RD9AdvlPUo_e8A.WBbl3AP5.mjs",
    "njw535iMlLnpnT_7lO84e4oS-pGyKg19GX-FnZynNg4.BlmL-tgm.mjs",
    "rg3GdFXHBje6nwXt2u4hztzHk7_FmYl-EBMT_T-vzhQ.DMwQQXfl.mjs",
    "lHHbxrI8d-SwzgoQubyUlrPZTfRV-aS7OXKy3CwDjBI.BMv0O-Tp.mjs",
    "kImSwm7VmJvlcXHEZSrWtFrA-kQaQUtmO-bh6Psp608.C4g16-ZX.mjs",
    "PX9hIOIVM.DXDAv_em.mjs"
]

for filename in needed:
    local_path = os.path.join(target_dir, filename)
    if not os.path.exists(local_path):
        url = base_cdn + filename
        print(f"Downloading {url} ...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                content = resp.read()
                with open(local_path, "wb") as f:
                    f.write(content)
            print(f"Saved {filename} ({len(content)} bytes)")
        except Exception as e:
            print(f"Failed to download {filename}: {e}")
    else:
        print(f"Already exists: {filename}")

