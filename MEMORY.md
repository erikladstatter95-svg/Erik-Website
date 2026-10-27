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
- **Grafo de Conocimiento Local:** `graphify-out/graph.json` activo en la raíz del proyecto.

---

## ⚙️ Convenciones y Preferencias Obligatorias
1. **Nombre del Autor:** Escribir siempre `Erik Ladstatter` (sin diéresis).
2. **Botones de WhatsApp:** No mostrar el número telefónico explícito en el texto del botón; usar textos limpios como `"Consultar por WhatsApp"` o `"Escribirme por WhatsApp"`.
3. **Navbar del Blog:** Las páginas del blog NO deben incluir enlaces a `#demos` ni `#precios` en la barra de navegación superior (únicamente `Inicio`, `San Juan`, `Blog` y el botón de WhatsApp).
4. **Imágenes del Blog:** Usar exclusivamente fotografía editorial auténtica de alta calidad (16:9, `1200x675`) representativa del rubro con pastilla superior izquierda de categoría y sello inferior derecho `erikwebsite.com`. Nunca usar infografías saturadas de texto pequeño ni mockups genéricos. Todo el contenido comparativo o técnico va maquetado en componentes HTML/Tailwind responsivos (tablas oscuras, tarjetas y acordeones).
5. **Títulos `<h1>` Concisos:** En los artículos del blog, mantener los `<h1>` directos y concisos, dejando las explicaciones secundarias para los subtítulos `<h2>` y párrafos.
6. **Traducción `/en/index.html`:** Debe mantener fidelidad estructural 1 a 1 con `index.html`.

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
