"""
Clean blog navbars:
1. Remove "Demos en Vivo" and "Precios Claros" from all blog navbars (blog/index.html and all blog articles).
2. Add "San Juan" (/san-juan/) link into blog navbars.
3. Add "San Juan" (/san-juan/) into index.html navbar and banner so it's clearly connected.
"""
import glob
import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Add link in top banner
old_banner_text = '<span>Desarrollo web para comercios y profesionales en San Juan y toda Argentina | Entrega en 3 a 5 días hábiles</span>'
new_banner_text = '<span>Desarrollo web para comercios y profesionales en <a href="/san-juan/" class="underline font-semibold text-emerald-400 hover:text-emerald-300">San Juan</a> y toda Argentina | Entrega en 3 a 5 días hábiles</span>'
if old_banner_text in idx_content:
    idx_content = idx_content.replace(old_banner_text, new_banner_text)
    print("Updated index.html top banner")

# Add San Juan to navbar
old_idx_nav = """        <a href="#precios" class="hover:text-neutral-900 transition-colors">Precios Claros</a>
        <a href="/blog/" class="hover:text-emerald-600 transition-colors font-semibold text-emerald-700">Blog</a>"""

new_idx_nav = """        <a href="#precios" class="hover:text-neutral-900 transition-colors">Precios Claros</a>
        <a href="/san-juan/" class="hover:text-emerald-700 transition-colors font-semibold text-emerald-600">San Juan</a>
        <a href="/blog/" class="hover:text-emerald-600 transition-colors font-semibold text-neutral-600">Blog</a>"""

if old_idx_nav in idx_content:
    idx_content = idx_content.replace(old_idx_nav, new_idx_nav)
    print("Updated index.html navbar with San Juan link")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

# 2. Update blog/index.html
with open('blog/index.html', 'r', encoding='utf-8') as f:
    blog_idx = f.read()

# Replace navbar
old_blog_nav = """      <nav class="hidden md:flex items-center gap-6 text-sm font-medium text-neutral-600">
        <a href="/" class="hover:text-emerald-600 transition-colors">Inicio</a>
        <a href="/#demos" class="hover:text-emerald-600 transition-colors">Demos en Vivo</a>
        <a href="/#precios" class="hover:text-emerald-600 transition-colors">Precios Claros</a>
        <a href="/blog/" class="text-emerald-700 font-semibold border-b-2 border-emerald-600 pb-0.5">Blog y Guías</a>
      </nav>"""

new_blog_nav = """      <nav class="hidden md:flex items-center gap-6 text-sm font-medium text-neutral-600">
        <a href="/" class="hover:text-emerald-600 transition-colors">Inicio</a>
        <a href="/san-juan/" class="hover:text-emerald-600 transition-colors">San Juan</a>
        <a href="/blog/" class="text-emerald-700 font-semibold border-b-2 border-emerald-600 pb-0.5">Blog y Guías</a>
      </nav>"""

if old_blog_nav in blog_idx:
    blog_idx = blog_idx.replace(old_blog_nav, new_blog_nav)
    print("Updated blog/index.html navbar")

# Replace footer links
old_blog_footer = """        <a href="/" class="hover:text-emerald-400 transition-colors">Inicio</a>
        <a href="/#demos" class="hover:text-emerald-400 transition-colors">Demos</a>
        <a href="/#precios" class="hover:text-emerald-400 transition-colors">Precios</a>
        <a href="/blog/" class="text-emerald-400 font-medium">Blog</a>"""

new_blog_footer = """        <a href="/" class="hover:text-emerald-400 transition-colors">Inicio</a>
        <a href="/san-juan/" class="hover:text-emerald-400 transition-colors">San Juan</a>
        <a href="/blog/" class="text-emerald-400 font-medium">Blog y Guías</a>"""

if old_blog_footer in blog_idx:
    blog_idx = blog_idx.replace(old_blog_footer, new_blog_footer)
    print("Updated blog/index.html footer")

with open('blog/index.html', 'w', encoding='utf-8') as f:
    f.write(blog_idx)

# 3. Update all articles in blog/*/index.html
article_files = glob.glob('blog/*/index.html')
for apath in article_files:
    with open(apath, 'r', encoding='utf-8') as f:
        acontent = f.read()

    # Pattern for standard article navbar
    nav_pattern = r'<nav class="hidden md:flex items-center gap-6 text-sm font-medium text-slate-600">\s*<a href="/" class="hover:text-emerald-600 transition-colors">Inicio</a>\s*(?:<a href="/san-juan/".*?</a>\s*)?<a href="/#demos" class="hover:text-emerald-600 transition-colors">Demos en Vivo</a>\s*<a href="/#precios" class="hover:text-emerald-600 transition-colors">Precios Claros</a>\s*<a href="/blog/" class="text-emerald-700 font-semibold">Blog</a>\s*</nav>'
    
    clean_article_nav = """<nav class="hidden md:flex items-center gap-6 text-sm font-medium text-slate-600">
        <a href="/" class="hover:text-emerald-600 transition-colors">Inicio</a>
        <a href="/san-juan/" class="hover:text-emerald-600 transition-colors">San Juan</a>
        <a href="/blog/" class="text-emerald-700 font-semibold">Blog</a>
      </nav>"""

    new_acontent, count = re.subn(nav_pattern, clean_article_nav, acontent)
    if count > 0:
        with open(apath, 'w', encoding='utf-8') as f:
            f.write(new_acontent)
        print(f"Cleaned navbar in {apath}")
    else:
        # Check if already clean or different pattern
        if 'Demos en Vivo' in acontent:
            print(f"Warning: Demos en Vivo still present in {apath}")

print("All navbars updated successfully!")
