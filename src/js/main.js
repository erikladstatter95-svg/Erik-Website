import { initWhatsAppButtons } from './whatsapp.js';
import { initAccordion } from './accordion.js';
import { initScrollTop } from './scroll-top.js';

document.addEventListener('DOMContentLoaded', () => {
  // Inicializar botones de WhatsApp
  initWhatsAppButtons('5492645185359');

  // Inicializar acordeón de FAQs
  initAccordion('[data-accordion]');

  // Inicializar botón volver arriba (mobile & desktop)
  initScrollTop('btn-scroll-top');

  // Header scroll shadow effect
  const navbar = document.getElementById('main-nav');
  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        navbar.classList.add('shadow-md', 'bg-white/95', 'backdrop-blur-md');
        navbar.classList.remove('bg-transparent');
      } else {
        navbar.classList.remove('shadow-md', 'bg-white/95', 'backdrop-blur-md');
        navbar.classList.add('bg-transparent');
      }
    });
  }
});
