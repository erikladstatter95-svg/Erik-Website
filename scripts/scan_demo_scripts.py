import glob
import re

for f in sorted(glob.glob('demos/**/index.html', recursive=True)):
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
        scripts = re.findall(r'<script[^>]*src=[\'"]([^\'"]+)[\'"]', content)
        print(f, scripts)
