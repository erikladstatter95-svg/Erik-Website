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
- **Google Analytics 4 (GA4 API):** Vinculado oficialmente a la Propiedad ID `554839707` (`G-KWD0WYVK4J`) con la cuenta de servicio (`seo-asistente@erik-website-seo.iam.gserviceaccount.com`, rol Lector). Permite consultas programáticas de tráfico, fuentes por país y monitoreo de referencias de IA (`check_ai_traffic.py`).
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

8. **Criterio Visual Sturm (Heading + Image = Comprensión Inmediata):** Toda imagen de cabecera debe tener una relación temática directa, concreta y tangible con el encabezado (ej: si se habla de odontólogos, mostrar mostrador/recepción dental con dispositivo de turnos; si es de WhatsApp, mostrar el teléfono con chat/pedido real). Quedan prohibidas fotos de stock ambiguas (laptops genéricas en cafeterías, escritorios vacíos o abstractos). La imagen junto al título debe explicar el problema/solución sin necesidad de leer el párrafo.
9. **Fórmula de 4 Puntos Sturm para AEO/GEO:** Cada contenido nuevo o actualización debe ubicar la frase de búsqueda BoFu clave en: Title, Slug, H1 y en las primeras 5-10 palabras de la primera frase del texto.
10. **Skill Obligatoria `aeo-geo-tactics` y Extracción de Queries Fan-Out (Opción 3):** Antes de redactar cualquier artículo o cluster del blog, se debe activar y consultar obligatoriamente la skill `aeo-geo-tactics` y ejecutar la extracción de *Query Fan-Out* (vía Antigravity / script de autocompletado) para identificar las sub-preguntas y variaciones conversacionales que los usuarios hacen en ChatGPT, Perplexity y Google, integrándolas en los subtítulos `<h2>` y en el bloque de Respuesta Directa.
11. **Estrategia 'SEO Colonies' e Interlinking Continuo:** Toda guía debe incorporar enlaces contextuales cruzados hacia las herramientas y guías complementarias del blog (registro en NIC Argentina, correo corporativo en Gmail, Google Maps, generador de link/QR de WhatsApp, comparativas Canva/Wix) y canalizar autoridad hacia las Landing Pages comerciales y demos interactivas con textos ancla semánticos y enlaces de ancla (`#demos`, `#precios`).

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
- [x] **2026-10-30:** Rediseño de la demo de Fitness para Personal Trainers (`/demos/fitness/`) y creación de nueva demo independiente para Estudios de Pilates (`/demos/estudio-fitness/`):
  - **Personal Trainer (`/demos/fitness/`):** Calculadora interactiva reestructurada con matriz 3x3 (días: 2, 3, 5 por semana vs nivel: principiante, intermedio, avanzado), precios diferenciados y nota aclaratoria sobre evaluación física inicial.
  - **Pilates Studio (`/demos/estudio-fitness/`):** Estilo calm boutique en beige cálido (`#f7f5f0`), blanco y verde bosque (`#14532d`), con selector de turnos día por día (Lunes a Sábado) y generación de mensaje dinámico para reserva en WhatsApp.
  - **Navegación Cluster 3 & Home:** Actualizada la barra superior sticky con las 5 variaciones en todas las demos del cluster (`abogados`, `urgencias-hogar`, `contable`, `fitness`, `estudio-fitness` y retrocompatibilidad `cluster-3/`) y añadida la 5ta opción en la home (`index.html` y `en/index.html`) bajo la categoría "Autoridad, Urgencias y PyMEs" (5 Estilos).
  - **Sitemap & Build:** Registrado `/demos/estudio-fitness/` y `/demos/contable/` en `sitemap.xml`, compilación de producción validada con Vite (`0 errores`).
- [x] **2026-10-30:** Publicación del **Batch 6 de 2 artículos Long-Tail de alta intención y baja competencia** (alcanzando **50 guías y herramientas** activas en `/blog/`):
  1. `/blog/por-que-mi-negocio-no-aparece-en-google-maps/` (*Por Qué mi Negocio no Aparece en Google Maps y Cómo Solucionarlo — Diagnóstico de verificación, categorías y consistencia NAP*)
  2. `/blog/diseno-web-misiones-corrientes-chaco-posadas-resistencia/` (*Diseño de Páginas Web en Misiones, Corrientes y Chaco: Precios 2026 — Cobertura integral del NEA: Posadas, Corrientes Capital y Resistencia*)
  - Integrados en `blog/index.html` con tarjetas destacadas, registrados en `vite.config.js` y `sitemap.xml`, build 100% limpio en Vite y notificados a Google Indexing API v3 con status 200 OK.
