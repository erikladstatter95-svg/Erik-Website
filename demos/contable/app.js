import { initWhatsAppButtons } from '../../src/js/whatsapp.js';
import { initAccordion } from '../../src/js/accordion.js';
import { initScrollTop } from '../../src/js/scroll-top.js';
import { initScrollReveal, initHeroEntrance, initMobileDock } from '../../src/js/animations.js';

document.addEventListener('DOMContentLoaded', () => {
  const CONTABLE_PHONE = '5492645185359';

  // Base utilities
  initWhatsAppButtons(CONTABLE_PHONE);
  initAccordion('[data-accordion]');
  initScrollTop('btn-scroll-top');
  initHeroEntrance();
  initScrollReveal();
  initMobileDock();

  // 1. Header scroll shadow and progress bar
  const header = document.getElementById('contable-header');
  const prog = document.getElementById('prog');

  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    if (header) {
      if (scrollY > 25) {
        header.classList.add('header-scrolled');
      } else {
        header.classList.remove('header-scrolled');
      }
    }
    if (prog) {
      const total = document.documentElement.scrollHeight - window.innerHeight;
      if (total > 0) {
        const pct = Math.min(100, Math.max(0, (scrollY / total) * 100));
        prog.style.width = `${pct}%`;
      }
    }
  }, { passive: true });

  // 2. Spotlight effect (data-spot)
  const spotCards = document.querySelectorAll('[data-spot]');
  spotCards.forEach(card => {
    card.addEventListener('mousemove', e => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      card.style.setProperty('--mx', `${x}px`);
      card.style.setProperty('--my', `${y}px`);
    });
  });

  // 3. Interactive Diagnóstico Fiscal Wizard (Step 1 -> 2 -> 3 -> WhatsApp CTA)
  const wizard = document.getElementById('fiscal-wizard');
  if (wizard) {
    let state = {
      fiscal: 'Responsable Inscripto (IVA)',
      necesidad: 'Liquidación Mensual de Impuestos',
      escala: '1 a 5 empleados'
    };

    const chips = wizard.querySelectorAll('.wiz-chip');
    chips.forEach(chip => {
      chip.addEventListener('click', () => {
        const group = chip.getAttribute('data-grp');
        const val = chip.getAttribute('data-val');
        if (!group || !val) return;

        // Deselect others in group
        wizard.querySelectorAll(`.wiz-chip[data-grp="${group}"]`).forEach(c => {
          c.classList.remove('active-chip');
        });
        chip.classList.add('active-chip');

        if (group === 'fiscal') state.fiscal = val;
        if (group === 'necesidad') state.necesidad = val;
        if (group === 'escala') state.escala = val;

        updateWizardSummary();
      });
    });

    function updateWizardSummary() {
      const elFiscal = document.getElementById('wiz-res-fiscal');
      const elNecesidad = document.getElementById('wiz-res-necesidad');
      const elEscala = document.getElementById('wiz-res-escala');
      const btn = document.getElementById('wiz-submit-btn');

      if (elFiscal) elFiscal.textContent = state.fiscal;
      if (elNecesidad) elNecesidad.textContent = state.necesidad;
      if (elEscala) elEscala.textContent = state.escala;

      const customMsg = `Hola Estudio Sánchez! Completé el diagnóstico en su web: Soy ${state.fiscal}, mi principal necesidad es ${state.necesidad} y la escala de mi negocio es ${state.escala}. Quisiera coordinar una consulta contable.`;

      if (btn) {
        btn.setAttribute('data-wa-msg', customMsg);
      }
    }

    updateWizardSummary();
  }
});
