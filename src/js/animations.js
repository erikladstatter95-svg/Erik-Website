/**
 * Motor de Animaciones, Micro-interacciones y Widgets Interactivos para Móviles
 * Optimizado para rendimiento ultra liviano (< 6KB) con aceleración por GPU.
 */

// 1. Scroll Reveal con IntersectionObserver Nativo
export function initScrollReveal() {
  const elements = document.querySelectorAll('.reveal-on-scroll, .reveal-fade-left, .reveal-fade-right, .reveal-zoom');
  if (!elements.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        obs.unobserve(entry.target);
      }
    });
  }, {
    root: null,
    rootMargin: '0px 0px -40px 0px',
    threshold: 0.1
  });

  elements.forEach(el => observer.observe(el));
}

// 2. Antes y Después Táctil (Slider interactivo para Medicina Estética y Odontología)
export function initBeforeAfterSliders() {
  const sliders = document.querySelectorAll('[data-before-after]');
  sliders.forEach(slider => {
    const range = slider.querySelector('input[type="range"]');
    const beforeImg = slider.querySelector('.before-image');
    const handle = slider.querySelector('.slider-handle');

    if (!range || !beforeImg) return;

    const updateSlider = (val) => {
      beforeImg.style.clipPath = `polygon(0 0, ${val}% 0, ${val}% 100%, 0 100%)`;
      if (handle) {
        handle.style.left = `${val}%`;
      }
    };

    range.addEventListener('input', (e) => {
      updateSlider(e.target.value);
    });

    // Inicializar al 50%
    updateSlider(50);
  });
}

// 3. Calculador Dinámico de Eventos y Catering (Presupuesto interactivo en vivo)
export function initEventCalculator() {
  const calc = document.getElementById('catering-calculator');
  if (!calc) return;

  const guestsSlider = calc.querySelector('#calc-guests');
  const guestsLabel = calc.querySelector('#calc-guests-label');
  const serviceOptions = calc.querySelectorAll('.calc-service-btn');
  const totalDisplay = calc.querySelector('#calc-estimate-label');
  const waBtn = calc.querySelector('#calc-wa-btn');

  let currentGuests = guestsSlider ? parseInt(guestsSlider.value, 10) : 80;
  let currentService = 'Servicio Completo (Catering y Barra Libre)';
  let pricePerGuest = 18500; // Valor de referencia representativo

  const recalculate = () => {
    if (guestsLabel) guestsLabel.textContent = `${currentGuests} personas`;
    
    // Estimación sugerida
    const estimatedTotal = (currentGuests * pricePerGuest).toLocaleString('es-AR');
    if (totalDisplay) {
      totalDisplay.textContent = `$${estimatedTotal}`;
    }

    if (waBtn) {
      const msg = `Hola Fuego y Tragos! Estuve cotizando en su web para un evento de ${currentGuests} invitados (${currentService}). Me gustaria consultar disponibilidad de fecha y presupuesto formal.`;
      waBtn.setAttribute('data-wa-msg', msg);
    }
  };

  if (guestsSlider) {
    guestsSlider.addEventListener('input', (e) => {
      currentGuests = parseInt(e.target.value, 10);
      recalculate();
    });
  }

  serviceOptions.forEach(btn => {
    btn.addEventListener('click', () => {
      serviceOptions.forEach(b => b.classList.remove('active', 'border-amber-500', 'bg-amber-500/10'));
      btn.classList.add('active', 'border-amber-500', 'bg-amber-500/10');
      currentService = btn.getAttribute('data-service-name') || btn.textContent.trim();
      pricePerGuest = parseInt(btn.getAttribute('data-price') || '18500', 10);
      recalculate();
    });
  });

  recalculate();
}

