import os
import re
import urllib.request

img_pattern = re.compile(r'<img[^>]+src=["' + "'](https?://[^\"']+)[\"']", re.IGNORECASE)
bg_pattern = re.compile(r'url\(["' + "']?(https?://[^\"'\)]+)[\"']?\)", re.IGNORECASE)

urls_map = {}
for root, dirs, files in os.walk('.'):
    if any(x in root for x in ['node_modules', '.git', 'dist']):
        continue
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
                for url in img_pattern.findall(content):
                    urls_map.setdefault(url, []).append(path)
                for url in bg_pattern.findall(content):
                    urls_map.setdefault(url, []).append(path)

print(f"Total unique URLs to test: {len(urls_map)}")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

broken = []
for url, paths in urls_map.items():
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=7) as resp:
            if resp.status != 200:
                print(f"BROKEN [{resp.status}]: {url} -> {paths}")
                broken.append((url, resp.status, paths))
    except Exception as e:
        print(f"ERROR [{e}]: {url} -> {paths}")
        broken.append((url, str(e), paths))

print(f"\nScan complete. Total broken URLs: {len(broken)}")
