import { initWhatsAppButtons, buildWhatsAppUrl } from '../../src/js/whatsapp.js';
import { initAccordion } from '../../src/js/accordion.js';

document.addEventListener('DOMContentLoaded', () => {
  const TECH_PHONE = '5492640000000'; // San Juan

  initWhatsAppButtons(TECH_PHONE);
  initAccordion('[data-accordion]');

  // Header scroll
  const header = document.getElementById('tech-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.classList.add('shadow-md', 'bg-white/95', 'backdrop-blur-md');
      } else {
        header.classList.remove('shadow-md', 'bg-white/95', 'backdrop-blur-md');
      }
    });
  }

  // Selector interactivo de urgencia rápida
  const quickForm = document.getElementById('tech-emergency-form');
  if (quickForm) {
    quickForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const rubro = document.getElementById('tech-rubro')?.value || 'Urgencia General';
      const zona = document.getElementById('tech-zone')?.value || 'San Juan';
      const desc = document.getElementById('tech-problem')?.value || 'Necesito un técnico a domicilio';

      const message = `*URGENCIA A DOMICILIO - SAN JUAN*\n\n` +
        `• *Servicio:* ${rubro}\n` +
        `• *Zona / Departamento:* ${zona}\n` +
        `• *Problema:* ${desc}\n\n` +
        `¿Tienen un técnico disponible para venir ahora?`;

      const url = buildWhatsAppUrl(TECH_PHONE, message);
      window.open(url, '_blank', 'noopener,noreferrer');
    });
  }
});
