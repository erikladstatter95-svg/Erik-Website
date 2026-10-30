/**
 * fitness-calc.js
 * Calculadora interactiva de evaluación física y plan sugerido para Personal Trainers
 */
export function initFitnessCalc() {
  const genderInputs = document.querySelectorAll('input[name="fit-gender"]');
  const daysSelect = document.getElementById('fit-days');
  const goalSelect = document.getElementById('fit-goal');
  const levelSelect = document.getElementById('fit-level');
  
  const recPlanTitle = document.getElementById('rec-plan-title');
  const recPlanBadge = document.getElementById('rec-plan-badge');
  const recPlanDesc = document.getElementById('rec-plan-desc');
  const recPlanPrice = document.getElementById('rec-plan-price');
  const recPlanFeatures = document.getElementById('rec-plan-features');
  const recPlanWaBtn = document.getElementById('rec-plan-wa-btn');

  if (!daysSelect || !goalSelect || !recPlanTitle) return;

  function updateRecommendation() {
    const days = daysSelect.value;
    const goal = goalSelect.value;
    const level = levelSelect ? levelSelect.value : 'principiante';
    const gender = document.querySelector('input[name="fit-gender"]:checked')?.value || 'hombre';

    let planName = 'Asesoría Integral 1 a 1';
    let badgeText = 'RECOMENDADO PARA VOS';
    let priceText = '$35.000 ARS / mes';
    let descText = 'Plan 100% individualizado con rutina en app, ajustes semanales y corrección de técnica por video.';
    let features = [
      'Rutina adaptada a tu gimnasio o casa',
      'Pautas de alimentación flexible sin pasar hambre',
      'Corrección de videos de ejecución de ejercicios',
      'Contacto directo 1 a 1 por WhatsApp'
    ];

    if (days === '2' && level === 'principiante') {
      planName = 'Rutina a Distancia Estructurada';
      badgeText = 'IDEAL PARA ARRANCAR';
      priceText = '$22.000 ARS / mes';
      descText = 'Rutina paso a paso con videos explicativos de cada ejercicio para entrenar a tu ritmo con técnica segura.';
      features = [
        'Rutina estructurada dividida en 2 o 3 días',
        'Videos en alta definición de cada movimiento',
        'Guía básica de calentamiento y movilidad',
        'Soporte mensual de dudas por mensaje'
      ];
    } else if (days === '5' || level === 'avanzado' || goal === 'fuerza') {
      planName = 'Coaching de Alto Rendimiento VIP';
      badgeText = 'MÁXIMO SEGUIMIENTO';
      priceText = '$55.000 ARS / mes';
      descText = 'Para quienes buscan romper estancamientos, hipertrofia exigente o preparación específica con control fino de cargas.';
      features = [
        'Periodización avanzada RPE / RIR semana a semana',
        'Ajustes diarios de macronutrientes y calorías',
        'Llamada mensual de balance y revisión biomecánica',
        'Cupo súper limitado a 10 alumnos simultáneos'
      ];
    }

    recPlanTitle.textContent = planName;
    recPlanBadge.textContent = badgeText;
    recPlanDesc.textContent = descText;
    recPlanPrice.textContent = priceText;

    if (recPlanFeatures) {
      recPlanFeatures.innerHTML = features.map(f => `
        <li class="flex items-center gap-2 text-xs sm:text-sm text-neutral-300">
          <svg class="w-4 h-4 text-lime-400 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/>
          </svg>
          <span>${f}</span>
        </li>
      `).join('');
    }

    if (recPlanWaBtn) {
      const msg = `Hola Franco! Hice el test en tu web:%0A- Objetivo: ${goal}%0A- Disponibilidad: ${days} días/semana%0A- Nivel: ${level}%0A%0AQuiero consultar por el plan ${encodeURIComponent(planName)} para arrancar.`;
      recPlanWaBtn.href = `https://wa.me/5492645185359?text=${msg}`;
    }
  }

  daysSelect.addEventListener('change', updateRecommendation);
  goalSelect.addEventListener('change', updateRecommendation);
  if (levelSelect) levelSelect.addEventListener('change', updateRecommendation);
  genderInputs.forEach(i => i.addEventListener('change', updateRecommendation));

  // Run on load
  updateRecommendation();
}