// 4. Selector Empático de Motivo de Consulta (Psicología)
export function initPsychologySelector() {
  const container = document.getElementById('psico-selector-container');
  if (!container) return;

  const buttons = container.querySelectorAll('.psico-btn');
  const card = container.querySelector('#psico-result-card');
  const title = container.querySelector('#psico-result-title');
  const text = container.querySelector('#psico-result-text');
  const waBtn = container.querySelector('#psico-result-wa');

  const infoMap = {
    ansiedad: {
      title: 'Acompañamiento en Ansiedad y Crisis de Pánico',
      text: 'Herramientas prácticas cognitivo-conductuales para regular el sistema nervioso, recuperar la calma en tu día a día y cortar el ciclo de pensamientos rumiantes.',
      msg: 'Hola Lic. Florencia Morales! Le escribo desde su web para consultar por disponibilidad de horarios para abordar temas de ansiedad y estrés.'
    },
    autoestima: {
      title: 'Autoestima, Vínculos y Límites Saludables',
      text: 'Un espacio confidencial para trabajar en tu valor propio, aprender a decir que no sin culpa y construir relaciones sanas con tu entorno.',
      msg: 'Hola Lic. Florencia Morales! Le escribo desde su web para consultar por sesiones para trabajar mi autoestima y relaciones personales.'
    },
    duelo: {
      title: 'Elaboración de Duelos, Separaciones y Cambios',
      text: 'Procesar el dolor de una pérdida o ruptura con escucha cálida y sin juzgar, encontrando el ritmo para reconstruir tu proyecto de vida.',
      msg: 'Hola Lic. Florencia Morales! Le escribo para consultar disponibilidad de consulta para transitar un momento de duelo o cambio personal.'
    },
    burnout: {
      title: 'Estrés Laboral, Agotamiento y Exigencia',
      text: 'Estrategias para desarmar la sobrecarga mental, gestionar la frustración y equilibrar tu vida profesional con tu bienestar emocional.',
      msg: 'Hola Lic. Florencia Morales! Quisiera consultar por turnos para tratar agotamiento mental y estrés laboral.'
    }
  };

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const type = btn.getAttribute('data-psico-type');
      buttons.forEach(b => b.classList.remove('active', 'border-emerald-600', 'bg-emerald-50', 'text-emerald-900'));
      btn.classList.add('active', 'border-emerald-600', 'bg-emerald-50', 'text-emerald-900');

      const data = infoMap[type] || infoMap.ansiedad;
      if (title) title.textContent = data.title;
      if (text) text.textContent = data.text;
      if (waBtn) waBtn.setAttribute('data-wa-msg', data.msg);

      if (card) {
        card.classList.remove('hidden');
        card.classList.add('animate-fade-in');
      }
    });
  });
}

// 5. Switch Interactivo de Precios Mensual vs Trimestral (Fitness)
export function initFitnessPricingToggle() {
  const toggle = document.getElementById('fitness-pricing-toggle');
  if (!toggle) return;

  const planCards = document.querySelectorAll('[data-plan-price-monthly]');
  let isQuarterly = false;

  toggle.addEventListener('click', () => {
    isQuarterly = !isQuarterly;
    toggle.classList.toggle('active', isQuarterly);

    planCards.forEach(card => {
      const monthly = card.getAttribute('data-plan-price-monthly');
      const quarterly = card.getAttribute('data-plan-price-quarterly');
      const periodLabel = card.querySelector('.price-period');
      const amountLabel = card.querySelector('.price-amount');
      const waBtn = card.querySelector('.plan-wa-btn');
      const planName = card.getAttribute('data-plan-name') || 'Plan';

      if (amountLabel) {
        amountLabel.textContent = isQuarterly ? quarterly : monthly;
      }
      if (periodLabel) {
        periodLabel.textContent = isQuarterly ? '/trimestre (-20% OFF)' : '/mes';
      }
      if (waBtn) {
        const mode = isQuarterly ? 'Trimestral con descuento' : 'Mensual';
        waBtn.setAttribute('data-wa-msg', `Hola Marcos! Quiero sumarme a tu entrenamiento con el ${planName} (${mode}). Tenes cupo disponible?`);
      }
    });
  });
}

// 6. Asistente Rápido de Diagnóstico Legal (Abogados)
export function initLegalAssistant() {
  const container = document.getElementById('legal-assistant-container');
  if (!container) return;

  const tabs = container.querySelectorAll('.legal-tab-btn');
  const details = container.querySelectorAll('.legal-case-content');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const target = tab.getAttribute('data-legal-target');
      tabs.forEach(t => t.classList.remove('active', 'border-amber-500', 'bg-slate-800', 'text-amber-400'));
      tab.classList.add('active', 'border-amber-500', 'bg-slate-800', 'text-amber-400');

      details.forEach(d => {
        if (d.getAttribute('data-legal-case') === target) {
          d.classList.remove('hidden');
          d.classList.add('animate-fade-in');
        } else {
          d.classList.add('hidden');
        }
      });
    });
  });
}

// 7. Radar de Urgencias 24hs (Urgencias Hogar)
export function initEmergencySelector() {
  const selector = document.getElementById('emergency-selector');
  if (!selector) return;

  const emergencyButtons = selector.querySelectorAll('.emergency-btn');
  const waBtn = selector.querySelector('#emergency-main-wa');

  emergencyButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      emergencyButtons.forEach(b => b.classList.remove('ring-2', 'ring-amber-500', 'bg-amber-500/10'));
      btn.classList.add('ring-2', 'ring-amber-500', 'bg-amber-500/10');
      const emergencyType = btn.getAttribute('data-emergency') || 'urgencia general';
      if (waBtn) {
        waBtn.setAttribute('data-wa-msg', `URGENCIA 24HS: Tengo un problema de ${emergencyType} en mi domicilio en San Juan. Necesito asistencia urgente.`);
        waBtn.classList.add('animate-pulse');
        setTimeout(() => waBtn.classList.remove('animate-pulse'), 1000);
      }
    });
  });
}

// Inicializador Maestro de Widgets Dinámicos
export function initAllDynamicWidgets() {
  initScrollReveal();
  initBeforeAfterSliders();
  initEventCalculator();
  initPsychologySelector();
  initFitnessPricingToggle();
  initLegalAssistant();
  initEmergencySelector();
}
