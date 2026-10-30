# MEMORY.md — WebErik (`erikwebsite.com`)

## 📌 Contexto del Proyecto
- **Nombre:** WebErik (`erikwebsite.com`)
- **Autor:** Erik Ladstatter (siempre sin diéresis)
- **Propósito:** Plataforma comercial, portfolio de demos interactivas y hub de contenidos SEO / AEO / GEO para la venta de desarrollo web de alta conversión (Landing Pages a medida, Catálogos con carrito a WhatsApp y Posicionamiento en Google Maps) en Argentina y el exterior (`/en/`).
- **Oferta Principal (Argentina):** Landing Page profesional en código a medida por **$150.000 ARS finales** (pago único, entregada en 3 a 5 días hábiles, mantenimiento opcional de $20.000 ARS/mes). Catálogos multi-producto y tiendas online se cotizan a medida.
- **Oferta Internacional (`/en/`):** **$199 USD** setup único, **$20 USD/mes** mantenimiento opcional (PayPal, Wise, Wire, Crypto).

---

## 🛠️ Stack Tecnológico & Entorno
- **Frontend & Build:** HTML5 semántico multipágina, Tailwind CSS, Vanilla JavaScript modular (ES6+), GSAP (animaciones), Vite (`vite.config.js`).
- **Infraestructura & Dominio:** Cloudflare + Correo corporativo `erik@erikwebsite.com` configurado vía Cloudflare Email Routing (entrante) + SMTP oficial de Gmail (`smtp.gmail.com` con App Password de 16 caracteres, evitando reescritura de enlaces SSL de terceros).
- **Google Search Console & Indexing API:** Enlazado con credenciales de cuenta de servicio (`seo-asistente@erik-website-seo.iam.gserviceaccount.com`, nivel `siteOwner` en `sc-domain:erikwebsite.com`), permitiendo inspección de URLs en tiempo real, monitoreo de sitemaps y envío a la API de indexación.
- **Grafo de Conocimiento Local:** `graphify-out/graph.json` activo en la raíz del proyecto.

---

## ⚙️ Convenciones y Preferencias Obligatorias
1. **Nombre del Autor:** Escribir siempre `Erik Ladstatter` (sin diéresis).
2. **Botones de WhatsApp:** No mostrar el número telefónico explícito en el texto del botón; usar textos limpios como `"Consultar por WhatsApp"` o `"Escribirme por WhatsApp"`.
3. **Navbar del Blog:** Las páginas del blog NO deben incluir enlaces a `#demos` ni `#precios` en la barra de navegación superior (únicamente `Inicio`, `San Juan`, `Blog` y el botón de WhatsApp).
4. **Imágenes del Blog:** Usar exclusivamente fotografía editorial auténtica de alta calidad (16:9, `1200x675`) representativa del rubro con pastilla superior izquierda de categoría y sello inferior derecho `erikwebsite.com`. Nunca usar infografías saturadas de texto pequeño ni mockups genéricos. Todo el contenido comparativo o técnico va maquetado en componentes HTML/Tailwind responsivos (tablas oscuras, tarjetas y acordeones).
5. **Títulos `<h1>` Concisos:** En los artículos del blog, mantener los `<h1>` directos y concisos, dejando las explicaciones secundarias para los subtítulos `<h2>` y párrafos.
6. **Traducción `/en/index.html`:** Debe mantener fidelidad estructural 1 a 1 con `index.html`.
7. **Redacción Natural (Skills `humanizer` y `stop-slop`):** Todos los artículos nuevos que se redacten en el futuro deben aplicar obligatoriamente las directrices de las skills `humanizer` y `stop-slop` (AI Slop) para garantizar una lectura natural, directa y humana, libre de muletillas, estructuras predecibles o frases típicas de IA (no requiere revisar retroactivamente los artículos antiguos ya publicados).

---

## 🗄️ Decisiones de Arquitectura
- **Estrategia SEO + AEO + GEO:** Cada artículo del blog incorpora un bloque superior de **Respuesta Directa** (40–60 palabras para citación en Google AI Overviews, ChatGPT Search, Perplexity y Grok), encabezados `<h2>` formulados como preguntas reales de usuarios/IA (*Query Fan-Out*), tablas comparativas HTML y marcado estructurado `Schema.org` (`BlogPosting`, `BreadcrumbList`, `FAQPage`).
- **Script Local de Fan-Out (`scratch/free_alsoasked_ai_fanout.py`):** Herramienta propia gratuita en Python para recolectar preguntas de autocompletado y *People Also Ask* en Google Argentina (`gl=ar`, `hl=es-419`) sin depender de suscripciones pagas como AlsoAsked.

