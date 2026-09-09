/**
 * Acordeón accesible para FAQs
 */
export function initAccordion(selector = '[data-accordion]') {
  const containers = document.querySelectorAll(selector);

  containers.forEach((container) => {
    const triggers = container.querySelectorAll('[data-accordion-trigger]');

    triggers.forEach((trigger) => {
      trigger.addEventListener('click', () => {
        const item = trigger.closest('[data-accordion-item]');
        const content = item?.querySelector('[data-accordion-content]');
        const icon = trigger.querySelector('[data-accordion-icon]');
        const isExpanded = trigger.getAttribute('aria-expanded') === 'true';

        // Cerrar otros elementos si no queremos múltiples abiertos
        container.querySelectorAll('[data-accordion-trigger]').forEach((t) => {
          if (t !== trigger) {
            t.setAttribute('aria-expanded', 'false');
            const otherItem = t.closest('[data-accordion-item]');
            const otherContent = otherItem?.querySelector('[data-accordion-content]');
            const otherIcon = t.querySelector('[data-accordion-icon]');
            if (otherContent) otherContent.classList.add('hidden');
            if (otherIcon) otherIcon.classList.remove('rotate-180');
          }
        });

        // Alternar el actual
        if (isExpanded) {
          trigger.setAttribute('aria-expanded', 'false');
          content?.classList.add('hidden');
          icon?.classList.remove('rotate-180');
        } else {
          trigger.setAttribute('aria-expanded', 'true');
          content?.classList.remove('hidden');
          icon?.classList.add('rotate-180');
        }
      });
    });
  });
}
