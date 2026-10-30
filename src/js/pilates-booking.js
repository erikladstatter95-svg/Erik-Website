/**
 * pilates-booking.js
 * Selector dinámico de día individual y horario para el Estudio de Pilates & Movilidad
 */
export function initPilatesBooking() {
  const dayButtons = document.querySelectorAll('[data-day-btn]');
  const scheduleContainers = document.querySelectorAll('[data-day-schedule]');
  const slotButtons = document.querySelectorAll('[data-slot-btn]');
  const selectedInfo = document.getElementById('selected-schedule-info');
  const reserveBtn = document.getElementById('reserve-whatsapp-btn');

  let currentDay = 'Lunes';
  let currentHour = '18:00 hs';
  let currentClass = 'Pilates Reformer (Camas)';

  // Cambio de pestaña de día (Lunes, Martes, Miércoles, etc.)
  dayButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetDay = btn.getAttribute('data-day-btn');
      currentDay = targetDay;

      dayButtons.forEach(b => {
        b.classList.remove('bg-[#14532d]', 'text-white', 'shadow-xs');
        b.classList.add('bg-white', 'text-stone-700', 'border-stone-200');
      });
      btn.classList.add('bg-[#14532d]', 'text-white', 'shadow-xs');
      btn.classList.remove('bg-white', 'text-stone-700', 'border-stone-200');

      scheduleContainers.forEach(container => {
        if (container.getAttribute('data-day-schedule') === targetDay) {
          container.classList.remove('hidden');
        } else {
          container.classList.add('hidden');
        }
      });

      // Seleccionar el primer turno disponible de ese día
      const firstSlot = document.querySelector(`[data-day-schedule="${targetDay}"] [data-slot-btn]`);
      if (firstSlot) {
        firstSlot.click();
      } else {
        updateSummary();
      }
    });
  });

  // Selección de slot de horario
  slotButtons.forEach(slot => {
    slot.addEventListener('click', () => {
      slotButtons.forEach(s => {
        s.classList.remove('ring-2', 'ring-[#14532d]', 'bg-emerald-50/80', 'border-[#14532d]');
      });
      slot.classList.add('ring-2', 'ring-[#14532d]', 'bg-emerald-50/80', 'border-[#14532d]');
      currentHour = slot.getAttribute('data-hour') || currentHour;
      currentClass = slot.getAttribute('data-class') || currentClass;
      updateSummary();
    });
  });

  function updateSummary() {
    if (selectedInfo) {
      selectedInfo.textContent = `${currentDay} a las ${currentHour} • ${currentClass}`;
    }
    if (reserveBtn) {
      const msg = `Hola! Estuve viendo la grilla de horarios en Lumina Pilates y quiero consultar si hay cupo disponible para el día ${encodeURIComponent(currentDay)} a las ${encodeURIComponent(currentHour)} (${encodeURIComponent(currentClass)}). ¿Cómo hacemos para coordinar la clase de prueba?`;
      reserveBtn.href = `https://wa.me/5492645185359?text=${msg}`;
    }
  }

  updateSummary();
}