---

## 🕰️ Antecedentes y Memorias Previas (Importadas)
- **Rediseño Demo Abogados (`/demos/abogados/`):** Paleta marfil/alabastro (`#fbf9f5`) y burdeos (`#991b1b`), con **Calculadora Estimativa de Indemnización Laboral (Art. 245 LCT)** interactiva que envía el cálculo prearmado a WhatsApp.
- **Open Graph & Identidad Visual:** Configuradas tarjetas Open Graph y Twitter Cards en todas las páginas y demos. En la página principal (`index.html` y `en/index.html`) se utiliza el logo verde EW (`logo_erikwebsite_ig.png` y `og_main.jpg`).
- **Prospección Outbound con Apify:** Extracción de estudios jurídicos y comercios sin sitio web en provincias argentinas mediante `compass/crawler-google-places` con enlaces directos por `place_id`.

---

## 📝 Registro de Tareas & Estado
- [x] Creación e integración de 24 guías iniciales del blog en `blog/`.
- [x] **2026-10-25:** Análisis de 2.006 palabras clave de Google Ads Keyword Planner (6 CSVs de Argentina) y publicación del Batch 1 de 5 artículos Long-Tail AEO/GEO:
  1. `/blog/como-registrar-dominio-com-ar-nic-argentina/`
  2. `/blog/como-crear-correo-corporativo-dominio-propio-gmail/`
  3. `/blog/crear-pagina-web-google-sites-sirve-para-negocio/`
  4. `/blog/paginas-web-marketing-odontologos-argentina/`
  5. `/blog/como-crear-catalogo-online-pedidos-whatsapp/`
- [x] **2026-10-26:** Creación del script de *Query Fan-Out* local y publicación del Batch 2 de 5 artículos AEO/GEO (totalizando **34 guías** activas en `/blog/`):
  1. `/blog/crear-pagina-web-wix-conviene-argentina/`
  2. `/blog/paginas-web-medicos-consultorios-argentina/`
  3. `/blog/paginas-web-alquiler-vajilla-mobiliario-eventos/`
  4. `/blog/catalogo-pdf-canva-vs-catalogo-web/`
  5. `/blog/diseno-web-cordoba/`
- [x] **2026-10-26:** Desarrollo e integración de la **Herramienta Gratuita + Artículo Guía** (`/blog/generador-link-qr-whatsapp-gratis/`, módulo `src/js/whatsapp-tool.js` con `qrcode` client-side sin caducidad, cartel imprimible `1080x1350`, widget HTML flotante y enlace directo en el footer global del sitio; totalizando **35 guías y herramientas** en `/blog/`).
- [x] **2026-10-27:** Auditoría Hallmark UI y optimizaciones de accesibilidad/rendimiento en `index.html` y `en/index.html`:
  - Ignorada carpeta `manual de identidad/` en `.gitignore`.
  - Agregada 3ra tarjeta de desarrollo a medida para **UAQ Tours** (`uaqtours.com.ar`, Naranja UAQ `#FE5200` y Dark Mode `#0A0A0A` con `rel="noreferrer noopener"`).
  - Personalizada tarjeta de **Wink Studio** (`winkstudioar.com`) con colores de su manual oficial (Terracota `#D87B52` y Verde Salvia `#B7C9A8`).
  - Mantenidos intactos los colores de **3DMON Shop** (`3dmon.shop`).
  - Reestructurado el grid de proyectos a `grid lg:grid-cols-3 md:grid-cols-2 gap-7`.
  - Corregidos los 53 SVGs con `aria-hidden="true"` (eliminando los falsos positivos de "imágenes sin alt").
  - Agregados atributos `width="40" height="40" loading="lazy" decoding="async"` a imágenes de testimonios (prevención de CLS).
  - Enlazados atributos WAI-ARIA (`id="faq-header-X"`, `aria-controls="faq-answer-X"`, `role="region"`) en el acordeón FAQ.
  - Agregado Stamp de Hallmark Design System en `<head>`.
