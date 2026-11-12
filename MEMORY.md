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
12. **Sincronización Doble de Imágenes (`images/` + `public/images/`):** Toda imagen nueva o actualizada del sitio o del blog debe guardarse siempre en ambos directorios (`images/` y `public/images/`) para que Vite empaquete y copie correctamente los recursos estáticos a `dist/images/` en producción.
13. **Sitemap: el archivo que se publica es `public/sitemap.xml` (NO el de la raíz):** Vite copia `public/` a `dist/`; el `sitemap.xml` de la raíz se ignora en producción. Cada vez que se publiquen artículos hay que actualizar ambos (`Copy-Item sitemap.xml public\sitemap.xml -Force`). Este olvido dejó el sitemap en vivo congelado en 63 URLs (GSC mostraba `63 enviadas`) mientras el local tenía 121. Además, nunca listar URLs que no existan en disco ni las páginas stub de redirección (`diseno-web-salta-jujuy`, etc.) ni `/terminos/` (noindex).
14. **Antes de proponer un artículo nuevo, comparar contra los H1/H2 de las guías existentes** (no solo contra los slugs) para evitar canibalización: ya existen guías de cabañas/hoteles, arquitectos/constructoras, mantenimiento (3), tiendas online (6), WordPress vs. código y funnels.
15. **Git Push Obligatorio con Cada Cambio en la Web:** Con cada actualización, cambio o arreglo en el sitio, realizar siempre el commit y `git push` a GitHub (`origin/main`) para que el deploy se ejecute automáticamente y los cambios se vean reflejados en vivo en la web.
16. **Regla de Oro Geográfica (1 Provincia Exclusiva + 1 Ciudad Única o 1 Zona Metropolitana Reconocible por Artículo/Slug):**
    - **Nivel Provincia:** Cada una de las 24 jurisdicciones argentinas debe tener su propia página exclusiva nivel provincia (ej: `/blog/diseno-web-rio-negro/`, `/blog/diseno-web-chubut/`, `/blog/diseno-web-entre-rios/`, `/blog/diseno-web-mendoza/`, `/blog/diseno-web-cordoba/`, `/blog/diseno-web-santa-fe/`).
    - **Nivel Ciudad o Zona:** Cada artículo de ciudad debe cubrir **1 sola ciudad específica** aclarando explícitamente a qué provincia pertenece y enlazando a la guía provincial (ej: `/blog/diseno-web-san-rafael-mendoza/`, `/blog/diseno-web-bariloche/`, `/blog/diseno-web-rio-cuarto/`, `/blog/diseno-web-villa-maria/`, `/blog/diseno-web-puerto-madryn/`, `/blog/diseno-web-trelew/`, `/blog/diseno-web-rafaela/`, `/blog/diseno-web-venado-tuerto/`) o **1 zona metropolitana reconocible por la gente común** con un slug limpio sin concatenar localidades (ej: `/blog/diseno-web-zona-norte/`, `/blog/diseno-web-zona-oeste/`, `/blog/diseno-web-zona-sur/`), donde el vecino o comerciante sepa que al buscar una localidad de esa zona la va a encontrar cubierta adentro. Prohibido concatenar múltiples ciudades en un mismo slug (`rio-cuarto-villa-maria`, `puerto-madryn-trelew`, etc.).
17. **Prohibido Usar Emojis en la Web:** No utilizar emojis decorativos (`⚡`, `📈`, `📍`, `💻`, `💡`, `🚀`, `👉`, etc.) en textos, títulos, badges o botones del sitio web ni del blog (salvo pedido explícito o estrictamente necesario), ya que dan aspecto de página generada por IA. Usar únicamente tipografía limpia, indicadores CSS (puntos de color) o iconos SVG cuando haga falta.
18. **Slugs Cortos y Limpios (3 a 5 palabras clave máximo):** Todo artículo nuevo del blog debe usar un slug corto, directo y fácil de leer de entre **3 y 5 palabras clave** (ej: `/blog/paginas-web-distribuidoras-mayoristas/`, `/blog/errores-google-search-console-seo/`, `/blog/diseno-web-villa-carlos-paz/`), evitando URLs largas de 7 o más palabras.
19. **Prohibición Absoluta de Interlinking a Páginas Inexistentes (Cero Enlaces Fantasma):**
    - Queda estrictamente prohibido colocar enlaces (`href="/..."` o `href="https://erikwebsite.com/..."`) hacia artículos, páginas de servicios, demos o herramientas que no existan físicamente en el repositorio.
    - Se puede hablar y proponer la creación de una nueva página o demo si el negocio o artículo lo amerita, o mencionar la solución en el texto ("podemos desarrollar una demo o cotizador interactivo a medida"), pero **NUNCA inventar un slug o enlace hacia una página que no hay**.
    - En cada publicación o edición se debe verificar la existencia física del archivo `.html` de destino y ejecutar `scratch/audit_all_internal_links.py` para asegurar 0 enlaces rotos.

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
    5. `/blog/paginas-web-veterinarias-pet-shops-argentina/` (*Páginas Web para Veterinarias y Pet Shops en Argentina — Guardia 24 hs en Google Maps, turnos por WhatsApp y enlace a `#demos`*)
    6. `/blog/paginas-web-talleres-mecanicos-lubricentros-argentina/` (*Páginas Web para Talleres Mecánicos y Lubricentros en Argentina — Filtro de turnos por WhatsApp, posicionamiento en Maps y enlace a `#demos`*)
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
- [x] **2026-11-01 (Actualización de Diseño, Navbars, San Juan y Nuevo Servicio de Funnels):**
  1. **Fix de Grilla Desktop (`md:col-span-2`) y `tailwind.config.js`:** Se amplió el array `content` de `tailwind.config.js` para escanear `./auditoria-seo/**/*.html`, `./san-juan/**/*.html`, `./blog/**/*.{html,js}`, `./en/**/*.html` y `./terminos/**/*.html`, logrando que el bloque de *Mantenimiento Mensual, Hosting, Seguridad SSL y Actualizaciones* en `/auditoria-seo/index.html` ocupe las dos columnas completas en escritorio (`col-span-1 md:col-span-2 w-full`). Además se enriqueció el `Schema.org` (`ProfessionalService` con `hasOfferCatalog` y `OfferCatalog`) tanto en `/auditoria-seo/` como en `index.html`.
  2. **Unificación Total de Navbars y Footers:** Se estandarizaron todas las barras de navegación y footers en `index.html`, `auditoria-seo/index.html`, `san-juan/index.html`, `blog/index.html` y las 74 guías de `blog/*/index.html` para mostrar siempre los enlaces globales en el mismo orden y con el mismo nombre exacto (`Auditoría SEO`, `San Juan`, `Blog` — eliminando variaciones como "Blog y Guías").
  3. **Nueva Imagen del Centro Cívico en San Juan (`images/guia_diseno_web_san_juan.png` y `public/images/guia_diseno_web_san_juan.png`):** Se regeneró la fotografía editorial de `/san-juan/` y `/blog/diseno-web-san-juan/` tomando como referencia directa la foto del **Centro Cívico de San Juan** provista por el usuario, sincronizando `images/` y `public/images/`.
  4. **Nuevo Artículo y Servicio de Páginas Modo Funnel (`/blog/que-es-un-funnel-de-ventas-para-que-sirve-argentina/index.html`):** Guía comercial BoFu enfocada en vender páginas simples modo funnel para creadores de archivos digitales (ebooks, PDFs, plantillas, cursos) y ofertas puntuales de servicios, explicando las diferencias frente a las páginas web tipo demo y con CTA directo a WhatsApp (alcanzando **74 guías activas** en `/blog/` y **95 URLs canónicas** en `sitemap.xml`).
