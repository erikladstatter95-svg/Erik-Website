import { initWhatsAppButtons } from '../../src/js/whatsapp.js';
import { initAccordion } from '../../src/js/accordion.js';
import { initScrollTop } from '../../src/js/scroll-top.js';
import { initScrollReveal, initHeroEntrance, initMobileDock } from '../../src/js/animations.js';
import { initPilatesBooking } from '../../src/js/pilates-booking.js';

document.addEventListener('DOMContentLoaded', () => {
  const PILATES_PHONE = '5492645185359';

  initWhatsAppButtons(PILATES_PHONE);
  initAccordion('[data-accordion]');
  initScrollTop('btn-scroll-top');
  initHeroEntrance();
  initScrollReveal();
  initMobileDock();
  initPilatesBooking();

  // Header scroll blur & shadow
  const header = document.querySelector('header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.classList.add('shadow-md', 'bg-stone-50/95');
      } else {
        header.classList.remove('shadow-md', 'bg-stone-50/95');
      }
    });
  }
});
