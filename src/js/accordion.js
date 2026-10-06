/**
 * Acordeón accesible y fluido para FAQs
 * Con soporte para micro-interacciones suaves y prefers-reduced-motion
 */
export function initAccordion(selector = '[data-accordion]') {
  const containers = document.querySelectorAll(selector);

  containers.forEach((container) => {
    const triggers = container.querySelectorAll('[data-accordion-trigger]');

    triggers.forEach((trigger) => {
      const item = trigger.closest('[data-accordion-item]');
      const content = item?.querySelector('[data-accordion-content]');
      const icon = trigger.querySelector('[data-accordion-icon]');

      if (content && !content.classList.contains('accordion-content-grid')) {
        content.classList.add('accordion-content-grid');
        if (!content.querySelector('.accordion-inner')) {
          const inner = document.createElement('div');
          inner.className = 'accordion-inner';
          while (content.firstChild) {
            inner.appendChild(content.firstChild);
          }
          content.appendChild(inner);
        }
      }

      // Sincronizar estado inicial
      const initialExpanded = trigger.getAttribute('aria-expanded') === 'true';
      if (initialExpanded) {
        content?.classList.add('is-open');
        content?.classList.remove('hidden');
        icon?.classList.add('rotate-180');
      } else {
        content?.classList.remove('is-open');
        content?.classList.add('hidden');
        icon?.classList.remove('rotate-180');
      }

      trigger.addEventListener('click', () => {
        const isExpanded = trigger.getAttribute('aria-expanded') === 'true';

        // Cerrar otros elementos si no queremos múltiples abiertos
        container.querySelectorAll('[data-accordion-trigger]').forEach((t) => {
          if (t !== trigger) {
            t.setAttribute('aria-expanded', 'false');
            const otherItem = t.closest('[data-accordion-item]');
            const otherContent = otherItem?.querySelector('[data-accordion-content]');
            const otherIcon = t.querySelector('[data-accordion-icon]');
            if (otherContent) {
              otherContent.classList.remove('is-open');
              setTimeout(() => {
                if (t.getAttribute('aria-expanded') === 'false') {
                  otherContent.classList.add('hidden');
                }
              }, 300);
            }
            if (otherIcon) otherIcon.classList.remove('rotate-180');
          }
        });

        // Alternar el actual
        if (isExpanded) {
          trigger.setAttribute('aria-expanded', 'false');
          content?.classList.remove('is-open');
          icon?.classList.remove('rotate-180');
          setTimeout(() => {
            if (trigger.getAttribute('aria-expanded') === 'false') {
              content?.classList.add('hidden');
            }
          }, 300);
        } else {
          content?.classList.remove('hidden');
          // Forzar layout para que la transición CSS Grid se dispare
          void content?.offsetHeight;
          trigger.setAttribute('aria-expanded', 'true');
          content?.classList.add('is-open');
          icon?.classList.add('rotate-180');
        }
      });
    });
  });
}