- [x] **2026-11-02:** Auditoría en vivo de **Google Search Console (`sc-domain:erikwebsite.com`), GA4 (`554839707`), 11 CSVs de Google Ads y Autocomplete Fan-Out**, y publicación del **Batch 9 de 10 artículos sin canibalización (6 Relevantes BoFu/Rubros + 4 Ciudades/Provincias Individuales)** alcanzando **84 guías y herramientas activas** en `/blog/` y **105 URLs canónicas** en `sitemap.xml`:
  - **6 Artículos Relevantes BoFu, Rubros y Colonias SEO:**
    1. `/blog/precios-comisiones-tiendanube-alternativas-argentina/` (*Precios y Comisiones de Tiendanube en Argentina 2026: Cuánto Pagás Realmente y Alternativas — 500 búsquedas/mes para `precios tienda nube` y `tienda nube costos`, 150/mes para `comisiones tiendanube` y 100/mes para `alternativas a tiendanube`*)
    2. `/blog/paginas-web-locales-ropa-indumentaria-mayoristas-argentina/` (*Páginas Web para Locales de Ropa, Showrooms y Mayoristas en Argentina — Curvas de talles, pedidos a WhatsApp, caso real Wink Studio `winkstudioar.com` y comparativa Sumerlabs*)
    3. `/blog/paginas-web-agencias-de-viajes-excursiones-turismo-argentina/` (*Páginas Web para Agencias de Viajes, Excursiones y Turismo en Argentina — Itinerarios interactivos, reservas directas sin comisiones de OTAs y caso real UAQ Tours `uaqtours.com.ar`*)
    4. `/blog/configurar-correo-corporativo-outlook-firma-profesional/` (*Cómo Configurar tu Correo Corporativo en Outlook (PC y Celular) y Crear tu Firma Profesional — Competencia 0/100 en CSV para `firmas de correo corporativo` y refuerzo directo de la Colonia SEO #1 de GSC*)
    5. `/blog/paginas-web-fotografos-productoras-audiovisuales-argentina/` (*Páginas Web para Fotógrafos, Filmmakers y Productoras Audiovisuales en Argentina — Competencia 0/100 en CSV para `crear pagina web fotografia`, galerías WebP/AVIF y reels de carga instantánea*)
    6. `/blog/paginas-web-corralones-ferreterias-materiales-construccion/` (*Páginas Web para Corralones, Ferreterías Industriales, Aberturas y Techos en Argentina — Cotizador de lista de materiales por WhatsApp para obras y arquitectos*)
  - **4 Artículos de Ciudades y Provincias Individuales (1 localidad por artículo, guiados por CSV y tráfico real en GA4):**
    7. `/blog/diseno-web-quilmes/` (*Diseño de Páginas Web en Quilmes: Precios 2026 — 50 búsquedas/mes en CSV, Quilmes Centro, Bernal y Don Bosco*)
    8. `/blog/diseno-web-san-isidro/` (*Diseño de Páginas Web en San Isidro (Martínez, Acassuso y Beccar): Precios 2026 — 50 búsquedas/mes Zona Norte + tráfico activo detectado en GA4 desde Beccar/San Isidro*)
    9. `/blog/diseno-web-formosa/` (*Diseño de Páginas Web en Formosa: Precios 2026 — Tráfico activo de usuarios detectado en GA4 desde Formosa Capital*)
    10. `/blog/diseno-web-santiago-del-estero/` (*Diseño de Páginas Web en Santiago del Estero (Capital, La Banda y Termas): Precios 2026 — Tráfico activo detectado en GA4*)
  - Generadas y procesadas las 10 imágenes editoriales `1200x675` con pastilla y sello `erikwebsite.com` tanto en `images/` como en `public/images/`.
  - Sincronizados `blog/index.html` (`Mostrando 84 guías`), `vite.config.js` y `sitemap.xml` (`105` URLs canónicas), compilación limpia en Vite (`0 errores, 0 warnings`) y notificadas las 10 URLs a Google Indexing API v3.
- [x] **2026-11-02 (Noche — Demo Página Modo Funnel `/demos/funnel/` + Batch 10 de 5 Artículos BoFu):**
  1. **Corrección de enlaces de Demos y Escala de Precios:** Se eliminaron las referencias a `/demos/veterinaria/` y `/demos/taller/` (redirigiéndolas a `/#demos`) y se dejó explícita en las guías de e-commerce/indumentaria la diferenciación de precios: **$150.000 ARS (pago único)** corresponde a Landing Pages, Páginas Modo Funnel y Cotizadores Interactivos de ítems predefinidos (como `/demos/vajilla/`), mientras que **Tiendas Multi-Producto / Catálogos Autoadministrables a Medida** (como `3dmon.shop`) pertenecen a la categoría de Desarrollos Especiales y se cotizan a medida según el volumen de productos y mantenimiento. Also se corrigió la referencia a **Wink Studio** (`winkstudioar.com`, Self Photo Studio en San Juan).
  2. **Nueva Demo Interactiva de Página Modo Funnel (`/demos/funnel/index.html`):** Diseñada en columna única 100% libre de menús de distracción con **Selector de 2 Modos en vivo** (*1. Modo Archivo Digital / Ebook + Plantillas* y *2. Modo Servicio / Mentoría 1 a 1*), apilamiento de valor estilo Hormozi, selector de medio de pago (*Transferencia con 10% OFF vs. Mercado Pago*) y casilla interactiva de **Order Bump** (+ $4.500 ARS) que recalcula el total en tiempo real y arma el mensaje de compra hacia WhatsApp. Enlazada en `index.html`, `en/index.html` y en las guías de Funnels.
  3. **Publicación del Batch 10 de 5 Artículos de Alta Intención (extraídos de los nuevos CSVs de Google Ads, alcanzando 89 guías activas en `/blog/` y 111 URLs canónicas en `sitemap.xml`):**
     - `/blog/hotmart-argentina-comisiones-impuestos-alternativa-funnel/` (*Hotmart en Argentina 2026: Comisiones del 9,9%, Impuestos al comprador y Cómo Vender con tu Propio Funnel — 5.000 búsquedas/mes*)
     - `/blog/stan-store-argentina-precios-alternativa-pesos/` (*Stan Store en Argentina: ¿Conviene Pagar $29 a $99 USD/mes o Tener tu Propio Funnel en Pesos? — 500 búsquedas/mes*)
     - `/blog/que-es-pixel-de-meta-para-que-sirve-instalar-web/` (*Píxel de Meta: Qué Es, Para Qué Sirve y Cómo Multiplicar las Ventas de tus Anuncios — 500 búsquedas/mes, Competencia Baja 31/100*)
     - `/blog/paginas-web-constructoras-desarrolladoras-arquitectura-argentina/` (*Páginas Web para Constructoras, Estudios de Arquitectura y Desarrolladoras en Argentina — Competencia 33/100 + `funnel inmobiliario` Comp 0/100*)
     - `/blog/cuanto-cuesta-auditoria-seo-posicionamiento-web-google-argentina/` (*Auditoría SEO y Posicionamiento Web en Google en Argentina: Qué Incluye y Cómo Subir Posiciones — `posicionar web` 500/mes + `auditoria seo precio` Comp 0/100*)
- [x] **2026-11-04 (Cotizador en Tiempo Real en `/demos/vajilla/` + Nueva Demo de Restaurante `/demos/restaurante/` + Batch 11 de 10 Artículos `/non-obvious`):**
  1. **Cotizador Interactivo en Tiempo Real por WhatsApp en `/demos/vajilla/` (`demos/vajilla/index.html` y `demos/vajilla/app.js`):** Se agregaron selectores rápidos de cantidad (`-10`, `-1`, input numérico, `+1`, `+10`) en las 8 tarjetas del catálogo y una nueva sección `#cotizador` pre-cargada con el ejemplo del usuario (*10 Copas de Vino + 20 Sets de Cubiertos + 2 Manteles Redondos = $18.300 ARS*), con presets en 1 clic, vista previa en vivo del mensaje de WhatsApp y envío directo del presupuesto armado.
  2. **Nueva Demo de Restaurante y Reservas en Cluster 2 (`/demos/restaurante/index.html` y `demos/restaurante/app.js`):** Diseñada en estética Luxury Noir (`#0A0A0C`) y Dorado Champagne (`#D4AF37`) ("ÁUREA · Fuegos & Cava"), con carta digital filtrable y **3 diferenciales `/non-obvious` de conversión**:
     - *Pre-selección de cortes/vinos desde la carta (`+ Sumar a mi Mesa`)* que viajan directo a la reserva para descorche o marcha previa.
     - *Concierge de Mesa Pre-Llegada (Upsells)*: casillas para sumar 2 copas de Extra Brut de bienvenida (`+$7.500`), postre aniversario con lámina de oro (`+$9.500`) o recorrida guiada por la cava (`Sin cargo`).
     - *Cotizador Instantáneo de Mesas Largas y Cumpleaños (8 a 40 invitados)*: calculadora interactiva de menú cerrado de 3 pasos (`$28.500` o `$36.000` por persona) que calcula el total del grupo y envía la pre-reserva a WhatsApp.
  3. **Actualización del Cluster 2 a 4 Estilos:** Se actualizó la barra superior sticky en `demos/vajilla/`, `demos/catering/`, `demos/salones/` y `demos/restaurante/`, además de las tarjetas de la homepage en `index.html` y `en/index.html` (`1. Vajilla`, `2. Catering y Barras`, `3. Salones y Quintas`, `4. Restaurante y Reservas`).
  4. **Publicación del Batch 11 de 10 Artículos `/non-obvious` enriquecidos con los 4 nuevos CSVs de Google Ads (alcanzando 99 guías activas en `/blog/` y 121 URLs canónicas en `sitemap.xml`):**
     - `/blog/anuncios-instagram-facebook-clics-sin-ventas-whatsapp/` (*Publicidad en Instagram y Facebook con clics pero sin ventas en WhatsApp — `publicidad instagram` 500/mes + `funnel de conversión` Comp 16/100*)
     - `/blog/registrar-marca-inpi-vs-dominio-com-ar-nic-argentina/` (*Registrar Marca en INPI vs. Dominio .com.ar en NIC Argentina — `inpi marcas` 5.000/mes, Comp 22/100*)
     - `/blog/cotizador-online-whatsapp-vs-carrito-compras-tradicional/` (*Qué Es un Cotizador Online por WhatsApp y Por Qué Vende Más que un Carrito Tradicional — `cotizador online` / `presupuesto online` 500/mes*)
     - `/blog/como-saber-si-mi-pagina-web-esta-penalizada-google/` (*Cómo Saber si tu Página Web Está Penalizada en Google o Sale 'No es Seguro' sin SSL — `certificado ssl` 500/mes*)
     - `/blog/cuanto-cobra-agencia-mantenimiento-web-argentina/` (*Cuánto Cobra una Agencia por Mantener una Página Web en Argentina y Cómo Usar tu Webmail — `webmail` 50.000/mes, `ferozo webmail` y `hostinger webmail` 5.000/mes +900%*)
     - `/blog/paginas-web-energia-solar-paneles-solares-argentina/` (*Páginas Web para Empresas de Energía Solar e Instaladores de Paneles Solares — `paneles solares` 50.000/mes +900%, `paneles solares en san juan` 500/mes*)
     - `/blog/paginas-web-control-plagas-fumigacion-higiene-seguridad/` (*Páginas Web para Empresas de Control de Plagas, Fumigaciones e Higiene y Seguridad — `control de plagas` 5.000/mes +900%, `control fumigaciones` Comp 10/100*)
     - `/blog/paginas-web-alquiler-maquinaria-grupos-electrogenos-banos-quimicos/` (*Páginas Web para Alquiler de Maquinaria Vial, Grupos Electrógenos y Baños Químicos*)
     - `/blog/paginas-web-ortopedias-alquiler-camas-internacion-domiciliaria/` (*Páginas Web para Ortopedias, Alquiler de Camas Ortopédicas e Internación Domiciliaria — `internacion domiciliaria pami` 5.000/mes Comp 19/100*)
     - `/blog/paginas-web-salones-eventos-quintas-catering-argentina/` (*Páginas Web para Salones de Eventos, Quintas, Catering y Restaurantes — `alquiler de vajilla` 5.000/mes Comp 24/100, `precio de alquiler de vajilla para 50 personas` 500/mes*)
- [x] **Auditoría Integral de Coherencia, Píxel, Favicons, Términos, Categorías y Acordeones FAQ (2026-11-04):**
  1. **Unificación de Rondas de Revisión y Alcance de `$150.000 ARS`:**
     - Se eliminaron todas las menciones a *"revisiones ilimitadas"* y a la garantía de 30 días de consultas en `index.html` y demos, unificando en todo el sitio **hasta 2 rondas de revisiones del borrador antes de publicar**.
     - Se aclaró en `index.html`, `en/index.html`, `san-juan/index.html` y `terminos/index.html` que el precio de `$150.000 ARS` (`$199 USD` internacional) corresponde al diseño de una página web completa de una sola sección tal como se ve en las demos (o con modificaciones mínimas), mientras que las páginas web con múltiples secciones o desarrollos a medida se cotizan por separado.
  2. **Corrección Crítica del Píxel de Meta en 136 páginas:**
     - Se eliminaron los disparos automáticos de `fbq('track', 'Contact')` y `fbq('trackCustom', 'Whatsapp')` al cargar la página (`<head>`, `<noscript>` y `<body>`), dejando únicamente `PageView` en carga y el disparo de `Contact` exclusivamente cuando el usuario hace clic real en un botón o enlace de WhatsApp (`wa.me`, `whatsapp.com` o `[data-wa-msg]`).
  3. **Favicon Físico `/favicon.svg` y `og:image` Unificado:**
     - Se creó `/favicon.svg` (en raíz y `public/favicon.svg`) y se estandarizó `<link rel="icon" type="image/svg+xml" href="/favicon.svg">` en las 136 páginas públicas. Se unificó `logo_erikwebsite_ig.png` como `og:image` en las páginas principales.
  4. **Actualización de `/san-juan/index.html`, `/en/index.html` y `/terminos/index.html`:**
     - `/san-juan/` ahora muestra las 13 demos completas (incluyendo Restaurante y Funnel).
     - `/en/` tiene el 100% de textos visibles, botones, FAQs, mensajes de WhatsApp y Schema JSON-LD en inglés con tarifas en USD.
     - `/terminos/` fue actualizado a Abril 2026 incorporando el alcance de 1 sección tipo demo, Auditoría SEO, Páginas Modo Funnel, Píxel de Meta y la Cláusula 10 para Clientes Internacionales (USD).
  5. **Filtros Dinámicos del Blog (`blog/index.html`) y FAQs Desplegables con Auto-Cierre:**
     - `<select id="blog-cat-select">` incluye las 8 categorías activas con sus conteos exactos (`99` guías totales) y un script automático que recalcula las cantidades y agrega nuevas categorías dinámicamente cada vez que se publican artículos.
     - Los 99 artículos del blog, `/auditoria-seo/` y `/san-juan/` usan acordeones `<details name="faq-accordion">` que cierran automáticamente la pregunta abierta anterior cuando el usuario abre una nueva.
- [x] **2026-11-04 (Auditoría de Canónicas 100% Válidas + Refactor Guía Agencias de Viajes + Análisis de 4 Nuevos CSVs de Google Ads):**
  1. **Auditoría Global de Etiquetas Canónicas (`rel="canonical"`):**
     - Se auditaron las 130 páginas HTML públicas del proyecto (`check_canonicals.py`). Se detectaron y corrigieron 5 etiquetas en subdirectorios de demos (`/demos/cluster-1/`, `/demos/cluster-2/`, `/demos/cluster-3/`, `/demos/eventos/`, `/demos/servicios-hogar/`) garantizando que el 100% de las URLs canónicas terminen en barra `/` y apunten exactamente a su URL final en `https://erikwebsite.com` sin dilución de autoridad.
  2. **Refactor Guía Agencias de Viajes (`/blog/paginas-web-agencias-de-viajes-excursiones-turismo-argentina/`):**
     - Se actualizó el bloque de Respuesta Directa Sturm AEO/GEO clarificando que una web para agencia de viajes/turismo requiere una arquitectura multi-página con fichas de circuitos y cotización a medida superior a la landing base de $150.000 ARS.
     - Se añadió sección dedicada H2 explicando por qué se cotiza a medida (fichas de paquetes, políticas de cancelación, legajo habilitante de turismo).
     - Se vincularon demos reales existentes (`/demos/restaurante/`, `/demos/salones/`) y el proyecto real de referencia UAQ Tours (`uaqtours.com.ar`) en `/#trabajos`.
     - Se incorporó FAQ con acordeón `<details name="faq-accordion">` detallando rangos de inversión para agencias de viajes.
  3. **Análisis de los 4 Nuevos CSVs de Google Ads (Noviembre 2026):**
     - Se extrajeron 4 oportunidades clave de alta intención y 0 canibalización: 1) Migración de WordPress lento/hackeado a código limpio/hosting rápido, 2) Páginas web para Hoteles, Cabañas y Reservas directas sin comisiones de Booking, 3) Páginas web para Arquitectos y Estudios de Arquitectura con portfolio visual, 4) Presupuesto y Costos reales de Mantenimiento Web en Argentina.
