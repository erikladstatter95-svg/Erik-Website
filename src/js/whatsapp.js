/**
 * Helper dinámico para enlaces de WhatsApp de Alta Conversión (Argentina)
 * Formato internacional estándar: 549 + código de área sin 0 + número sin 15
 */

const DEFAULT_PORTFOLIO_PHONE = '5491130000000'; // Placeholder editable

export function normalizePhone(phone) {
  if (!phone) return DEFAULT_PORTFOLIO_PHONE;
  // Eliminar espacios, guiones, paréntesis y signos +
  let clean = phone.replace(/[^0-9]/g, '');
  if (!clean.startsWith('54')) {
    clean = '549' + clean;
  }
  return clean;
}

export function buildWhatsAppUrl(phone, message) {
  const normalized = normalizePhone(phone);
  const encodedText = encodeURIComponent(message.trim());
  return `https://wa.me/${normalized}?text=${encodedText}`;
}

export function initWhatsAppButtons(defaultPhone = DEFAULT_PORTFOLIO_PHONE) {
  const buttons = document.querySelectorAll('[data-wa-msg]');
  
  buttons.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const phone = btn.getAttribute('data-wa-phone') || defaultPhone;
      let msg = btn.getAttribute('data-wa-msg') || 'Hola! Me gustaría solicitar más información.';
      
      const service = btn.getAttribute('data-wa-service');
      if (service) {
        msg = msg.replace('{servicio}', service);
      }
      
      const url = buildWhatsAppUrl(phone, msg);
      window.open(url, '_blank', 'noopener,noreferrer');
    });
  });
}
