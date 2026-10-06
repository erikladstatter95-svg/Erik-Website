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
});