- [x] **2026-11-04 (Batch 12 de 9 artículos + corrección del Sitemap en producción):**
  1. **Publicación del Batch 12 (108 guías activas en `/blog/`, 126 URLs en el sitemap)**, usando los 2 bancos de ideas y diferenciando el ángulo de cada uno respecto de las guías previas para no canibalizar:
     - `/blog/migrar-wordpress-otro-hosting-o-codigo-limpio/`
     - `/blog/sistema-reservas-whatsapp-hoteles-cabanas-sin-comisiones/` (enfoque operativo de reservas; la guía de cabañas ya cubre la matemática de comisiones)
     - `/blog/portfolio-web-arquitectos-estudios-de-arquitectura/` (enfoque portfolio visual y peso de imágenes)
     - `/blog/presupuesto-mantenimiento-web-que-incluye-como-comparar/` (checklist para comparar propuestas; los precios ya están en la guía de agencias)
     - `/blog/codigo-qr-restaurante-carta-digital-que-no-caduque/`
     - `/blog/funnel-inmobiliario-captar-compradores-departamentos-pozo/`
     - `/blog/funnel-de-ventas-b2b-captar-leads-empresas-pymes/`
     - `/blog/tienda-online-propia-cuando-conviene-argentina/` (criterio de decisión por tamaño de catálogo; deriva a las comparativas de Tiendanube)
     - `/blog/mejorar-velocidad-wordpress-y-poner-sitio-en-mantenimiento/`
     - FAQs con `<details name="faq-accordion">`; enlaces entrantes agregados en 14 guías existentes; 9 imágenes en `images/` y `public/images/`; scripts en `scratch/create_batch12_articles.py` y `scratch/register_batch12.py`.
  2. **Causa raíz del sitemap estancado en 63 URLs en GSC:** `public/sitemap.xml` estaba desactualizado desde el Batch 5 y es el que Vite publica; el de la raíz se actualizaba pero no se desplegaba. Se sincronizó ambos. Se quitaron 4 URLs inexistentes (`/demos/taller/`, `/demos/arquitectura/`, `/demos/veterinaria/`, `/demos/inmobiliaria/`) que devolvían 404.
  3. **Otros 404 corregidos:** se eliminó la referencia huérfana a `/images/apple-touch-icon.png` en 15 guías del blog.
  4. **Ideas pendientes (banco reservado):** ninguna de los 2 bancos; quedan las keywords de funnels genéricos (`embudo de ventas`, `etapas del funnel`, 500/mes, comp. 18-27) como posible guía educativa futura, cuidando no canibalizar `que-es-un-funnel-de-ventas-para-que-sirve-argentina`.
