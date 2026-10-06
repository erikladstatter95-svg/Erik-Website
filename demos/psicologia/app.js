import { initWhatsAppButtons } from '../../src/js/whatsapp.js';
import { initAccordion } from '../../src/js/accordion.js';
import { initScrollTop } from '../../src/js/scroll-top.js';
import { initScrollReveal, initHeroEntrance, initMobileDock, initPsychologySelector } from '../../src/js/animations.js';

document.addEventListener('DOMContentLoaded', () => {
  const PSICO_PHONE = '5492645185359';

  initWhatsAppButtons(PSICO_PHONE);
  initAccordion('[data-accordion]');
  initScrollTop('btn-scroll-top');
  initHeroEntrance();
  initScrollReveal();
  initMobileDock();
  initPsychologySelector();
});
