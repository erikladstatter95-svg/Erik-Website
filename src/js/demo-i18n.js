/**
 * demo-i18n.js
 * Inhabilitado para evitar mutaciones de precios/textos en demos.
 * Los precios se mantienen siempre en moneda nacional fija ($150.000 ARS / $20.000 ARS/mes).
 */
(function () {
  try {
    localStorage.removeItem('preferred_lang');
  } catch (e) {}
})();
