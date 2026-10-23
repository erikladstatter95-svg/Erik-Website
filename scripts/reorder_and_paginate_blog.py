import re

ORDER_SLUGS = [
    'por-que-tener-una-pagina-web',
    'paginas-web-personal-trainers-gimnasios',
    'paginas-web-salones-eventos-catering',
    'paginas-web-salones-belleza-estetica',
    'paginas-web-estudios-contables-argentina',
    'paginas-web-oficios-servicios-hogar',
    'paginas-web-para-psicologos-argentina',
    'que-negocios-necesitan-una-pagina-web',
    'como-automatizar-turnos-consultorio',
    'paginas-web-para-abogados-argentina',
    'pagina-web-vs-instagram',
    'como-conseguir-clientes-google-maps',
    'cuanto-cuesta-una-pagina-web-argentina'
]

def reorder_and_paginate():
    with open('blog/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract all articles
    # Matching <article class="blog-card ...> ... </article>
    pattern = re.compile(r'(<!-- ARTÍCULO \d+:.*?-->\s*<article class="blog-card.*?</article>)', re.DOTALL)
    matches = pattern.findall(html)
    
    if len(matches) < 13:
        # Fallback regex if comments differ slightly
        pattern = re.compile(r'(<article class="blog-card.*?</article>)', re.DOTALL)
        matches = pattern.findall(html)

    print(f"Total articles found: {len(matches)}")

    # Map by slug
    card_by_slug = {}
    for m in matches:
        for slug in ORDER_SLUGS:
            if f'/blog/{slug}/' in m:
                card_by_slug[slug] = m
                break

    print(f"Mapped {len(card_by_slug)} of {len(ORDER_SLUGS)} articles.")

    # Rebuild cards string in exact newest-first order
    reordered_cards = []
    for i, slug in enumerate(ORDER_SLUGS):
        if slug in card_by_slug:
            card_html = card_by_slug[slug]
            # Update comment number
            clean_card = re.sub(r'<!-- ARTÍCULO \d+:', f'<!-- ARTÍCULO {i+1}:', card_html)
            reordered_cards.append(clean_card)
        else:
            print(f"Warning: missing slug {slug}")

    new_cards_html = '\n\n          '.join(reordered_cards)

    # Replace grid content
    grid_pattern = re.compile(r'(<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8" id="blog-grid">).*?(</div>\s*<!-- ESTADO VACÍO)', re.DOTALL)
    
    replacement_grid = f'''\\1
          {new_cards_html}
        </div>

        <!-- PAGINACIÓN APPLE STYLE -->
        <nav id="blog-pagination" class="flex items-center justify-center gap-2 mt-12 pt-8 border-t border-black/[0.06] text-xs font-semibold" aria-label="Paginación de guías">
          <!-- Se renderiza dinámicamente por JavaScript -->
        </nav>

        <!-- ESTADO VACÍO'''

    html = grid_pattern.sub(replacement_grid, html)

    # Now update the script with pagination support
    new_script = '''  <!-- SCRIPT DE BÚSQUEDA, FILTRADO Y PAGINACIÓN CON PROTECCIÓN CONTRA INYECCIONES -->
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const searchInput = document.getElementById('blog-search-input');
      const searchClear = document.getElementById('blog-search-clear');
      const catSelect = document.getElementById('blog-cat-select');
      const articles = Array.from(document.querySelectorAll('.blog-card'));
      const emptyState = document.getElementById('blog-empty-state');
      const counter = document.getElementById('articles-counter');
      const resetBtn = document.getElementById('btn-reset-filters');
      const paginationNav = document.getElementById('blog-pagination');
      const grid = document.getElementById('blog-grid');

      const ITEMS_PER_PAGE = 12;
      let currentPage = 1;
      let currentCategory = 'all';

      // Sanitizador seguro contra inyecciones XSS / HTML / caracteres maliciosos
      function sanitizeInput(str) {
        if (!str) return '';
        return str
          .replace(/[<>"'`;()&]/g, '')
          .trim()
          .toLowerCase();
      }

      function renderPagination(totalItems, totalPages) {
        if (!paginationNav) return;

        if (totalPages <= 1) {
          paginationNav.innerHTML = '';
          paginationNav.classList.add('hidden');
          return;
        }

        paginationNav.classList.remove('hidden');
        let html = '';

        // Botón Anterior
        const prevDisabled = currentPage === 1;
        html += `
          <button class="px-3.5 py-2 rounded-full border ${prevDisabled ? 'border-neutral-200 text-neutral-300 cursor-not-allowed bg-neutral-50' : 'border-black/[0.08] text-neutral-700 hover:bg-neutral-100 bg-white cursor-pointer'} transition-all flex items-center gap-1"
                  ${prevDisabled ? 'disabled' : ''} 
                  data-page="${currentPage - 1}">
            <span>‹</span>
            <span>Anterior</span>
          </button>
        `;

        // Botones de Páginas
        for (let p = 1; p <= totalPages; p++) {
          const isActive = p === currentPage;
          html += `
            <button class="w-9 h-9 rounded-full ${isActive ? 'bg-neutral-900 text-white shadow-2xs font-bold' : 'bg-white border border-black/[0.08] text-neutral-600 hover:bg-neutral-50 cursor-pointer'} transition-all"
                    data-page="${p}">
              ${p}
            </button>
          `;
        }

        // Botón Siguiente
        const nextDisabled = currentPage === totalPages;
        html += `
          <button class="px-3.5 py-2 rounded-full border ${nextDisabled ? 'border-neutral-200 text-neutral-300 cursor-not-allowed bg-neutral-50' : 'border-black/[0.08] text-neutral-700 hover:bg-neutral-100 bg-white cursor-pointer'} transition-all flex items-center gap-1"
                  ${nextDisabled ? 'disabled' : ''} 
                  data-page="${currentPage + 1}">
            <span>Siguiente</span>
            <span>›</span>
          </button>
        `;

        paginationNav.innerHTML = html;

        // Listeners para los botones de paginación
        paginationNav.querySelectorAll('button[data-page]').forEach(btn => {
          btn.addEventListener('click', () => {
            const targetPage = parseInt(btn.getAttribute('data-page'), 10);
            if (!isNaN(targetPage) && targetPage >= 1 && targetPage <= totalPages && targetPage !== currentPage) {
              currentPage = targetPage;
              filterArticles(false);
              // Scroll suave al inicio del grid
              grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
          });
        });
      }

      function filterArticles(resetPage = true) {
        if (resetPage) {
          currentPage = 1;
        }

        const query = sanitizeInput(searchInput.value);

        // 1. Filtrar artículos que coinciden con categoría y búsqueda
        const matchingCards = [];
        articles.forEach((card) => {
          const cardCat = card.getAttribute('data-cat') || '';
          const cardTitle = (card.getAttribute('data-title') || '').toLowerCase();
          const cardDesc = (card.getAttribute('data-desc') || '').toLowerCase();

          const matchesCat = currentCategory === 'all' || cardCat === currentCategory;
          const matchesQuery = query === '' || cardTitle.includes(query) || cardDesc.includes(query);

          if (matchesCat && matchesQuery) {
            matchingCards.push(card);
          } else {
            card.classList.add('hidden');
          }
        });

        const totalItems = matchingCards.length;
        const totalPages = Math.ceil(totalItems / ITEMS_PER_PAGE) || 1;

        if (currentPage > totalPages) {
          currentPage = 1;
        }

        // 2. Aplicar paginación a los artículos que coincidieron
        const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
        const endIndex = startIndex + ITEMS_PER_PAGE;

        matchingCards.forEach((card, idx) => {
          if (idx >= startIndex && idx < endIndex) {
            card.classList.remove('hidden');
          } else {
            card.classList.add('hidden');
          }
        });

        // 3. Alternar botón de limpieza de input
        if (searchInput.value.length > 0) {
          searchClear.classList.remove('hidden');
        } else {
          searchClear.classList.add('hidden');
        }

        // 4. Estado vacío
        if (totalItems === 0) {
          emptyState.classList.remove('hidden');
        } else {
          emptyState.classList.add('hidden');
        }

        // 5. Contador detallado
        if (counter) {
          if (totalItems === 0) {
            counter.textContent = 'Sin resultados';
          } else if (totalItems <= ITEMS_PER_PAGE) {
            counter.textContent = totalItems === 1 
              ? 'Mostrando 1 guía' 
              : `Mostrando ${totalItems} guías`;
          } else {
            const shownStart = startIndex + 1;
            const shownEnd = Math.min(endIndex, totalItems);
            counter.textContent = `Mostrando ${shownStart}-${shownEnd} de ${totalItems} guías (Página ${currentPage} de ${totalPages})`;
          }
        }

        // 6. Renderizar botones de paginación
        renderPagination(totalItems, totalPages);
      }

      // Eventos de Input
      if (searchInput) {
        searchInput.addEventListener('input', () => filterArticles(true));
      }

      if (searchClear) {
        searchClear.addEventListener('click', () => {
          searchInput.value = '';
          searchInput.focus();
          filterArticles(true);
        });
      }

      // Evento de Selector Desplegable de Categoría
      if (catSelect) {
        catSelect.addEventListener('change', () => {
          currentCategory = catSelect.value || 'all';

          const url = new URL(window.location);
          if (currentCategory === 'all') {
            url.searchParams.delete('cat');
          } else {
            url.searchParams.set('cat', currentCategory);
          }
          window.history.replaceState({}, '', url);

          filterArticles(true);
        });
      }

      // Resetear filtros
      if (resetBtn) {
        resetBtn.addEventListener('click', () => {
          searchInput.value = '';
          if (catSelect) {
            catSelect.value = 'all';
          }
          currentCategory = 'all';
          const url = new URL(window.location);
          url.searchParams.delete('cat');
          window.history.replaceState({}, '', url);
          filterArticles(true);
        });
      }

      // Soporte para URL con parámetro inicial (ej: /blog/?cat=precios)
      const urlParams = new URLSearchParams(window.location.search);
      const initialCat = sanitizeInput(urlParams.get('cat'));
      if (initialCat && catSelect) {
        const optionExists = Array.from(catSelect.options).some(opt => opt.value === initialCat);
        if (optionExists) {
          catSelect.value = initialCat;
          currentCategory = initialCat;
        }
      }

      // Filtrado y paginación inicial
      filterArticles(false);
    });
  </script>'''

    script_pattern = re.compile(r'<!-- SCRIPT DE BÚSQUEDA Y FILTRADO.*?<\/script>', re.DOTALL)
    html = script_pattern.sub(new_script, html)

    with open('blog/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("blog/index.html reordenado cronológicamente y paginación añadida con éxito!")

if __name__ == '__main__':
    reorder_and_paginate()