- [x] **2026-10-30:** Desacoplamiento y reestructuración completa de artículos geográficos en URLs y entidades únicas para evitar señales confusas a Google:
  - Se dividieron los 5 artículos que agrupaban múltiples localidades en **12 artículos individuales independientes** con sus propios slugs, esquemas `LocalBusiness`, imágenes editoriales auténticas con pastilla personalizada y contenido específico:
    1. `/blog/diseno-web-rosario/` (Rosario & Gran Rosario)
    2. `/blog/diseno-web-santa-fe/` (Santa Fe Capital)
    3. `/blog/diseno-web-salta/` (Salta Capital & Valle de Lerma)
    4. `/blog/diseno-web-jujuy/` (San Salvador de Jujuy & Quebrada)
    5. `/blog/diseno-web-mar-del-plata/` (Mar del Plata & Costa Atlántica)
    6. `/blog/diseno-web-la-plata/` (La Plata Capital)
    7. `/blog/diseno-web-bahia-blanca/` (Bahía Blanca & Polo Industrial)
    8. `/blog/diseno-web-bariloche/` (San Carlos de Bariloche & Río Negro)
    9. `/blog/diseno-web-comodoro-rivadavia/` (Comodoro Rivadavia & Chubut)
    10. `/blog/diseno-web-posadas-misiones/` (Posadas & Misiones)
    11. `/blog/diseno-web-corrientes/` (Corrientes Capital)
    12. `/blog/diseno-web-resistencia-chaco/` (Resistencia & Chaco)
  - Los 5 slugs combinados originales se configuraron con redirección instantánea canonical y meta-refresh hacia su destino principal para prevenir errores 404.
  - Sincronizados en `blog/index.html`, `vite.config.js`, `sitemap.xml`, compilación en producción limpia (`0 errores`) y notificados a Google Indexing API v3 (`200 OK`). Totalizando **57 guías y herramientas activas**.
