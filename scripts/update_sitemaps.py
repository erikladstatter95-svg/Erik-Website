"""
Update sitemap.xml and public/sitemap.xml with English version and xhtml:link alternates.
"""

for s_path in ['public/sitemap.xml', 'sitemap.xml']:
    with open(s_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add xmlns:xhtml if not present
    if 'xmlns:xhtml' not in content:
        content = content.replace(
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n        xmlns:xhtml="http://www.w3.org/1999/xhtml">'
        )

    # Add English url block right after main url
    en_block = """  <!-- Versión en Inglés (Internacional) -->
  <url>
    <loc>https://erikwebsite.com/en/</loc>
    <lastmod>2026-03-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
    <xhtml:link rel="alternate" hreflang="es" href="https://erikwebsite.com/" />
    <xhtml:link rel="alternate" hreflang="en" href="https://erikwebsite.com/en/" />
  </url>
"""
    if 'https://erikwebsite.com/en/' not in content:
        content = content.replace('  <!-- Hub del Blog -->', en_block + '\n  <!-- Hub del Blog -->')

    # Update Spanish main url with xhtml alternates
    old_es = """  <url>
    <loc>https://erikwebsite.com/</loc>
    <lastmod>2026-03-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>"""
    new_es = """  <url>
    <loc>https://erikwebsite.com/</loc>
    <lastmod>2026-03-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
    <xhtml:link rel="alternate" hreflang="es" href="https://erikwebsite.com/" />
    <xhtml:link rel="alternate" hreflang="en" href="https://erikwebsite.com/en/" />
  </url>"""
    if old_es in content:
        content = content.replace(old_es, new_es)

    with open(s_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Successfully updated {s_path}')
