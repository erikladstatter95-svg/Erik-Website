import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

/**
 * Helper para verificar preferencia de movimiento reducido del usuario
 */
export const isReducedMotion = () => {
  return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
};

// 1. Scroll Reveal Potenciado por GSAP ScrollTrigger
export function initScrollReveal() {
  const elements = document.querySelectorAll('.reveal-on-scroll, .reveal-fade-left, .reveal-fade-right, .reveal-zoom');
  if (!elements.length) return;

  if (isReducedMotion()) {
    elements.forEach(el => el.classList.add('revealed'));
    return;
  }

  elements.forEach((el) => {
    // Definir desplazamiento inicial sutil según la clase
    let fromVars = { opacity: 0, duration: 0.65, ease: 'power2.out' };
    if (el.classList.contains('reveal-fade-left')) {
      fromVars.x = -24;
    } else if (el.classList.contains('reveal-fade-right')) {
      fromVars.x = 24;
    } else if (el.classList.contains('reveal-zoom')) {
      fromVars.scale = 0.95;
    } else {
      fromVars.y = 22;
    }

    gsap.fromTo(el, fromVars, {
      opacity: 1,
      x: 0,
      y: 0,
      scale: 1,
      duration: 0.65,
      ease: 'power2.out',
      scrollTrigger: {
        trigger: el,
        start: 'top 88%',
        once: true,
        onEnter: () => el.classList.add('revealed')
      }
    });
  });
}

// 2. Entrada Suave del Hero y Encabezados
export function initHeroEntrance() {
  if (isReducedMotion()) return;

  const heroItems = document.querySelectorAll('[data-hero-anim]');
  if (heroItems.length) {
    gsap.fromTo(heroItems, 
      { opacity: 0, y: 16 },
      { opacity: 1, y: 0, duration: 0.7, stagger: 0.08, ease: 'power2.out', delay: 0.05 }
    );
  }
}

// 3. Barra Flotante Móvil Suave (Mobile Action Dock)
export function initMobileDock() {
  const dock = document.querySelector('.mobile-action-dock');
  if (!dock) return;

  if (isReducedMotion()) {
    dock.style.opacity = '1';
    return;
  }

  // Revelar la barra móvil suavemente tras scroll
  ScrollTrigger.create({
    trigger: document.body,
    start: '120px top',
    onEnter: () => {
      gsap.to(dock, { y: 0, opacity: 1, duration: 0.35, ease: 'power2.out' });
    },
    onLeaveBack: () => {
      gsap.to(dock, { y: 60, opacity: 0, duration: 0.25, ease: 'power2.in' });
    }
  });
}

// 4. Antes y Después Táctil (Slider interactivo para Medicina Estética y Odontología)
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

// 5. Calculador Dinámico de Eventos y Catering (Presupuesto interactivo en vivo)
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
  let pricePerGuest = 18500;

  const recalculate = () => {
    if (guestsLabel) {
      guestsLabel.textContent = `${currentGuests} personas`;
      guestsLabel.classList.add('tabular-nums');
    }
    
    const estimatedTotal = (currentGuests * pricePerGuest).toLocaleString('es-AR');
    if (totalDisplay) {
      totalDisplay.textContent = `$${estimatedTotal}`;
      totalDisplay.classList.add('tabular-nums');
      if (!isReducedMotion()) {
        gsap.fromTo(totalDisplay, { scale: 0.97 }, { scale: 1, duration: 0.15, ease: 'power1.out' });
      }
    }

    if (waBtn) {
      const msg = `Hola Fuego y Tragos! Estuve cotizando en su web para un evento de ${currentGuests} invitados (${currentService}). Me gustaría consultar disponibilidad de fecha y presupuesto formal.`;
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

// 6. Selector Empático de Motivo de Consulta (Psicología)
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
        if (!isReducedMotion()) {
          gsap.fromTo(card, { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.28, ease: 'power2.out' });
        }
      }
    });
  });
}

// 7. Switch Interactivo de Precios Mensual vs Trimestral (Fitness)
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
        amountLabel.classList.add('tabular-nums');
        if (!isReducedMotion()) {
          gsap.fromTo(amountLabel, 
            { opacity: 0, y: -6 }, 
            { opacity: 1, y: 0, duration: 0.22, ease: 'power2.out' }
          );
        }
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

// 8. Asistente Rápido de Diagnóstico Legal (Abogados)
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
          if (!isReducedMotion()) {
            gsap.fromTo(d, { opacity: 0, y: 8 }, { opacity: 1, y: 0, duration: 0.25, ease: 'power2.out' });
          }
        } else {
          d.classList.add('hidden');
        }
      });
    });
  });
}

// 9. Radar de Urgencias 24hs (Urgencias Hogar)
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
        if (!isReducedMotion()) {
          gsap.fromTo(waBtn, { scale: 0.95 }, { scale: 1, duration: 0.2, ease: 'back.out(2)' });
        }
      }
    });
  });
}

// Inicializador Maestro de Widgets Dinámicos y Animaciones
export function initAllDynamicWidgets() {
  initHeroEntrance();
  initScrollReveal();
  initMobileDock();
  initBeforeAfterSliders();
  initEventCalculator();
  initPsychologySelector();
  initFitnessPricingToggle();
  initLegalAssistant();
  initEmergencySelector();
}

