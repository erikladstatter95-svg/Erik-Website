/**
 * fitness-calc.js
 * Calculadora interactiva de evaluación física y plan sugerido para Personal Trainers
 */
export function initFitnessCalc() {
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
    const days = parseInt(daysSelect.value, 10) || 3;
    const goal = goalSelect.value;
    const level = levelSelect ? levelSelect.value : 'principiante';

    // Matriz de precios transparentes y diferenciados según Días y Nivel de Experiencia
    // Principiante: Rutina de adaptación guiada y técnica segura
    // Intermedio: Rutina con sobrecarga progresiva y nutrición flexible
    // Avanzado: Periodización avanzada de alto rendimiento, microciclos y control fino de fatiga
    const pricingMatrix = {
      2: {
        principiante: {
          name: 'Plan Adaptación Inicial (2 Días)',
          badge: 'IDEAL PARA ARRANCAR DE CERO',
          price: '$20.000 ARS / mes',
          desc: 'Rutina Full Body de 2 días a la semana diseñada para crear el hábito sin fatiga excesiva ni agujetas dolorosas.',
          features: [
            '2 sesiones semanales de 45 min con ejercicios básicos',
            'Videos explicativos en app de cada movimiento',
            'Enfoque en salud articular y movilidad postural',
            'Contacto de dudas por WhatsApp'
          ]
        },
        intermedio: {
          name: 'Plan Rutina Mantenimiento (2 Días)',
          badge: 'EFICIENCIA MÁXIMA DE TIEMPO',
          price: '$24.000 ARS / mes',
          desc: 'Para quienes tienen poco tiempo pero quieren mantener masa muscular y fuerza con mínima dosis efectiva.',
          features: [
            '2 sesiones semanales de alta intensidad inteligente',
            'Pautas de proteínas y energía diaria',
            'Planilla de registro de pesos y repeticiones',
            'Revisión mensual de técnica por video'
          ]
        },
        avanzado: {
          name: 'Plan Específico de Rendimiento (2 Días)',
          badge: 'COMPLEMENTO PARA ATLETAS',
          price: '$29.000 ARS / mes',
          desc: 'Complemento de fuerza y prevención de lesiones para runners, ciclistas, jugadores de pádel o artes marciales.',
          features: [
            'Rutina de potencia y estabilidad según tu deporte',
            'Gestión de fatiga neuromuscular combinada',
            'Ajustes quincenales según tu calendario de partidos/carreras',
            'Soporte técnico directo con Franco'
          ]
        }
      },
      3: {
        principiante: {
          name: 'Plan Integral Principiante (3 Días)',
          badge: 'EL MÁS ELEGIDO PARA EMPEZAR',
          price: '$28.000 ARS / mes',
          desc: 'Frecuencia óptima de 3 días para ver cambios visibles de fuerza y composición corporal desde el primer mes.',
          features: [
            'Rutina dividida (Torso / Pierna / Full Body)',
            'Guía de alimentación simple sin pasar hambre',
            'Corrección semanal de técnica por video',
            'Seguimiento cercano por WhatsApp 1 a 1'
          ]
        },
        intermedio: {
          name: 'Asesoría Integral 1 a 1 (3 Días)',
          badge: 'MÁS ELEGIDO • RECOMENDADO',
          price: '$35.000 ARS / mes',
          desc: 'Acompañamiento completo para romper estancamientos, ganar masa muscular y definir con nutrición flexible calculada.',
          features: [
            'Periodización personalizada con sobrecarga progresiva',
            'Cálculo de calorías y macronutrientes a tu medida',
            'Corrección ilimitada de videos de ejecución',
            'Ajuste semanal según peso, medidas y sensaciones'
          ]
        },
        avanzado: {
          name: 'Coaching Biomecánico de Élite (3 Días)',
          badge: 'ALTO NIVEL Y PRECISIÓN',
          price: '$42.000 ARS / mes',
          desc: 'Optimización de perfiles de resistencia, selección milimétrica de ejercicios y control de RPE/RIR por serie.',
          features: [
            'Rutina de hipertrofia y fuerza de máxima especificidad',
            'Análisis biomecánico cuadro por cuadro de tus levantamientos',
            'Estrategias de nutrición peri-entrenamiento y suplementación',
            'Prioridad de respuesta en WhatsApp los 7 días'
          ]
        }
      },
      5: {
        principiante: {
          name: 'Plan Hábito Activo Guiado (5 Días)',
          badge: 'CAMBIO DE RITMO Y CONSTANCIA',
          price: '$36.000 ARS / mes',
          desc: 'Para quienes quieren estar activos de lunes a viernes combinando fuerza moderada, cardio estructurado y movilidad.',
          features: [
            'División inteligente de 5 días para no sobrecargar articulaciones',
            'Bloques de movilidad y prevención de dolor de espalda',
            'Pautas de hidratación, descanso y pasos diarios',
            'Feedback continuo semanal por WhatsApp'
          ]
        },
        intermedio: {
          name: 'Asesoría de Alto Volumen (5 Días)',
          badge: 'HIPERTROFIA & DEFINICIÓN AVANZADA',
          price: '$45.000 ARS / mes',
          desc: 'Para entrenar 5 días con división Push-Pull-Legs-Upper-Lower y acelerar la recomposición corporal.',
          features: [
            'Distribución de volumen semanal óptimo por grupo muscular',
            'Ajustes dinámicos de déficit calórico o superávit limpio',
            'Monitoreo semanal de fuerza, fatiga y estrés',
            'Seguimiento intensivo 1 a 1 en WhatsApp'
          ]
        },
        avanzado: {
          name: 'Coaching de Máximo Rendimiento VIP (5 Días)',
          badge: 'PREPARACIÓN DEPORTIVA DE ÉLITE',
          price: '$55.000 ARS / mes',
          desc: 'El servicio más exigente: periodización ondulatoria, volumen individualizado y acompañamiento total.',
          features: [
            'Periodización avanzada RPE / RIR semana a semana',
            'Ajustes diarios de macronutrientes, ciclo de carbohidratos y timing',
            'Llamada mensual de balance y revisión biomecánica',
            'Cupo súper limitado a 10 alumnos simultáneos'
          ]
        }
      }
    };

    const plan = pricingMatrix[days]?.[level] || pricingMatrix[3]['intermedio'];

    recPlanTitle.textContent = plan.name;
    recPlanBadge.textContent = plan.badge;
    recPlanDesc.textContent = plan.desc;
    recPlanPrice.textContent = plan.price;

    if (recPlanFeatures) {
      recPlanFeatures.innerHTML = plan.features.map(f => `
        <li class="flex items-start gap-2.5 text-xs sm:text-sm text-neutral-300">
          <svg class="w-4 h-4 text-lime-400 shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/>
          </svg>
          <span>${f}</span>
        </li>
      `).join('');
    }

    if (recPlanWaBtn) {
      const msg = `Hola Franco! Hice el test en tu web:%0A- Objetivo: ${goal}%0A- Disponibilidad: ${days} días/semana%0A- Nivel: ${level}%0A- Plan sugerido: ${plan.name} (${plan.price})%0A%0AQuiero consultar para coordinar la evaluación inicial y arrancar.`;
      recPlanWaBtn.href = `https://wa.me/5492645185359?text=${msg}`;
    }
  }

  daysSelect.addEventListener('change', updateRecommendation);
  goalSelect.addEventListener('change', updateRecommendation);
  if (levelSelect) levelSelect.addEventListener('change', updateRecommendation);

  // Run on load
  updateRecommendation();
}
