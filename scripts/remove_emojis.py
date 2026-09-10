import os
import glob
import re

svg_favicon = '<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22><rect width=%2232%22 height=%2232%22 rx=%228%22 fill=%22%23059669%22/><text x=%2216%22 y=%2222%22 font-family=%22sans-serif%22 font-size=%2218%22 font-weight=%22900%22 fill=%22white%22 text-anchor=%22middle%22>E</text></svg>">'

replacements = [
    # Favicons
    (r'<link rel="icon" href="data:image/svg\+xml,[^"]+">', svg_favicon),
    # Switcher button
    (r'<span>🏠\s*Salir al Portfolio</span>', r'<span>Salir al Portfolio</span>'),
    (r'🏠\s*Salir al Portfolio', r'Salir al Portfolio'),
    # Odontologia
    (r'<span class="text-2xl block mb-2">🦷</span>', ''),
    (r'<span class="text-2xl block mb-2">🔩</span>', ''),
    (r'<span class="text-2xl block mb-2">💎</span>', ''),
    (r'<div class="w-9 h-9 rounded-xl bg-cyan-100 flex items-center justify-center font-bold text-lg text-cyan-700">🦷</div>', r'<div class="w-9 h-9 rounded-xl bg-cyan-600 text-white flex items-center justify-center font-bold text-sm">D</div>'),
    (r'<span[^>]*>🦷</span>', ''),
    # Psicologia
    (r'<span class="text-2xl block mb-2">🛋️?</span>', ''),
    (r'<span class="text-2xl block mb-2">💻</span>', ''),
    (r'<div class="w-9 h-9 rounded-xl bg-emerald-100 flex items-center justify-center font-bold text-lg text-emerald-800">🌱</div>', r'<div class="w-9 h-9 rounded-xl bg-emerald-700 text-white flex items-center justify-center font-bold text-sm">P</div>'),
    (r'<span>🌱</span>', ''),
    # Catering
    (r'<span class="text-3xl block mb-3">🥩</span>', ''),
    (r'<span class="text-3xl block mb-3">🍸</span>', ''),
    (r'<span class="text-3xl block mb-3">🍹</span>', ''),
    (r'<div class="w-9 h-9 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold text-lg border border-amber-500/30">🔥</div>', r'<div class="w-9 h-9 rounded-xl bg-amber-500 text-zinc-950 flex items-center justify-center font-bold text-sm">C</div>'),
    (r'<span>🔥</span>', ''),
    # Vajilla
    (r'<span>🍽️?</span>', ''),
    (r'<div class="w-9 h-9 rounded-xl bg-amber-100 text-amber-800 flex items-center justify-center font-bold text-lg">🍷</div>', r'<div class="w-9 h-9 rounded-xl bg-amber-600 text-white flex items-center justify-center font-bold text-sm">V</div>'),
    # Salones
    (r'<span>🌿</span>', ''),
    (r'<div class="w-9 h-9 rounded-xl bg-emerald-100 text-emerald-800 flex items-center justify-center font-bold text-lg">🌿</div>', r'<div class="w-9 h-9 rounded-xl bg-emerald-700 text-white flex items-center justify-center font-bold text-sm">S</div>'),
    # Contable
    (r'<span class="text-3xl block mb-3">💼</span>', ''),
    (r'<span class="text-3xl block mb-3">📊</span>', ''),
    (r'<div class="w-9 h-9 rounded-xl bg-blue-100 text-blue-700 flex items-center justify-center font-bold text-lg">📊</div>', r'<div class="w-9 h-9 rounded-xl bg-blue-600 text-white flex items-center justify-center font-bold text-sm">C</div>'),
    (r'<span>🛡️?</span>', ''),
    # Abogados
    (r'<span class="text-3xl block mb-3">💼</span>', ''),
    (r'<span class="text-3xl block mb-3">🚗</span>', ''),
    (r'<span class="text-3xl block mb-3">📜</span>', ''),
    (r'<p>📍\s*', r'<p>'),
    (r'<span>🏛️?</span>', ''),
    (r'📍', ''),
    (r'🏛️?', ''),
    (r'🏥', ''),
    (r'🏢', ''),
    (r'👨‍👩‍👦', ''),
    # Urgencias
    (r'📞\s*Llamar', 'Llamar'),
    (r'<span>🔧</span>', ''),
    (r'<span class="text-3xl block mb-3">🔌</span>', ''),
    (r'<span class="text-3xl block mb-3">🚰</span>', ''),
    (r'<span class="text-3xl block mb-3">🔥</span>', ''),
    (r'🔧', ''),
    (r'🕒', ''),
    (r'🅿️?', ''),
]

html_files = glob.glob('demos/**/*.html', recursive=True) + glob.glob('*.html')

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content)

    # General regex cleanup for any remaining 4-byte UTF-8 emoji
    content = re.sub(r'[\U00010000-\U0010ffff]', '', content)

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Cleaned emojis in: {fpath}')

print('Emoji cleanup script complete.')
