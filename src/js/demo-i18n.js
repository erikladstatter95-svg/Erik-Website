/**
 * demo-i18n.js
 * Automatically adapts pricing in demo preview banners and footers
 * when viewed from English pages (/en/), ?lang=en, or when user prefers USD.
 *
 * ARS: $150.000 setup | $20.000 ARS/mes maintenance
 * USD: $199 USD setup | $20 USD/mo maintenance
 */

(function () {
  function checkEnglish() {
    try {
      const urlParams = new URLSearchParams(window.location.search);
      if (urlParams.get('lang') === 'en' || urlParams.get('currency') === 'usd') {
        localStorage.setItem('preferred_lang', 'en');
        return true;
      }
      if (urlParams.get('lang') === 'es' || urlParams.get('currency') === 'ars') {
        localStorage.setItem('preferred_lang', 'es');
        return false;
      }
      if (document.referrer && document.referrer.includes('/en/')) {
        localStorage.setItem('preferred_lang', 'en');
        return true;
      }
      return localStorage.getItem('preferred_lang') === 'en';
    } catch (e) {
      return false;
    }
  }

  function applyEnglishDemoPricing() {
    if (!checkEnglish()) return;

    // 1. Text elements with $150.000 ARS
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
    let node;
    const textNodesToUpdate = [];
    while ((node = walker.nextNode())) {
      if (
        node.nodeValue.includes('150.000') ||
        node.nodeValue.includes('20.000') ||
        node.nodeValue.includes('Pedir mi Web') ||
        node.nodeValue.includes('Setup Inicial') ||
        node.nodeValue.includes('Mantenimiento + Hosting') ||
        node.nodeValue.includes('Tu web incluye todo resuelto')
      ) {
        textNodesToUpdate.push(node);
      }
    }

    textNodesToUpdate.forEach(n => {
      n.nodeValue = n.nodeValue
        .replace('$150.000 ARS', '$199 USD')
        .replace('$150.000', '$199')
        .replace('150.000', '199')
        .replace('$20.000 ARS/mes', '$20 USD/mo')
        .replace('$20.000', '$20')
        .replace('20.000', '20')
        .replace('ARS/mes', 'USD/mo')
        .replace('ARS', 'USD')
        .replace('Pedir mi Web por WhatsApp (264-518-5359)', 'Order my Website via WhatsApp ($199 USD)')
        .replace('Pedir mi Web por WhatsApp', 'Order my Website via WhatsApp ($199 USD)')
        .replace('Setup Inicial (Diseño, Programación y Lanzamiento):', 'Initial Setup (Design, Coding & Launch):')
        .replace('Mantenimiento + Hosting de Alta Velocidad + SSL:', 'Cloud Care + High-Speed Hosting + SSL:')
        .replace('A partir del 2º mes (1º mes bonificado)', 'Starts 2nd month (1st month free)')
        .replace('50% al iniciar y 50% contra entrega final', '50% to start and 50% upon final delivery')
        .replace('Tu web incluye todo resuelto:', 'Everything included in your website:')
        .replace('Entrega en 3 a 5 días hábiles con 2 rondas de revisiones incluidas.', 'Delivered in 3 to 5 business days with 2 revision rounds.');
    });

    // 2. Update WhatsApp buttons in banner & floating docks
    const waEnUrl = 'https://wa.me/5492645185359?text=Hello%20Erik!%20I%20am%20viewing%20this%20demo%20and%20would%20like%20to%20order%20a%20website%20for%20my%20business%20for%20%24199%20USD.';
    document.querySelectorAll('a[href*="wa.me"]').forEach(a => {
      const h = a.getAttribute('href');
      if (h && (h.includes('150.000') || h.includes('abogados') || h.includes('demo') || h.includes('Quiero%20una%20web'))) {
        a.setAttribute('href', waEnUrl);
      }
    });

    // 3. Update currency badges
    document.querySelectorAll('[data-currency-setup]').forEach(el => el.textContent = 'USD');
    document.querySelectorAll('[data-price-setup]').forEach(el => el.textContent = '$199');
    document.querySelectorAll('[data-currency-maint]').forEach(el => el.textContent = 'USD/mo');
    document.querySelectorAll('[data-price-maint]').forEach(el => el.textContent = '$20');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyEnglishDemoPricing);
  } else {
    applyEnglishDemoPricing();
  }
})();
