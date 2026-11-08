/**
 * Helper dinámico para enlaces de WhatsApp de Alta Conversión (Argentina)
 * + Sistema Integral de Eventos y Conversiones GA4 (G-KWD0WYVK4J) & Meta Pixel
 * Formato internacional estándar: 549 + código de área sin 0 + número sin 15
 */

const DEFAULT_PORTFOLIO_PHONE = '5492645185359'; // San Juan, Argentina (2645185359)

export function normalizePhone(phone) {
  if (!phone) return DEFAULT_PORTFOLIO_PHONE;
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

/**
 * Detecta la intención comercial de la página o del botón (Auditoría SEO, Funnel o Diseño Web)
 */
function detectServiceIntent(textOrHref = '') {
  const path = (window.location.pathname || '').toLowerCase();
  const combined = `${path} ${(textOrHref || '').toLowerCase()}`;
  if (
    combined.includes('seo') ||
    combined.includes('indexa') ||
    combined.includes('velocidad') ||
    combined.includes('analytics') ||
    combined.includes('ga4') ||
    combined.includes('vitals') ||
    combined.includes('chatgpt')
  ) {
    return 'auditoria_seo';
  }
  if (combined.includes('funnel') || combined.includes('embudo') || combined.includes('hotmart') || combined.includes('stan-store')) {
    return 'funnel';
  }
  return 'diseno_web';
}

/**
 * Envía eventos de forma segura a Google Analytics 4 (gtag)
 */
export function trackGA4Event(eventName, params = {}) {
  try {
    if (typeof window.loadThirdPartyAnalytics === 'function') {
      window.loadThirdPartyAnalytics();
    }
    if (typeof window.gtag === 'function') {
      window.gtag('event', eventName, params);
    } else if (Array.isArray(window.dataLayer)) {
      window.dataLayer.push({ event: eventName, ...params });
    }
  } catch (err) {
    // Silencioso en caso de bloqueadores de anuncios
  }
}

/**
 * Registra conversión de contacto por WhatsApp en GA4 (generate_lead + whatsapp_click) y Meta Pixel (Contact)
 */
export function trackWhatsAppConversion(element, customMsg = '') {
  try {
    const rawText = (
      element?.getAttribute('aria-label') ||
      element?.textContent ||
      'Boton WhatsApp'
    )
      .replace(/\s+/g, ' ')
      .trim()
      .slice(0, 80);

    const href = element?.getAttribute('href') || customMsg || '';
    const serviceIntent = detectServiceIntent(`${rawText} ${href}`);
    const isEnglish = (document.documentElement.lang || '').toLowerCase().startsWith('en');

    // 1. Evento Oficial Recomendado de GA4 para Conversiones (Key Event)
    trackGA4Event('generate_lead', {
      currency: isEnglish ? 'USD' : 'ARS',
      value: isEnglish ? 199 : 150000,
      lead_source: window.location.pathname,
      page_title: document.title,
      service_intent: serviceIntent,
      cta_text: rawText
    });

    // 2. Evento Personalizado Detallado para Reportes Semanales de Domingos
    trackGA4Event('whatsapp_click', {
      page_path: window.location.pathname,
      page_title: document.title,
      service_intent: serviceIntent,
      cta_text: rawText
    });

    // 3. Evento Contact en Meta Pixel (exclusivamente ante clic humano real)
    if (typeof window.fbq === 'function') {
      window.fbq('track', 'Contact', {
        content_name: document.title,
        content_category: serviceIntent,
        value: isEnglish ? 199 : 150000,
        currency: isEnglish ? 'USD' : 'ARS'
      });
    }
  } catch (err) {
    // Fallback seguro
  }
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

      trackWhatsAppConversion(btn, msg);

      const url = buildWhatsAppUrl(phone, msg);
      window.open(url, '_blank', 'noopener,noreferrer');
    });
  });

  // Listener delegado global para todos los enlaces <a href="https://wa.me/...">, Demos, Calculadoras y FAQs
  if (!window._erikGlobalTrackingInitialized) {
    window._erikGlobalTrackingInitialized = true;

    document.addEventListener('click', (e) => {
      const target = e.target;
      if (!target || typeof target.closest !== 'function') return;

      // A. Clic en enlace directo a WhatsApp (<a href="https://wa.me/...">) que no sea [data-wa-msg]
      const waLink = target.closest('a[href*="wa.me"], a[href*="whatsapp.com"]');
      if (waLink && !waLink.hasAttribute('data-wa-msg')) {
        trackWhatsAppConversion(waLink, waLink.getAttribute('href') || '');
        return;
      }

      // B. Clic hacia cualquiera de las 13 Demos Interactivas (<a href*="/demos/">)
      const demoLink = target.closest('a[href*="/demos/"]');
      if (demoLink) {
        const href = demoLink.getAttribute('href') || '';
        const match = href.match(/\/demos\/([^/#?]+)/);
        const demoName = match ? match[1] : 'catalogo_demos';
        trackGA4Event('view_demo', {
          demo_name: demoName,
          source_page: window.location.pathname,
          cta_text: (demoLink.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 60)
        });
      }

      // C. Interacción con Calculadoras / Cotizadores en Demos o Generador QR
      const calcTrigger = target.closest(
        '#catering-calculator button, #psico-selector-container button, #fitness-pricing-toggle, #legal-assistant-container button, #emergency-selector button, #wa-copy-url, #wa-download-qr, #wa-download-card, [data-qty-btn], [data-bump-toggle], [data-calc-action]'
      );
      if (calcTrigger && !window._calcTrackedOnPage) {
        window._calcTrackedOnPage = true;
        trackGA4Event('use_interactive_calculator', {
          page_path: window.location.pathname,
          tool_element: (calcTrigger.id || calcTrigger.textContent || 'calculator').replace(/\s+/g, ' ').trim().slice(0, 50)
        });
      }
    }, { passive: true });

    // D. Apertura de Preguntas Frecuentes (<details>)
    document.addEventListener('toggle', (e) => {
      const detail = e.target;
      if (detail && detail.tagName === 'DETAILS' && detail.open) {
        const summary = detail.querySelector('summary');
        const questionText = (summary ? summary.textContent : 'FAQ')
          .replace(/▼/g, '')
          .replace(/\s+/g, ' ')
          .trim()
          .slice(0, 100);
        trackGA4Event('faq_expand', {
          page_path: window.location.pathname,
          question_text: questionText
        });
      }
    }, true);

    // E. Lectura Profunda del 75% (article_read_75) tras al menos 8 segundos en página
    let read75Fired = false;
    let timeQualified = false;
    setTimeout(() => {
      timeQualified = true;
    }, 8000);

    window.addEventListener('scroll', () => {
      if (read75Fired || !timeQualified) return;
      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      if (docHeight > 300 && scrollTop / docHeight >= 0.75) {
        read75Fired = true;
        trackGA4Event('article_read_75', {
          page_path: window.location.pathname,
          page_title: document.title
        });
      }
    }, { passive: true });
  }
}
