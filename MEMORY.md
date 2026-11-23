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
18. **Alineación del Slug con la Main Keyword (Regla #18 & Fórmula Sturm):** El slug de la URL debe reflejar de forma natural y exacta la Palabra Clave Principal (Main Keyword) del artículo, sin forzar un conteo artificial de palabras (puede tener 3, 4, 5 o 6 palabras según la longitud real de la consulta, ej: `/blog/conseguir-resenas-google-maps-seo/`, `/blog/seo-vs-google-ads-argentina/` o `/blog/paginas-web-logistica-transporte/`). Prohibido crear slugs kilométricos de 8 a 12 palabras con términos redundantes. **Alineación total de 4 puntos de Sturm:** La Main Keyword exacta debe estar presente en `<title>` (50 a 60 chars), slug, `<h1>`, `meta description` y en las primeras 5 a 10 palabras del texto / Direct Answer.
19. **Prohibición Absoluta de Interlinking a Páginas Inexistentes (Cero Enlaces Fantasma):**
    - Queda estrictamente prohibido colocar enlaces (`href="/..."` o `href="https://erikwebsite.com/..."`) hacia artículos, páginas de servicios, demos o herramientas que no existan físicamente en el repositorio.
    - Se puede hablar y proponer la creación de una nueva página o demo si el negocio o artículo lo amerita, o mencionar la solución en el texto ("podemos desarrollar una demo o cotizador interactivo a medida"), pero **NUNCA inventar un slug o enlace hacia una página que no hay**.
    - En cada publicación o edición se debe verificar la existencia física del archivo `.html` de destino y ejecutar `scratch/audit_all_internal_links.py` para asegurar 0 enlaces rotos.
20. **Protocolo de Propuestas Privadas y Bocetos a Clientes (`/propuestas/<nombre-cliente>/`):**
    - **Estructura de URL:** Todas las propuestas comerciales personalizadas y wireframes/bocetos previos para prospectos se alojan estrictamente bajo la ruta `/propuestas/<nombre-cliente>/` (ej: `/propuestas/inmobiliaria-raul/`, `/propuestas/alvarez-maldonado-abogados/`).
    - **Privacidad Estricta (`noindex, nofollow`):** Las páginas de propuestas deben incluir siempre `<meta name="robots" content="noindex, nofollow">` y quedar excluidas de `sitemap.xml` para no diluir el SEO del dominio con páginas efímeras o privadas de clientes.
    - **Informe de Competidores en Lenguaje 100% Natural (Cero Jerga Técnica hacia el Cliente):**
      - Por dentro el código debe tener toda la ingeniería SEO impecable (`<title>`, `<h1>`, `<h2>`, Direct Answer Sturm, `Schema.org`, paridad FAQ 1:1), pero **en la sección/lámina donde se le explica la propuesta y la comparativa de competidores al cliente queda prohibido usar jerga técnica que un dueño de negocio no entiende** (nunca hablarle de `H1`, `H2`, `Schema JSON-LD`, `DOM`, `meta description` o `KB de HTML`).
      - Traducir cada hallazgo a **lenguaje de negocio natural** (ej: *"el título principal no dice en qué ciudad atienden"*, *"no tiene resumen de presentación en Google"*, *"tienen todos los temas mezclados en una sola hoja en vez de una página dedicada para cada especialidad"*), reconociendo además con honestidad cuando un competidor tiene una buena estructura visual o presentación de servicios (como *Clavijo Abogados*), pero mostrando por qué su configuración interna para Google deja libre el primer lugar.
    - **Escala de Precios Dinámica según la Complejidad del Proyecto:**
      - **Landing Page Estándar (tipo Demos de 1 sección):** **$150.000 ARS** base (+ **$200.000 ARS** pack de 8 páginas de servicios = **$350.000 ARS**).
      - **Desarrollos Personalizados / Corporativos a Medida (ej. sistema ejecutivo interactivo estilo Moraga & Cía. con múltiples servicios integrados):**
        - **Opción 01 (Sitio Personalizado a Medida + Servicios Base):** entre **$400.000 y $500.000 ARS** (ej. **$450.000 ARS**).
        - **Opción 02 (Plataforma Completa + 8 Páginas Individuales + Posicionamiento Fino + Sección de Equipo + Blog / Datos):** entre **$800.000 y $900.000 ARS** (ej. **$850.000 ARS**).
    - **Registro Técnico:** Añadir cada propuesta a `vite.config.js` (`propuestas_<cliente>`) para garantizar su compilación limpia y empaquetado estático.
21. **Prohibición de `str.replace()` Ciego y Verificación Post-Cirugía Obligatoria (`verify_article_hygiene.py` + `git diff`):**
    - Nunca ejecutar scripts de Boost con `.replace()` sobre strings adivinados de memoria sin validar que el reemplazo efectivamente ocurrió (`assert old in html` o inspección previa del archivo). El 13/11 un `.replace()` silencioso dejó sin aplicar el Boost de nuestra URL #1 en impresiones (`/blog/como-registrar-dominio-com-ar-nic-argentina/`, 1.191 impr) mientras se marcaba como `[x] Completado`.
    - Antes de marcar cualquier artículo nuevo o Boost como completado, ejecutar obligatoriamente:
      `python scratch/verify_article_hygiene.py --hub <archivo_modificado_1> <archivo_modificado_2>`
      y verificar `git diff --stat` para confirmar que cada archivo editado realmente cambió en disco.
22. **Paridad Estricta 1:1 entre HTML `<details>` y Schema JSON-LD `FAQPage`:**
    - Cada vez que se crea un artículo o se amplían las preguntas frecuentes de un Boost (ej. de 2 a 6 FAQs), es obligatorio sincronizar el bloque JSON-LD `FAQPage` (`mainEntity`) para que tenga exactamente la misma cantidad y contenido que los `<details name="faq-accordion">` visibles en el HTML (`N == N`). Tener más o menos preguntas en Schema que en el HTML visible viola las directrices de datos estructurados de Google.
23. **Checklist Técnico Innegociable de Plantilla en Todo Artículo (`/blog/*/index.html`):**
    - Ningún artículo nuevo ni script generador puede publicarse sin incluir los 6 bloques técnicos verificados por `verify_article_hygiene.py`:
      1. Filtro de tráfico interno Capa 1 (`id="ew-internal-filter"`) en `<head>`.
      2. Google Analytics 4 (`G-KWD0WYVK4J`).
      3. Meta Pixel (`1143177121539028`) + `<noscript>` al inicio de `<body>`.
      4. Google Preferred Sources (`news.google.com/swg/js/v1/publisher.js` async + widget `<div google-add-preferred-source-btn ...>`).
      5. `<script type="module" src="/src/js/main.js"></script>` antes de `</body>` (indispensable para que funcionen los botones `data-wa-msg`, menú móvil, `whatsapp_click`, `generate_lead`, `faq_expand` y `article_read_75` — su omisión rompió las conversiones en 11 artículos del sprint del 13–14/11).
      6. Navbar unificada del blog sin `#demos` ni `#precios` (Regla #3).
24. **Taxonomía Cerrada de `data-cat` y Contadores Sincronizados en `blog/index.html`:**
    - Al registrar tarjetas en `blog/index.html`, usar exclusivamente una de las **9 claves válidas** del `<select>` de filtro: `seo`, `precios`, `maps` (incluye TODAS las provincias y ciudades), `servicios`, `negocios`, `rubros`, `redes`, `ventas` (funnels y conversión), `dominios`.
    - Queda prohibido inventar claves inexistentes como `diseno` o `geo` (dejan tarjetas invisibles al filtrar). Cada vez que se suma una tarjeta, actualizar el contador exacto de esa categoría en el `<option>`, el total en `Todas las categorías (N)` y el span `Mostrando N guías`.
25. **Límites Duros de Metadatos en Artículos/Boosts y Voseo Rioplatense Estricto:**
    - `<title>`: **50 a 60 caracteres máximo** (sincronizado con `og:title` y `twitter:title`).
    - `<h1>`: **45 a 75 caracteres máximo** (cumplimiento real de Regla #5; prohibido crear `<h1>` de 90–120 caracteres).
    - `meta description`: **135 a 158 caracteres** (sincronizado con `og:description` y `twitter:description`; obligatorio acortar también en Boosts cuando el original supera 160c).
    - **Voseo Argentino Consistente:** Redactar todo contenido en español con voseo rioplatense natural (*podés, tenés, buscás, elegís, querés*). Prohibido mezclar tuteo neutro (*puedes, tienes, quieres*) en textos o FAQs.
26. **Doble Filtro de Demanda Real + Query Fan-Out IA Antes de Planificar Keywords o Boosts:**
    - **Selección de Boosts:** Priorizar URLs con **>= 14 días de maduración** que cumplan al menos uno de estos criterios medidos en vivo: (a) tráfico real entrante de asistentes IA (`chatgpt.com`, `gemini.google.com`, `perplexity.ai` en GA4), (b) impresiones altas (`>= 25` impr en GSC) con `<title>` truncado (`> 62c`) o paridad FAQ rota, o (c) consultas comerciales en *Striking Distance* (Pos 4–20). No gastar un slot de Boost en páginas con `1` sola impresión si existen páginas maduras con `30–100+` impresiones en el mismo eje.
    - **Selección de Artículos Nuevos:** Nunca elegir temas "de memoria". Toda keyword nueva debe superar: (1) `check_cannibalization.py` **< 60%** (nunca ≥ 70%), (2) demanda real verificada en los CSVs de Google Ads o **>= 4 sugerencias en Google Argentina Autocomplete** (`suggestqueries.google.com?gl=ar&hl=es-419`), y (3) inclusión explícita en el outline de un bloque de **Preguntas IA / Query Fan-Out** con las consultas conversacionales exactas que un usuario argentino le hace a ChatGPT/Perplexity/Google AI y las entidades numéricas concretas (precios en ARS, entes locales como ARCA/NIC.ar/Mercado Pago, tiempos reales) que habilitan citación GEO.
27. **Sincronización Obligatoria de `llms.txt` y `public/llms.txt`:**
    - Mantener `llms.txt` y `public/llms.txt` idénticos y actualizados cada vez que se lanza una demo nueva (ej. `/demos/arquitectura/`, `/demos/contable/`) o se publica un lote relevante de guías pilares. Verificar con `verify_article_hygiene.py --hub` que no contenga URLs inexistentes (404).
28. **Clave Oficial Única de IndexNow (`e7a9c4b2f8d143e6a0b5c8d9e2f1a3b4`) y Redirecciones HTTP `301` Reales (`public/_redirects`):**
    - El archivo de verificación físico en producción es `public/e7a9c4b2f8d143e6a0b5c8d9e2f1a3b4.txt`. Nunca hardcodear otra clave en scripts de notificación (enviar una clave distinta genera `404` / `Code4xx` en Bing Webmaster Tools y anula la indexación instantánea).
    - Todas las redirecciones de URLs retiradas o combinadas deben declararse como `301` reales a nivel servidor en `public/_redirects` (Cloudflare Pages), no solo con `<meta http-equiv="refresh">`.
29. **Integridad Estricta de Teléfono Oficial Único (`5492645185359`), Botones WhatsApp y Meta Pixel Sin Doble Disparo:**
    - **Regla de Oro de Teléfono Oficial (Obligatoria antes de cada commit/deploy):** En TODA página pública de Erik Website (`index.html`, `/en/`, `/san-juan/`, `/auditoria-seo/`, `/blog/*`, `/demos/*`), el ÚNICO número telefónico permitido en `wa.me/`, `data-wa-phone` y `Schema.org telephone` es **`5492645185359`**. Jamás copiar ni reutilizar teléfonos de otros proyectos, plantillas viejas ni demos externas (excepción exclusiva: `/propuestas/<cliente>/` noindex donde va el teléfono del prospecto). `verify_article_hygiene.py` bloquea automáticamente cualquier teléfono diferente.
    - Todo botón de WhatsApp debe usar `<a href="https://wa.me/5492645185359?text=...">` o `<button data-wa-msg="..." data-wa-phone="5492645185359">` (prohibido usar `data-wa-lead` sin `data-wa-msg`, aunque `src/js/whatsapp.js` ya tiene soporte de respaldo).
    - `src/js/whatsapp.js` es la única fuente de verdad para disparar `fbq('track', 'Contact')`, `generate_lead` y `whatsapp_click` respetando `window._ewIgnoreAnalytics`. Prohibido duplicar listeners inline (`trackCustom', 'Whatsapp'`) y obligatorio envolver `gtag('config')` y Microsoft Clarity dentro de `if (!window._ewIgnoreAnalytics)`.
30. **Estética Editorial Clara Unificada en Todo el Blog (Cero Modo Oscuro No Aprobado) y Prohibición de Enlazar Redirect Stubs:**
    - El 100% de los artículos del blog (`/blog/*/index.html`) debe usar la plantilla editorial **CLARA** (`bg-[#fafafa]` / `bg-slate-50` con texto oscuro legible, dejando el bloque CTA final y el footer global en oscuro). Queda prohibido crear o mantener artículos del blog con fondo oscuro `bg-neutral-950` (nunca aprobado por el usuario). `verify_article_hygiene.py` bloquea automáticamente `bg-neutral-950`.
    - Prohibido colocar enlaces internos hacia páginas stub de redirección (`/demos/taller/`, `/demos/inmobiliaria/`, `/demos/veterinaria/`, `/blog/diseno-web-rosario-santa-fe/`, etc.). Enlazar únicamente a URLs canónicas activas.

---

## 🗄️ Decisiones de Arquitectura
- **Estrategia SEO + AEO + GEO:** Cada artículo del blog incorpora un bloque superior de **Respuesta Directa** (40–60 palabras para citación en Google AI Overviews, ChatGPT Search, Perplexity y Grok), encabezados `<h2>` formulados como preguntas reales de usuarios/IA (*Query Fan-Out*), tablas comparativas HTML y marcado estructurado `Schema.org` (`BlogPosting`, `BreadcrumbList`, `FAQPage`).
- **Protocolo Operativo Semanal Híbrido (Planificación High Reasoning ➔ Ejecución Ágil):**
  - **Domingo / Revisión Estratégica (Modelo High Reasoning):** Auditoría semanal (GSC, Bing, GA4, SerpBear) y resolución de los **Pasos 1 y 2 para toda la semana** (Lunes a Sábado): detección de canibalización (< 60%), validación de demanda en Google AR Autocomplete + CSVs, asignación de Boosts/H2 sobre páginas maduras (>= 14 días) y diseño de **Outlines maestros cerrados** (Título ≤ 60c, slug alineado a la Main Keyword, H1 ≤ 75c, Meta Description 135–158c, Direct Answer Sturm en primeras 5–10 palabras, bloque de Preguntas IA / Query Fan-Out, categoría `data-cat` válida, H2s, interlinking verificado en disco y 6 FAQs con paridad 1:1).
  - **Lunes a Sábado (Modelo Ejecutor Ágil):** Ejecución de los **Pasos 3 y 4** de cada día apegada al outline maestro, imágenes PIL cuantizadas (`< 490 KB` dual-sync), validación automática obligatoria con `python scratch/verify_article_hygiene.py --hub <archivos>`, auditoría de enlaces (`scratch/audit_all_internal_links.py`), `git diff --stat`, compilación limpia en Vite (`npm run build`), notificaciones a Google Indexing API v3 / GSC Sitemap / IndexNow / Bing y `git push origin main`.
- **Scripts Locales de Calidad y Fan-Out:** `scratch/free_alsoasked_ai_fanout.py` (autocompletado y preguntas Google Argentina `gl=ar`), `scratch/check_cannibalization.py` (solapamiento y Boost), `scratch/audit_all_internal_links.py` (0 enlaces rotos) y `scratch/verify_article_hygiene.py` (puerta de calidad técnica Reglas #3, #5, #7, #12, #13, #17, #22–#27).

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
- [x] **2026-11-13 (Ejecución del Viernes 13/11: 2 Boosts Cirugías + Sprint Día 3 con 6 Nuevas Guías de Autoridad SEO y Diseño Web B2B):**
  - **Boost 1 (Dominio .ar y .com.ar con 395 impresiones en GSC):**
    - En `/blog/como-registrar-dominio-com-ar-nic-argentina/`: Título acortado a 53 caracteres (`Comprar Dominio .ar y .com.ar en NIC Argentina 2026`) absorbiendo las queries `'comprar dominio .ar'` y `'registro de dominios .ar'`. Inyectadas en H2, meta description, agregada la 4ta FAQ interactiva con `<details name="faq-accordion">` y evento GA4 `faq_expand`, y actualizado `dateModified` y Schema `FAQPage`.
  - **Boost 2 (Empresas de Limpieza con 71% de solapamiento de intención):**
    - En `/blog/paginas-web-empresas-limpieza-finales-obra-tapizados/`: Título acortado a 55 caracteres (`Páginas Web para Empresas de Limpieza en Argentina 2026`) absorbiendo en H2 y FAQs el cluster de *Abonos Corporativos de Limpieza para Oficinas y Consorcios: Cómo Captar Clientes B2B*, con `dateModified` actualizado.
  - **Sprint Día 3 — 6 Artículos Nuevos (Regla #17 0 emojis, Regla #18 slugs de 3 a 5 palabras, Regla #19 0 enlaces rotos):**
    1. `/blog/paginas-web-logistica-transporte/` (Webs para logística, distribución, transporte de carga pesada, cotizador online y tracking de envíos B2B).
    2. `/blog/presupuesto-diseno-web-argentina/` (Qué debe incluir un presupuesto profesional: alcance, Core Web Vitals, hosting, dominio y analítica GA4).
    3. `/blog/seo-internacional-etiqueta-hreflang-argentina/` (Guía de rel="alternate" hreflang="es-AR", subdirectorios vs ccTLD y prevención de duplicados regionales).
    4. `/blog/crawl-budget-optimizacion-rastreo-google/` (Optimización del presupuesto de rastreo de Googlebot, tiempo de respuesta de servidor y sitemaps limpios).
    5. `/blog/migracion-web-seo-redirecciones-301/` (Migración web SEO sin pérdida de tráfico, mapeo 301 individual, auditoría pre y post lanzamiento en GSC).
    6. `/blog/seguridad-web-certificados-ssl-https/` (Certificados SSL/TLS, protocolo HTTPS, HSTS, prevención de cartel 'No seguro' y factor de ranking en Google).
  - Todas las 6 imágenes editoriales generadas, cuantizadas a 256 colores (`< 490 KB`, entre 376 KB y 447 KB) y dual-sincronizadas en `images/` y `public/images/`.
  - Total actualizado: **174 guías activas** en `/blog/index.html` y **192 URLs canónicas** en `sitemap.xml` / `public/sitemap.xml`.
  - Verificados 0 enlaces rotos con `audit_all_internal_links.py`, compilación 100% limpia en Vite (`8.05s`, `0 errores`), y notificado con status 200 OK a Google Indexing API v3 (9 URLs), GSC Sitemap, 202 Accepted en IndexNow y 200 OK en Bing Webmaster API.
- [x] **2026-11-14 (Ejecución del Sábado 14/11: Protocolo Híbrido Argon High + Flash 3.8 High · 2 Boosts + Cierre del Sprint con 6 Nuevos Artículos):**
  - **Fase Estratégica (Argon High):** Auditoría de canibalización (0% solapamiento), selección de 2 Boosts con altas impresiones en GSC y redacción de 6 Outlines maestros cerrados.
  - **Fase de Redacción y Despliegue (Flash 3.8 High):**
    - **Boost 1 (`/blog/dominio-com-vs-com-ar-cual-conviene-argentina/` — 239 impr en GSC):** `<title>` acortado a 54 chars (`Dominio .com vs .com.ar y .ar: ¿Cuál Conviene en 2026?`), añadido H2 #4 sobre diferencias entre `.com.ar`, `.ar` y `.com`, expandido a 6 FAQs interactivas con GA4 tracking y Schema `FAQPage`.
    - **Boost 2 (`/blog/como-crear-correo-corporativo-dominio-propio-gmail/` — 201 impr en GSC):** `<title>` acortado a 56 chars (`Correo con Dominio Propio en Gmail: Cómo Crearlo en 2026`), añadido H2 #4 con checklist de SPF, DKIM y DMARC anti-spam, expandido a 6 FAQs interactivas con GA4 tracking y Schema `FAQPage`.
    - **Sprint Día 4 — 6 Artículos Nuevos (5 palabras exactas, 6 FAQs interactivas cada uno, 0 emojis, 0 enlaces rotos):**
      1. `/blog/conseguir-resenas-google-maps-seo/` (Estrategias de reseñas locales, link directo, QR físico en locales y ranking en Local Pack).
      2. `/blog/seo-vs-google-ads-argentina/` (Comparativa comercial, ROI, tiempos, costos por clic, impuestos y estrategia híbrida).
      3. `/blog/seo-b2b-empresas-industriales-argentina/` (SEO industrial para jefes de compras, especificaciones técnicas, normas y catálogos HTML).
      4. `/blog/actualizar-contenido-antiguo-seo-google/` (Detección de Content Decay en Search Console, refresh de contenido y señales de freshness).
      5. `/blog/eeat-google-autoridad-confianza-seo/` (Marco E-E-A-T, directrices YMYL, autoría real verificada y Schema de entidad para LLMs).
      6. `/blog/mejorar-ctr-organico-titulos-google/` (Optimización de CTR, títulos magnéticos de 50 a 60 caracteres y prevención de truncamiento).
    - Todas las 6 imágenes editoriales generadas, cuantizadas a 256 colores (`< 490 KB`, peso real 364–439 KB) y dual-sincronizadas en `images/` y `public/images/`.
    - **Inventario Actualizado:** **180 guías activas** en `/blog/index.html` (41 en Google Maps y 33 en Auditoría SEO) y **198 URLs canónicas** en `sitemap.xml` / `public/sitemap.xml`.
    - Auditoría de enlaces 100% limpia (0 enlaces rotos), `npm run build` en 8.57s con 0 errores y notificaciones exitosas a Google Indexing API v3 (`200 OK`), GSC Sitemap, IndexNow (`202 Accepted`) y Bing Webmaster API (`200 OK`).
- [x] **2026-11-14 (Nueva Demo Integral para Estudios de Arquitectura, Reformas & Consorcios `/demos/arquitectura/`):**
  - **Motivación y Caso Comercial:** Respuesta calificada al prospecto de CABA (`aireyluzarquitectura.com`, +54 9 11 3642-0064) requiriendo experiencia demostrable, portfolio estético, velocidad móvil superior frente a su WordPress obsoleto con Visual Composer en GoDaddy y captación en remodelaciones + consorcios (Ley 257).
  - **Desarrollo Integral de la Demo (`/demos/arquitectura/index.html` y `demos/arquitectura/app.js`):**
    - **Identidad:** *"VÉRTICE · Arquitectura & Gestión de Obras"* (CABA y GBA, Matrícula CPAU / CAPBA).
    - **Portfolio Filtrable (8 Casos de Estudio):** Filtros instantáneos en JS (`Todos`, `Residencial`, `Remodelaciones`, `Consorcios & Ley 257`, `Comercial & Oficinas`), cada uno con badges técnicos (Ubicación, Superficie, Plazo) y Modal interactivo de Ficha Técnica con memoria descriptiva y CTA directo a WhatsApp.
    - **Slider Interactivo Antes / Después (Before & After):** Componente táctil y con mouse que permite deslizar y comparar la demolición inicial vs departamento remodelado terminado en Palermo.
    - **Segmentación de 3 Unidades de Negocio:** 1) Residencial & Reformas Integrales, 2) Consorcios, Edificios & Ley 257 (informes, fachadas, balcones y obras de gas con matriculado), 3) Locales Comerciales & Oficinas (habilitaciones express AGC).
    - **Cotizador de Obra Interactivo:** Selector de tipo de obra, m², ubicación en CABA/GBA y modalidad llave en mano con previsualización dinámica del mensaje para WhatsApp.
    - **FAQ Acordeón y Footer Global:** Acordeones `<details name="faq-accordion">` y footer de 2 niveles mobile-first.
  - **Build & Registro:** Actualizado `vite.config.js` (`demo_arquitectura`), incorporado a `sitemap.xml` y `public/sitemap.xml` (**199 URLs canónicas**), compilación en Vite validada en 5.63s (`0 errores`) y commit + git push a GitHub.
  - **Rediseño Radical de Arquitectura Estilo Aconif.com (`/demos/arquitectura/`):**
    - **Inspiración y Estructura 1:1 con Aconif:** Superando la versión preliminar que se asemejaba a la anterior, se implementó una reconstrucción total basada en la anatomía real de Aconif.com:
      1. **Tipografía Global Montserrat (300 a 900):** Estética editorial limpia de estudio de arquitectura de alta gama.
      2. **Paleta y Gradientes Aconif:** Fondo dark ink `--bg-dark: #0c120d`, acento lima `--a-lime: #7cda24`, verde salvia `--a-sage: #abcb67` y gradiente de texto `.ac-keyword` (`linear-gradient(135deg, #7cda24 0%, #abcb67 55%, #fff 120%)`).
      3. **Hero Cinemático a Pantalla Completa:** Background full-bleed con efecto sutil Ken Burns (`scale(1.05)`), gradiente oscuro superior/inferior, kicker pulsante con indicador verde (`Buenos Aires · Desde 2014 · Matrícula CPAU & DGFYCO`), titular monumental de dos líneas, botón píldora blanco de alto contraste con pastilla negra y flecha lima (`ac-btn-hero`), y tarjeta flotante de obra (`.ac-vcard`) en la esquina inferior derecha.
      4. **Sección Statement con Métricas Monumentales (`.ac-statement`):** *"La confianza no se comunica. Se construye."* con 4 números gigantes (`12` años en CABA, `100%` presupuesto cerrado por contrato, `52` consorcios Ley 257 y `< 48h` visita de relevamiento in situ).
      5. **Sección "Dónde Intervenimos" (`.ac-donde`):** Organización en filas horizontales numeradas con hover/active (`01 Palermo / Colegiales`, `02 Recoleta / Barrio Norte`, `03 Belgrano / Núñez`, `04 Consorcios CABA`) detallando tipologías y volumen de obras ejecutadas.
      6. **Slider Antes / Después Integrado:** Cocina clásica porteña de los 80s vs cocina contemporánea con isla y cuarzo Calacatta, operado por slider táctil/mouse con etiquetas Aconif-styled.
      7. **Obras / Portfolio (`.ac-casas`):** Grid de 8 proyectos con filtros dinámicos, chips de categoría, metros cuadrados, ubicación y modal con memoria técnica.
      8. **Servicios & Consorcios (`.ac-servicios`):** 3 bloques numerados de especialidad y sección dedicada a Administradores de Consorcios con certificación DGFYCO.
      9. **Cotizador Interactivo & FAQ:** Acordeones y cotizador adaptados con la paleta dark ink y acentos lima.
    - **Validaciones:** Compilación en Vite limpia en 6.60s (`dist/demos/arquitectura/index.html 91.22 kB`), 0 enlaces rotos (`audit_all_internal_links.py`), 0 emojis decorativos (Regla #17), imágenes WebP dual-sincronizadas (Regla #12) y push obligatorio a GitHub (Regla #15).
  - **Iteración 2 Arquitectura Aconif (Ritmo Dual Blanco/Negro, Scroll Reveal & Arreglo Slider):**
    - **Ritmo Dual-Tone de Alto Contraste (Blanco & Dark Ink):** Siguiendo la referencia de Aconif donde el sitio no es un bloque negro monótono sino que alterna fondos con estética de revista de arquitectura:
      1. *Hero & Statement:* Dark Ink `#0c120d`.
      2. *Obras / Portfolio (`#obras`):* Blanco puro (`bg-white` / `#ffffff`) con tipografía carbón oscuro (`#111827`), tarjetas de obra nítidas con sutil sombra y pestañas de filtro invertidas (`bg-[#0c120d] text-white`).
      3. *Dónde Intervenimos (`#donde`):* Dark Ink `#0c120d` para contraste rítmico.
      4. *Servicios (`#servicios`):* Off-White (`#f9f9f7` / `--bg-light-alt`), tarjetas blancas con bordes limpios y acentos verdes.
      5. *Consorcios (`#consorcios`):* Tarjeta monumental oscura `#0c120d` dentro de contenedor claro.
      6. *Cotizador:* Dark Ink `#0c120d`.
      7. *FAQ:* Off-White `#f9f9f7` con tarjetas blancas.
    - **Scroll Reveal Fluido a 60 FPS (GPU-Accelerated):** Implementado con transiciones CSS nativas (`cubic-bezier(0.2, 0.7, 0.2, 1)`, traslación de 28px o escala sutil a 0.96) y un `IntersectionObserver` ligero que ejecuta `unobserve()` al instante en cada elemento visible, garantizando carga instantánea (100/100 en Core Web Vitals) y cero impacto en velocidad móvil.
    - **Solución al Colapso de Letras en el Slider Antes/Después:** El badge de "Antes" colapsaba en columna vertical de una sola palabra al arrastrar el manejador a la izquierda porque el contenedor recortado `#ba-layer` forzaba el salto de línea. Se solucionó incorporando `whitespace-nowrap w-max max-w-none select-none pointer-events-none` y control programático de opacidad en `app.js` (`opacity: 0` suave cuando el tirador pasa por debajo del 22% en "Antes" o por encima del 78% en "Después").
    - **Integración de Footer Comercial y Precios Erik Website (`#erikwebsite-cta`):** Se incorporó la sección promocional oficial de erikwebsite.com ($150.000 ARS setup, $20.000 ARS/mes, 1º mes gratis, 3 a 5 días de entrega y WhatsApp sin teléfono en el botón según Regla #2), seguida por el footer oficial (`Erik Website • San Juan, Argentina`) y el botón flotante `#btn-scroll-top`.
    - **Verificaciones:** Compilación exitosa en Vite (5.76s), 0 enlaces rotos, 0 emojis y commit + git push a GitHub.
- [x] **2026-11-15 (Comando Estratégico Dominical #2 — Auditoría Semana 2 + Pasos 1 y 2 en Argon High para Lunes 16/11 a Sábado 21/11):**
  - **Crecimiento Semanal Auditado (`sunday_seo_command.py` — Semana 2 vs. Semana 1):**
    - **Google Search Console (28d):** Las impresiones saltaron de `1.434` a **`3.310` (+130,8% en 7 días)**; los clics orgánicos subieron de `6` a **`7`** (`/blog/por-que-mi-pagina-web-no-aparece-en-google-como-indexar/` consiguió su primer clic orgánico); las consultas en *Striking Distance* (Pos 4.0 a 20.0) crecieron de `23` a **`37` (+60,9%)**, y `/blog/como-crear-catalogo-online-pedidos-whatsapp/` entró al Top 10 del sitio con **`200` impresiones en Posición `11.6`**.
    - **Bing Webmaster Tools (API + IndexNow):** Las páginas indexadas (`InIndex`) subieron de `6` a **`10` (+66,7%)**, las páginas rastreadas en 7 días saltaron de `13` a **`42` (+223,1%)** y `0` errores de rastreo.
    - **Google Analytics 4 (Primera semana completa de eventos personalizados en vivo):** `4` conversiones `generate_lead` / `whatsapp_click` (`3` usuarios), `18` lecturas profundas `article_read_75` (`7` usuarios), `9` aperturas `faq_expand` (`2` usuarios) y **90,9% de Engagement Rate** en el canal `Organic Search` (`10/11` sesiones).
  - **Ejecución de Pasos 1 y 2 Completos en Argon High para Toda la Semana 2 (Lunes 16/11 al Sábado 21/11) en `PLAN_SEMANAL_SEO.md`:**
    - Respetando la **Regla de Maduración (14+ días)**, no se tocan los artículos recientes del Sprint SEO; todos los Boosts de la semana apuntan a guías maduras de **Diseño Web, NIC.ar, Comparativas BoFu, Ciudades y Arquitectura**, tejiendo además la nueva **Demo de Arquitectura (`/demos/arquitectura/`)**:
      1. **Lunes 16/11:** Boost `/blog/como-crear-catalogo-online-pedidos-whatsapp/` (Pos 11.6, 200 impr) + Nuevo `/blog/paginas-web-mueblerias-fabricas-muebles/`
      2. **Martes 17/11:** Doble Boost Diseño Web Maduro (`/blog/como-delegar-dns-renovar-dominio-nic-argentina/` Pos 6.9, 78 impr + integración de `/demos/arquitectura/` en `/blog/paginas-web-constructoras-desarrolladoras-arquitectura-argentina/` y `/blog/portfolio-web-arquitectos-estudios-de-arquitectura/`) + Nuevo SEO `/blog/google-tag-manager-vs-ga4-seo/`
      3. [x] **Miércoles 18/11 (Completado):** Boost `/blog/diseno-web-zona-sur/` (Pos 9.0–19.5 en 5 queries comerciales + enlace a `/demos/arquitectura/`) + Nuevo `/blog/diseno-web-lujan/` (Regla #16)
      4. **Jueves 19/11:** Doble Boost Comparativas Diseño Web Maduras (`/blog/precios-shopify-argentina-conviene/` 34 impr + `/blog/hacer-landing-page-canva-sirve-para-vender/` Pos 6.0, 22 impr) + Nuevo SEO `/blog/seo-hoteles-cabanas-turismo-argentina/`
      5. **Viernes 20/11:** Doble Boost Herramientas & Cotizador (`/blog/generador-link-qr-whatsapp-gratis/` 50 impr + `/blog/cotizador-online-whatsapp-vs-carrito-compras-tradicional/` Pos 10.0 integrando el Cotizador de Obra de `/demos/arquitectura/`) + Nuevo Diseño Web `/blog/paginas-web-administracion-consorcios-countries/` (conectado a la sección *Consorcios & Ley 257* de `/demos/arquitectura/`)
      6. **Sábado 21/11:** Doble Boost Ciudades Maduras (`/blog/diseno-web-rosario/` 35 impr + `/blog/diseno-web-santa-fe/` 32 impr, integrando `/demos/arquitectura/`) + Nuevo SEO Local `/blog/estadisticas-google-business-profile-maps/`
  - **Implementación Global de Filtro de Tráfico Interno para GA4, Clarity y Meta Pixel (`id="ew-internal-filter"` en las 214 páginas activas):**
    - Desactiva automáticamente GA4 (`window['ga-disable-G-KWD0WYVK4J'] = true` y bloqueo de `gtag.js`), Microsoft Clarity y Meta Pixel (`PageView` y `Contact`) en `localhost`/`127.0.0.1` y en cualquier navegador donde se abra una sola vez `https://erikwebsite.com/?soy_erik=1` (guardando `localStorage.setItem('ew_ignore_analytics', '1')` con banner visual de confirmación; reversible con `?soy_erik=0`).
    - Se inyectó además la etiqueta GA4 (`G-KWD0WYVK4J`) en las 26 guías iniciales del blog que no la tenían y se reparó el `<title>` escapado en `<head>` de los 6 artículos del sábado 14/11.
- [x] **2026-11-15 (Auditoría UI/UX & Rediseño Contextual con `design-master` en `index.html`):**
  - **Coherencia y Tono de Voz Comercial:**
    - Se refinó el titular H2 de la sección `#precios` que utilizaba una traducción literal e informal del framework de Alex Hormozi (*"Una propuesta donde sería estúpido decir que no"*), sustituyéndolo por un titular comercial de alta autoridad y persuasión: *"Una propuesta transparente donde todo el trabajo técnico queda resuelto"*.
    - Se profesionalizó el badge de oferta de precios (`Oferta Grand Slam • Todo Resuelto` -> `Propuesta Completa • Llave en Mano`) y se ajustó el mensaje predeterminado de WhatsApp para prospectos serios (`data-wa-msg`).
    - Se aclaró el badge de ahorro en el desglose de precios (`Ahorro Total de $210.000 ARS` frente al valor completo de $360.000 ARS de componentes y bonos combinados).
  - **Refinamiento de Iconografía y UI Craft (Regla #17):**
    - Se erradicaron los caracteres de texto plano `✕` y `✓` en la comparativa de `#solucion`, reemplazándolos por iconos vectoriales SVG inline de 16x16px ultra nítidos y accesibles (`stroke-width="2.5"`).
    - Se reparó el enlace vacío `<a href="#">` en el pie de página global, reemplazándolo por `<a href="/" aria-label="Ir al inicio de erikwebsite.com">`.
  - **Verificaciones:**
    - Compilación en Vite exitosa en 15.80s con 0 errores.
    - Auditoría de enlaces internos (`scratch/audit_all_internal_links.py`) con 0 enlaces rotos.
    - Verificación estricta de Regla #17: 0 emojis decorativos en todo el documento.
- [x] **2026-11-16 (Integración Global del Módulo Google Preferred Source en todo el Blog):**
  - **Script Asíncrono Oficial:** Integrado `https://news.google.com/swg/js/v1/publisher.js` con carga `async` en `<head>` en las 181 guías de `/blog/` (pautas de `modern-web-guidance` para no penalizar LCP ni INP).
  - **Módulo Visual Hallmark:** Diseñado e insertado al pie de cada artículo con isotipo SVG oficial de Google, badge de *Google Search & AI Overviews*, copy de autoridad y el contenedor interactivo `<div google-add-preferred-source-btn data-theme="light" data-lang="es"></div>`.
  - **Impacto AEO / GEO:** Permite a lectores fidelizados marcar `erikwebsite.com` como fuente preferida, habilitando la etiqueta «Preferida» en AI Overviews y mayor frecuencia en Top Stories / Google Discover.
  - **Verificaciones:** Compilación en Vite en 5.98s con 0 errores y 0 enlaces rotos (`audit_all_internal_links.py`).
- [x] **2026-11-16 (Ejecución de Lunes 16/11 — Eje Diseño Web y Conversión):**
  - **Boost Striking Distance en `/blog/como-crear-catalogo-online-pedidos-whatsapp/`:**
    - `<title>` optimizado de 76 a **54 caracteres**: `Cómo Crear un Catálogo Online con Pedidos por WhatsApp`.
    - `meta description` actualizada (157 chars) y Direct Answer Sturm ajustado en las primeras 10 palabras integrando `catálogo digital para WhatsApp` y `catálogo de venta por WhatsApp`.
    - Incorporada nueva Sección 4 con tabla comparativa HTML responsiva: `4. Catálogo Digital en WhatsApp vs. Catálogo en PDF: Qué Convierte Más en Argentina`.
    - Ampliado de 2 a **6 FAQs interactivas** (`<details name="faq-accordion">` con evento GA4 `faq_expand`) + Schema `FAQPage` y `dateModified: 2026-11-16T10:30:00-03:00`.
  - **Nuevo Artículo de Nicho Comercial en `/blog/paginas-web-mueblerias-fabricas-muebles/`:**
    - Main Keyword: `Páginas web para mueblerías y fábricas de muebles` (5 palabras exactas, slug alineado a Regla #18).
    - `<title>` de **54 caracteres**, `<h1>` con cotizador y catálogo, `meta description` de 154 caracteres y Direct Answer Sturm en primeras 8 palabras.
    - 4 secciones `<h2>`, tabla comparativa HTML (*Solo Instagram/Facebook* vs *E-commerce tradicional con comisiones* vs *Catálogo Web + Cotizador a WhatsApp por $150.000 ARS*).
    - 6 FAQs interactivas con GA4 tracking y marcado `Schema.org` (`BlogPosting`, `BreadcrumbList`, `FAQPage`).
    - Fotografía editorial auténtica procesada con PIL (`guia_paginas_web_mueblerias_fabricas_muebles.png`, 383.1 KB, sincronizada en `images/` y `public/images/`).
    - Añadido a `blog/index.html` (**181 guías activas**), `vite.config.js`, `sitemap.xml` y `public/sitemap.xml` (**200 URLs canónicas**).
  - **Infraestructura y Notificaciones:**
    - 0 enlaces rotos (`audit_all_internal_links.py`).
    - Build exitoso en Vite (`npm run build`) en 10.91s con 0 errores.
    - Notificaciones enviadas: Google Indexing API v3 (`200 OK` en ambas URLs), GSC sitemap enviado con éxito, IndexNow API (`202 Accepted`), Bing Webmaster API (`200 OK`).
  - **Filtro de Tráfico GA4:** Capa 1 (`id="ew-internal-filter"` client-side con `?soy_erik=1` y `localhost`) activa en las 214 páginas bloqueando de inmediato los eventos de GA4 y Meta Pixel de la navegación de Erik. Reportado diagnóstico de Capa 2 (Google Analytics Admin API deshabilitada en el proyecto de GCP `483493239372`, mientras que Google Analytics Data API para reportes opera normalmente).
- [x] **2026-11-16 (Arquitectura y Plantilla de Propuestas Privadas `/propuestas/<cliente>/` — Regla #20):**
  - Creación del directorio y plantilla base `propuestas/template/index.html` con `<meta name="robots" content="noindex, nofollow">` y filtro `id="ew-internal-filter"`.
  - Diseñado con barra superior de propuesta exclusiva (`Propuesta y Boceto Exclusivo para [Cliente] · Validez 7 días`), banner de advertencia de borrador preliminar, hero y servicios del cliente, tarjeta de alcance llave en mano ($150.000 ARS setup, 5 días de entrega, 50/50 pago) y botón de aprobación directa a WhatsApp.
  - Vinculado en `vite.config.js` (`propuestas_template`), compilado en Vite en 9.75s con 0 errores y 0 enlaces rotos (`audit_all_internal_links.py`).
- [x] **2026-11-16 (Rediseño Estructural Completo de SEGU24 — Enfoque Cliente Real + Pitch ErikWebsite):**
  - **Reestructuración Conceptual Total:** Se eliminó el formato de "página de ventas invasiva" en el cuerpo de la web. Ahora el 85% superior es una **plataforma web completa y realista para SEGU24** inspirada en las mejores empresas de seguridad de Argentina (*maxmonitoreo.com.ar*, *x-28.com*, *uss.com.ar*).
  - **Estética Corporativa y Paleta Limpia:** Fondo blanco institucional (`bg-white` y `bg-slate-50`), textos oscuros de alta legibilidad (`text-slate-900`), acentos en el dorado/amarillo de seguridad de SEGU24 (`#fdc60e`), y fotografías reales optimizadas en WebP (central operativa en Chacabuco, alarmas residenciales, videovigilancia CCTV y monitoreo rural de campos y silos).
  - **Secciones de la Web del Cliente:**
    - Top bar corporativo (Santa Fe 211, Chacabuco, 24hs, 0810-999-9629).
    - Header con logo oficial y navegación completa (*Inicio*, *Hogar*, *Comercios*, *Seguridad Rural*, *CCTV*, *App Móvil*, *Nosotros*, *Contacto*).
    - Hero principal con foto real de operadores y propuesta de valor local.
    - Protocolo de 4 pasos (*Relevamiento*, *Instalación*, *Monitoreo*, *Respuesta*).
    - Grilla de 3 soluciones con fotografías editoriales y bullets claros.
    - Sección de control remoto vía App Móvil (SmartPanics / Alonso).
    - Sección sobre la trayectoria local desde 2007 fundada por Rubén Barrón con foto real de la central física.
    - Canales de contacto directos y Footer oficial de SEGU24.
  - **Subpágina Rural Optimizada (`/propuestas/segu24/seguridad-rural-campos/`):** Landing de servicio completa con formato SEO (H1 y H2s para búsqueda local de campos, silos y estancias en Chacabuco), fotos de campo/solar, 4 pilares tecnológicos, FAQs del productor y canales de contacto.
  - **Sección de Pitch & Precios de ErikWebsite (Al Pie y Claramente Diferenciada):**
    - Ubicada estrictamente al final, tras el cierre del footer de SEGU24.
    - Con los colores oficiales de **Erik Website (Blanco + Verde Esmeralda `#16a34a` / `#15803d`)**.
    - Explicación concisa de por qué dejar Wix (velocidad en 0.8s, contacto móvil en 1 toque y SEO limpio).
    - Paquetes claros: Plan Base Home ($150.000 ARS) y Plan Integral con 8 Páginas SEO ($350.000 ARS). Páginas individuales a $30.000 ARS c/u o en bloques recurrentes de a 8 páginas por $200.000 ARS ($25.000 c/u, ahorran $40.000 frente al costo individual de $240.000). Mantenimiento mensual $20.000/mes (mes 1 bonificado) y rediseño de página aprobada a $30.000.
    - Footer de Segu24 incluye atribución limpia: `Página creada por Erik Website` con link a `https://erikwebsite.com`.
    - Cabecera simplificada con dropdown de `Servicios` (*Alarmas Hogar*, *Comercios*, *Seguridad Rural*), `App Móvil` y `Nosotros & Contacto` (eliminados badges y botones redundantes).
    - Reemplazado azul navy por el tono de grafito carbón `#373435` / `#242223` del logo oficial de SEGU24.
  - **Verificaciones:** Compilación exitosa en Vite (`npm run build`), 0 enlaces rotos (`audit_all_internal_links.py`), 0 emojis (Regla #17), `noindex, nofollow` estricto (Regla #20).
- [x] **2026-11-17 (Semana 2 · Martes 17/11 — Eje Especialista SEO, Velocidad e IA):**
  - **Boost 1 (`/blog/como-delegar-dns-renovar-dominio-nic-argentina/` — Pos `6.9` y `78` impr en GSC):**
    - `<title>` acortado de 96 a **56 caracteres**: `Cómo Delegar Dominio en NIC Argentina y Renovar .com.ar`.
    - Ampliado de 2 a **6 FAQs interactivas** (`<details name="faq-accordion">` con evento GA4 `faq_expand`) + Schema `FAQPage` y `dateModified: 2026-11-17T09:30:00-03:00` cubriendo estado *"No Delegado"*, cambio a DNS de Cloudflare y tiempos de propagación.
  - **Boost 2 (`/blog/paginas-web-constructoras-desarrolladoras-arquitectura-argentina/` y `/blog/portfolio-web-arquitectos-estudios-de-arquitectura/`):**
    - Acortados `<title>` a **57 caracteres** (`Páginas Web para Constructoras y Estudios de Arquitectura`) y **49 caracteres** (`Portfolio Web para Arquitectos y Obras: Guía 2026`).
    - Agregado en ambas guías el bloque destacado de prueba en vivo hacia la nueva **Demo Interactiva `/demos/arquitectura/`** (*VÉRTICE · Arquitectura & Gestión de Obras*), destacando el portfolio filtrable, el slider interactivo antes/después, consorcios y cotizador de m² a WhatsApp.
    - Ampliado a **6 FAQs interactivas** con Schema `FAQPage` y `dateModified: 2026-11-17T09:30:00-03:00`.
  - **Nuevo Artículo de Autoridad SEO en `/blog/google-tag-manager-vs-ga4-seo/`:**
    - Main Keyword: `Google Tag Manager vs GA4 directo` (6 palabras naturales, slug exacto Regla #18).
    - `<title>` de **56 caracteres**: `Google Tag Manager vs GA4 Directo: ¿Cuál Conviene 2026?`.
    - `<h1>`: `Google Tag Manager vs. GA4 Directo (gtag.js): Qué Conviene Más para tu Velocidad Web y el SEO`.
    - `meta description` de 156 caracteres y Direct Answer Sturm en primeras 8 palabras.
    - Tabla comparativa técnica HTML (peso de scripts, ejecución en hilo principal / INP, medición de clics a WhatsApp y riesgo de tags obsoletos).
    - 6 FAQs interactivas con GA4 tracking y marcado `Schema.org` (`BlogPosting`, `BreadcrumbList`, `FAQPage`).
    - Fotografía editorial auténtica de especialista en analítica en Buenos Aires con dual monitor mostrando métricas Core Web Vitals en verde y dashboard GA4 (`guia_google_tag_manager_vs_ga4_seo.png`, 316.6 KB, dual-sync en `images/` y `public/images/`).
    - Añadido a `blog/index.html` (**182 guías activas**), `vite.config.js`, `sitemap.xml` y `public/sitemap.xml` (**201 URLs canónicas**).
  - **Infraestructura & Notificaciones Oficiales:**
    - 0 enlaces rotos (`audit_all_internal_links.py`).
    - 0 emojis (Regla #17).
    - Compilación limpia en Vite (`npm run build`) en 17.41s con 0 errores y 0 advertencias.
    - Notificaciones enviadas: Google Indexing API v3 (`200 OK` en las 5 URLs), GSC sitemap enviado con éxito, IndexNow API (`202 Accepted` en 5 URLs) y Bing Webmaster API `SubmitUrlBatch` (`200 OK`).
- [x] **2026-11-17 (Rediseño Estético y Estructural de la Demo Contable `/demos/contable/` con `design-master` inspirado en Estudio Paz):**
  - **Inspiración Visual & Dirección de Arte:** Adopción del ADN estético de `estudiopaz.com.ar` (estética editorial sobria, prestigio y rigor corporativo para estudios contables de alto nivel, adaptado a código limpio sin dependencias pesadas ni copias de contenido).
  - **Par Tipográfico & Jerarquía Editorial:** `Playfair Display` para titulares con acentos selectivos en cursiva (`em`) combinada con `Inter` (300 a 700) para el cuerpo y componentes de interfaz.
  - **Paleta de Lujo & Ritmo Dual (Dark Ink & Warm Alabaster):**
    - Deep Ink `#0A0A0A`, Warm Charcoal `#141412`, `#1C1C19`.
    - Champagne Gold `#C8A96E`, Luminous Gold `#E0C68F`, Línea dorada sutil y oro accesible `#7F6329` para textos sobre fondos claros.
    - Alabastro cálido `#F7F7F4` y blanco puro `#FFFFFF`.
  - **Componentes y Estructura Transformada:**
    - Navbar con brand editorial, scroll progress bar dorada `#prog` y botón `btn-gold` con glow sutil en hover.
    - Hero cinemático `on-dark` con tipografía Playfair Display, palabras clave en cursiva dorada y botones `btn-gold` + `btn-ghost-dark`.
    - Trust Band horizontal de 4 columnas en dark ink (*Desde 2012*, *Equipo Matriculado CPCESJ*, *+250 PyMEs Asesoradas*, *Metodología 100% Digital*).
    - Sección "Por qué elegirnos" con 3 tarjetas de lujo y efecto spotlight (`data-spot`).
    - Grilla de Servicios 3x2 con números grandes en serif dorada (`01` a `06`) y trigger directo a WhatsApp.
    - Sección "Gestión Digital & Nube PyME" en dark ink con previsualización de tablero empresarial, comprobantes por foto en WhatsApp y alertas preventivas.
    - Retrato editorial con anillo dorado (`gold-ring`), credenciales y firma institucional de Cr. Martín Sánchez.
    - Presencia en San Juan y cobertura remota a todo el país.
    - Testimonios con estrellas SVG doradas y comillas tipográficas.
    - Wizard interactivo de "Diagnóstico Fiscal en 3 Pasos" con selección dinámica de chips y generación automática del mensaje para WhatsApp.
    - Acordeón FAQ con Schema.org y CTA final de alto impacto.
  - **Verificaciones:** Compilación limpia en Vite (8.54s), 0 enlaces rotos (`audit_all_internal_links.py`), 0 emojis decorativos (Regla #17) y preservación estricta de la sección comercial de Erik Website (`#erikwebsite-cta` de $150.000 / $20.000) y controles flotantes.

- **Miércoles 18/11/2026 — Ejecución Completa Eje Diseño Web y Localidades (Boost Zona Sur GBA + Nuevo Artículo Luján):**
  - **Cirugía / Boost Aplicado (`/blog/diseno-web-zona-sur/`):**
    - `<title>` optimizado a 56 caracteres: `Diseño Web, Hosting y SEO en Zona Sur GBA: Precios 2026`.
    - `<h2>` #2 actualizado para responder directamente a 5 consultas comerciales de GSC (`'diseño web landing page y hosting zona sur'`, `'diseño web profesional en zona sur'`, `'diseño web para Google Ads en Zona Sur'`, `'diseño web posicionamiento seo zona sur'`).
    - Enlace contextual hacia la demo interactiva `/demos/arquitectura/` para estudios y constructoras de Zona Sur (Canning, Lomitas, Quilmes).
    - Ampliado a 6 FAQs interactivas (`<details name="faq-accordion">` con evento GA4 `faq_expand`), Schema.org `FAQPage` sincronizado y `dateModified: 2026-11-18T09:30:00-03:00`.
  - **Nuevo Artículo Publicado (`/blog/diseno-web-lujan/`):**
    - Main Keyword: `Diseño web en Luján`.
    - Slug natural de 4 palabras: `/blog/diseno-web-lujan/` (Reglas #16 y #18).
    - `<title>` (55 caracteres): `Diseño Web en Luján: Páginas para Empresas y Comercios`.
    - `<h1>`: `Diseño de Páginas Web en Luján (Buenos Aires): Desarrollo Rápido y Google Maps para Empresas, Turismo y Profesionales`.
    - Direct Answer Sturm en las primeras palabras con la Main Keyword.
    - Tabla comparativa transparente ($150.000 ARS vs creadores gratuitos/WordPress lento).
    - 6 FAQs interactivas + Schema `FAQPage`.
    - Imagen editorial propia generada y optimizada con PIL: `images/guia_diseno_web_lujan.png` y `public/images/guia_diseno_web_lujan.png` (255.8 KB, 1200x675, pastilla y marca de agua).
    - Interlinking bidireccional: enlace desde `/blog/diseno-web-zona-oeste/` hacia `/blog/diseno-web-lujan/` y enlaces internos hacia `/blog/diseno-web-pilar/`, `/demos/arquitectura/`, `/auditoria-seo/`, etc.
  - **Integración y Configuración:**
    - Card agregada en `blog/index.html` bajo categoría `maps` (42 guías en la categoría) y contador actualizado a 183 guías.
    - Endpoint registrado en `vite.config.js`.
    - Sitemaps actualizados a 202 URLs canónicas (`sitemap.xml` y `public/sitemap.xml`).
  - **Auditoría y Despliegue:**
    - 0 enlaces rotos (`audit_all_internal_links.py`).
    - 0 emojis decorativos (Regla #17).
    - Build de Vite exitoso en 28.22s.
    - Notificación exitosa a Google Indexing API v3 (`200 OK`), GSC Sitemap ping, IndexNow (`202 Accepted`) y Bing Webmaster API (`200 OK`).
- [x] **2026-11-19 (Auditoría Profunda de Medio Término, Reglas #21–#27 y Re-optimización del Plan Restante de la Semana 2 en `PLAN_SEMANAL_SEO.md` — Sin Redacción):**
  - **Pulso en Vivo (GSC + Bing + GA4 al 19/11/2026):**
    - GSC saltó a **`4.772` impresiones (+44% en 4 días vs. 3.310 del domingo)** y `44` consultas en *Striking Distance* (Pos 4–20); nuevo clic orgánico en `/blog/registrar-marca-inpi-vs-dominio-com-ar-nic-argentina/` (Pos `6.3`); `/blog/generador-link-qr-whatsapp-gratis/` duplicó a `106` impr (+112%); `/blog/precios-shopify-argentina-conviene/` saltó a `63` impr (+85%, `'shopify argentina'` en Pos `13.2`).
    - Bing `InIndex` subió de `10` a **`17` páginas (+70% en 4 días)**.
    - GA4 registró **tráfico real de asistentes IA (`AI Assistant`: `3` usuarios, `3` sesiones, `100%` engaged)**: `chatgpt.com` hacia `/blog/diseno-web-rosario/` y `/demos/odontologia/`, y `gemini.google.com` hacia `/blog/como-delegar-dns-renovar-dominio-nic-argentina/`.
  - **Errores Sistémicos Detectados y Bloqueados con Nuevas Reglas #21–#27 + Validador `scratch/verify_article_hygiene.py`:**
    1. **Boosts fantasma por `.replace()` ciego (13/11):** `/blog/como-registrar-dominio-com-ar-nic-argentina/` (1.191 impr) y `/blog/paginas-web-empresas-limpieza-finales-obra-tapizados/` nunca cambiaron en disco (siguen con títulos de 88c y 93c).
    2. **Desfase HTML `<details>` vs JSON-LD `FAQPage` en 62 artículos:** incluidos los Boosts del 14/11 (`como-crear-correo-corporativo-dominio-propio-gmail` 6/2; `dominio-com-vs-com-ar` 6/3).
    3. **11 artículos del Sprint SEO (13–14/11) sin `/src/js/main.js`:** botones de WhatsApp y eventos GA4 inactivos hasta inyectar el script.
    4. **Taxonomía `blog/index.html` desfasada:** 6 provincias con `data-cat="geo"` huérfano, el plan indicaba `diseno` (inexistente) y contadores de `servicios`/`ventas`/`dominios` desactualizados.
    5. **`<h1>` de 93–120 caracteres violando Regla #5**, `meta description` > 160c sin recortar en Boosts, y mezcla puntual de tuteo neutro (`puedes`).
    6. **`llms.txt` / `public/llms.txt` desactualizados** con URL 404 (`/demos/medicina/`), sin `/demos/arquitectura/` y contador congelado en 153 guías.
    7. **SerpBear local en `0` keywords rastreadas.**
  - **Reestructuración del Plan Restante (Bloque 0 de Saneamiento + Jueves 19/11 + Viernes 20/11 + Sábado 21/11) con Validación Real de Demanda (32 CSVs + Google AR Autocomplete + AI Query Fan-Out) y 33/33 Enlaces Verificados en Disco:**
    - **Jueves 19/11:** Boosts Shopify (63 impr, Pos 13.2) + Canva (27 impr, Pos 7.3) + Nuevo **`/blog/seo-odontologos-consultorios-dentales/`** (0% canibalización, 11 sugerencias AR, potencia `/demos/odontologia/` ya citado por ChatGPT — reemplaza Hoteles/Cabañas que tenía 67% overlap).
    - **Viernes 20/11:** Boosts Generador QR WhatsApp (106 impr) + **`/blog/hotmart-argentina-comisiones-impuestos-alternativa-funnel/`** (32 impr, 1 clic, Pos 8.0, título 100c — reemplaza Cotizador que solo tenía 1 impr) + Nuevo **`/blog/landing-page-vender-cursos-online/`** (500/mes CSV + 5 sugerencias AR + sinergia 1:1 con `/demos/funnel/` y Hotmart — reemplaza Consorcios que tenía 0 sugerencias web en AR).
    - **Sábado 21/11:** Boosts **`/blog/diseno-web-rosario/`** (35 impr + tráfico real de ChatGPT!) + **`/blog/como-poner-agregar-negocio-local-google-maps-gratis/`** (101 impr, Pos 10.0, título 98c — reemplaza Santa Fe, que pasa a Miércoles 25/11) + Nuevo **`/blog/parametros-utm-google-analytics-4-maps/`** (40% overlap, 12 sugerencias AR, absorbe estadísticas GBP + atribución real en GA4).
    - Creado `scratch/verify_article_hygiene.py` como puerta de calidad obligatoria antes de cada `npm run build` y `git push`.
- [x] **2026-11-19 (Ejecución Completa Bloque 0 Saneamiento Técnico + Jueves 19/11 Pasos 3 y 4 — 100% PASS en `verify_article_hygiene.py`):**
  - **Bloque 0 — Saneamiento Técnico Completado:**
    - Inyectado `<script type="module" src="/src/js/main.js"></script>` en los 11 artículos del Sprint 13–14/11 (reactivando botones `data-wa-msg`, menú móvil y eventos GA4/Meta Pixel) y recortada la meta description de `seguridad-web-certificados-ssl-https` de 161c a 132c.
    - Reparado el Boost fantasma del 13/11 en `/blog/como-registrar-dominio-com-ar-nic-argentina/` (1.191 impr): `<title>` a 53c, `meta description` a 147c, paridad 6/6 HTML/Schema `FAQPage`, H2 #1 reforzado con `'comprar un dominio .ar'` e imagen cuantizada de 614.9 KB a 178.5 KB dual-sync.
    - Sincronizada paridad 6/6 HTML/Schema `FAQPage`, recortadas meta descriptions <= 155c, corregido tuteo neutro (`tenés`/`podés`) y cuantizadas imágenes dual-sync en `/blog/como-crear-correo-corporativo-dominio-propio-gmail/` (1.033 impr, 537.4 KB -> 122.5 KB) y `/blog/dominio-com-vs-com-ar-cual-conviene-argentina/` (580 impr, 714.7 KB -> 170.3 KB).
    - Saneado `blog/index.html`: migradas las 6 tarjetas `data-cat="geo"` huérfanas a `data-cat="maps"` (48 en Maps) y sincronizados todos los contadores del dropdown.
    - Actualizados `llms.txt` y `public/llms.txt`: eliminado `/demos/medicina/` (404), incorporado `/demos/arquitectura/`, destacado `/demos/contable/` y sumadas guías pilares SEO + contador actualizado a 184 guías.
  - **Jueves 19/11 — Doble Boost + Nuevo Artículo SEO Odontólogos:**
    - **Boost 1 (`/blog/precios-shopify-argentina-conviene/` — 63 impr, Pos `13.2` `'shopify argentina'`):** `<title>` 85c -> 53c, `meta description` 146c, refuerzo `'Shopify Argentina'` y doble comisión Mercado Pago, paridad 6/6 FAQs HTML/Schema, interlinking a Tiendanube/WooCommerce/Tienda Propia e imagen cuantizada 516.4 KB -> 127.8 KB dual-sync.
    - **Boost 2 (`/blog/hacer-landing-page-canva-sirve-para-vender/` — 27 impr, Pos `7.3`):** `<title>` 87c -> 55c, `meta description` 171c -> 146c, bloque comparativo enlazando `/demos/arquitectura/`, `/demos/contable/` y `/demos/estetica/`, paridad 6/6 FAQs HTML/Schema.
    - **Nuevo Artículo (`/blog/seo-odontologos-consultorios-dentales/`):** Main Keyword `SEO para odontólogos y consultorios dentales` (0% canibalización), `<title>` 57c, `<h1>` 69c (Regla #5), `meta description` 154c, Direct Answer Sturm, 4 H2s + tabla comparativa + bloque Demo `/demos/odontologia/` + paridad 6/6 FAQs, imagen editorial propia PIL 425.7 KB dual-sync, enlace entrante desde `/blog/paginas-web-marketing-odontologos-argentina/`.
    - **Inventario Actualizado:** **184 guías activas** en `blog/index.html` (`35` en `seo`, `48` en `maps`) y **203 URLs canónicas** sincronizadas en `sitemap.xml` y `public/sitemap.xml`; registrado en `vite.config.js`.
    - **Validación y Despliegue:** `verify_article_hygiene.py --hub` + 17 artículos en **EXIT 0 (0 FAIL)**, `audit_all_internal_links.py` en **0 enlaces rotos**, compilación limpia en Vite, notificación oficial a Google Indexing API v3, GSC Sitemap, IndexNow y Bing Webmaster API, y `git push origin main`.
- [x] **2026-11-20 (Ejecución Completa Viernes 20/11 — Eje Diseño Web, Demos y Embudos · 100% PASS en `verify_article_hygiene.py`):**
  - **Boost 1 (`/blog/generador-link-qr-whatsapp-gratis/` — `106` impr +112%, `1` clic, Pos `16.7`):** `<title>` acortado de 72c a **54c** (`Generador de QR y Link de WhatsApp Gratis (Sin Vencer)`), `meta description` **148c**, H2 #1 reforzado con `'generar código QR para WhatsApp'` y `'generador de QR WhatsApp sin caducidad'`, limpieza de banderas Unicode/símbolos y asteriscos Markdown, paridad exacta **6/6 FAQs** (`<details>` == JSON-LD `FAQPage`), e imágenes cuantizadas dual-sync (`guia_generador_link_qr_whatsapp.png` 581.5 KB -> 469.4 KB y `uso_qr_whatsapp_negocios.png` 949.3 KB -> 293.3 KB).
  - **Boost 2 (`/blog/hotmart-argentina-comisiones-impuestos-alternativa-funnel/` — `32` impr, `1` clic, Pos `8.0` en Página 1):** `<title>` acortado de 100c a **57c** (`Hotmart en Argentina 2026: Comisiones, Impuestos y Funnel`), `<h1>` acortado de 83c a **66c** (Regla #5), `meta description` de 218c a **148c**, paridad exacta **6/6 FAQs** cubriendo impuestos, CUIT/ARCA y comisión del 9,9%, e interlinking bidireccional con `/blog/landing-page-vender-cursos-online/` y `/demos/funnel/`.
  - **Nuevo Artículo (`/blog/landing-page-vender-cursos-online/`):** Main Keyword `Landing page para vender cursos online`, `<title>` **56c** (`Landing Page para Vender Cursos Online y Ebooks en Pesos`), `<h1>` **69c** (Regla #5), `meta description` **152c**, Direct Answer Sturm, 4 secciones `<h2>` respondiendo las 5 consultas IA / Query Fan-Out, tabla comparativa numérica sobre 50 ventas de $40.000 ARS (Hotmart vs. Stan Store vs. Página Modo Funnel Propia), bloque en vivo a `/demos/funnel/`, paridad **6/6 FAQs**, e imagen editorial propia PIL (`guia_landing_page_vender_cursos_online.png`, `399.8 KB`, pastilla `"FUNNELS & CURSOS"` y sello `erikwebsite.com` dual-sync).
  - **Inventario y Despliegue:** Card agregada en `blog/index.html` (`data-cat="ventas"`, `10` en Funnels y **185 guías activas**), registrado en `vite.config.js`, `llms.txt` / `public/llms.txt` actualizados (185 Guías), `sitemap.xml` / `public/sitemap.xml` sincronizados con **204 URLs canónicas**, `verify_article_hygiene.py --hub` en **EXIT 0 (0 FAIL, 0 WARN)**, `audit_all_internal_links.py` con **0 enlaces rotos**, build de producción Vite exitoso, notificación `200 OK` / `202 Accepted` a Google Indexing API v3, GSC Sitemap, IndexNow y Bing Webmaster API, y `git push origin main`.
- [x] **2026-11-21 (Propuesta Privada + Subpágina SEO Demo para Álvarez & Maldonado Estudio Jurídico en San Juan `/propuestas/alvarez-maldonado-abogados/` — Regla #20):**
  - **Relevamiento del Prospecto (`@alvarez.maldonado.abogados`):** Estudio jurídico con +30 años de trayectoria en la provincia de San Juan, sede física en **Mitre 486 Oeste, San Juan Capital**, teléfono/WhatsApp `264 5618327` y `1.663` seguidores en Instagram, que actualmente solo cuenta con un enlace a `turnito.app/c/4GnGb2fcSzD8yT` en su bio y carece de sitio web propio en Google.
  - **Ingeniería Inversa Estética de `moragaycia.cl` + Corrección Total de sus 9 Fallos SEO:**
    - Se aplicó el sistema de diseño *Quiet Luxury Editorial* extraído en `C:\Users\erikl\Downloads\SEO\clientes\moragaycia.cl.md`: paleta Obsidiana (`#050505`), Alabastro Cálido (`#fcfaf9`), Crema (`#f8f5f2`), Arena (`#e8e3df`) y Carmesí Jurídico (`#b50027` / `#e5352c`), punto final carmesí `.` en titulares, barra lateral fija izquierda de `90px` en Desktop (`writing-mode: vertical-rl`) convertida en Topbar de `64px` en Mobile con unidades `svh`, menú fullscreen numerado (`01` a `06`), efecto fotográfico de escala de grises a color con zoom lento sobre **un único nodo `<img>`** (sin duplicar DOM) y panel lateral deslizable (Drawer) para las 9 áreas de práctica reales del estudio.
    - Se corrigieron de raíz los defectos técnicos de `moragaycia.cl`: 100% HTML5 semántico estático indexable (sin parches ocultos de `1x1px` ni SPA client-side), **Triaje Jurídico Interactivo** que deriva consultas pre-filtradas al WhatsApp `264 5618327`, sección de cápsulas *"En 30' Te Explico"* basada en sus reels reales (monotributistas y obras sociales, cuentas bancarias vaciadas, alquileres) y paridad 1:1 entre `<details name="faq-accordion">` y Schema `FAQPage`.
  - **Subpágina SEO Demo (`/propuestas/alvarez-maldonado-abogados/amparos-de-salud-discapacidad/`):** Demostración en vivo del Plan Integral ($350.000 ARS: Portada + 8 Páginas SEO de Especialidades) con su propio `<h1>`, bloque de Respuesta Directa AEO/GEO y Schema `Service` + `FAQPage` para posicionar en Google San Juan.
  - **Dossier Comercial Exportado:** Guardado en [`C:\Users\erikl\Downloads\SEO\clientes\alvarez-maldonado-abogados.md`](file:///C:/Users/erikl/Downloads/SEO/clientes/alvarez-maldonado-abogados.md) con diagnóstico y guiones listos para WhatsApp e Instagram DM.
  - **Validación y Despliegue:** `<meta name="robots" content="noindex, nofollow">` estricto, excluido de `sitemap.xml`, registrado en `vite.config.js`, 0 enlaces rotos (`audit_all_internal_links.py`), compilación limpia en Vite y `git push origin main`.
- [x] **2026-11-21 (Ejecución Completa Sábado 21/11 — Eje Especialista SEO Local, Maps y Analítica · 100% PASS en `verify_article_hygiene.py`):**
  - **Boost 1 (`/blog/diseno-web-rosario/` — `35` impr en GSC + tráfico real de `chatgpt.com` en GA4):** `<title>` acortado de 61c a **53c** (`Diseño Web en Rosario: Páginas, Precios y Maps (2026)`), `meta description` **145c**, bloque de Respuesta Directa GEO reforzado con entidades explícitas ($150.000 ARS finales pago único, entrega en 3 a 5 días hábiles, cobertura Centro, Pichincha, Puerto Norte, Fisherton, Funes y Gran Rosario), enlazado contextual a `/demos/arquitectura/`, `/demos/contable/` y `/demos/abogados/`, corrección de typo duplicado, y paridad exacta **6/6 FAQs** (`<details>` == JSON-LD `FAQPage`).
  - **Boost 2 (`/blog/como-poner-agregar-negocio-local-google-maps-gratis/` — `101` impr en GSC, Pos `10.0` en Página 1):** `<title>` acortado de 98c a **57c** (`Cómo Poner tu Negocio en Google Maps Gratis (Paso a Paso)`), `<h1>` acortado de 78c a **64c** (Regla #5), `meta description` de 171c a **150c**, conversión de `<h2>` promocional final a `<h3>` (higiene semántica), respuestas directas a consultas de Google AR (*alta desde el celular*, *por qué es 100% gratis*, *sincronización con Waze*), interlinking hacia `/blog/parametros-utm-google-analytics-4-maps/`, paridad exacta **6/6 FAQs**, e imagen cuantizada dual-sync (`guia_como_agregar_negocio_google_maps.png` 530.1 KB -> 263.2 KB).
  - **Nuevo Artículo (`/blog/parametros-utm-google-analytics-4-maps/`):** Main Keyword `Parámetros UTM en Google Analytics 4`, `<title>` **56c** (`Parámetros UTM en Google Analytics 4: Medir Maps y Redes`), `<h1>` **68c** (Regla #5), `meta description` **148c**, Direct Answer Sturm, 4 secciones `<h2>` + tabla comparativa con 5 plantillas UTM listas para copiar (Botón Sitio Web de Google Business Profile `?utm_source=google&utm_medium=organic&utm_campaign=gbp`, Link de Turnos en Maps, Bio de Instagram, Cartel QR impreso, Meta Ads), ruta paso a paso para cruzar estadísticas de Google Business Profile con GA4 (`Fuente / Medio de la sesión` + `Campaña de la sesión` + eventos `whatsapp_click` / `generate_lead`), los 4 errores fatales con UTM y protección `<link rel="canonical">`, paridad exacta **6/6 FAQs**, e imagen editorial propia PIL (`guia_parametros_utm_google_analytics_4_maps.png`, `222.1 KB`, pastilla `"ANALÍTICA GA4 & MAPS"` y sello `erikwebsite.com` dual-sync).
  - **Interlinking Bidireccional e Higiene Adicional:** Enlace contextual entrante agregado en `/blog/como-instalar-google-analytics-4-ga4-medir-clics-whatsapp/` (además de ajustar su `<h1>` de 91c a **63c** y `og:title` a **56c** para pasar 100% Regla #5).
  - **Inventario y Despliegue:** Card agregada en `blog/index.html` (`data-cat="maps"`, `49` en Maps y **186 guías activas**), registrado en `vite.config.js`, `llms.txt` / `public/llms.txt` actualizados (186 Guías), `sitemap.xml` / `public/sitemap.xml` sincronizados con **205 URLs canónicas**, `verify_article_hygiene.py --hub` en **EXIT 0 (0 FAIL, 0 WARN)**, `audit_all_internal_links.py` con **0 enlaces rotos**, build de producción Vite exitoso, notificación a Google Indexing API v3, GSC Sitemap, IndexNow y Bing Webmaster API, y `git push origin main`.
- [x] **2026-11-22 (Comando Dominical Forense SEO, Bing, GA4 & Auditoría Global — Semana 3 · Actualización de `PLAN_SEMANAL_SEO.md`, Reglas #28–#30 y `verify_article_hygiene.py`):**
  - **Pulso en Vivo (`sunday_seo_command.py` + auditoría profunda 7d/28d):** **205 URLs** en sitemap (`159` recibiendo impresiones) y **186 guías** en `/blog/`; GSC **7.055 impresiones en 28d** (`+113,1%` vs. S2) y **`3.587` impr en últimos 7d vs. `2.043` previos (`+75,6%` semanal)**, `7` clics (`0,10%` CTR, nuevo clic en `/blog/registrar-marca-inpi-vs-dominio-com-ar-nic-argentina/` Pos `6.4`) y **52 consultas en Striking Distance** (`+40,5%`); Bing `InIndex` **19 páginas** (`+90%`, `3` impr, `4` errores / `Code4xx: 2`); GA4 `AI Assistant` **3 usuarios / 3 sesiones (`100%` engaged)** desde `chatgpt.com` (`diseno-web-rosario` con `article_read_75` + `2 faq_expand`, `/demos/odontologia/` con `article_read_75`) y `gemini.google.com` (`como-delegar-dns`), mientras `17` sesiones Direct de EE.UU. (`0%` eng.) son bots; `4` `generate_lead` + `4` `whatsapp_click` (`3` u.); SerpBear sin base local (`False`).
  - **7 Fallos Críticos de Producción Detectados en Auditoría Forense (Agrupados en Bloque 0 de Emergencia):**
    1. Botones WhatsApp **100% muertos** (`data-wa-lead` sin listener) en `como-poner-agregar-negocio-local-google-maps-gratis` (101 impr) y `parametros-utm-google-analytics-4-maps`, más teléfono erróneo `5492644869263`.
    2. **15 artículos en modo oscuro con FAQs ilegibles** (`text-slate-900` sobre `bg-neutral-950`), incluyendo `por-que-mi-negocio-no-aparece-en-google-maps` (74 impr).
    3. **Doble disparo de Meta Pixel (`Contact` x2)** y fuga de `?soy_erik=1` por listener inline duplicado en `62` archivos (`index.html`, `en/`, `san-juan/`, `blog/index.html` + 58 blogs).
    4. **Causa raíz de `Code4xx` en Bing:** clave IndexNow enviada distinta de `e7a9c4b2f8d143e6a0b5c8d9e2f1a3b4` (`public/e7a9c4b2f8d143e6a0b5c8d9e2f1a3b4.txt`) + `<link rel="stylesheet" href="/src/css/style.css">` roto en `404.html` + falta de `public/_redirects` HTTP `301` (los stubs `<meta refresh>` siguen robando impresiones en GSC, ej. `diseno-web-rosario-santa-fe` con 27 impr).
    5. `1` artículo aún sin `/src/js/main.js` (`blog/crawl-budget-optimizacion-rastreo-google/index.html`) y `86` imágenes > 490 KB (incluyendo `guia_configurar_correo_corporativo_outlook.png` de 960 KB).
    6. `blog/index.html` llegó a `571 KB` de HTML estático (`186` tarjetas juntas en DOM) -> planificada paginación/carga diferida en Semana 4.
    7. **Techo de Autoridad Off-Page (`InLinks: 0` en Bing):** `/san-juan/` (2 impr, Pos 60.5) y `/auditoria-seo/` (19 impr, Pos 63.9) requieren Google Business Profile de Erik Website en San Juan + enlaces `"Desarrollado por Erik Website"` en clientes + perfiles de autoridad.
  - **Plan Semana 3 Blindado (`PLAN_SEMANAL_SEO.md`, Lunes 23 al Sábado 28/11):** Bloque 0 de emergencia + 12 Boosts maduros + 6 artículos nuevos 100% validados en Google AR Autocomplete y `< 60%` canibalización (`wordpress-hackeado-limpiar-migrar-seguro`, `archivo-llms-txt-seo-ia`, `diseno-web-avellaneda`, `seo-shopify-argentina`, `integrar-mercado-pago-pagina-web`, `bing-webmaster-tools-indexnow-chatgpt`), corrigiendo enlaces a stubs (`/demos/taller/`, `/demos/inmobiliaria/`) y eliminando el tema redundante de eventos GA4. Agregadas Reglas #28–#30 y actualizados los checks automáticos en `scratch/verify_article_hygiene.py`.
- [x] **2026-11-22 (Ejecución Completa Bloque 0 de Saneamiento Técnico + Unificación 100% Modo Claro + Fix Filtro `?soy_erik=1` + SerpBear Reconectado):**
  - **Conversión WhatsApp Blindada:** Reparados los 4 botones muertos (`data-wa-lead` -> `data-wa-msg`) en `como-poner-agregar-negocio-local-google-maps-gratis` y `parametros-utm-google-analytics-4-maps`, corregido teléfono erróneo `5492644869263` -> `5492645185359`, y blindado `src/js/whatsapp.js` para soportar ambos atributos.
  - **Eliminación Total del Modo Oscuro en el Blog (17/17 migrados a Claro Editorial):** Convertidos los 17 artículos legacy del 30/10 (`bg-neutral-950`) a la estética clara unificada (`bg-[#fafafa] text-neutral-900`), eliminando además los 15 fallos de FAQs negro-sobre-negro.
  - **Blindaje Total de `?soy_erik=1` (0 Fugas) y Meta Pixel Sin Doble Conteo:** Envolvimos con `if (!window._ewIgnoreAnalytics)` los `23` bloques de `gtag('config')` y `32` bloques de Microsoft Clarity que filtraban tráfico propio en todas las demos (incluyendo `/demos/contable/`), y eliminamos los `70` listeners inline duplicados de Meta Pixel (`trackCustom', 'Whatsapp'`) en `index.html`, `en/`, `san-juan/`, `blog/index.html` y 66 páginas.
  - **Infraestructura, Bing 4xx y Velocidad:** Creado `public/_redirects` con `16` reglas HTTP `301` reales para Cloudflare Pages, corregidos `404.html` / `public/404.html` (removido `/src/css/style.css` roto), actualizado `robots.txt` / `public/robots.txt` (`Disallow: /propuestas/`), actualizado `public/ai-catalog.json`, inyectado `/src/js/main.js` en `blog/crawl-budget-optimizacion-rastreo-google/index.html`, y cuantizadas `61` imágenes PNG `> 490 KB` dual-sync ahorrando **`31,38 MB`** (`0` imágenes > 490 KB en todo el blog).
  - **SerpBear Reconectado (`748` keywords):** Corregida la ruta real (`C:\Users\erikl\.gemini\tools\serpbear\data\database.sqlite`) en `scratch/sunday_seo_command.py` y sincronizadas `748` keywords reales de `erikwebsite.com` en SQLite.
  - **Verificación y Despliegue:** `0` defectos globales (0 gtag/Clarity sin filtro, 0 doble píxel, 0 modo oscuro en blog, 0 botones muertos, 0 teléfonos erróneos, 0 PNGs > 490 KB), `verify_article_hygiene.py --hub` PASS, `audit_all_internal_links.py` 0 rotos, build Vite limpio, re-notificación IndexNow con clave real `e7a9c4b2f8d143e6a0b5c8d9e2f1a3b4` + Bing + Google Indexing API, y `git push origin main`.
- [x] **2026-11-23 (Ejecución Completa Lunes 23/11 — Eje Diseño Web y Conversión · 100% PASS en `verify_article_hygiene.py`):**
  - **Boost 1 (`/blog/crear-pagina-web-google-sites-sirve-para-negocio/` — `66` impr en GSC, Pos `5.0–8.0`):** `<title>` y `og:title` acortados de 84c a **55c** (`Crear Web en Google Sites: ¿Sirve para un Negocio 2026?`), `meta description` de 189c a **147c**, nueva Sección 4 comparando `'hacer una página web con Google'` vs. Landing a medida (\$150.000 ARS) con enlaces a `/blog/hacer-landing-page-canva-sirve-para-vender/` y `/#demos`, y paridad exacta **6/6 FAQs** (`<details name="faq-accordion">` == JSON-LD `FAQPage`).
  - **Boost 2 (`/blog/catalogo-pdf-canva-vs-catalogo-web/` — `12` impr, Pos `6.3`):** `<title>` y `og:title` acortados de 80c a **53c** (`Catálogo PDF en Canva vs. Catálogo Web: Qué Vende Más`), `meta description` de 177c a **149c**, limpieza de Markdown crudo `**...**` a `<strong>`, refuerzo hacia `/blog/como-crear-catalogo-online-pedidos-whatsapp/` (Pos `9.5`) y paridad exacta **6/6 FAQs**.
  - **Nuevo Artículo (`/blog/wordpress-hackeado-limpiar-migrar-seguro/`):** Main Keyword `WordPress hackeado` (5 sugerencias AR, `50%` overlap), `<title>` **56c** (`WordPress Hackeado: Cómo Limpiarlo o Migrar a Web Segura`), `<h1>` **63c** (Regla #5), `meta description` **150c**, Direct Answer Sturm, 4 `<h2>` + tabla comparativa (*Limpiar WordPress Actual* vs. *Migrar a Código Estático Blindado* \$150.000 ARS pago único), paridad **6/6 FAQs**, imagen editorial propia PIL (`guia_wordpress_hackeado_limpiar_migrar_seguro.png`, `255.9 KB` dual-sync con pastilla `"SEGURIDAD & MIGRACIÓN"`), e interlinking entrante desde `/blog/migrar-wordpress-otro-hosting-o-codigo-limpio/`.
  - **Inventario y Despliegue:** Card añadida en `blog/index.html` (`data-cat="dominios"`, `6` en Dominios y **187 guías activas**), registrado en `vite.config.js`, `llms.txt` / `public/llms.txt` (`187` Guías), `sitemap.xml` / `public/sitemap.xml` (**206 URLs canónicas**), `verify_article_hygiene.py --hub` en **EXIT 0**, `audit_all_internal_links.py` en **0 enlaces rotos**, build Vite limpio, notificación a Google Indexing API v3, GSC Sitemap y Bing Webmaster `SubmitUrlbatch`, y `git push origin main`.







