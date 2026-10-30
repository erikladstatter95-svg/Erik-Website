/**
 * pilates-booking.js
 * Selector de disciplina, turnos y reserva para el Estudio de Pilates & Movilidad
 */
export function initPilatesBooking() {
  const disciplineButtons = document.querySelectorAll('[data-pilates-disc]');
  const scheduleSlots = document.querySelectorAll('[data-slot-btn]');
  const bookedModal = document.getElementById('pilates-modal');
  const selectedInfo = document.getElementById('selected-schedule-info');
  const reserveBtn = document.getElementById('reserve-whatsapp-btn');

  let currentDisc = 'Pilates Reformer (Camas)';
  let currentDay = 'Lunes y Miércoles';
  let currentHour = '18:00 hs';

  disciplineButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      disciplineButtons.forEach(b => {
        b.classList.remove('bg-emerald-800', 'text-white', 'border-emerald-600');
        b.classList.add('bg-stone-100', 'text-stone-700', 'border-stone-200');
      });
      btn.classList.add('bg-emerald-800', 'text-white', 'border-emerald-600');
      btn.classList.remove('bg-stone-100', 'text-stone-700', 'border-stone-200');
      currentDisc = btn.getAttribute('data-pilates-disc');
      updateSummary();
    });
  });

  scheduleSlots.forEach(slot => {
    slot.addEventListener('click', () => {
      scheduleSlots.forEach(s => {
        s.classList.remove('ring-2', 'ring-emerald-600', 'bg-emerald-50');
      });
      slot.classList.add('ring-2', 'ring-emerald-600', 'bg-emerald-50');
      currentDay = slot.getAttribute('data-day') || currentDay;
      currentHour = slot.getAttribute('data-hour') || currentHour;
      updateSummary();
    });
  });

  function updateSummary() {
    if (selectedInfo) {
      selectedInfo.textContent = `${currentDisc} • ${currentDay} a las ${currentHour}`;
    }
    if (reserveBtn) {
      const msg = `Hola! Quiero reservar una clase de prueba o consultar cupo en Lumina Pilates:%0A- Disciplina: ${encodeURIComponent(currentDisc)}%0A- Horario de preferencia: ${encodeURIComponent(currentDay)} a las ${encodeURIComponent(currentHour)}%0A%0A¿Tienen disponibilidad para esta semana?`;
      reserveBtn.href = `https://wa.me/5492645185359?text=${msg}`;
    }
  }

  updateSummary();
}
