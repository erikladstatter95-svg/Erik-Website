import { initWhatsAppButtons } from '../../src/js/whatsapp.js';
import { initAccordion } from '../../src/js/accordion.js';
import { initScrollTop } from '../../src/js/scroll-top.js';
import { initScrollReveal, initHeroEntrance, initMobileDock, isReducedMotion } from '../../src/js/animations.js';
import { gsap } from 'gsap';

document.addEventListener('DOMContentLoaded', () => {
  const EVENT_PHONE = '5492645185359';

  initWhatsAppButtons(EVENT_PHONE);
  initAccordion('[data-accordion]');
  initScrollTop('btn-scroll-top');
  initHeroEntrance();
  initScrollReveal();
  initMobileDock();

  // Filtro interactivo de artículos con GSAP
  const filterBtns = document.querySelectorAll('.filter-tab');
  const productCards = document.querySelectorAll('.product-card');

  if (filterBtns.length > 0 && productCards.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => {
          b.classList.remove('bg-amber-700', 'text-white');
          b.classList.add('bg-stone-100', 'text-stone-700');
        });
        btn.classList.remove('bg-stone-100', 'text-stone-700');
        btn.classList.add('bg-amber-700', 'text-white');

        const filter = btn.getAttribute('data-filter');
        const visibleCards = [];

        productCards.forEach(card => {
          const matches = (filter === 'todos' || card.getAttribute('data-category') === filter);
          if (matches) {
            card.style.display = 'flex';
            visibleCards.push(card);
          } else {
            card.style.display = 'none';
          }
        });

        if (!isReducedMotion() && visibleCards.length > 0) {
          gsap.fromTo(visibleCards,
            { opacity: 0, y: 15 },
            { opacity: 1, y: 0, duration: 0.35, stagger: 0.05, ease: 'power2.out' }
          );
        }
      });
    });
  }

  // =========================================================================
  // COTIZADOR EN TIEMPO REAL DE VAJILLA Y MOBILIARIO -> WHATSAPP
  // =========================================================================
  const CATALOG_ITEMS = {
    copas_vino: {
      id: 'copas_vino',
      name: 'Copa de Vino y Agua Cristal',
      unitLabel: 'un.',
      price: 350,
      max: 1000
    },
    copas_champagne: {
      id: 'copas_champagne',
      name: 'Copa Flauta Champagne',
      unitLabel: 'un.',
      price: 380,
      max: 1000
    },
    platos_playos: {
      id: 'platos_playos',
      name: 'Plato Playo Porcelana y Oro',
      unitLabel: 'un.',
      price: 450,
      max: 1000
    },
    cubiertos_acero: {
      id: 'cubiertos_acero',
      name: 'Set Cubiertos Premium (3 piezas)',
      unitLabel: 'juegos',
      price: 420,
      max: 1000
    },
    manteles_lino: {
      id: 'manteles_lino',
      name: 'Mantel Redondo Lino (3m)',
      unitLabel: 'un.',
      price: 3200,
      max: 200
    },
    servilletas_tela: {
      id: 'servilletas_tela',
      name: 'Servilletas de Tela 45x45 cm',
      unitLabel: 'un.',
      price: 280,
      max: 1000
    },
    living_nordico: {
      id: 'living_nordico',
      name: 'Juego de Living Nórdico (10 pers.)',
      unitLabel: 'sets',
      price: 18500,
      max: 50
    },
    guirnaldas_luces: {
      id: 'guirnaldas_luces',
      name: 'Guirnaldas Kermesse Luces (20m)',
      unitLabel: 'tramos',
      price: 8500,
      max: 50
    }
  };

  // Pre-cargamos el ejemplo que pidió el usuario (10 copas, 20 juegos de cubiertos, 2 manteles redondos)
  // para que apenas entre vea el cotizador vivo funcionando y pueda modificarlo a gusto.
  const state = {
    quantities: {
      copas_vino: 10,
      copas_champagne: 0,
      platos_playos: 0,
      cubiertos_acero: 20,
      manteles_lino: 2,
      servilletas_tela: 0,
      living_nordico: 0,
      guirnaldas_luces: 0
    }
  };

  const formatARS = (num) => '$' + Math.round(num).toLocaleString('es-AR');

  const dateInput = document.getElementById('quote-date');
  const zoneSelect = document.getElementById('quote-zone');
  const itemsListEl = document.getElementById('quote-items-list');
  const totalPriceEl = document.getElementById('quote-total-price');
  const badgeCountEl = document.getElementById('quote-badge-count');
  const waPreviewEl = document.getElementById('quote-wa-preview');
  const sendBtn = document.getElementById('btn-send-custom-quote');
  const mobileQuoteTotalEl = document.getElementById('mobile-dock-total');

  function buildWhatsAppMessage() {
    const selected = [];
    let totalAmount = 0;
    let totalPieces = 0;

    Object.values(CATALOG_ITEMS).forEach(item => {
      const qty = state.quantities[item.id] || 0;
      if (qty > 0) {
        const sub = qty * item.price;
        totalAmount += sub;
        totalPieces += qty;
        selected.push({
          ...item,
          qty,
          sub
        });
      }
    });

    const dateVal = dateInput && dateInput.value.trim() ? dateInput.value.trim() : 'A confirmar';
    const zoneVal = zoneSelect && zoneSelect.value ? zoneSelect.value : 'Gran San Juan';

    if (selected.length === 0) {
      return {
        selected,
        totalAmount: 0,
        totalPieces: 0,
        text: 'Hola Vajilla y Estilo! Quisiera consultar disponibilidad y cotizar alquiler de vajilla para un evento en San Juan.'
      };
    }

    const lines = [
      'Hola Vajilla y Estilo! Armé mi cotización a medida en la web:',
      ''
    ];

    selected.forEach(s => {
      lines.push(`• ${s.qty}x ${s.name} (${formatARS(s.price)} c/u) = ${formatARS(s.sub)}`);
    });

    lines.push('');
    lines.push(`*Total estimado alquiler: ${formatARS(totalAmount)} ARS*`);
    lines.push(`• Fecha del evento: ${dateVal}`);
    lines.push(`• Entrega: ${zoneVal}`);
    lines.push('');
    lines.push('¿Tienen disponibilidad para reservar estas cantidades?');

    return {
      selected,
      totalAmount,
      totalPieces,
      text: lines.join('\n')
    };
  }

  function renderQuoteUI() {
    // 1. Sincronizar todos los inputs y subtotales en tarjetas
    Object.values(CATALOG_ITEMS).forEach(item => {
      const qty = state.quantities[item.id] || 0;
      const sub = qty * item.price;

      document.querySelectorAll(`[data-qty-input="${item.id}"]`).forEach(inp => {
        if (document.activeElement !== inp) {
          inp.value = qty;
        } else {
          inp.value = qty;
        }
      });

      document.querySelectorAll(`[data-card-subtotal="${item.id}"]`).forEach(el => {
        el.textContent = qty > 0 ? `Subtotal: ${formatARS(sub)}` : '$0';
        if (qty > 0) {
          el.classList.add('bg-amber-100', 'px-2', 'py-0.5', 'rounded-md');
        } else {
          el.classList.remove('bg-amber-100', 'px-2', 'py-0.5', 'rounded-md');
        }
      });

      const card = document.querySelector(`.product-card[data-item-id="${item.id}"]`);
      if (card) {
        if (qty > 0) {
          card.classList.add('ring-2', 'ring-amber-600', 'border-amber-600');
        } else {
          card.classList.remove('ring-2', 'ring-amber-600', 'border-amber-600');
        }
      }
    });

    // 2. Actualizar lista y totales
    const summary = buildWhatsAppMessage();

    if (badgeCountEl) {
      badgeCountEl.textContent = `${summary.totalPieces} ${summary.totalPieces === 1 ? 'pieza seleccionada' : 'piezas seleccionadas'}`;
    }

    if (totalPriceEl) {
      totalPriceEl.textContent = `${formatARS(summary.totalAmount)} ARS`;
    }

    if (mobileQuoteTotalEl) {
      mobileQuoteTotalEl.textContent = summary.totalAmount > 0
        ? `Tu lista: ${formatARS(summary.totalAmount)} (${summary.totalPieces} ítem/s)`
        : 'Seleccioná tus cantidades';
    }

    if (itemsListEl) {
      if (summary.selected.length === 0) {
        itemsListEl.innerHTML = `
          <div class="p-4 rounded-xl bg-stone-950/60 border border-stone-800/80 text-center text-stone-400">
            Todavía no sumaste artículos. Usá los botones <strong>+1</strong> o <strong>+10</strong> para armar tu lista en vivo.
          </div>
        `;
      } else {
        itemsListEl.innerHTML = summary.selected.map(s => `
          <div class="flex items-center justify-between gap-2 py-2 px-3 rounded-xl bg-stone-950/80 border border-stone-800">
            <div class="min-w-0">
              <span class="font-bold text-amber-400 tabular-nums">${s.qty}x</span>
              <span class="text-stone-100 font-medium ml-1">${s.name}</span>
              <span class="text-[11px] text-stone-400 block">${formatARS(s.price)} por ${s.unitLabel}</span>
            </div>
            <div class="flex items-center gap-2 shrink-0">
              <span class="font-bold text-white tabular-nums">${formatARS(s.sub)}</span>
              <button type="button" data-remove-item="${s.id}" class="text-stone-400 hover:text-red-400 p-1 cursor-pointer" title="Quitar artículo" aria-label="Quitar ${s.name}">✕</button>
            </div>
          </div>
        `).join('');

        itemsListEl.querySelectorAll('[data-remove-item]').forEach(btn => {
          btn.addEventListener('click', () => {
            const id = btn.getAttribute('data-remove-item');
            state.quantities[id] = 0;
            renderQuoteUI();
          });
        });
      }
    }

    if (waPreviewEl) {
      waPreviewEl.textContent = summary.text;
    }
  }

  // Eventos de botones step (-10, -1, +1, +10)
  document.querySelectorAll('[data-step-id]').forEach(btn => {
    btn.addEventListener('click', () => {
      const id = btn.getAttribute('data-step-id');
      const step = parseInt(btn.getAttribute('data-step') || '0', 10);
      const item = CATALOG_ITEMS[id];
      if (!item) return;
      const current = state.quantities[id] || 0;
      const next = Math.max(0, Math.min(item.max, current + step));
      state.quantities[id] = next;
      renderQuoteUI();
    });
  });

  // Eventos de inputs numéricos directos
  document.querySelectorAll('[data-qty-input]').forEach(inp => {
    inp.addEventListener('input', () => {
      const id = inp.getAttribute('data-qty-input');
      const item = CATALOG_ITEMS[id];
      if (!item) return;
      const parsed = parseInt(inp.value, 10);
      const next = isNaN(parsed) ? 0 : Math.max(0, Math.min(item.max, parsed));
      state.quantities[id] = next;
      renderQuoteUI();
    });
  });

  // Eventos de presets
  document.querySelectorAll('[data-preset]').forEach(btn => {
    btn.addEventListener('click', () => {
      const preset = btn.getAttribute('data-preset');
      Object.keys(state.quantities).forEach(k => { state.quantities[k] = 0; });

      if (preset === 'ejemplo_pedido') {
        state.quantities.copas_vino = 10;
        state.quantities.cubiertos_acero = 20;
        state.quantities.manteles_lino = 2;
      } else if (preset === 'cumple_50') {
        state.quantities.copas_vino = 50;
        state.quantities.copas_champagne = 50;
        state.quantities.platos_playos = 50;
        state.quantities.cubiertos_acero = 50;
        state.quantities.manteles_lino = 5;
        state.quantities.servilletas_tela = 50;
        state.quantities.living_nordico = 1;
        state.quantities.guirnaldas_luces = 1;
      }
      renderQuoteUI();
    });
  });

  if (dateInput) dateInput.addEventListener('input', renderQuoteUI);
  if (zoneSelect) zoneSelect.addEventListener('change', renderQuoteUI);

  if (sendBtn) {
    sendBtn.addEventListener('click', () => {
      const summary = buildWhatsAppMessage();
      const url = `https://wa.me/${EVENT_PHONE}?text=${encodeURIComponent(summary.text)}`;
      window.open(url, '_blank', 'noopener,noreferrer');
    });
  }

  // Inicializar vista del cotizador
  renderQuoteUI();
});
