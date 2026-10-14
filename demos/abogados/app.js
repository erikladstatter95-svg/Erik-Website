import { initWhatsAppButtons, buildWhatsAppUrl } from '../../src/js/whatsapp.js';
import { initAccordion } from '../../src/js/accordion.js';
import { initScrollTop } from '../../src/js/scroll-top.js';
import { initLegalAssistant, initScrollReveal, initHeroEntrance, initMobileDock, isReducedMotion } from '../../src/js/animations.js';
import { gsap } from 'gsap';

export function initIndemnizacionCalculator() {
  const calc = document.getElementById('indemnizacion-calculator');
  if (!calc) return;

  const salaryRange = calc.querySelector('#calc-salary-range');
  const salaryInput = calc.querySelector('#calc-salary-input');
  const seniorityRange = calc.querySelector('#calc-seniority-range');
  const seniorityLabel = calc.querySelector('#calc-seniority-label');
  const causeButtons = calc.querySelectorAll('.calc-cause-btn');

  const resAntiguedad = calc.querySelector('#calc-res-antiguedad');
  const resPreaviso = calc.querySelector('#calc-res-preaviso');
  const resSac = calc.querySelector('#calc-res-sac');
  const resTotal = calc.querySelector('#calc-res-total');
  const waBtn = calc.querySelector('#calc-wa-send');
  const presetBtns = calc.querySelectorAll('.calc-preset-salary');

  let currentSalary = salaryRange ? parseInt(salaryRange.value, 10) : 850000;
  let currentSeniority = seniorityRange ? parseInt(seniorityRange.value, 10) : 3;
  let currentCause = 'sin_causa'; // 'sin_causa' | 'no_registrado'

  const formatCurrency = (val) => {
    return '$' + Math.round(val).toLocaleString('es-AR');
  };

  const calculate = () => {
    // 1. Antigüedad (Art. 245 LCT): 1 sueldo por cada año de antigüedad
    const antiguedadMonto = currentSalary * currentSeniority;

    // 2. Preaviso (Art. 231/232 LCT): 1 mes si < 5 años, 2 meses si >= 5 años
    const preavisoMonto = currentSeniority >= 5 ? currentSalary * 2 : currentSalary;

    // 3. Integración mes de despido y proporcional SAC / Vacaciones (~1.5 a 2 meses promedio proporcional)
    const sacMonto = Math.round((currentSalary / 12) * 6 + (currentSalary / 25) * 14);

    let totalBase = antiguedadMonto + preavisoMonto + sacMonto;

    // Si es trabajo no registrado, agregamos estimación de multas laborales (Art. 8, 15 Ley 24.013 / Ley 25.323)
    let multasTexto = '';
    if (currentCause === 'no_registrado') {
      const multasEstimadas = totalBase * 0.5; // Estimado legal prudencial
      totalBase += multasEstimadas;
      multasTexto = ' (incluyendo estimación de multas por falta de registración)';
    }

    // Actualizar visualmente los campos
    if (resAntiguedad) resAntiguedad.textContent = formatCurrency(antiguedadMonto);
    if (resPreaviso) resPreaviso.textContent = formatCurrency(preavisoMonto);
    if (resSac) resSac.textContent = formatCurrency(sacMonto);
    
    if (resTotal) {
      resTotal.textContent = formatCurrency(totalBase);
      if (!isReducedMotion() && typeof gsap !== 'undefined' && gsap.fromTo) {
        gsap.fromTo(resTotal, { scale: 0.96 }, { scale: 1, duration: 0.18, ease: 'power1.out' });
      }
    }

    if (seniorityLabel) {
      seniorityLabel.textContent = `${currentSeniority} ${currentSeniority === 1 ? 'año' : 'años'}`;
    }

    // Actualizar enlace directo de WhatsApp con mensaje personalizado
    if (waBtn) {
      const motivoDesc = currentCause === 'no_registrado' ? 'trabajo en negro / mal registrado con multas' : 'despido sin causa';
      const msg = `Hola Dr. Albarracín! Hice el cálculo de liquidación en su web para un sueldo de ${formatCurrency(currentSalary)} con ${currentSeniority} años de antigüedad (${motivoDesc}). El cálculo orientativo me da ${formatCurrency(totalBase)}. Quisiera una consulta para evaluar el reclamo formal con mis recibos/telegrama.`;
      waBtn.setAttribute('data-wa-msg', msg);
    }
  };

  // Listeners de Sueldo
  if (salaryRange && salaryInput) {
    salaryRange.addEventListener('input', (e) => {
      currentSalary = parseInt(e.target.value, 10);
      salaryInput.value = currentSalary;
      calculate();
    });

    salaryInput.addEventListener('change', (e) => {
      let val = parseInt(e.target.value, 10) || 300000;
      val = Math.max(200000, Math.min(5000000, val));
      currentSalary = val;
      salaryRange.value = val;
      salaryInput.value = val;
      calculate();
    });
  }

  // Presets de sueldo
  presetBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const val = parseInt(btn.getAttribute('data-preset-val') || '850000', 10);
      currentSalary = val;
      if (salaryRange) salaryRange.value = val;
      if (salaryInput) salaryInput.value = val;
      presetBtns.forEach(b => b.classList.remove('active', 'border-rose-900', 'bg-rose-900/10', 'text-rose-950'));
      btn.classList.add('active', 'border-rose-900', 'bg-rose-900/10', 'text-rose-950');
      calculate();
    });
  });

  // Antigüedad
  if (seniorityRange) {
    seniorityRange.addEventListener('input', (e) => {
      currentSeniority = parseInt(e.target.value, 10);
      calculate();
    });
  }

  // Causa / Motivo
  causeButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      causeButtons.forEach(b => b.classList.remove('active', 'border-rose-900', 'bg-rose-50', 'text-rose-950', 'font-bold'));
      btn.classList.add('active', 'border-rose-900', 'bg-rose-50', 'text-rose-950', 'font-bold');
      currentCause = btn.getAttribute('data-calc-cause') || 'sin_causa';
      calculate();
    });
  });

  calculate();
}

document.addEventListener('DOMContentLoaded', () => {
  const LAW_PHONE = '5492645185359';

  try { initWhatsAppButtons(LAW_PHONE); } catch (err) { console.error('Error initWhatsAppButtons:', err); }
  try { initAccordion('[data-accordion]'); } catch (err) { console.error('Error initAccordion:', err); }
  try { initScrollTop('btn-scroll-top'); } catch (err) { console.error('Error initScrollTop:', err); }
  try { initHeroEntrance(); } catch (err) { console.error('Error initHeroEntrance:', err); }
  try { initLegalAssistant(); } catch (err) { console.error('Error initLegalAssistant:', err); }
  try { initIndemnizacionCalculator(); } catch (err) { console.error('Error initIndemnizacionCalculator:', err); }
  try { initScrollReveal(); } catch (err) { console.error('Error initScrollReveal:', err); }
  try { initMobileDock(); } catch (err) { console.error('Error initMobileDock:', err); }

  // Header scroll con sombra suave en fondo cálido
  const header = document.getElementById('abogados-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.classList.add('shadow-md', 'bg-[#fcfaf7]/95', 'backdrop-blur-md');
        header.classList.remove('bg-transparent');
      } else {
        header.classList.remove('shadow-md', 'bg-[#fcfaf7]/95', 'backdrop-blur-md');
        header.classList.add('bg-transparent');
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
      const zone = document.getElementById('inquiry-zone')?.value || 'CABA / GBA / San Juan';
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
