import { initWhatsAppButtons } from '../../src/js/whatsapp.js';
import { initAccordion } from '../../src/js/accordion.js';
import { initScrollTop } from '../../src/js/scroll-top.js';
import { initScrollReveal, initHeroEntrance, initMobileDock } from '../../src/js/animations.js';

document.addEventListener('DOMContentLoaded', () => {
  const CONTABLE_PHONE = '5492645185359';

  initWhatsAppButtons(CONTABLE_PHONE);
  initAccordion('[data-accordion]');
  initScrollTop('btn-scroll-top');
  initHeroEntrance();
  initScrollReveal();
  initMobileDock();

  // Header scroll shadow
  const header = document.getElementById('contable-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.classList.add('shadow-md', 'bg-white/95', 'backdrop-blur-md');
      } else {
        header.classList.remove('shadow-md', 'bg-white/95', 'backdrop-blur-md');
      }
    });
  }
});
