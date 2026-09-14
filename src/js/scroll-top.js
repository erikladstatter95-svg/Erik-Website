/**
 * Botón Flotante "Volver Arriba" (Scroll to top) para Mobile y Desktop
 */
export function initScrollTop(buttonId = 'btn-scroll-top') {
  const btn = document.getElementById(buttonId);
  if (!btn) return;

  const toggleVisibility = () => {
    if (window.scrollY > 280) {
      btn.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-3');
      btn.classList.add('opacity-100', 'pointer-events-auto', 'translate-y-0');
    } else {
      btn.classList.add('opacity-0', 'pointer-events-none', 'translate-y-3');
      btn.classList.remove('opacity-100', 'pointer-events-auto', 'translate-y-0');
    }
  };

  window.addEventListener('scroll', toggleVisibility, { passive: true });
  toggleVisibility();

  btn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}
