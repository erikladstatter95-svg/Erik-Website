import glob

for f in glob.glob('demos/**/*.html', recursive=True):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if '<script src="/src/js/demo-i18n.js"></script>' in c:
        c = c.replace('<script src="/src/js/demo-i18n.js"></script>', '<script type="module" src="/src/js/demo-i18n.js"></script>')
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)

print('Updated script tags with type="module"')
