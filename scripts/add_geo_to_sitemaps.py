"""
Add Geo landing San Juan and Regional Blog Guides to sitemap.xml and public/sitemap.xml
"""

geo_urls = """  <!-- Landing Geo Local: San Juan -->
  <url>
    <loc>https://erikwebsite.com/san-juan/</loc>
    <lastmod>2026-03-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.95</priority>
  </url>

  <!-- Guías Regionales Cuyo (SEO / GEO) -->
  <url>
    <loc>https://erikwebsite.com/blog/diseno-web-san-juan/</loc>
    <lastmod>2026-03-24</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.90</priority>
  </url>
  <url>
    <loc>https://erikwebsite.com/blog/diseno-web-mendoza/</loc>
    <lastmod>2026-03-24</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.90</priority>
  </url>
  <url>
    <loc>https://erikwebsite.com/blog/diseno-web-san-luis/</loc>
    <lastmod>2026-03-24</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.90</priority>
  </url>
"""

for path in ['sitemap.xml', 'public/sitemap.xml']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'https://erikwebsite.com/san-juan/' not in content:
        content = content.replace(
            '  <!-- Hub del Blog -->',
            geo_urls + '\n  <!-- Hub del Blog -->'
        )
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added Geo URLs to {path}")
    else:
        print(f"Geo URLs already present in {path}")
