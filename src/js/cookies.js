/**
 * Banner de Consentimiento de Cookies y Privacidad
 * Conforme a Ley 25.326 (Argentina) y estándares web internacionales.
 * Discreto, accesible, no intrusivo y persistente en localStorage.
 */
export function initCookieBanner() {
  try {
    const CONSENT_KEY = 'erikwebsite_cookie_consent';
    if (localStorage.getItem(CONSENT_KEY)) {
      return; // El usuario ya tomó una decisión previamente
    }

    const isEnglish = document.documentElement.lang && document.documentElement.lang.toLowerCase().startsWith('en');

    const banner = document.createElement('aside');
    banner.id = 'cookie-consent-banner';
    banner.setAttribute('role', 'region');
    banner.setAttribute('aria-label', isEnglish ? 'Privacy & Cookie Notice' : 'Aviso de Cookies y Privacidad');
    
    // Apple-style Frosted Glass Floating Card
    banner.className = 'fixed bottom-4 left-4 right-4 sm:left-6 sm:right-auto sm:max-w-md z-50 p-4 sm:p-5 rounded-2xl bg-neutral-900/95 text-white backdrop-blur-xl border border-white/10 shadow-[0_12px_36px_rgba(0,0,0,0.35)] transition-all duration-300 translate-y-6 opacity-0';

    const title = isEnglish ? 'Privacy & Cookies' : 'Privacidad y Cookies';
    const description = isEnglish
      ? 'We use technical cookies and anonymous analytics (Google Analytics & Microsoft Clarity) to optimize site speed and performance. Read our <a href="/terminos/" class="text-emerald-400 hover:underline font-normal">Terms & Privacy Policy</a>.'
      : 'Utilizamos cookies técnicas y analítica anónima (Google Analytics y Microsoft Clarity) para optimizar la velocidad y funcionamiento del sitio. Consultá nuestros <a href="/terminos/" class="text-emerald-400 hover:underline font-normal">Términos y Condiciones</a>.';
    
    const btnEssential = isEnglish ? 'Essential only' : 'Solo necesarias';
    const btnAccept = isEnglish ? 'Accept all' : 'Aceptar todas';

    banner.innerHTML = `
      <div class="flex items-start gap-3">
        <div class="w-8 h-8 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center shrink-0 mt-0.5">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
          </svg>
        </div>
        <div class="text-xs text-neutral-300 leading-relaxed font-light">
          <p class="font-medium text-white mb-1">${title}</p>
          ${description}
        </div>
      </div>
      <div class="mt-3.5 flex items-center justify-end gap-2 pt-2 border-t border-white/[0.08]">
        <button id="btn-cookie-essential" class="px-3 py-1.5 rounded-lg text-xs font-medium text-neutral-400 hover:text-white hover:bg-white/10 transition-colors cursor-pointer">
          ${btnEssential}
        </button>
        <button id="btn-cookie-accept" class="px-4 py-1.5 rounded-lg text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white transition-colors cursor-pointer shadow-xs">
          ${btnAccept}
        </button>
      </div>
    `;

    document.body.appendChild(banner);

    // Animación suave de entrada tras medio segundo para no competir con el primer render
    setTimeout(() => {
      banner.classList.remove('translate-y-6', 'opacity-0');
    }, 600);

    const closeBanner = (choice) => {
      try {
        localStorage.setItem(CONSENT_KEY, choice);
      } catch (e) {
        // Fallback si cookies están deshabilitadas
      }
      banner.classList.add('translate-y-6', 'opacity-0');
      setTimeout(() => {
        banner.remove();
      }, 350);
    };

    document.getElementById('btn-cookie-accept')?.addEventListener('click', () => closeBanner('all'));
    document.getElementById('btn-cookie-essential')?.addEventListener('click', () => closeBanner('essential'));
  } catch (err) {
    console.warn('Cookie banner deferred safely:', err);
  }
}
