import { initWhatsAppButtons } from '../../src/js/whatsapp.js';
import { initAccordion } from '../../src/js/accordion.js';
import { initScrollTop } from '../../src/js/scroll-top.js';
import { initBeforeAfterSliders, initScrollReveal, initHeroEntrance, initMobileDock, isReducedMotion } from '../../src/js/animations.js';
import { gsap } from 'gsap';

document.addEventListener('DOMContentLoaded', () => {
  // Teléfono específico de la clínica estética
  const CLINIC_PHONE = '5492645185359';

  // Inicializar botones de WhatsApp con número y parámetros
  initWhatsAppButtons(CLINIC_PHONE);

  // Inicializar acordeón de FAQs
  initAccordion('[data-accordion]');

  // Inicializar botón volver arriba
  initScrollTop('btn-scroll-top');

  // Inicializar slider interactivo antes/después y animaciones
  initHeroEntrance();
  initBeforeAfterSliders();
  initScrollReveal();
  initMobileDock();

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

      // Filter cards con transición fluida
      const matchingCards = [];
      treatmentCards.forEach((card) => {
        const cardCat = card.getAttribute('data-treatment-category');
        if (category === 'all' || cardCat === category) {
          card.classList.remove('hidden');
          matchingCards.push(card);
        } else {
          card.classList.add('hidden');
        }
      });

      if (!isReducedMotion() && matchingCards.length) {
        gsap.fromTo(matchingCards, 
          { opacity: 0, y: 12, scale: 0.98 },
          { opacity: 1, y: 0, scale: 1, duration: 0.35, stagger: 0.05, ease: 'power2.out' }
        );
      }
    });
  });
});

