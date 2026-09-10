import { initWhatsAppButtons, buildWhatsAppUrl } from '../../src/js/whatsapp.js';
import { initAccordion } from '../../src/js/accordion.js';

document.addEventListener('DOMContentLoaded', () => {
  const LAW_PHONE = '5491130000000';

  initWhatsAppButtons(LAW_PHONE);
  initAccordion('[data-accordion]');

  // Header scroll
  const header = document.getElementById('abogados-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.classList.add('shadow-md', 'bg-slate-900/95', 'backdrop-blur-md');
      } else {
        header.classList.remove('shadow-md', 'bg-slate-900/95', 'backdrop-blur-md');
      }
    });
  }

  // Formulario de consulta legal urgente
  const legalForm = document.getElementById('legal-inquiry-form');
  if (legalForm) {
    legalForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const area = document.getElementById('inquiry-area')?.value || 'Consulta Legal General';
      const name = document.getElementById('inquiry-name')?.value || 'Cliente';
      const zone = document.getElementById('inquiry-zone')?.value || 'CABA / GBA';
      const detail = document.getElementById('inquiry-detail')?.value || '';

      const message = `*CONSULTA LEGAL INMEDIATA*\n\n` +
        `• *Nombre:* ${name}\n` +
        `• *Área de práctica:* ${area}\n` +
        `• *Zona / Jurisdicción:* ${zone}\n` +
        `• *Detalle del caso:* ${detail}\n\n` +
        `Solicito evaluación del caso y contacto a la brevedad.`;

      const url = buildWhatsAppUrl(LAW_PHONE, message);
      window.open(url, '_blank', 'noopener,noreferrer');
    });
  }
});
