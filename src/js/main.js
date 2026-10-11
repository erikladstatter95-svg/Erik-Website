import { initWhatsAppButtons } from './whatsapp.js';
import { initAccordion } from './accordion.js';
import { initScrollTop } from './scroll-top.js';
import { initAllDynamicWidgets } from './animations.js';

document.addEventListener('DOMContentLoaded', () => {
  // 1. Inicializar botones de WhatsApp (Prioridad máxima de negocio)
  try {
    initWhatsAppButtons('5492645185359');
  } catch (err) {
    console.error('Error al inicializar botones de WhatsApp:', err);
  }

  // 2. Inicializar acordeón de FAQs
  try {
    initAccordion('[data-accordion]');
  } catch (err) {
    console.error('Error al inicializar acordeón FAQ:', err);
  }

  // 3. Inicializar botón volver arriba (mobile & desktop)
  try {
    initScrollTop('btn-scroll-top');
  } catch (err) {
    console.error('Error al inicializar scroll-top:', err);
  }

  // 4. Inicializar widgets dinámicos y animaciones de scroll protegidos
  try {
    initAllDynamicWidgets();
  } catch (err) {
    console.error('Error al inicializar widgets dinámicos:', err);
  }

  // 5. Header scroll shadow effect
  try {
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
  } catch (err) {
    console.warn('Aviso: navbar scroll listener no asignado:', err);
  }
});
