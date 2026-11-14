import { initWhatsAppButtons } from '../../src/js/whatsapp.js';
import { initScrollTop } from '../../src/js/scroll-top.js';
import { initScrollReveal, initHeroEntrance, initMobileDock } from '../../src/js/animations.js';

document.addEventListener('DOMContentLoaded', () => {
  const WHATSAPP_PHONE = '5492645185359';

  initWhatsAppButtons(WHATSAPP_PHONE);
  initScrollTop('btn-scroll-top');
  initHeroEntrance();
  initScrollReveal();
  initMobileDock();

  // =========================================================================
  // 1. FILTRADO INTERACTIVO DE OBRAS / PORTFOLIO
  // =========================================================================
  const filterTabs = document.querySelectorAll('.portfolio-tab');
  const projectCards = document.querySelectorAll('.project-card');

  if (filterTabs.length > 0 && projectCards.length > 0) {
    filterTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        // Estilos activos
        filterTabs.forEach(t => {
          t.classList.remove('bg-white', 'text-neutral-950', 'font-bold');
          t.classList.add('bg-neutral-900', 'text-neutral-400', 'border', 'border-white/10');
        });
        tab.classList.remove('bg-neutral-900', 'text-neutral-400', 'border', 'border-white/10');
        tab.classList.add('bg-white', 'text-neutral-950', 'font-bold');

        const filter = tab.getAttribute('data-filter');

        projectCards.forEach(card => {
          const category = card.getAttribute('data-category');
          if (filter === 'todos' || category === filter) {
            card.style.display = 'flex';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // =========================================================================
  // 2. MODAL INTERACTIVO DE FICHA TÉCNICA DE PROYECTO
  // =========================================================================
  const modal = document.getElementById('project-modal');
  const btnCloseModal = document.getElementById('btn-close-modal');
  const modalCategory = document.getElementById('modal-category');
  const modalTitle = document.getElementById('modal-title');
  const modalLocation = document.getElementById('modal-location');
  const modalSurface = document.getElementById('modal-surface');
  const modalTime = document.getElementById('modal-time');
  const modalImage = document.getElementById('modal-image');
  const modalDesc = document.getElementById('modal-desc');
  const modalWaBtn = document.getElementById('modal-wa-btn');

  if (modal && btnCloseModal) {
    document.querySelectorAll('.btn-open-modal').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const card = e.target.closest('.project-card');
        if (!card) return;

        const title = card.getAttribute('data-title') || '';
        const category = card.getAttribute('data-category') || '';
        const location = card.getAttribute('data-location') || '';
        const surface = card.getAttribute('data-surface') || '';
        const time = card.getAttribute('data-time') || '';
        const desc = card.getAttribute('data-desc') || '';
        const image = card.getAttribute('data-image') || '';

        modalCategory.textContent = category.toUpperCase();
        modalTitle.textContent = title;
        modalLocation.textContent = location;
        modalSurface.textContent = surface;
        modalTime.textContent = time;
        modalDesc.textContent = desc;
        modalImage.src = image;
        modalImage.alt = title;

        const waText = encodeURIComponent(`Hola Estudio Vértice! Estuve viendo la ficha de "${title}" (${location}) y me interesa consultar por un proyecto similar.`);
        modalWaBtn.href = `https://wa.me/${WHATSAPP_PHONE}?text=${waText}`;

        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
      });
    });

    const closeModal = () => {
      modal.classList.remove('active');
      document.body.style.overflow = '';
    };

    btnCloseModal.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal();
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('active')) {
        closeModal();
      }
    });
  }

  // =========================================================================
  // 3. COMPARADOR INTERACTIVO "ANTES Y DESPUÉS" (SLIDER)
  // =========================================================================
  const baSlider = document.getElementById('before-after-slider');
  const baLayer = document.getElementById('ba-layer');
  const baHandle = document.getElementById('ba-handle');
  const baBeforeImg = document.getElementById('ba-before-img');

  if (baSlider && baLayer && baHandle && baBeforeImg) {
    let isDragging = false;

    const setSliderPosition = (x) => {
      const rect = baSlider.getBoundingClientRect();
      let pos = (x - rect.left) / rect.width;
      if (pos < 0) pos = 0;
      if (pos > 1) pos = 1;

      const percentage = pos * 100;
      baLayer.style.width = `${percentage}%`;
      baHandle.style.left = `${percentage}%`;

      // Mantener ancho constante de la imagen de antes
      baBeforeImg.style.width = `${rect.width}px`;
    };

    // Ajustar imagen inicial
    const initSliderWidth = () => {
      const rect = baSlider.getBoundingClientRect();
      baBeforeImg.style.width = `${rect.width}px`;
    };
    initSliderWidth();
    window.addEventListener('resize', initSliderWidth);

    // Eventos Mouse
    baSlider.addEventListener('mousedown', (e) => {
      isDragging = true;
      setSliderPosition(e.clientX);
    });
    window.addEventListener('mouseup', () => { isDragging = false; });
    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      setSliderPosition(e.clientX);
    });

    // Eventos Touch (Celulares)
    baSlider.addEventListener('touchstart', (e) => {
      isDragging = true;
      setSliderPosition(e.touches[0].clientX);
    }, { passive: true });
    window.addEventListener('touchend', () => { isDragging = false; });
    window.addEventListener('touchmove', (e) => {
      if (!isDragging) return;
      setSliderPosition(e.touches[0].clientX);
    }, { passive: true });
  }

  // =========================================================================
  // 4. COTIZADOR INTERACTIVO DE PROYECTO A WHATSAPP
  // =========================================================================
  const typeBtns = document.querySelectorAll('.calc-type-btn');
  const surfaceBtns = document.querySelectorAll('.calc-surface-btn');
  const locationSelect = document.getElementById('calc-location');
  const scopeSelect = document.getElementById('calc-scope');
  const msgPreview = document.getElementById('whatsapp-message-preview');
  const btnSendWa = document.getElementById('btn-send-whatsapp-calc');

  let selectedType = 'Remodelación Integral';
  let selectedSurface = '60 a 140 m² (Estándar 3/4 amb)';

  const updateWhatsAppMessage = () => {
    const loc = locationSelect ? locationSelect.value : 'CABA';
    const scope = scopeSelect ? scopeSelect.value : 'Llave en mano';

    const text = `Hola Estudio Vértice! Quiero consultar por un proyecto de: *${selectedType}* en *${loc}*, superficie estimada *${selectedSurface}*. Modalidad: *${scope}*. ¿Podemos coordinar un relevamiento técnico inicial?`;

    if (msgPreview) {
      msgPreview.textContent = text;
    }
    if (btnSendWa) {
      btnSendWa.href = `https://wa.me/${WHATSAPP_PHONE}?text=${encodeURIComponent(text)}`;
    }
  };

  if (typeBtns.length > 0) {
    typeBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        typeBtns.forEach(b => {
          b.classList.remove('border-amber-400', 'bg-amber-500/10', 'text-white');
          b.classList.add('border-white/10', 'bg-neutral-950', 'text-neutral-400');
        });
        btn.classList.remove('border-white/10', 'bg-neutral-950', 'text-neutral-400');
        btn.classList.add('border-amber-400', 'bg-amber-500/10', 'text-white');
        selectedType = btn.getAttribute('data-type') || 'Remodelación Integral';
        updateWhatsAppMessage();
      });
    });
  }

  if (surfaceBtns.length > 0) {
    surfaceBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        surfaceBtns.forEach(b => {
          b.classList.remove('border-amber-400', 'bg-amber-500/10', 'text-white', 'font-bold');
          b.classList.add('border-white/10', 'bg-neutral-950', 'text-neutral-400');
        });
        btn.classList.remove('border-white/10', 'bg-neutral-950', 'text-neutral-400');
        btn.classList.add('border-amber-400', 'bg-amber-500/10', 'text-white', 'font-bold');
        selectedSurface = btn.getAttribute('data-surface') || '60 a 140 m²';
        updateWhatsAppMessage();
      });
    });
  }

  if (locationSelect) {
    locationSelect.addEventListener('change', updateWhatsAppMessage);
  }
  if (scopeSelect) {
    scopeSelect.addEventListener('change', updateWhatsAppMessage);
  }

  // Inicializar mensaje al cargar
  updateWhatsAppMessage();
});