- [x] **2026-10-27:** Integración global de **Meta Pixel (Dataset ID `1143177121539028`)**:
  - Código base de Meta Pixel con tracking `PageView` inyectado en el `<head>` de las 63 páginas públicas del sitio (`index.html`, `en/`, `san-juan/`, `/blog/`, `/demos/`, `/terminos/`).
  - Fallback `<noscript>` de píxel `1x1` ubicado al inicio del `<body>` con `alt=""` para cumplimiento estricto de HTML5/W3C y evitar advertencias de accesibilidad o errores de parseo en Vite.
  - Tracking automático de evento de conversión `fbq('track', 'Contact', ...)` añadido en `src/js/whatsapp.js` en cada clic a botones de WhatsApp para optimización de campañas publicitarias en Meta Ads.
- [x] **2026-10-28:** Investigación profunda de oportunidades Long-Tail de baja competencia (sin canibalización) y publicación del **Batch 3 de 5 artículos ultra-específicos AEO / GEO / SEO** (alcanzando **40 guías y herramientas** activas en `/blog/`):
  1. `/blog/como-delegar-dns-renovar-dominio-nic-argentina/` (*NIC Argentina: delegar dominio, estado "No Delegado", cambiar DNS en TAD y renovación anual*)
  2. `/blog/hacer-landing-page-canva-sirve-para-vender/` (*Hacer página web o Landing Page en Canva vs. web profesional con Píxel de Meta y SEO*)
  3. `/blog/paginas-web-restaurantes-carta-qr-pedidos-whatsapp/` (*Páginas web para restaurantes y bares con Carta Digital QR y pedidos a WhatsApp sin comisiones de apps*)
  4. `/blog/diseno-web-neuquen/` (*Diseño web en Neuquén Capital, Añelo / Vaca Muerta, Alto Valle y cordillera patagónica — Competencia SEO Baja 12/100*)
  5. `/blog/rediseno-paginas-web-actualizar-sitio-lento/` (*Rediseño y migración de páginas web viejas, lentas, no responsive o con aviso "No es seguro"*)
- [x] **2026-10-28:** Enlace oficial y autenticación completa con **Google Search Console (GSC) y Web Search Indexing API v3**:
  - Credenciales de cuenta de servicio configuradas en `~/.config/claude-seo/service_account.json` y `google-api.json`.
  - Verificada propiedad `sc-domain:erikwebsite.com` con permisos de `siteOwner`.
  - Probada inspección de URLs y lectura de sitemaps (`https://erikwebsite.com/sitemap.xml`, 0 errores).
- [x] **2026-10-29:** Análisis de rendimiento en GSC + Google Ads CSV + Autocomplete Fan-Out y publicación del **Batch 4 de 6 artículos (4 Provincias + 2 Long-Tail AEO / GEO / SEO)** aplicando las skills `humanizer` y `stop-slop` (alcanzando **46 guías y herramientas** activas en `/blog/`):
  1. `/blog/diseno-web-rosario-santa-fe/` (*Diseño de Páginas Web en Rosario y Santa Fe: Precios 2026 — 500 búsquedas/mes*)
  2. `/blog/diseno-web-tucuman/` (*Diseño de Páginas Web en Tucumán: Precios 2026 y Desarrollo a Medida*)
  3. `/blog/diseno-web-salta-jujuy/` (*Diseño de Páginas Web en Salta y Jujuy: Precios 2026 — Turismo, Hoteles y Proveedores Mineros*)
  4. `/blog/diseno-web-mar-del-plata-la-plata-bahia-blanca/` (*Diseño de Páginas Web en Mar del Plata, La Plata y Bahía Blanca: Precios 2026*)
  5. `/blog/crear-pagina-web-hostinger-conviene-argentina/` (*Crear una página web en Hostinger: ¿conviene en Argentina en 2026? — Renovación dólar tarjeta e IA*)
  6. `/blog/dominio-com-vs-com-ar-cual-conviene-argentina/` (*Dominio .com vs .com.ar: ¿cuál conviene elegir para tu negocio? — 1.000 búsquedas/mes combinadas*)
- [x] **2026-10-30:** Análisis de 5 nuevos CSVs de Google Ads y publicación del **Batch 5 de 2 artículos de competencia ultra-baja** (alcanzando **48 guías y herramientas** activas en `/blog/`):
  1. `/blog/diseno-web-bariloche-comodoro-rivadavia-patagonia/` (*Diseño Web en Bariloche, Comodoro Rivadavia y Patagonia Sur — Competencia 0/100 a 40/100*)
  2. `/blog/como-poner-agregar-negocio-local-google-maps-gratis/` (*Cómo hacer que mi negocio o local aparezca en Google Maps gratis — Competencia Baja 30/100 y +1.200 búsquedas/mes*)
