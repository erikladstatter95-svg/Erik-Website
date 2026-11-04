import { initWhatsAppButtons } from '../../src/js/whatsapp.js';
import { initScrollTop } from '../../src/js/scroll-top.js';
import { initScrollReveal, initHeroEntrance, initMobileDock, isReducedMotion } from '../../src/js/animations.js';
import { gsap } from 'gsap';

document.addEventListener('DOMContentLoaded', () => {
  const RESTAURANT_PHONE = '5492645185359';

  initWhatsAppButtons(RESTAURANT_PHONE);
  initScrollTop('btn-scroll-top');
  initHeroEntrance();
  initScrollReveal();
  initMobileDock();

  // =========================================================================
  // 1. FILTRO DE CARTA DIGITAL CON GSAP
  // =========================================================================
  const menuTabs = document.querySelectorAll('.menu-tab');
  const menuCards = document.querySelectorAll('.menu-card');

  if (menuTabs.length > 0 && menuCards.length > 0) {
    menuTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        menuTabs.forEach(t => {
          t.classList.remove('bg-[#D4AF37]', 'text-zinc-950');
          t.classList.add('bg-[#16161D]', 'text-zinc-300', 'border', 'border-zinc-800');
        });
        tab.classList.remove('bg-[#16161D]', 'text-zinc-300', 'border', 'border-zinc-800');
        tab.classList.add('bg-[#D4AF37]', 'text-zinc-950');

        const filter = tab.getAttribute('data-menu-filter');
        const visible = [];

        menuCards.forEach(card => {
          const matches = (filter === 'todos' || card.getAttribute('data-menu-cat') === filter);
          if (matches) {
            card.style.display = 'flex';
            visible.push(card);
          } else {
            card.style.display = 'none';
          }
        });

        if (!isReducedMotion() && visible.length > 0) {
          gsap.fromTo(visible,
            { opacity: 0, y: 12 },
            { opacity: 1, y: 0, duration: 0.3, stagger: 0.04, ease: 'power2.out' }
          );
        }
      });
    });
  }

  // =========================================================================
  // 2. SISTEMA DE PRE-SELECCIÓN DE PLATOS + RESERVAS DE MESA / FESTEJOS
  // =========================================================================
  const DISHES = {
    mollejas_hierro: { id: 'mollejas_hierro', name: 'Mollejas al Quebracho', price: 14500 },
    burrata_higos: { id: 'burrata_higos', name: 'Burrata, Higos & Pistachos', price: 13800 },
    ojo_bife_dry: { id: 'ojo_bife_dry', name: 'Ojo de Bife Dry-Aged (550g)', price: 26900 },
    costillar_braseado: { id: 'costillar_braseado', name: 'Costillar Braseado 8hs (Para 2)', price: 42000 },
    agnolotti_cordero: { id: 'agnolotti_cordero', name: 'Agnolotti de Cordero & Hongos', price: 19500 },
    risotto_azafran: { id: 'risotto_azafran', name: 'Risotto al Azafrán & Langostinos', price: 22400 },
    vino_pedernal: { id: 'vino_pedernal', name: 'Gran Malbec Valle de Pedernal (Descorchar)', price: 24000 },
    volcan_dulce: { id: 'volcan_dulce', name: 'Lingote de Chocolate Belga 70%', price: 9800 }
  };

  const state = {
    mode: 'mesa', // 'mesa' | 'grupo'
    dishes: {
      mollejas_hierro: 0,
      burrata_higos: 0,
      ojo_bife_dry: 0,
      costillar_braseado: 0,
      agnolotti_cordero: 0,
      risotto_azafran: 0,
      vino_pedernal: 1, // Pre-cargamos 1 vino en mesa para mostrar el poder del pre-descorche
      volcan_dulce: 0
    }
  };

  const formatARS = (n) => '$' + Math.round(n).toLocaleString('es-AR');

  // Elementos DOM
  const modeBtns = document.querySelectorAll('.booking-mode-btn');
  const panelMesa = document.getElementById('panel-mode-mesa');
  const panelGrupo = document.getElementById('panel-mode-grupo');
  const modePill = document.getElementById('booking-mode-pill');
  const menuSelectionBadge = document.getElementById('menu-selection-badge');
  const dishesListEl = document.getElementById('booking-dishes-list');
  const clearDishesBtn = document.getElementById('btn-clear-dishes');
  const totalLabelEl = document.getElementById('booking-total-label');
  const totalAmountEl = document.getElementById('booking-total-amount');
  const totalNoteEl = document.getElementById('booking-total-note');
  const waPreviewEl = document.getElementById('booking-wa-preview');
  const sendBookingBtn = document.getElementById('btn-send-booking');

  // Inputs Modo Mesa
  const resName = document.getElementById('res-name');
  const resGuests = document.getElementById('res-guests');
  const resDay = document.getElementById('res-day');
  const resShift = document.getElementById('res-shift');
  const resSector = document.getElementById('res-sector');
  const upsellChecks = document.querySelectorAll('[data-upsell-price]');

  // Inputs Modo Grupo
  const groupRadios = document.querySelectorAll('input[name="group-menu"]');
  const groupGuestsInput = document.getElementById('group-guests');
  const groupMinusBtn = document.getElementById('group-minus');
  const groupPlusBtn = document.getElementById('group-plus');
  const groupDateInput = document.getElementById('group-date');
  const pack1Label = document.getElementById('group-pack-1-label');
  const pack2Label = document.getElementById('group-pack-2-label');

  function computeBookingSummary() {
    // Platos pre-seleccionados
    const selectedDishes = [];
    let dishesTotal = 0;
    let dishesCount = 0;

    Object.values(DISHES).forEach(d => {
      const qty = state.dishes[d.id] || 0;
      if (qty > 0) {
        const sub = qty * d.price;
        dishesTotal += sub;
        dishesCount += qty;
        selectedDishes.push({ ...d, qty, sub });
      }
    });

    if (state.mode === 'mesa') {
      const nameVal = resName && resName.value.trim() ? resName.value.trim() : 'Cliente Web';
      const guestsVal = resGuests ? resGuests.value : '2 personas';
      const dayVal = resDay ? resDay.value : 'Este Viernes';
      const shiftVal = resShift ? resShift.value : 'Cena 1º Turno (20:30 hs)';
      const sectorVal = resSector ? resSector.value : 'Salón Cava Principal';

      const upsells = [];
      let upsellsTotal = 0;
      upsellChecks.forEach(chk => {
        if (chk.checked) {
          const p = parseInt(chk.getAttribute('data-upsell-price') || '0', 10);
          const lbl = chk.getAttribute('data-upsell-label') || '';
          upsellsTotal += p;
          upsells.push({ label: lbl, price: p });
        }
      });

      const grandTotal = dishesTotal + upsellsTotal;

      const lines = [
        'Hola ÁUREA! Quiero confirmar una reserva de mesa desde la web:',
        '',
        `• *A nombre de:* ${nameVal}`,
        `• *Comensales:* ${guestsVal}`,
        `• *Día y Turno:* ${dayVal} — ${shiftVal}`,
        `• *Sector elegido:* ${sectorVal}`
      ];

      if (upsells.length > 0) {
        lines.push('');
        lines.push('*Atenciones Concierge al llegar:*');
        upsells.forEach(u => {
          lines.push(`✓ ${u.label}${u.price > 0 ? ` (+${formatARS(u.price)})` : ''}`);
        });
      }

      if (selectedDishes.length > 0) {
        lines.push('');
        lines.push('*Pre-selección de Carta / Cava para la mesa:*');
        selectedDishes.forEach(s => {
          lines.push(`• ${s.qty}x ${s.name} (${formatARS(s.sub)})`);
        });
      }

      if (grandTotal > 0) {
        lines.push('');
        lines.push(`*Total estimado pre-seleccionado: ${formatARS(grandTotal)} ARS*`);
      }

      lines.push('');
      lines.push('¿Me confirman disponibilidad de la mesa?');

      return {
        selectedDishes,
        dishesCount,
        total: grandTotal,
        label: 'Total pre-seleccionado / Concierge:',
        note: 'La reserva de mesa es sin cargo. Solo abonás tu consumo en el restaurante.',
        text: lines.join('\n')
      };
    } else {
      // Modo Grupo (8 a 40 personas)
      let menuTitle = 'Menú 3 Pasos Fuegos & Malbec ($28.500/pers)';
      let menuPrice = 28500;
      groupRadios.forEach(r => {
        if (r.checked) {
          menuPrice = parseInt(r.getAttribute('data-menu-price') || '28500', 10);
          menuTitle = r.getAttribute('data-menu-title') || menuTitle;
        }
      });

      const parsedGuests = parseInt(groupGuestsInput ? groupGuestsInput.value : '14', 10);
      const guests = isNaN(parsedGuests) ? 14 : Math.max(8, Math.min(40, parsedGuests));
      const dateStr = groupDateInput && groupDateInput.value.trim() ? groupDateInput.value.trim() : 'Fecha a coordinar';

      const groupBaseTotal = guests * menuPrice;
      const grandTotal = groupBaseTotal + dishesTotal;

      const lines = [
        'Hola ÁUREA! Quiero cotizar y reservar una Mesa Larga / Festejo Grupal:',
        '',
        `• *Propuesta elegida:* ${menuTitle}`,
        `• *Cantidad de invitados:* ${guests} personas`,
        `• *Fecha / Motivo:* ${dateStr}`,
        `• *Subtotal Menú Grupal (${guests} x ${formatARS(menuPrice)}):* ${formatARS(groupBaseTotal)} ARS`
      ];

      if (selectedDishes.length > 0) {
        lines.push('');
        lines.push('*Adicionales de Cava / Carta sumados:*');
        selectedDishes.forEach(s => {
          lines.push(`• ${s.qty}x ${s.name} (${formatARS(s.sub)})`);
        });
      }

      lines.push('');
      lines.push(`*Total cerrado estimado: ${formatARS(grandTotal)} ARS*`);
      lines.push('');
      lines.push('¿Tienen disponibilidad en la Cava o Salón para esta fecha?');

      return {
        selectedDishes,
        dishesCount,
        total: grandTotal,
        label: `Presupuesto Grupal (${guests} invitados):`,
        note: `Incluye entrada, plato principal, postre y bebida según menú (${formatARS(menuPrice)} por persona).`,
        text: lines.join('\n')
      };
    }
  }

  function renderAll() {
    // Actualizar contadores en tarjetas de la carta
    Object.values(DISHES).forEach(d => {
      const qty = state.dishes[d.id] || 0;
      document.querySelectorAll(`[data-dish-qty="${d.id}"]`).forEach(el => {
        el.textContent = qty;
      });
      const card = document.querySelector(`.menu-card[data-dish-id="${d.id}"]`);
      if (card) {
        if (qty > 0) {
          card.classList.add('border-[#D4AF37]', 'bg-[#191922]');
          card.classList.remove('border-zinc-800/90', 'bg-[#14141A]');
        } else {
          card.classList.remove('border-[#D4AF37]', 'bg-[#191922]');
          card.classList.add('border-zinc-800/90', 'bg-[#14141A]');
        }
      }
    });

    const summary = computeBookingSummary();

    if (menuSelectionBadge) {
      menuSelectionBadge.textContent = summary.dishesCount > 0
        ? `${summary.dishesCount} ítem/s adjunto/s a tu mesa`
        : '0 platos / vinos adjuntos';
    }

    if (clearDishesBtn) {
      clearDishesBtn.classList.toggle('hidden', summary.selectedDishes.length === 0);
    }

    if (dishesListEl) {
      if (summary.selectedDishes.length === 0) {
        dishesListEl.innerHTML = `<p class="text-[11px] text-zinc-500 italic">Sin pre-selección de carta (elegirás tus platos directamente en la mesa).</p>`;
      } else {
        dishesListEl.innerHTML = summary.selectedDishes.map(s => `
          <div class="flex items-center justify-between py-1.5 px-2.5 rounded-lg bg-[#0A0A0C] border border-zinc-800">
            <span class="text-zinc-200"><strong class="text-[#D4AF37] font-mono">${s.qty}x</strong> ${s.name}</span>
            <span class="font-mono text-[#F3E5AB] font-bold">${formatARS(s.sub)}</span>
          </div>
        `).join('');
      }
    }

    if (totalLabelEl) totalLabelEl.textContent = summary.label;
    if (totalAmountEl) totalAmountEl.textContent = `${formatARS(summary.total)} ARS`;
    if (totalNoteEl) totalNoteEl.textContent = summary.note;
    if (waPreviewEl) waPreviewEl.textContent = summary.text;
  }

  // Eventos de platos (+ / -)
  document.querySelectorAll('[data-dish-step]').forEach(btn => {
    btn.addEventListener('click', () => {
      const id = btn.getAttribute('data-dish-step');
      const step = parseInt(btn.getAttribute('data-step') || '0', 10);
      if (!DISHES[id]) return;
      const curr = state.dishes[id] || 0;
      state.dishes[id] = Math.max(0, Math.min(30, curr + step));
      renderAll();
    });
  });

  if (clearDishesBtn) {
    clearDishesBtn.addEventListener('click', () => {
      Object.keys(state.dishes).forEach(k => { state.dishes[k] = 0; });
      renderAll();
    });
  }

  // Cambio de modo (Mesa vs Grupo)
  modeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const m = btn.getAttribute('data-booking-mode');
      state.mode = m;
      modeBtns.forEach(b => {
        b.classList.remove('bg-[#D4AF37]', 'text-zinc-950', 'shadow-md');
        b.classList.add('text-zinc-300');
      });
      btn.classList.add('bg-[#D4AF37]', 'text-zinc-950', 'shadow-md');
      btn.classList.remove('text-zinc-300');

      if (m === 'mesa') {
        panelMesa.classList.remove('hidden');
        panelGrupo.classList.add('hidden');
        if (modePill) modePill.textContent = 'Mesa Habitual';
      } else {
        panelMesa.classList.add('hidden');
        panelGrupo.classList.remove('hidden');
        if (modePill) modePill.textContent = 'Festejo Grupal';
      }
      renderAll();
    });
  });

  // Listeners de inputs Modo Mesa
  [resName, resGuests, resDay, resShift, resSector].forEach(el => {
    if (el) {
      el.addEventListener('input', renderAll);
      el.addEventListener('change', renderAll);
    }
  });
  upsellChecks.forEach(chk => chk.addEventListener('change', renderAll));

  // Listeners de inputs Modo Grupo
  groupRadios.forEach(r => {
    r.addEventListener('change', () => {
      if (pack1Label && pack2Label) {
        if (r.value === 'fuegos') {
          pack1Label.classList.add('border-2', 'border-[#D4AF37]');
          pack1Label.classList.remove('border', 'border-zinc-800');
          pack2Label.classList.remove('border-2', 'border-[#D4AF37]');
          pack2Label.classList.add('border', 'border-zinc-800');
        } else {
          pack2Label.classList.add('border-2', 'border-[#D4AF37]');
          pack2Label.classList.remove('border', 'border-zinc-800');
          pack1Label.classList.remove('border-2', 'border-[#D4AF37]');
          pack1Label.classList.add('border', 'border-zinc-800');
        }
      }
      renderAll();
    });
  });

  if (groupMinusBtn && groupGuestsInput) {
    groupMinusBtn.addEventListener('click', () => {
      const v = parseInt(groupGuestsInput.value || '14', 10);
      groupGuestsInput.value = Math.max(8, v - 2);
      renderAll();
    });
  }
  if (groupPlusBtn && groupGuestsInput) {
    groupPlusBtn.addEventListener('click', () => {
      const v = parseInt(groupGuestsInput.value || '14', 10);
      groupGuestsInput.value = Math.min(40, v + 2);
      renderAll();
    });
  }
  if (groupGuestsInput) groupGuestsInput.addEventListener('input', renderAll);
  if (groupDateInput) groupDateInput.addEventListener('input', renderAll);

  if (sendBookingBtn) {
    sendBookingBtn.addEventListener('click', () => {
      const summary = computeBookingSummary();
      const url = `https://wa.me/${RESTAURANT_PHONE}?text=${encodeURIComponent(summary.text)}`;
      window.open(url, '_blank', 'noopener,noreferrer');
    });
  }

  renderAll();
});