- [x] **2026-11-05 (Auditoría Ahrefs: Corrección Cloudflare Email Protection + Optimización Masiva de Imágenes > 1MB):**
  1. **Solución a `/cdn-cgi/l/email-protection`:**
     - Ahrefs detectaba enlaces internos a `/cdn-cgi/l/email-protection` debido a la función "Email Address Obfuscation" de Cloudflare, que intercepta direcciones de correo en el HTML y las reescribe dinámicamente.
     - Se envolvieron todas las direcciones de email educativas en `<!--email_off-->...<!--/email_off-->` en los 3 artículos reportados (`blog/configurar-correo-corporativo-outlook-firma-profesional/`, `blog/registrar-marca-inpi-vs-dominio-com-ar-nic-argentina/`, `blog/como-crear-correo-corporativo-dominio-propio-gmail/`), desactivando la ofuscación de Cloudflare en esos bloques sin alterar el diseño ni romper enlaces.
  2. **Compresión y Optimización de 47 Imágenes Pesadas (> 1MB):**
     - Se optimizaron las 47 imágenes reportadas en `images/` y `public/images/` mediante cuantización RGB (256 colores, MEDIANCUT) para PNGs y calidad 82 para JPEGs (`vajilla_living.jpg`).
     - Peso total reducido de **56.54 MB a 19.39 MB (ahorro de 37.14 MB / 65.7% de reducción)**.
     - Ninguna imagen supera ahora los 650 KB (todas muy por debajo del umbral de 1 MB de Ahrefs), conservando dimensiones originales de 1200x675, extensión `.png` e integridad de metadatos OpenGraph y Schema.org.
- [x] **2026-11-06 (Batch 13: Cobertura Nacional 100% de Argentina + 9 Joyas Comerciales de Google Ads):**
  - **15 artículos nuevos publicados** (totalizando **123 guías activas** en `/blog/index.html` y **141 URLs canónicas** en `sitemap.xml` y `public/sitemap.xml`):
    - **6 Provincias (Cierre 100% Federal - 24/24 Jurisdicciones de Argentina):**
      1. `/blog/diseno-web-caba-buenos-aires/` (*CABA: Palermo, Microcentro, Belgrano, código limpio vs. agencias porteñas*)
      2. `/blog/diseno-web-catamarca/` (*Catamarca: San Fernando del Valle, litio, Puna, proveedores mineros*)
      3. `/blog/diseno-web-la-rioja/` (*La Rioja: Chilecito, agroindustria olivo/vid, turismo Talampaya*)
      4. `/blog/diseno-web-santa-cruz/` (*Santa Cruz: El Calafate, Río Gallegos, glaciares, minería sin comisiones Booking*)
      5. `/blog/diseno-web-tierra-del-fuego/` (*Tierra del Fuego: Ushuaia, Río Grande, turismo antártico, manufactura*)
      6. `/blog/diseno-web-la-pampa/` (*La Pampa: Santa Rosa, General Pico, cabañas ganaderas, maquinaria agrícola*)
    - **9 Joyas Comerciales BoFu de Google Ads (Descartada la de mayoristas por requerir panel/mantenimiento diario):**
      7. `/blog/paginas-web-seguridad-privada-alarmas-monitoreo/` (*Seguridad privada, habilitaciones ministeriales, alarmas y monitoreo 24/7*)
      8. `/blog/paginas-web-productores-asesores-seguros-brokers/` (*Productores asesores de seguros (PAS), cotizador rápido de autos, hogar y ART a WhatsApp*)
      9. `/blog/paginas-web-concesionarias-autos-usados-agencias-motos/` (*Concesionarias de autos usados y motos, sin comisiones de MercadoLibre, permutas y financiación*)
      10. `/blog/paginas-web-empresas-limpieza-finales-obra-tapizados/` (*Limpieza corporativa, abonos para oficinas y clínicas, personal con ART, finales de obra*)
      11. `/blog/paginas-web-imprentas-graficas-carteleria-merchandising/` (*Imprentas gráficas, cotizador por tiradas, cartelería de seguridad e higiene y merchandising*)
      12. `/blog/paginas-web-salones-fiestas-infantiles-peloteros-inflables/` (*Salones infantiles, peloteros, turnos de 3 horas, combos y reservas a WhatsApp*)
      13. `/blog/whatsapp-business-vs-pagina-web-ventas-argentina/` (*WhatsApp Business vs. página web: por qué el catálogo de WhatsApp no alcanza y cómo combinarlos*)
      14. `/blog/paginas-web-academias-institutos-cursos-oficios/` (*Academias y cursos de oficios con salida laboral, cobro en pesos sin 10% en USD a Hotmart*)
      15. `/blog/landing-page-para-google-ads-conversion-argentina/` (*Landing page para Google Ads: Quality Score, carga sub-1 segundo y cómo no quemar clics*)
  - **Imágenes Editoriales Sturm (15/15):** 16:9 (`1200x675`), badge semántico superior izquierdo y sello inferior derecho `erikwebsite.com`, optimizadas con cuantización a 256 colores (< 480 KB todas, previniendo advertencias de Ahrefs), sincronizadas en `images/` y `public/images/`.
  - **Interlinking "SEO Colonies":** Inyectados enlaces entrantes contextuales en más de 12 guías existentes.
  - **Build & Indexing:** Compilación en producción con Vite validada en 7.66s (`0 errores, 0 warnings`). 15 URLs notificadas exitosamente a la Google Web Search Indexing API v3 (`200 OK`).
