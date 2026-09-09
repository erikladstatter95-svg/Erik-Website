import { initWhatsAppButtons } from './whatsapp.js';
import { initAccordion } from './accordion.js';

document.addEventListener('DOMContentLoaded', () => {
  // Inicializar botones de WhatsApp
  initWhatsAppButtons('5491130000000');

  // Inicializar acordeón de FAQs
  initAccordion('[data-accordion]');

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
