import os
import glob
import re

LIGHTBOX_MODAL_AND_SCRIPT = '''  <!-- LIGHTBOX / ZOOM MODAL (PANTALLA COMPLETA PARA MÓVILES Y DESKTOP) -->
  <div id="image-lightbox" class="fixed inset-0 z-50 bg-black/95 backdrop-blur-md flex items-center justify-center p-3 sm:p-6 opacity-0 pointer-events-none transition-opacity duration-200" role="dialog" aria-modal="true" aria-label="Visor de imagen">
    <button id="lightbox-close" class="absolute top-4 right-4 z-50 p-3 rounded-full bg-white/10 hover:bg-white/20 text-white backdrop-blur-md transition-colors cursor-pointer" aria-label="Cerrar imagen">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
    </button>
    <div class="relative max-w-5xl max-h-[92vh] overflow-auto rounded-2xl flex items-center justify-center">
      <img id="lightbox-img" src="" alt="Infografía ampliada" class="w-auto h-auto max-w-full max-h-[88vh] object-contain rounded-xl select-none shadow-2xl">
    </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const lightbox = document.getElementById('image-lightbox');
      const lightboxImg = document.getElementById('lightbox-img');
      const closeBtn = document.getElementById('lightbox-close');

      function openLightbox(src, alt) {
        if (!lightbox || !lightboxImg) return;
        lightboxImg.src = src;
        lightboxImg.alt = alt || 'Infografía ampliada';
        lightbox.classList.remove('opacity-0', 'pointer-events-none');
        lightbox.classList.add('opacity-100');
        document.body.style.overflow = 'hidden';
      }

      function closeLightbox() {
        if (!lightbox) return;
        lightbox.classList.add('opacity-0', 'pointer-events-none');
        lightbox.classList.remove('opacity-100');
        document.body.style.overflow = '';
      }

      // Activar lightbox en todas las imágenes zoomables e infografías
      document.querySelectorAll('.blog-zoomable-img').forEach(item => {
        item.addEventListener('click', () => {
          const img = item.querySelector('img');
          if (img) openLightbox(img.src, img.alt);
        });
      });

      // Detectar infografías dentro del cuerpo de texto que no tengan wrapper
      document.querySelectorAll('article img').forEach(img => {
        // Excluir avatares pequeños o cards recomendadas
        if (img.src.includes('/images/') && !img.closest('#image-lightbox') && !img.closest('.grid') && !img.classList.contains('w-8')) {
          if (!img.closest('.blog-zoomable-img')) {
            img.classList.add('cursor-zoom-in');
            img.addEventListener('click', () => openLightbox(img.src, img.alt));
          }
        }
      });

      if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
      if (lightbox) {
        lightbox.addEventListener('click', (e) => {
          if (e.target === lightbox || e.target.tagName === 'DIV') closeLightbox();
        });
      }
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeLightbox();
      });
    });
  </script>
</body>
</html>'''

PILL_BADGE_HTML = '''<div class="absolute bottom-3 right-3 sm:bottom-4 sm:right-4 inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-black/75 backdrop-blur-md text-white text-[11px] font-medium shadow-md pointer-events-none group-hover:bg-black/90 transition-colors">
            <svg class="w-3.5 h-3.5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v6m3-3H7"/></svg>
            <span>Tocar para ampliar</span>
          </div>'''

MOBILE_HINT_HTML = '''<p class="text-[11px] text-neutral-400 mt-2 text-center font-light sm:hidden">
          Tip: Tocá la infografía para verla en pantalla completa
        </p>'''

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Clean existing lightbox if re-running
    if 'id="image-lightbox"' in html:
        html = re.sub(r'<!-- LIGHTBOX.*?<\/html>', '</body>\n</html>', html, flags=re.DOTALL)

    # 2. Upgrade featured image container
    # Case A: Standard featured container in the 7 new articles
    # <div class="mb-10 rounded-3xl overflow-hidden border border-black/[0.06] shadow-sm bg-neutral-900">\s*<img src="(.*?)" alt="(.*?)" class="w-full h-auto object-cover"(.*?)>
    pattern_new = re.compile(
        r'<div class="mb-10 rounded-3xl overflow-hidden border border-black/\[0.06\] shadow-sm bg-neutral-900">\s*<img src="([^"]+)"\s+alt="([^"]+)"\s+class="w-full h-auto object-cover"([^>]*)>\s*</div>',
        re.DOTALL
    )
    if pattern_new.search(html):
        def repl_new(m):
            src, alt, extra = m.group(1), m.group(2), m.group(3)
            return f'''<div class="mb-10">
        <div class="blog-zoomable-img relative group cursor-zoom-in overflow-hidden rounded-3xl border border-black/[0.06] shadow-sm bg-neutral-900 transition-all hover:shadow-md">
          <img src="{src}" 
               alt="{alt}" 
               class="w-full h-auto object-cover group-hover:scale-[1.01] transition-transform duration-300 select-none"
               {extra}>
          {PILL_BADGE_HTML}
        </div>
        {MOBILE_HINT_HTML}
      </div>'''
        html = pattern_new.sub(repl_new, html)

    # Case B: Featured container in older articles
    # <div class="my-6 rounded-2xl overflow-hidden border border-slate-200 shadow-sm">\s*<img src="([^"]+)"\s+alt="([^"]+)"\s+class="w-full h-auto object-cover"([^>]*)>\s*</div>
    pattern_old = re.compile(
        r'<div class="my-6 rounded-2xl overflow-hidden border border-slate-200 shadow-sm">\s*<img src="([^"]+)"\s+alt="([^"]+)"\s+class="w-full h-auto object-cover"([^>]*)>\s*</div>',
        re.DOTALL
    )
    if pattern_old.search(html):
        def repl_old(m):
            src, alt, extra = m.group(1), m.group(2), m.group(3)
            return f'''<div class="my-6">
          <div class="blog-zoomable-img relative group cursor-zoom-in overflow-hidden rounded-2xl border border-slate-200 shadow-sm bg-slate-900 transition-all hover:shadow-md">
            <img src="{src}" 
                 alt="{alt}" 
                 class="w-full h-auto object-cover group-hover:scale-[1.01] transition-transform duration-300 select-none"
                 {extra}>
            {PILL_BADGE_HTML}
          </div>
          {MOBILE_HINT_HTML}
        </div>'''
        html = pattern_old.sub(repl_old, html)

    # 3. Optimize Mobile Typography & Spacing
    # Ensure H1 is responsive (text-2xl sm:text-4xl md:text-5xl or lg:text-5xl)
    html = re.sub(r'class="text-3xl sm:text-4xl md:text-5xl', 'class="text-2xl sm:text-4xl md:text-5xl', html)
    html = re.sub(r'class="text-3xl sm:text-4xl lg:text-5xl', 'class="text-2xl sm:text-4xl lg:text-5xl', html)

    # 4. Append Lightbox Modal and Script before </body>
    if '</body>' in html:
        html = html.replace('</body>\n</html>', LIGHTBOX_MODAL_AND_SCRIPT)
        html = html.replace('</body></html>', LIGHTBOX_MODAL_AND_SCRIPT)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated lightbox in: {filepath}")

def main():
    articles = glob.glob('blog/*/index.html')
    print(f"Processing {len(articles)} blog articles...")
    for art in articles:
        process_file(art)

if __name__ == '__main__':
    main()
