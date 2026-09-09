import { initWhatsAppButtons } from '../../src/js/whatsapp.js';
import { initAccordion } from '../../src/js/accordion.js';

document.addEventListener('DOMContentLoaded', () => {
  // Teléfono específico de la clínica estética (demo editable)
  const CLINIC_PHONE = '5491130000000';

  // Inicializar botones de WhatsApp con número y parámetros
  initWhatsAppButtons(CLINIC_PHONE);

  // Inicializar acordeón de FAQs
  initAccordion('[data-accordion]');

  // Header scroll shadow
  const header = document.getElementById('clinic-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.classList.add('shadow-md', 'bg-white/95', 'backdrop-blur-md');
        header.classList.remove('bg-white');
      } else {
        header.classList.remove('shadow-md', 'bg-white/95', 'backdrop-blur-md');
        header.classList.add('bg-white');
      }
    });
  }

  // Filtro de categorías de tratamientos (Todos / Facial / Corporal)
  const filterButtons = document.querySelectorAll('[data-treatment-filter]');
  const treatmentCards = document.querySelectorAll('[data-treatment-category]');

  filterButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      const category = btn.getAttribute('data-treatment-filter');

      // Update active state in buttons
      filterButtons.forEach((b) => {
        b.classList.remove('bg-rose-600', 'text-white');
        b.classList.add('bg-stone-100', 'text-stone-700');
      });
      btn.classList.remove('bg-stone-100', 'text-stone-700');
      btn.classList.add('bg-rose-600', 'text-white');

      // Filter cards
      treatmentCards.forEach((card) => {
        const cardCat = card.getAttribute('data-treatment-category');
        if (category === 'all' || cardCat === category) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    });
  });
});
