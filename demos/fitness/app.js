import { initWhatsAppButtons } from '../../src/js/whatsapp.js';
import { initAccordion } from '../../src/js/accordion.js';
import { initScrollTop } from '../../src/js/scroll-top.js';
import { initScrollReveal, initHeroEntrance, initMobileDock } from '../../src/js/animations.js';

document.addEventListener('DOMContentLoaded', () => {
  const FITNESS_PHONE = '5492645185359';

  initWhatsAppButtons(FITNESS_PHONE);
  initAccordion('[data-accordion]');
  initScrollTop('btn-scroll-top');
  initHeroEntrance();
  initScrollReveal();
  initMobileDock();

  // Header scroll blur & shadow
  const header = document.querySelector('header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.classList.add('shadow-lg', 'bg-slate-900/98');
      } else {
        header.classList.remove('shadow-lg', 'bg-slate-900/98');
      }
    });
  }

  // Pricing toggle (Mensual vs Trimestral)
  const toggleBtn = document.getElementById('fitness-pricing-toggle');
  if (toggleBtn) {
    let isQuarterly = false;
    const planCards = document.querySelectorAll('[data-plan-name]');
    const knob = toggleBtn.querySelector('span');

    toggleBtn.addEventListener('click', () => {
      isQuarterly = !isQuarterly;

      if (knob) {
        if (isQuarterly) {
          knob.classList.remove('translate-x-0');
          knob.classList.add('translate-x-7');
          toggleBtn.classList.remove('bg-slate-800');
          toggleBtn.classList.add('bg-emerald-600');
        } else {
          knob.classList.remove('translate-x-7');
          knob.classList.add('translate-x-0');
          toggleBtn.classList.remove('bg-emerald-600');
          toggleBtn.classList.add('bg-slate-800');
        }
      }

      planCards.forEach((card) => {
        const priceEl = card.querySelector('.price-amount');
        const periodEl = card.querySelector('.price-period');
        const waBtn = card.querySelector('.plan-wa-btn');
        const planName = card.getAttribute('data-plan-name') || 'Plan Fitness';

        if (priceEl && periodEl) {
          if (isQuarterly) {
            priceEl.textContent = card.getAttribute('data-plan-price-quarterly') || '';
            periodEl.textContent = 'ARS / trimestre';
          } else {
            priceEl.textContent = card.getAttribute('data-plan-price-monthly') || '';
            periodEl.textContent = 'ARS / mes';
          }
        }

        if (waBtn) {
          const billingType = isQuarterly ? 'Trimestral (-20% OFF)' : 'Mensual';
          waBtn.setAttribute(
            'data-wa-msg',
            `Hola Franco! Quiero empezar con el ${planName} en modalidad ${billingType}. ¿Tenés cupos disponibles?`
          );
        }
      });
    });
  }
});
