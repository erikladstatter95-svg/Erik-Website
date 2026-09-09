import { initWhatsAppButtons, buildWhatsAppUrl } from '../../src/js/whatsapp.js';
import { initAccordion } from '../../src/js/accordion.js';

document.addEventListener('DOMContentLoaded', () => {
  const EVENTOS_PHONE = '5491130000000';

  initWhatsAppButtons(EVENTOS_PHONE);
  initAccordion('[data-accordion]');

  // Header scroll
  const header = document.getElementById('eventos-header');
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

  // Filtro de catálogo
  const filterBtns = document.querySelectorAll('[data-catalog-filter]');
  const items = document.querySelectorAll('[data-catalog-category]');

  filterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      const category = btn.getAttribute('data-catalog-filter');

      filterBtns.forEach((b) => {
        b.classList.remove('bg-amber-600', 'text-white');
        b.classList.add('bg-stone-100', 'text-stone-700');
      });
      btn.classList.remove('bg-stone-100', 'text-stone-700');
      btn.classList.add('bg-amber-600', 'text-white');

      items.forEach((item) => {
        const itemCat = item.getAttribute('data-catalog-category');
        if (category === 'all' || itemCat === category) {
          item.classList.remove('hidden');
        } else {
          item.classList.add('hidden');
        }
      });
    });
  });

  // Cotizador interactivo directo a WhatsApp
  const quoteForm = document.getElementById('event-quote-form');
  if (quoteForm) {
    quoteForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const eventType = document.getElementById('quote-event-type')?.value || 'Fiesta';
      const guests = document.getElementById('quote-guests')?.value || '50';
      const date = document.getElementById('quote-date')?.value || 'A coordinar';
      const zone = document.getElementById('quote-zone')?.value || 'CABA / GBA';
      const notes = document.getElementById('quote-notes')?.value || 'Sin comentarios adicionales';

      const message = `¡Hola! Quisiera solicitar cotización y consultar disponibilidad de vajilla/mobiliario:\n\n` +
        `• Tipo de evento: ${eventType}\n` +
        `• Cantidad aproximada de invitados: ${guests} personas\n` +
        `• Fecha estimada: ${date}\n` +
        `• Zona de entrega: ${zone}\n` +
        `• Detalle / Pedido especial: ${notes}\n\n` +
        `¿Tienen disponibilidad para esa fecha? ¡Muchas gracias!`;

      const url = buildWhatsAppUrl(EVENTOS_PHONE, message);
      window.open(url, '_blank', 'noopener,noreferrer');
    });
  }
});
