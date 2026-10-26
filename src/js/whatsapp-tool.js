import QRCode from 'qrcode';

document.addEventListener('DOMContentLoaded', () => {
  const countrySelect = document.getElementById('wa-country');
  const phoneInput = document.getElementById('wa-phone');
  const messageInput = document.getElementById('wa-message');
  const phoneHint = document.getElementById('wa-phone-hint');
  const resultUrlInput = document.getElementById('wa-result-url');
  const copyUrlBtn = document.getElementById('wa-copy-url');
  const testUrlBtn = document.getElementById('wa-test-url');
  const previewBubble = document.getElementById('wa-preview-bubble');
  const previewPhoneHeader = document.getElementById('wa-preview-phone');
  const qrCanvas = document.getElementById('wa-qr-canvas');
  const downloadQrBtn = document.getElementById('wa-download-qr');
  const downloadCardBtn = document.getElementById('wa-download-card');
  const htmlCodeOutput = document.getElementById('wa-html-code');
  const copyHtmlBtn = document.getElementById('wa-copy-html');
  const templateBtns = document.querySelectorAll('[data-wa-template]');

  if (!phoneInput || !resultUrlInput || !qrCanvas) return;

  function normalizePhone(countryCode, rawPhone) {
    let digits = (rawPhone || '').replace(/\D+/g, '');
    if (!digits) return '';

    // Si ya pegaron el prefijo del país al principio, lo evitamos duplicar
    if (countryCode === '549') {
      if (digits.startsWith('549')) {
        digits = digits.slice(3);
      } else if (digits.startsWith('54')) {
        digits = digits.slice(2);
      }
      // Quitar el 0 inicial del código de área argentino (ej: 0264 -> 264, 011 -> 11)
      if (digits.startsWith('0')) {
        digits = digits.slice(1);
      }
    } else if (countryCode && digits.startsWith(countryCode)) {
      digits = digits.slice(countryCode.length);
    }

    return countryCode + digits;
  }

  function buildWhatsAppUrl() {
    const country = countrySelect ? countrySelect.value : '549';
    const rawPhone = phoneInput.value.trim();
    const msg = messageInput.value.trim();

    const cleanFullPhone = normalizePhone(country, rawPhone) || '5492645185359';
    const isPlaceholder = !rawPhone;

    if (phoneHint) {
      if (isPlaceholder) {
        phoneHint.textContent = 'Ingresá tu número sin 0 ni 15 (ej: 11 2345 6789 o 264 518 5359)';
        phoneHint.className = 'text-[11px] text-slate-500 mt-1.5';
      } else {
        phoneHint.textContent = `✓ Número internacional listo: +${cleanFullPhone}`;
        phoneHint.className = 'text-[11px] text-emerald-700 font-semibold mt-1.5';
      }
    }

    if (previewPhoneHeader) {
      previewPhoneHeader.textContent = `+${cleanFullPhone}`;
    }

    let url = `https://wa.me/${cleanFullPhone}`;
    if (msg) {
      url += `?text=${encodeURIComponent(msg)}`;
    }

    // Actualizar input de resultado y botón de prueba
    resultUrlInput.value = url;
    if (testUrlBtn) {
      testUrlBtn.href = url;
    }

    // Actualizar burbuja del simulador
    if (previewBubble) {
      previewBubble.textContent = msg || 'Hola! Quiero hacer una consulta...';
    }

    // Actualizar snippet de botón HTML
    if (htmlCodeOutput) {
      htmlCodeOutput.value = `<a href="${url}" target="_blank" rel="noopener noreferrer" style="position:fixed;bottom:22px;right:22px;z-index:9999;background:#10b981;color:#ffffff;font-family:sans-serif;font-weight:700;font-size:14px;padding:12px 20px;border-radius:999px;text-decoration:none;box-shadow:0 8px 20px rgba(16,185,129,0.35);">Consultar por WhatsApp</a>`;
    }

    // Actualizar Código QR en el Canvas visible
    QRCode.toCanvas(qrCanvas, url, {
      width: 220,
      margin: 2,
      color: {
        dark: '#0f172a',
        light: '#ffffff'
      },
      errorCorrectionLevel: 'H'
    }).catch(() => {});

    return { url, cleanFullPhone, msg };
  }

  // Eventos en tiempo real
  [countrySelect, phoneInput, messageInput].forEach(el => {
    if (el) {
      el.addEventListener('input', buildWhatsAppUrl);
      el.addEventListener('change', buildWhatsAppUrl);
    }
  });

  // Botones de plantillas por rubro
  templateBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const tpl = btn.getAttribute('data-wa-template');
      if (tpl && messageInput) {
        messageInput.value = tpl;
        buildWhatsAppUrl();
        messageInput.focus();
      }
    });
  });

  // Copiar Link wa.me
  if (copyUrlBtn) {
    copyUrlBtn.addEventListener('click', async () => {
      const { url } = buildWhatsAppUrl();
      try {
        await navigator.clipboard.writeText(url);
      } catch {
        resultUrlInput.select();
        document.execCommand('copy');
      }
      const orig = copyUrlBtn.innerHTML;
      copyUrlBtn.innerHTML = '<span>✓ ¡Link Copiado!</span>';
      copyUrlBtn.classList.add('bg-emerald-700');
      setTimeout(() => {
        copyUrlBtn.innerHTML = orig;
        copyUrlBtn.classList.remove('bg-emerald-700');
      }, 2200);
    });
  }

  // Copiar Código HTML
  if (copyHtmlBtn && htmlCodeOutput) {
    copyHtmlBtn.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(htmlCodeOutput.value);
      } catch {
        htmlCodeOutput.select();
        document.execCommand('copy');
      }
      const orig = copyHtmlBtn.textContent;
      copyHtmlBtn.textContent = '✓ ¡Código HTML Copiado!';
      setTimeout(() => {
        copyHtmlBtn.textContent = orig;
      }, 2200);
    });
  }

  // Descargar QR Limpio en Alta Resolución (1024x1024 PNG)
  if (downloadQrBtn) {
    downloadQrBtn.addEventListener('click', async () => {
      const { url, cleanFullPhone } = buildWhatsAppUrl();
      const hiResCanvas = document.createElement('canvas');
      await QRCode.toCanvas(hiResCanvas, url, {
        width: 1024,
        margin: 3,
        color: {
          dark: '#0f172a',
          light: '#ffffff'
        },
        errorCorrectionLevel: 'H'
      });
      const link = document.createElement('a');
      link.download = `qr-whatsapp-${cleanFullPhone}.png`;
      link.href = hiResCanvas.toDataURL('image/png');
      link.click();
    });
  }

  // Descargar Tarjeta Imprimible para Mostrador / Consultorio (1080x1350 PNG)
  if (downloadCardBtn) {
    downloadCardBtn.addEventListener('click', async () => {
      const { url, cleanFullPhone } = buildWhatsAppUrl();
      const cardCanvas = document.createElement('canvas');
      cardCanvas.width = 1080;
      cardCanvas.height = 1350;
      const ctx = cardCanvas.getContext('2d');

      // Fondo oscuro elegante
      ctx.fillStyle = '#0f172a';
      ctx.fillRect(0, 0, 1080, 1350);

      // Tarjeta blanca central
      ctx.fillStyle = '#ffffff';
      ctx.beginPath();
      ctx.roundRect(90, 110, 900, 1130, 44);
      ctx.fill();

      // Pastilla superior verde esmeralda
      ctx.fillStyle = '#ecfdf5';
      ctx.beginPath();
      ctx.roundRect(310, 180, 460, 64, 32);
      ctx.fill();

      ctx.fillStyle = '#047857';
      ctx.font = 'bold 26px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('ATENCIÓN DIRECTA POR WHATSAPP', 540, 222);

      // Título principal
      ctx.fillStyle = '#0f172a';
      ctx.font = 'bold 54px sans-serif';
      ctx.fillText('Escaneá el código QR', 540, 320);

      ctx.fillStyle = '#475569';
      ctx.font = '30px sans-serif';
      ctx.fillText('Abrí la cámara de tu celular para enviarnos un mensaje', 540, 378);

      // Generar el QR en un canvas auxiliar de 640x640
      const qrTemp = document.createElement('canvas');
      await QRCode.toCanvas(qrTemp, url, {
        width: 640,
        margin: 2,
        color: {
          dark: '#0f172a',
          light: '#ffffff'
        },
        errorCorrectionLevel: 'H'
      });

      // Marco suave alrededor del QR
      ctx.strokeStyle = '#e2e8f0';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.roundRect(210, 430, 660, 660, 32);
      ctx.stroke();

      ctx.drawImage(qrTemp, 220, 440, 640, 640);

      // Número al pie de la tarjeta blanca
      ctx.fillStyle = '#0f172a';
      ctx.font = 'bold 34px sans-serif';
      ctx.fillText(`WhatsApp: +${cleanFullPhone}`, 540, 1165);

      // Sello discreto inferior
      ctx.fillStyle = '#94a3b8';
      ctx.font = '22px sans-serif';
      ctx.fillText('QR permanente sin vencimiento • erikwebsite.com', 540, 1295);

      const link = document.createElement('a');
      link.download = `tarjeta-qr-whatsapp-${cleanFullPhone}.png`;
      link.href = cardCanvas.toDataURL('image/png');
      link.click();
    });
  }

  // Inicializar estado por defecto
  buildWhatsAppUrl();
});