- [x] **2026-10-31:** Análisis integral de la metodología de Edward Sturm (AEO, GEO y Bottom-of-Funnel SEO):
  - Creada e instalada la nueva Skill global [`aeo-geo-tactics`](file:///C:/Users/erikl/.gemini/config/skills/aeo-geo-tactics/SKILL.md) que codifica la fórmula de 4 ubicaciones clave, extracción de *Query Fan-Out* en ChatGPT/Gemini/Perplexity, minería de consultas conversacionales en GSC y reglas de imágenes hiper-específicas.
  - Ejecutado script de análisis en Google Search Console para `sc-domain:erikwebsite.com` detectando consultas conversacionales de 6+ palabras (ej: *"como crear correos con dominio propio"*, *"cuanto cobrar por una pagina web argentina"*, *"cuanto sale hacer una pagina web"*).
  - Diseñado el blueprint de Custom GPTs para OpenAI en [`chatgpt_custom_gpts_blueprint.md`](file:///c:/Users/erikl/Downloads/WebErik/chatgpt_custom_gpts_blueprint.md) con prompts de sistema y flujos para canalizar tráfico orgánico desde ChatGPT hacia el generador de QR y la web principal.
  - **Auditoría y Optimización Global del Blog (57/57 artículos):**
    - Se inyectaron bloques de **Respuesta Directa AEO/GEO** en los 7 artículos legacy que no lo tenían (`estudios-contables`, `oficios-servicios-hogar`, `psicologos`, `personal-trainers`, `salones-belleza`, `salones-eventos`, `por-que-tener-una-pagina-web`), enlazando hacia sus demos correspondientes (`/demos/contable/`, `/demos/urgencias-hogar/`, `/demos/fitness/`, `/demos/estudio-fitness/`).
    - Se optimizaron las primeras frases (Sturm Rule #4) en artículos clave (`mantenimiento-web-argentina`, `anuncios-no-venden`, `pagina-web-vs-instagram`, `wordpress-vs-codigo-a-medida`, `tiendanube-linktree-vs-web-propia`, `turnos-consultorio`, `clientes-google-maps`) eliminando introducciones retóricas y colocando la entidad/solución en las primeras 5 a 10 palabras.
    - Se corrigieron los textos alternativos `alt` eliminando prefijos obsoletos ("Infografía explicativa") por descripciones editoriales directas.
    - **Reestructuración de Interlinking Global ("SEO Colonies"):** Se auditaron y enlazaron los 57 artículos eliminando cualquier página aislada (0 artículos con menos de 2 enlaces a otros blogs). Se interconectaron los 12 artículos provinciales con guías de Google Maps, Correo Corporativo y Demos; y se tejieron enlaces cruzados en los clusters de Dominios/DNS, Comparativas (Canva/Wix/WordPress/Tiendanube) y Rubros comerciales.
    - Compilación de producción validada en Vite (`0 errores, built in 5.51s`).
- [x] **2026-10-31:** Publicación del **Batch 7 de 5 artículos estratégicos BoFu y Contrarian** aplicando la metodología de Edward Sturm (`aeo-geo-tactics`, fórmula de 4 puntos clave, imágenes editoriales hiper-específicas, lenguaje natural rioplatense y "SEO Colonies", alcanzando **62 guías y herramientas activas** en `/blog/` y 67 rutas en total):
  1. `/blog/empretienda-vs-tiendanube-cual-conviene-argentina/` (*Empretienda vs. Tiendanube: ¿Cuál Conviene en Argentina en 2026? — Comparativa BoFu de costos, comisiones por transacción y pasarelas*)
  2. `/blog/paginas-web-para-inmobiliarias-argentina/` (*Páginas Web para Inmobiliarias en Argentina: Claves de Éxito — Catálogo de propiedades ágil, filtro a WhatsApp y reducción de dependencia de portales*)
  3. `/blog/embudo-de-ventas-por-whatsapp-argentina/` (*Cómo Armar un Embudo de Ventas por WhatsApp en Argentina — Estructura de 3 pasos: Tráfico -> Landing Page filtro -> Cierre en WhatsApp*)
  4. `/blog/por-que-nadie-me-compra-por-whatsapp/` (*Por Qué Nadie me Compra por WhatsApp y Cómo Solucionarlo — Análisis de los 5 errores comerciales, curiosos y cómo duplicar cierres*)
  5. `/blog/crear-pagina-web-gratis-para-vender-argentina/` (*Crear Página Web Gratis para Vender en Argentina: Mitos y la Realidad — Limitaciones de Google Sites y Canva, subdominios y la alternativa profesional a $150.000 ARS*)
  - Integradas 5 imágenes editoriales `1200x675` con pastilla y sello en `/images/`.
  - Agregadas las 5 tarjetas en `blog/index.html` (contador global actualizado a 62 guías).
  - Registradas las 5 entradas en `vite.config.js` y sincronizado `sitemap.xml` completo (82 URLs canónicas totales).
  - Compilación de producción validada en Vite (`0 errores, built in 7.09s`).
  - Enviadas y confirmadas las 5 URLs a la **Google Web Search Indexing API v3** con respuesta `200 OK`.
- [x] **2026-11-01:** Investigación cruzada en **Google Search Console, GA4 (`554839707`), Autocomplete Fan-Out y 2.147 keywords de Google Ads CSV**, y publicación del **Batch 8 de 10 artículos (6 Relevantes BoFu + 4 Ciudades Individuales)** aplicando todas las reglas de `aeo-geo-tactics` (Sturm 4-Point Rule, Criterio Visual Sturm, `humanizer`, `stop-slop` e interlinking "SEO Colonies", alcanzando **72 guías y herramientas activas** en `/blog/`):
  - **6 Artículos Relevantes BoFu & Demos:**
    1. `/blog/precios-shopify-argentina-conviene/` (*Precios de Shopify en Argentina: ¿Conviene en 2026? — Análisis de planes en dólar tarjeta, doble comisión con Mercado Pago y alternativa en pesos*)
    2. `/blog/woocommerce-vs-tiendanube-cual-conviene-argentina/` (*WooCommerce vs. Tiendanube: ¿Cuál Conviene Elegir en Argentina? — Comisiones por venta vs. costos de hosting/plugins y la tercera vía en código limpio*)
    3. `/blog/crear-pagina-web-godaddy-conviene-argentina/` (*Crear una Página Web en GoDaddy desde Argentina: ¿Conviene en 2026? — Renovaciones en dólares de SSL, correo Microsoft 365 y constructor cerrado*)
    4. `/blog/como-pedir-presupuesto-pagina-web-argentina/` (*Presupuesto de Página Web en Argentina: Qué Debe Incluir para No Pagar de Más — Checklist de 7 puntos críticos para comparar cotizaciones*)
    5. `/blog/paginas-web-veterinarias-pet-shops-argentina/` (*Páginas Web para Veterinarias y Pet Shops en Argentina — Guardia 24 hs en Google Maps, turnos por WhatsApp y enlace directo a `/demos/veterinaria/`*)
    6. `/blog/paginas-web-talleres-mecanicos-lubricentros-argentina/` (*Páginas Web para Talleres Mecánicos y Lubricentros en Argentina — Filtro de turnos por WhatsApp, posicionamiento en Maps y enlace a `/demos/taller/`*)
  - **4 Artículos de Ciudades / Provincias Individuales (1 localidad por artículo):**
    7. `/blog/diseno-web-parana/` (*Diseño de Páginas Web en Paraná: Precios 2026 — Capital de Entre Ríos, Parque Industrial General Belgrano, turismo y salud*)
    8. `/blog/diseno-web-tandil/` (*Diseño de Páginas Web en Tandil: Precios 2026 — Competencia ultra-baja 11/100 en CSV + visitas activas en GA4; cabañas, agroindustria y comercios*)
    9. `/blog/diseno-web-pilar/` (*Diseño de Páginas Web en Pilar: Precios 2026 — Competencia 0/100 en CSV; Parque Industrial Pilar, centros médicos y servicios de Zona Norte*)
    10. `/blog/diseno-web-lomas-de-zamora/` (*Diseño de Páginas Web en Lomas de Zamora: Precios 2026 — Competencia baja 29/100 en CSV; Las Lomitas, polo judicial y comercios de Zona Sur*)
  - Generadas 10 imágenes editoriales `1200x675` con pastilla y sello `erikwebsite.com` en `/images/`.
  - Corregido el enlace CSS (`/src/styles/main.css`) en los artículos del Batch 7 eliminando cualquier advertencia en tiempo de compilación.
  - Sincronizados `blog/index.html` (72 guías), `vite.config.js` y `sitemap.xml` (92 URLs canónicas), compilación limpia en Vite (`0 errores, 0 warnings`) y notificadas las 10 URLs a Google Indexing API v3 (`200 OK`).
- [x] **2026-11-01:** Lanzamiento de la oferta **Grand Slam Offer (`$100M Offers` — `/grand-slam-offers`)** para el servicio universal de **Auditoría SEO, Optimización y Mantenimiento Web para Sitios Existentes** (precio a consultar según diagnóstico):
  1. **Mejora en Homepage (`index.html` y espejo 1:1 en `en/index.html`):** Reemplazo de la pastilla pequeña de mantenimiento por una sección destacada (`#auditoria-seo`) con 3 pilares (*1. Auditoría SEO y Google*, *2. Velocidad y Conversión*, *3. Mantenimiento y Soporte*), badge *"Inversión: Precio a consultar según tu web"*, botón directo a WhatsApp y enlace a `/auditoria-seo/`. También se sumó `Auditoría SEO` (`SEO Audit`) en la barra de navegación superior y en el footer.
  2. **Landing Comercial Dedicada (`/auditoria-seo/index.html`):** Página completa inspirada en la estructura de `/san-juan/index.html` y construida con la ecuación de valor de Alex Hormozi (explicación sin tecnicismos con 3 metáforas simples: *"El Local en un Pasillo sin Salida"*, *"La Puerta Trabada en el Celular"* y *"La Web Abandonada o Sin Embudo"*; apilamiento de valor Done-For-You vs. agencias que solo mandan PDFs; e inversión de riesgo con **Diagnóstico Inicial Gratuito** por WhatsApp).
  3. **Guía de Blog para Prospección (`/blog/auditoria-seo-optimizacion-mantenimiento-web-argentina/index.html`):** Artículo comercial pensado para enviar a dueños de negocios con webs existentes (*"Auditoría SEO, Optimización y Mantenimiento Web en Argentina: Cómo Revivir tu Página"*), con imagen editorial `images/guia_auditoria_seo_optimizacion_web.png`, alcanzando **73 guías y herramientas activas** en `/blog/` y **94 URLs canónicas** en `sitemap.xml` (compilación Vite `0 errores` y envío confirmado `200 OK` a Google Indexing API v3).
