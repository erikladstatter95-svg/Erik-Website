import { initWhatsAppButtons } from './whatsapp.js';
import { initAccordion } from './accordion.js';
import { initScrollTop } from './scroll-top.js';

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

  // 4. Header scroll shadow effect con rAF pasivo (evita reflows forzados en móvil)
  try {
    const navbar = document.getElementById('main-nav');
    if (navbar) {
      let ticking = false;
      window.addEventListener('scroll', () => {
        if (!ticking) {
          window.requestAnimationFrame(() => {
            if (window.scrollY > 20) {
              navbar.classList.add('shadow-md', 'bg-white/95', 'backdrop-blur-md');
              navbar.classList.remove('bg-transparent');
            } else {
              navbar.classList.remove('shadow-md', 'bg-white/95', 'backdrop-blur-md');
              navbar.classList.add('bg-transparent');
            }
            ticking = false;
          });
          ticking = true;
        }
      }, { passive: true });
    }
  } catch (err) {
    console.warn('Aviso: navbar scroll listener no asignado:', err);
  }

  // 5. Carga diferida de widgets interactivos y GSAP (0ms de retraso de renderizado para LCP y FCP)
  const loadDynamicWidgets = () => {
    import('./animations.js').then((mod) => {
      if (mod && mod.initAllDynamicWidgets) {
        mod.initAllDynamicWidgets();
      }
    }).catch(err => console.warn('Carga diferida de animaciones:', err));
  };

  if ('requestIdleCallback' in window) {
    window.requestIdleCallback(loadDynamicWidgets, { timeout: 2500 });
  } else {
    setTimeout(loadDynamicWidgets, 1200);
  }
});
