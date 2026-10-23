"""
Inject demo-i18n.js script tag into all demo index.html files.
"""
import glob

script_tag = '  <!-- Script de Adaptación de Moneda / Idioma (USD / ARS) -->\n  <script src="/src/js/demo-i18n.js"></script>\n'
modified = 0

for f in glob.glob('demos/**/*.html', recursive=True):
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    if 'demo-i18n.js' not in content:
        if '</head>' in content:
            content = content.replace('</head>', script_tag + '</head>')
            with open(f, 'w', encoding='utf-8') as fp:
                fp.write(content)
            modified += 1

print(f"Injected demo-i18n.js in {modified} demo files.")