- [x] **2026-11-07 (Instalación Global de SerpBear, Auditor SEO Comercial + Mejora de Extensión Chrome, Bing IndexNow & Corrección de Canibalización):**
  1. **Skill Global `serpbear` e Instalación Local (`C:\Users\erikl\.gemini\tools\serpbear\`):**
     - Se clonó `https://github.com/towfiqi/serpbear.git` en `C:\Users\erikl\.gemini\tools\serpbear` y se creó la skill global en `C:\Users\erikl\.gemini\config\skills\serpbear\SKILL.md`.
     - Se desarrolló `serpbear_cli.py`, conectando la base SQLite de SerpBear (`data/database.sqlite`) y los archivos `data/SC_<domain>.json` directamente a la API oficial de Google Search Console (`~/.config/claude-seo/service_account.json`) y a los CSV de Google Ads, sincronizando **225 keywords de `erikwebsite.com`** y **31 keywords de `winkstudioar.com`** (100% gratuito, sin requerir proxies pagos).
  2. **Resolución de Canibalización detectada por SerpBear (`comprar dominio .ar` / `.com.ar`):**
     - SerpBear detectó que 9 variantes de `comprar dominio .ar` (~250 impresiones) se dividían entre `/blog/como-registrar-dominio-com-ar-nic-argentina/` y `/blog/dominio-com-vs-com-ar-cual-conviene-argentina/`.
     - Se diferenció la intención en ambas guías: `como-registrar-dominio-com-ar-nic-argentina` absorbió explícitamente la intención transaccional ("Cómo Comprar y Registrar un Dominio .com.ar y .ar") y `dominio-com-vs-com-ar-cual-conviene-argentina` se enfocó en "Cuál Elegir" con enlace directo hacia el tutorial paso a paso de NIC Argentina.
  3. **Auditor SEO Comercial y Espía de Competencia (`auditor_seo_comercial.py`) + Upgrade de Extensión Chrome:**
     - Se actualizó la extensión de Chrome de Erik en `C:\Users\erikl\OneDrive\Desktop\mi-extension-seo` (`popup.html` y `popup.js`) agregando:
       - **Radiografía Tecnológica y Píxeles:** Detección automática de WordPress, Elementor, WooCommerce, Tiendanube, Wix, Shopify o Código a Medida, más Meta Pixel, GA4 y GTM.
       - **Botón "📋 Copiar Diagnóstico para WhatsApp":** Genera automáticamente un mensaje comercial personalizado con el puntaje (`X/100`), tecnologías detectadas y los 3 problemas críticos para enviar por WhatsApp a prospectos.
     - Se creó `C:\Users\erikl\.gemini\tools\serpbear\auditor_seo_comercial.py` (copiado también en `scratch/auditor_seo_comercial.py`) para auditar cualquier URL o comparar `cliente vs. competidor` desde consola con tabla comparativa y pitch de WhatsApp.
  4. **Bing Webmaster Tools API & IndexNow:**
     - Se generó y desplegó la llave oficial de verificación IndexNow (`e7a9c4b2f8d143e6a0b5c8d9e2f1a3b4.txt`) en la raíz y `public/`.
     - Se creó `C:\Users\erikl\.gemini\tools\serpbear\bing_indexnow_and_api.py` (y `scratch/bing_indexnow_and_api.py`) para enviar las 141 URLs del sitemap a IndexNow en lote y conectar la API Key de Bing Webmaster Tools (`~/.config/claude-seo/bing_api.json`).
- [x] **2026-11-07 (Rediseño y Corrección Crítica del Footer Global: 2 Niveles Mobile-First y Eliminación de Desborde Horizontal):**
  - **Diagnóstico del problema:** En modo celular, el footer en `index.html` y `en/index.html` tenía una fila `flex` sin `flex-wrap` con 10 elementos que forzaba un ancho de ~970px en pantallas móviles de 360-390px, provocando un desborde horizontal masivo (la web se movía hacia los costados). Además, acumulaba demasiados enlaces secundarios y viñetas `•` sueltas que fragmentaban la lectura.
  - **Solución implementada (Arquitectura de 2 Niveles Mobile-First):**
    - **Nivel 1 (Superior):** Identidad de marca clara (`erikwebsite.com` + tagline `Páginas web a medida y alta conversión en celulares.`) a la izquierda / arriba en mobile, junto con una navegación esencial limpia de 4-5 enlaces prioritarios (`Auditoría SEO`, `San Juan`, `Blog`, `Términos y Condiciones`, e `Inicio` en páginas secundarias) usando `flex-wrap`, `gap-x-6 gap-y-2.5` y touch-targets cómodos sin viñetas rígidas. Se eliminaron enlaces de relleno como el generador de QR del footer primario.
    - **Nivel 2 (Inferior / Barra Legal):** Separador sutil `border-t border-white/[0.08]` con copyright a la izquierda y nota de optimización a la derecha (`© 2026 erikwebsite.com. Todos los derechos reservados.` / `San Juan, Argentina • Diseñado y optimizado para celulares.`).
    - **Garantía Anti-Desborde:** Incorporado `overflow-hidden` en el tag `<footer>` en todas las páginas.
  - **Estandarización Total (153 archivos):** Aplicado en `index.html`, `en/index.html`, `auditoria-seo/index.html`, `san-juan/index.html`, `blog/index.html`, `terminos/index.html`, los 123 artículos de `blog/*/index.html` y las 24 páginas de `demos/**/*.html`.
  - **Compilación Vite:** `npm run build` ejecutado y validado en 11.41s (`0 errores, 0 warnings`). Cero desbordes detectados (`check_all_footers.py` = 0).
- [x] **2026-11-08 (Batch 14 + Reestructuración Geográfica Limpia 1 Ciudad / 1 Zona / 24 Provincias Exclusivas + Optimización SerpBear de Quilmes #11.0):**
  - **18 artículos nuevos publicados en total** (alcanzando **141 guías activas** en `/blog/index.html` y **159 URLs canónicas** en `sitemap.xml` y `public/sitemap.xml`):
    - **3 Recomendados de los CSV de Google Ads (0% canibalización):**
      1. `/blog/ferozo-webmail-roundcube-vs-gmail-outlook-corporativo/` (*Ferozo Webmail y Roundcube vs. Gmail/Outlook: salir del correo lento y sin espacio de DonWeb/cPanel*)
      2. `/blog/cuanto-cuesta-publicidad-instagram-argentina-mercadopago/` (*Precios de publicidad en Instagram en Argentina 2026, pago en pesos con Mercado Pago y conversión con landing page*)
      3. `/blog/diseno-paginas-web-corporativas-empresariales-pymes-argentina/` (*Diseño de páginas web corporativas e institucionales para empresas y PyMEs B2B en Argentina*)
    - **3 Artículos con la Skill `/non-obvious` (Ordenados de menor a mayor probabilidad + Filtro Hormozi):**
      4. `/blog/paginas-web-camiones-atmosfericos-desagotes-destapaciones-24hs/` (*Rareza <1%: Camiones atmosféricos, desagotes industriales y destapaciones con hidrojet 24 hs*)
      5. `/blog/paginas-web-consultoras-higiene-seguridad-puesta-tierra-carga-fuego/` (*Rareza ~2.5%: Consultoras de Higiene y Seguridad, medición de Puesta a Tierra SRT 900/15 y Carga de Fuego*)
      6. `/blog/paginas-web-fabricas-aberturas-aluminio-pvc-dvh-steel-framing/` (*Rareza ~6%: Fábricas de aberturas de aluminio/PVC DVH y constructoras en Steel Framing con pre-cotizador de obra*)
    - **3 Nuevas Páginas Exclusivas Nivel Provincia (separadas de sus ciudades principales):**
      7. `/blog/diseno-web-rio-negro/` (*Provincia de Río Negro: Alto Valle, Cipolletti, General Roca, Viedma y Las Grutas — separada de `/blog/diseno-web-bariloche/`*)
      8. `/blog/diseno-web-chubut/` (*Provincia del Chubut: Esquel, Trevelin, Rawson, Comodoro, Puerto Madryn y Trelew — separada de sus 3 ciudades*)
      9. `/blog/diseno-web-entre-rios/` (*Provincia de Entre Ríos: Concordia, Gualeguaychú, Concepción del Uruguay, Colón y Federación — separada de `/blog/diseno-web-parana/`*)
    - **2 Zonas Metropolitanas Reconocibles con Slug Limpio y 7 Ciudades Individuales:**
      10. `/blog/diseno-web-zona-norte/` (*Zona Norte GBA: Tigre, Nordelta, Vicente López, Olivos, San Fernando y Escobar*)
      11. `/blog/diseno-web-zona-oeste/` (*Zona Oeste GBA: Morón, Ituzaingó, Castelar, Ramos Mejía, Haedo y Hurlingham*)
      12. `/blog/diseno-web-san-rafael-mendoza/` (*San Rafael · Sur de la Provincia de Mendoza*)
      13. `/blog/diseno-web-rio-cuarto/` (*Río Cuarto · Sur de la Provincia de Córdoba*)
      14. `/blog/diseno-web-villa-maria/` (*Villa María · Centro de la Provincia de Córdoba*)
      15. `/blog/diseno-web-puerto-madryn/` (*Puerto Madryn · Costa de la Provincia del Chubut*)
      16. `/blog/diseno-web-trelew/` (*Trelew · Valle Inferior de la Provincia del Chubut*)
      17. `/blog/diseno-web-rafaela/` (*Rafaela · Centro-Oeste de la Provincia de Santa Fe*)
      18. `/blog/diseno-web-venado-tuerto/` (*Venado Tuerto · Sur de la Provincia de Santa Fe*)
    - **Redirecciones Limpias:** Los 5 slugs multi-ciudad previos (`diseno-web-zona-norte-tigre-nordelta-vicente-lopez`, `diseno-web-zona-oeste-moron-ituzaingo-castelar-ramos-mejia`, `diseno-web-rio-cuarto-villa-maria`, `diseno-web-puerto-madryn-trelew`, `diseno-web-rafaela-venado-tuerto`) quedaron con redirección instantánea `<meta http-equiv="refresh">` + `window.location.replace` y excluidos de `sitemap.xml`.
  - **Optimización On-Page + Interlinking de `/blog/diseno-web-quilmes/` (Posición #11.0 en SerpBear/GSC -> Push a Top 5):**
    - Ampliado el contenido de ~480 a +1.050 palabras con micro-zonas de Quilmes (Quilmes Centro, Las Lomitas de Quilmes, Peatonal Rivadavia, Bernal, Don Bosco, Ezpeleta, San Francisco Solano, Parque Industrial Tecnológico de Quilmes y Av. Calchaquí), H2 exactos (`Diseño web en Quilmes vs. estudio creativo o agencia tradicional`), corrección del 3er y 4to acordeón `<details name="faq-accordion">` y refuerzo de enlaces entrantes desde `lomas-de-zamora`, `la-plata` y `caba-buenos-aires`.
  - **Bing Webmaster API (`SubmitUrlBatch` / `SubmitFeed`) + Bugfix Extensión Chrome + Panel Visual SerpBear (`localhost:4321`):**
    - Solucionado el bug de `title.includes('')` en `C:\Users\erikl\OneDrive\Desktop\mi-extension-seo\popup.js` que reportaba falso positivo de charset roto en todas las webs.
    - Creado el panel visual local de SerpBear en `http://localhost:4321` (`Abrir_Panel_SerpBear.bat`).
- [x] **2026-11-08 (Batch 15: Posicionamiento como Especialista SEO en San Juan y Argentina + Sinergia SEO/Redes + Guía Zona Sur GBA):**
  - **Actualización de [`/auditoria-seo/index.html`](file:///c:/Users/erikl/Downloads/WebErik/auditoria-seo/index.html) y [`/san-juan/index.html`](file:///c:/Users/erikl/Downloads/WebErik/san-juan/index.html):**
    - En `/auditoria-seo/`: incorporadas la sección **`#redes`** (*"Cómo nuestra optimización SEO hace crecer tus Redes Sociales y duplica tus ventas"* — velocidad sub-1s para enlaces en bio/Reels, Píxel de Meta con evento `Contact` limpio y autoridad cruzada `Schema.org sameAs`) y la sección B2B **`#agencias`** (*"Especialista SEO Técnico para Empresas y Agencias de Marketing en Argentina"*, exhibiendo puntajes verificables `95/100` en `winkstudioar.com` y `92/100` en `erikwebsite.com`).
    - En `/san-juan/`: presentada la doble propuesta comercial en San Juan (*Servicio #1: Diseño Web Nuevo por $150.000 ARS* y *Servicio #2: Consultor SEO, Posicionamiento en Google y Potenciador de Redes Sociales en San Juan* en `#seo-san-juan`).
  - **Separación Visual y Categoría Especialista SEO en [`/blog/index.html`](file:///c:/Users/erikl/Downloads/WebErik/blog/index.html):**
    - Añadida la categoría `seo` (`Auditoría SEO, Velocidad e IA`) y una barra de píldoras de acceso rápido arriba del listado (`Todas las Guías`, `⚡ Especialista SEO, Velocidad e IA`, `📈 Redes Sociales y Meta Ads`, `📍 Google Maps, Provincias y Zonas`, `💻 Diseño Web y Precios`) permitiendo filtrar los artículos técnicos de SEO en 1 clic (`/blog/?cat=seo`) sin dividir la autoridad del dominio.
  - **6 Artículos Nuevos Publicados (5 de Autoridad Técnica SEO + 1 Zona Metropolitana Reconocible, alcanzando 147 guías activas en `/blog/` y 165 URLs canónicas en `sitemap.xml` y `public/sitemap.xml`):**
    1. `/blog/consultor-seo-san-juan-posicionamiento-web-google/` (*Consultor SEO en San Juan: Posicionamiento Web en Google, Auditoría Técnica y Crecimiento para Redes*)
    2. `/blog/especialista-consultor-seo-argentina-posicionamiento-google/` (*Especialista y Consultor SEO en Argentina: Cómo Subir al Primer Lugar de Google con Ingeniería Real*)
    3. `/blog/como-optimizar-pagina-web-para-crecer-redes-sociales-instagram/` (*Cómo Optimizar tu Página Web para Hacer Crecer tus Redes Sociales y Duplicar tus Ventas de Instagram*)
    4. `/blog/seo-para-inteligencia-artificial-como-aparecer-chatgpt-perplexity-google/` (*SEO para Inteligencia Artificial (AEO y GEO) en Argentina: Cómo Aparecer en ChatGPT, Perplexity y Google AI Overviews*)
    5. `/blog/auditoria-velocidad-web-core-web-vitals-lcp-inp-google/` (*Auditoría de Velocidad Web y Core Web Vitals (LCP e INP): Por Qué una Web Lenta Frena tu SEO y tus Ventas*)
    6. `/blog/diseno-web-zona-sur/` (*Diseño de Páginas Web en Zona Sur GBA: Avellaneda, Lanús, Lomas de Zamora, Banfield, Quilmes, Bernal y Adrogué — Competencia Baja 0 a 17/100 en CSV*)
- [x] **2026-11-08 (Batch 16: 6 Artículos de Autoridad SEO de los 4 Nuevos CSVs + Eventos de Conversión en GA4 + Sistema Semanal Dominical `PLAN_SEMANAL_SEO.md` + Skill + Automation):**
  1. **Arquitectura de Eventos de Negocio en Google Analytics 4 (`G-KWD0WYVK4J` — `src/js/whatsapp.js` + `src/js/main.js` en las 171 páginas):**
     - Implementado listener delegado global que registra automáticamente en GA4:
       - `generate_lead` (Evento oficial de conversión de GA4 con `service_intent`: `auditoria_seo` | `funnel` | `diseno_web`, `lead_source`, `cta_text`, `value`, `currency`).
       - `whatsapp_click` (Evento detallado de clic a cualquier botón `[data-wa-msg]` o enlace `wa.me`).
       - `view_demo` (Registro de cuál de las 13 Demos Interactivas abre el usuario y desde qué página).
       - `use_interactive_calculator` (Uso de las calculadoras de indemnización laboral, cotizador de vajilla, catering, funnel o generador QR).
       - `faq_expand` (Apertura de preguntas frecuentes `<details>` con el texto de la pregunta).
       - `article_read_75` (Lectura humana profunda superior al 75% del artículo tras +8s en página).
     - Inyectado `<script type="module" src="/src/js/main.js"></script>` en las 103 guías del blog que no lo tenían, garantizando cobertura del 100% del sitio.
  2. **Publicación del Batch 16 de 6 Artículos de Autoridad SEO (0% Canibalización, 0 Emojis, alcanzando 153 guías activas en `/blog/` y 171 URLs canónicas en `sitemap.xml` / `public/sitemap.xml`):**
     - `/blog/por-que-mi-pagina-web-no-aparece-en-google-como-indexar/` (*Por Qué Mi Página Web No Aparece en Google y Cómo Indexarla Rápido en Search Console — Comp 0 a 29/100*)
     - `/blog/seo-para-tiendanube-ecommerce-argentina-posicionar-productos/` (*SEO para Tiendanube y Tiendas Online en Argentina: Cómo Posicionar tus Productos en Google — Comp 22 a 29/100*)
     - `/blog/posicionamiento-seo-wordpress-wix-yoast-seo-sirve/` (*Posicionamiento SEO en WordPress y Wix: Para Qué Sirve Yoast SEO y Por Qué No Alcanza — Comp 0 a 36/100*)
     - `/blog/seo-para-inmobiliarias-desarrolladoras-argentina-google/` (*SEO para Inmobiliarias y Desarrolladoras en Argentina: Cómo Posicionar Propiedades en Google — Comp 0 a 8/100*)
     - `/blog/como-instalar-google-analytics-4-ga4-medir-clics-whatsapp/` (*Cómo Instalar Google Analytics 4 (GA4) y Medir Clics a WhatsApp y Ventas de Redes en tu Web — Comp 21 a 43/100*)
     - `/blog/seo-para-abogados-estudios-juridicos-argentina-google/` (*SEO para Abogados y Estudios Jurídicos en Argentina: Cómo Captar Consultas en Google — Comp 29/100 + enlace a `/demos/abogados/`*)
  3. **Archivo `/llms.txt` y `public/llms.txt`:**
     - Desplegado el catálogo estructurado para agentes e IAs generativas (ChatGPT, Perplexity, Claude, Gemini) con los 2 servicios principales, las 13 demos interactivas y las guías pilares de SEO y Diseño Web.
  4. **Sistema Operativo Semanal (`PLAN_SEMANAL_SEO.md` + Skill `seo-weekly-command` + Automation `Domingo SEO & GA4 Command (WebErik)`):**
     - Creado [`PLAN_SEMANAL_SEO.md`](file:///c:/Users/erikl/Downloads/WebErik/PLAN_SEMANAL_SEO.md) con la cadencia Lunes/Miércoles/Viernes (Diseño Web), Martes/Jueves/Sábado (SEO) y Domingo (Auditoría y Plan de Ataque), inicializado con la bitácora de la Semana 1 (8/11/2026) y el Plan Lunes 9/11 a Sábado 14/11.
     - Creados los scripts `scratch/sunday_seo_command.py` y `scratch/check_cannibalization.py`.
     - Instalada la Skill global `seo-weekly-command` (`C:\Users\erikl\.gemini\config\skills\seo-weekly-command\SKILL.md`) y la Automation programada `Domingo SEO & GA4 Command (WebErik)` (`C:\Users\erikl\.gemini\config\sidecars\domingo-seo-command\sidecar.json`).
- [x] **2026-11-08 (Ejecución Exitosa del Comando Dominical SEO & GA4):**
  - Ejecutado `scratch/sunday_seo_command.py` con consulta a las APIs oficiales de GSC (`sc-domain:erikwebsite.com`), GA4 (`properties/554839707`) y SerpBear local.
  - GSC: `1.434` impresiones, `6` clics, `23` consultas en Striking Distance (destacando `pagina web inmobiliarias` en pos 8.7, `correo corporativo outlook` en pos 10.5, `diseño web quilmes` en pos 11.0 y `godaddy argentina` en pos 16.5).
  - GA4: `56` usuarios activos, 70,8% de engagement rate en Organic Search (el canal de mayor calidad de lectura).
  - Control de Canibalización (`check_cannibalization.py`): Se detectó un 71% de solapamiento en la propuesta preliminar de limpieza de oficinas sobre `/blog/paginas-web-empresas-limpieza-finales-obra-tapizados/`. Aplicando la regla de oro "Actualizar antes que Duplicar", se convirtió en Cirugía de Boost sobre la URL existente y se aprobó para el viernes un nuevo nicho B2B con 0% de canibalización: *Páginas Web para Empresas de Logística, Transporte de Carga y Fletes*.
  - Actualizado [`PLAN_SEMANAL_SEO.md`](file:///c:/Users/erikl/Downloads/WebErik/PLAN_SEMANAL_SEO.md) con la bitácora histórica profunda y la hoja de ruta de Lunes a Sábado (Lunes/Miércoles/Viernes Diseño Web, Martes/Jueves/Sábado SEO).
- [x] **2026-11-09 (Ejecución del Lunes 9/11 del Plan Semanal — 2 Cirugías Striking Distance + 1 Artículo Nuevo B2B con Slug Corto):**
  - **Cirugía + Boost 1 (`/blog/paginas-web-para-inmobiliarias-argentina/` — Pos 8.7 en GSC para `'pagina web inmobiliarias'`):**
    - Acortado el `<title>` de 81 a 57 caracteres (`Páginas Web para Inmobiliarias en Argentina: Precios 2026`) para evitar truncamiento en SERP.
    - Incorporada la Sección 3 (*Diseño de página web para inmobiliarias vs. Portales y Plantillas lentas*) con tabla comparativa y enlaces bidireccionales hacia `/blog/seo-para-inmobiliarias-desarrolladoras-argentina-google/` y `/auditoria-seo/`.
    - Corregidos enlaces internos hacia `/blog/paginas-web-constructoras-desarrolladoras-arquitectura-argentina/` y `/demos/funnel/`, y estandarizadas las 4 FAQs con `<details name="faq-accordion">` (trackeado en GA4 con `faq_expand`).
  - **Cirugía + Boost 2 (`/blog/crear-pagina-web-godaddy-conviene-argentina/` — Pos 16.5 en GSC para `'godaddy argentina'`):**
    - Acortado el `<title>` de 87 a 56 caracteres (`GoDaddy Argentina 2026: Precios en Dólares y si Conviene`) encabezando con la keyword exacta.
    - Incorporada la Sección 4 (*Cómo migrar de GoDaddy sin perder tu dominio ni tus correos*) y 4 FAQs con `<details name="faq-accordion">`.
  - **Artículo Nuevo Lunes (`/blog/paginas-web-distribuidoras-mayoristas/` — Regla #18 Slug de 4 palabras, 0% Canibalización, 0 Emojis):**
    - Publicada la guía *Páginas Web para Distribuidoras y Mayoristas en Argentina: Catálogo Ágil y Pedidos por WhatsApp* con imagen editorial propia (`guia_paginas_web_distribuidoras_mayoristas.png`), enlazada desde `/blog/cotizador-online-whatsapp-vs-carrito-compras-tradicional/` y `/blog/paginas-web-locales-ropa-indumentaria-mayoristas-argentina/`.
    - Alcanzadas **154 guías activas** en `/blog/index.html` y **172 URLs canónicas** en `sitemap.xml` / `public/sitemap.xml`.
- [x] **2026-11-09 (Resolución de URLs "Página alternativa con canónica adecuada" en GSC + Redirecciones Limpias + 404.html):**
  - **Diagnóstico de Raíz:** Explicado por qué GSC mostraba 7 URLs no existentes (`/demos/taller/`, `/demos/veterinaria/`, `/demos/inmobiliaria/`, `/demos/arquitectura/`, `/images/`, `/blog/wordpress-vs-codigo-a-medida/`, `/blog/tiendanube-linktree-vs-web-propia/`). El servidor web (Cloudflare/Vercel) al no encontrar archivo estático ni `404.html` devolvía la home `index.html` con HTTP 200 OK y `<link rel="canonical" href="https://erikwebsite.com/">`. Googlebot interpretaba correctamente que esas URLs declaraban como canónica a la home y las excluía como alternativas válidas.
  - **Corrección de Enlaces Internos:**
    - Corregido `blog/posicionamiento-seo-wordpress-wix-yoast-seo-sirve/index.html` (apuntaba a `/blog/wordpress-vs-codigo-a-medida/` en vez de `...-velocidad/`).
    - Corregidos `diseno-web-quilmes` y `seo-para-inteligencia-artificial` (apuntaban a `...-cual-conviene/` en vez de `...-velocidad/`).
    - Corregidos `diseno-web-quilmes` y `diseno-web-zona-sur` (apuntaban a `/blog/diseno-web-buenos-aires-gba/` en vez de `/blog/diseno-web-caba-buenos-aires/`). Auditados todos los enlaces internos del sitio con 0 enlaces rotos restantes.
  - **Redirecciones Dedicadas y 404:**
    - Creados archivos de redirección con `<meta name="robots" content="noindex, follow">` y canónica a sus destinos reales para los 6 slugs históricos.
    - Creado `public/404.html` y `404.html` para evitar el fallback silencioso de 200 OK con canónica a la home.
- [x] **2026-11-10 (Ejecución del Martes 10/11 del Plan Semanal — Cirugía Striking Distance Outlook #8.0–14.7 + Guía Nueva Errores Google Search Console):**
  - **Cirugía + Boost (`/blog/configurar-correo-corporativo-outlook-firma-profesional/` — Pos 8.0–14.7 en GSC):**
    - Acortado el `<title>` de 85 a 58 caracteres (`Correo Corporativo en Outlook: Cómo Configurarlo y Firma`) encabezando con la consulta exacta de GSC.
    - Inyectadas las consultas de la Radiografía Quirúrgica de GSC: `'como abrir un correo empresarial en outlook'` (H2 #1), `'crear correo corporativo outlook gratis'` (nueva Sección 3 con tabla comparativa frente a licencias de Microsoft 365 en dólares) y `'como configurar un correo corporativo en outlook'` (Respuesta Directa).
    - Estandarizadas las 4 FAQs con `<details name="faq-accordion">` y `FAQPage` JSON-LD.
  - **Artículo Nuevo Martes (`/blog/errores-google-search-console-seo/` — Regla #18 Slug de 5 palabras, Regla #17 0 Emojis, Regla #19 0 Enlaces Fantasma):**
    - Publicada la guía técnica *Errores de Google Search Console en Argentina: Cómo Solucionarlos y Subir Posiciones* con imagen editorial propia (`guia_errores_google_search_console_seo.png`), diccionario comparativo de los 6 estados de Search Console (*Página alternativa con etiqueta canónica adecuada*, *Descubierta/Rastreada sin indexar*, *Soft 404*, *Duplicada sin canónica* y *5xx*) y enlazado bidireccional con `/blog/por-que-mi-pagina-web-no-aparece-en-google-como-indexar/`.
    - Alcanzadas **155 guías activas** en `/blog/index.html` (`13` en la categoría Especialista SEO) y **173 URLs canónicas** en `sitemap.xml` / `public/sitemap.xml`.
- [x] **2026-11-11 (Ejecución del Miércoles 11/11 del Plan Semanal — Cirugías Cuyo Mendoza #55 impr y San Luis #25 impr + Guía Nueva Villa Carlos Paz):**
  - **Cirugía + Boost 1 (`/blog/diseno-web-mendoza/` — 55 impresiones en GSC para `'diseño web mendoza'` y `'diseño web en mendoza'`):**
    - Acortado el `<title>` de 78 a 50 caracteres (`Diseño Web en Mendoza: Precios y Google Maps 2026`), actualizado `dateModified` al 11/11/2026, inyectado Google Tag GA4 en `<head>` y sumada la 4ta FAQ interactiva (`¿Cuánto tarda el desarrollo de una página web en Mendoza y qué necesito enviar?`) con `<details name="faq-accordion">` y `FAQPage` JSON-LD.
    - Reforzado el interlinking regional con San Rafael (`/blog/diseno-web-san-rafael-mendoza/`), San Luis y Auditoría SEO.
  - **Cirugía + Boost 2 (`/blog/diseno-web-san-luis/` — 25 impresiones en GSC para `'diseño web san luis'`):**
    - Acortado el `<title>` de 77 a 52 caracteres (`Diseño Web en San Luis: Precios y Google Maps 2026`), actualizado `dateModified` al 11/11/2026, inyectado Google Tag GA4 en `<head>` y sumada la 4ta FAQ interactiva (`¿Cuánto demora hacer una página web en San Luis y qué incluye el mantenimiento?`) con `<details name="faq-accordion">` y `FAQPage` JSON-LD.
  - **Artículo Nuevo Miércoles (`/blog/diseno-web-villa-carlos-paz/` — Regla #16 1 Ciudad en Córdoba, Regla #17 0 Emojis, Regla #18 Slug de 5 palabras, Regla #19 0 Enlaces Fantasma):**
    - Publicada la guía *Diseño Web en Villa Carlos Paz: Turismo, Hoteles y Comercios* enfocada en captar turistas en el Valle de Punilla, reservas directas por WhatsApp para independizarse del 15% al 22% de comisión de Booking/Airbnb, gastronomía en Costanera y teatros.
    - Imagen editorial propia creada y cuantizada: `images/guia_diseno_web_villa_carlos_paz.png` y `public/images/guia_diseno_web_villa_carlos_paz.png` (`360 KB`).
    - Enlazada desde `/blog/diseno-web-cordoba/` y `/blog/diseno-web-villa-maria/`. Auditado el 100% de enlaces internos del proyecto (`0` rotos).
    - Alcanzadas **156 guías activas** en `/blog/index.html` (`40` en categoría Google Maps) y **174 URLs canónicas** en `sitemap.xml` / `public/sitemap.xml`.
- [x] **2026-11-11 (Kickoff del Sprint de Autoridad SEO — Publicación de 6 Guías Técnicas de Alto Nivel con Cero Canibalización):**
  - Publicado el primer batch de 6 artículos técnicos para inundar de autoridad temática a `erikwebsite.com` en Argentina y canalizar tráfico a `/auditoria-seo/`:
    1. `/blog/schema-markup-datos-estructurados-seo/` (Schema JSON-LD `LocalBusiness`, `FAQPage`, `Product`, rich snippets y AEO/GEO).
    2. `/blog/canibalizacion-palabras-clave-seo/` (Diagnóstico en Search Console, técnica de *Keyword Absorbing* y redirección 301).
    3. `/blog/link-building-menciones-prensa-argentina/` (Digital PR, notas en medios provinciales/nacionales y Brand Mentions para LLMs).
    4. `/blog/robots-txt-sitemap-xml-seo/` (Directivas User-agent, crawl budget, sitemaps limpios y prevención de bloqueos CSS/JS).
    5. `/blog/etiqueta-canonica-redireccion-301-seo/` (Resolución de "Página alternativa con canónica adecuada", cadenas 301 y prevención de duplicados).
    6. `/blog/enlazado-interno-silos-seo/` (Topic Clusters, distribución de PageRank, anchor text contextual y eliminación de páginas huérfanas).
  - Todas las 6 imágenes editoriales auténticas generadas, cuantizadas a 256 colores (`< 440 KB`) y dual-sincronizadas en `images/` y `public/images/`.
  - Cero emojis decorativos (Regla #17), slugs limpios de 4 a 5 palabras (Regla #18), cero enlaces rotos (Regla #19 — auditado con `scratch/audit_all_internal_links.py`).
  - Total actualizado: **162 guías activas** en `/blog/index.html` (19 en la categoría Especialista SEO) y **180 URLs canónicas** en `sitemap.xml` / `public/sitemap.xml`. Compilación 100% limpia en Vite (`28.94s`). Notificadas con status 200 OK a Google Indexing API v3, 202 Accepted en IndexNow y SubmitFeed en Bing.
- [x] **2026-11-12 (Ejecución del Jueves 12/11: 2 Boosts Striking Distance + Sprint Día 2 con 6 Nuevas Guías de Autoridad SEO):**
  - **Boost 1 (SEO E-Commerce Striking Distance Pos 4.7–8.0 en GSC):**
    - En `/blog/precios-comisiones-tiendanube-alternativas-argentina/`: Título acortado de 65 a 60 caracteres (`¿Tiendanube Cobra Comisión por Venta? Precios Argentina 2026`) captando la query exacta `'tiendanube cobra comision por venta'`. Inyectada la query en H2, meta description, agregada la 4ta FAQ interactiva con `<details name="faq-accordion">` y evento GA4 `faq_expand`, y actualizado `dateModified` y `FAQPage` JSON-LD.
  - **Boost 2 (Diseño Web Bariloche Pos 11.3 en GSC):**
    - En `/blog/diseno-web-bariloche/`: Título acortado de 64 a 55 caracteres (`Diseño Web en Bariloche: Sitios Profesionales y Precios`) captando la query con impresiones `'desarrollo de sitios web profesionales bariloche'`. Inyectado Google Tag GA4 faltante en `<head>`, modernizadas las FAQs con `<details name="faq-accordion">` con texto legible sobre fondo oscuro (`text-white`) y añadida 4ta FAQ con `FAQPage` JSON-LD.
  - **Sprint Día 2 — 6 Guías Nuevas de Autoridad SEO (Regla #17 0 emojis, Regla #18 slugs de 3 a 5 palabras, Regla #19 0 enlaces rotos):**
    1. `/blog/seo-medicos-clinicas-argentina/` (SEO local en Google Maps y reputación para clínicas, centros médicos y consultorios en Argentina).
    2. `/blog/seo-local-google-maps-argentina/` (Factores del algoritmo local de Google, optimización del Perfil de Negocio, citaciones NAP y reseñas).
    3. `/blog/consultor-seo-vs-agencia-argentina/` (Comparativa de honorarios mensuales, atención directa vs. pasantías, tiempos y ROI para pymes).
    4. `/blog/seo-on-page-checklist-optimizacion/` (Checklist de Title, H1-H3, slugs limpios, interlinking semántico, Core Web Vitals y Schema JSON-LD).
    5. `/blog/keyword-research-palabras-clave-argentina/` (Intenciones de búsqueda locales, modismos de compra, Google Search Console y Search Intent).
    6. `/blog/optimizar-imagenes-seo-peso-webp/` (Conversión a WebP, compresión &lt; 150 KB, dimensiones explícitas para evitar CLS y atributo alt descriptivo).
  - Todas las 6 imágenes editoriales auténticas generadas, cuantizadas a 256 colores (`< 490 KB`) y dual-sincronizadas en `images/` y `public/images/`.
  - Alcanzadas **168 guías activas** en `/blog/index.html` (25 en la categoría Especialista SEO) y **186 URLs canónicas** en `sitemap.xml` / `public/sitemap.xml`.
  - Verificados 0 enlaces rotos con `audit_all_internal_links.py`, compilación 100% limpia en Vite (`19.68s`), y notificado con status 200 OK a Google Indexing API v3, GSC Sitemap, 202 Accepted en IndexNow y 200 OK en Bing Webmaster API.
- [x] **2026-11-12 (Optimización Integral de Modo Mobile en Demos y Home):**
  - **Resolución de Colisión de Botones Flotantes y Mobile Action Dock:**
    - Se resolvió la superposición en mobile donde #btn-scroll-top (abajo a la izquierda) y el botón flotante de WhatsApp de Erik (abajo a la derecha) tapaban el dock fijo inferior (.mobile-action-dock).
    - Se configuraron los botones flotantes para elevarse armónicamente por encima del dock en mobile (ottom-20 sm:bottom-5), con tamaños más compactos y táctiles (w-10 h-10 / w-11 h-11) para no tapar los títulos ni los botones de acción de cada demo.
    - Se agregó regla global en src/styles/main.css (ody:has(.mobile-action-dock)) garantizando despeje inferior (calc(4.75rem + env(safe-area-inset-bottom))) y padding de seguridad en el pie de página (ooter pb-24 sm:pb-8).
  - **Demo de Pilates (demos/estudio-fitness/index.html):**
    - Se incorporó la barra inferior fija (mobile-action-dock) adaptada a la temática de Lumina Pilates con llamado a la acción ('Consultar Cupos'), más el botón de volver arriba y el botón flotante de WhatsApp.
  - **Demo de Fitness (demos/fitness/index.html) y Restaurante (demos/restaurante/index.html):**
    - Se sumó el botón flotante de WhatsApp integrado por encima del dock con dimensiones compactas para mobile.
  - **Barra Superior de Selector de Demos en Mobile:**
    - Se estandarizó el contenedor de pestañas en todas las demos con overflow-x-auto w-full sm:w-auto no-scrollbar py-1 y whitespace-nowrap shrink-0, evitando que las pestañas se apilen en 3 o 4 líneas verticales y asegurando un desplazamiento horizontal limpio con el pulgar.
  - **Página Principal (index.html y en/index.html):**
    - Se calibraron los botones flotantes en mobile (w-12 h-12 sm:w-14 sm:h-14) para máxima estética y ergonomía táctil sin recargar la pantalla.
