# PLAN_SEMANAL_SEO.md — Comando Estratégico Dominical (`erikwebsite.com`)

> **Propósito:** Archivo maestro vivo donde cada domingo registramos la evolución real de `erikwebsite.com` (**Google Search Console**, **Bing Webmaster Tools / IndexNow**, **GA4 con eventos de conversión a WhatsApp**, **SerpBear** e inventario de URLs), auditamos qué funcionó tras la ventana de maduración de 14 días, convertimos palabras solapadas en **Boosts de contenido** y dejamos trazado el **Plan de Ataque de Lunes a Sábado**.

---

## 1. Reglas del Sistema Operativo Semanal (Cadencia 3 + 3 + 1)

| Día | Eje Estratégico | Objetivo Principal | Cuota Recomendada |
| :--- | :--- | :--- | :--- |
| **Lunes** | Diseño Web y Conversión | Rubros comerciales, comparativas BoFu o cirugía/boost de páginas de Diseño Web en posiciones 4–20 | 1 cirugía/boost + 1 página nueva |
| **Martes** | Especialista SEO, Velocidad e IA | Posicionamiento en Google/Bing, casos técnicos, Core Web Vitals y sinergia Web + Redes | 1 cirugía/boost + 1 página nueva |
| **Miércoles** | Diseño Web y Localidades | Ciudades o zonas estratégicas (Regla #16: 1 sola ciudad o 1 zona reconocible por slug) | 1 cirugía/boost + 1 página nueva |
| **Jueves** | Especialista SEO por Rubro / CMS | SEO aplicado a industrias (inmobiliarias, abogados, salud, tiendas) y plataformas | 1 cirugía/boost + 1 página nueva |
| **Viernes** | Diseño Web, Demos y Embudos | Páginas conectadas a las 13 Demos Interactivas, cotizadores y Landings Modo Funnel | 1 cirugía/boost + 1 página nueva |
| **Sábado** | Especialista SEO Local, Maps y Analítica | Dominio de San Juan, Google Maps, Search Console, Bing, GA4 y citación en IA (AEO/GEO) | 1 cirugía/boost + 1 página nueva |
| **Domingo** | **Comando Estratégico y Auditoría** | Ejecución de `sunday_seo_command.py` (GSC + Bing + GA4 + SerpBear) y Plan de la Semana | 1 Reporte Profundo + Hoja de Ruta |

---

## 2. Cómo Funcionan el "Boost por Solapamiento" y la "Cirugía de Optimización"

### A. Solapamiento >= 70% = Oportunidad de Boost ("Keyword Absorbing")
Cuando `python scratch/check_cannibalization.py "<keyword>"` detecta que una palabra clave nueva se solapa en `>= 70%` con un artículo que ya tenemos publicado:
1. **No se descarta la palabra clave ni se crea otra URL que compita.**
2. **La usamos para darle un Boost al artículo existente:** el script nos muestra qué términos nuevos trae esa búsqueda (`Terminos nuevos para inyectar como Boost`) y los agregamos dentro del artículo que ya existe como:
   - Un nuevo subtítulo `<h2>` o `<h3>` respondiendo esa variación exacta.
   - Una pregunta nueva dentro del acordeón de Preguntas Frecuentes (`Schema FAQPage`).
   - Un párrafo o fila adicional en la tabla comparativa.
3. **Caso real detectado hoy:** Al evaluar *"Páginas web para empresas de limpieza de oficinas y consorcios"*, `check_cannibalization.py` detectó un **71% de solapamiento** con `/blog/paginas-web-empresas-limpieza-finales-obra-tapizados/`. En lugar de crear otra URL que la canibalice, usamos esos términos nuevos (`oficinas`, `consorcios`, `abonos mensuales`) para hacerle un **Boost** a esa página existente el viernes.

### B. ¿Cómo hacemos la Cirugía de Optimización de una página existente? (¿Hace falta buscar CSVs nuevos?)
En el **85% de los casos NO hace falta que descargues ningún CSV nuevo** para optimizar un artículo existente, porque el sistema extrae las palabras automáticamente de **4 fuentes que ya tenemos conectadas**:
1. **Radiografía Quirúrgica de Google Search Console (`page` + `query`):** `sunday_seo_command.py` cruza cada URL contra las consultas reales con las que Google ya la está mostrando en los puestos 4 a 90. Por ejemplo, hoy detectó que `/blog/configurar-correo-corporativo-outlook-firma-profesional/` está saliendo en puesto `9.0` para `'como abrir un correo empresarial en outlook'` y puesto `14.7` para `'outlook corporativo'`. La cirugía consiste en meter esas frases exactas en sus subtítulos `<h2>` y FAQs para subirla al Top 3.
2. **Datos de Bing Webmaster Tools API:** Revisa qué consultas y páginas están entrando en el índice de Bing (que alimenta directamente a **ChatGPT Search y Microsoft Copilot**).
3. **Base Local Histórica de +25 CSVs de Google Ads (+4.500 keywords ya descargadas en el proyecto):** Cruzamos el artículo contra todos los CSVs que ya bajaste para ver qué variaciones con volumen mensual en Argentina nos faltó incluir en el texto.
4. **Extractor Automático de *Query Fan-Out* (`free_alsoasked_ai_fanout.py`):** Consulta en vivo el autocompletado de Google Argentina para sumar las preguntas reales que hace la gente.
- **¿Cuándo SÍ te pido un CSV nuevo el domingo?** Únicamente cuando queramos abrir un rubro o servicio 100% nuevo que no esté en nuestros CSVs guardados.

### C. Regla de Slugs Cortos y Limpios (Regla #18)
Todo artículo nuevo debe tener un **slug corto, limpio y directo de 3 a 5 palabras clave máximo** (por ejemplo: `/blog/paginas-web-distribuidoras-mayoristas/` o `/blog/errores-google-search-console-seo/`), evitando URLs largas de 7 u 8 palabras.

---

## 3. Evolución Histórica de Domingos (Bitácora de Métricas)

### Semana 1 (Baseline Inicial) — Domingo 8 de Noviembre de 2026

#### A. Estado del Inventario y Arquitectura Técnica
- **URLs Canónicas en `sitemap.xml` / `public/sitemap.xml`:** `171` URLs activas (`200 OK`, 0 redirecciones en sitemap).
- **Guías y Herramientas en `/blog/`:** `153` guías activas (`12` en la categoría *Auditoría SEO, Velocidad e IA*).
- **Archivo `/llms.txt`:** Activo en raíz y `public/llms.txt` para descubrimiento por crawlers de ChatGPT, Perplexity, Claude y Gemini.
- **Implementación en GA4 (`G-KWD0WYVK4J` — Propiedad `554839707`):**
  - Activados en las 171 páginas los 6 eventos estratégicos: `generate_lead`, `whatsapp_click`, `view_demo`, `use_interactive_calculator`, `faq_expand` y `article_read_75`.

#### B. Métricas de Google Search Console (Últimos 28 días)
- **Impresiones Totales:** `1.434` impresiones | **Clics Orgánicos:** `6` clics.
- **Páginas con Clics y Posiciones Líderes:**
  - `/` (Home): `2` clics, `8` impr, **Posición `3.0`** (`erik web`, `erik site`)
  - `/blog/configurar-correo-corporativo-outlook-firma-profesional/`: `1` clic, `32` impr, **Posición `10.3`** (`outlook corporativo`, `correo corporativo outlook`, `como abrir un correo empresarial en outlook`)
  - `/blog/generador-link-qr-whatsapp-gratis/`: `1` clic, `17` impr, **Posición `21.3`** (`generador qr whatsapp`)
  - `/blog/hotmart-argentina-comisiones-impuestos-alternativa-funnel/`: `1` clic, `12` impr, **Posición `6.3`**
  - `/blog/tiendanube-linktree-vs-web-propia-a-medida/`: `1` clic, `10` impr, **Posición `4.7`** (`tiendanube cobra comision por venta`)
- **Páginas con Mayor Volumen de Impresiones + Consultas que las Activan (Radiografía GSC):**
  - `/blog/como-registrar-dominio-com-ar-nic-argentina/` (`395` impr): `'comprar dominio .ar'`, `'comprar dominios .ar'`, `'registro de dominios .ar'`, `'registrar dominio .ar'`
  - `/blog/dominio-com-vs-com-ar-cual-conviene-argentina/` (`239` impr): `'dominio .com .ar'`, `'dominios .ar'`, `'dominio .com'`
  - `/blog/como-crear-correo-corporativo-dominio-propio-gmail/` (`201` impr): `'correo con dominio propio'`
  - `/blog/diseno-web-mendoza/` (`55` impr): `'diseño web mendoza'`, `'diseño web en mendoza'`
  - `/blog/cuanto-cuesta-una-pagina-web-argentina/` (`54` impr)
- **Consultas en "Striking Distance" (23 consultas en Posiciones 4.0 a 20.0 — Candidatas a Boost a Top 3):**
  - `[Pos 8.7]` `pagina web inmobiliarias` (`3` impr)
  - `[Pos 8.0–14.7]` `crear correo corporativo outlook gratis` / `correo corporativo outlook` / `outlook corporativo` (`6` impr)
  - `[Pos 8.0]` `tiendanube cobra comision por venta` (`1` impr)
  - `[Pos 11.0]` `diseño web quilmes` (`2` impr — optimizada el 8/11)
  - `[Pos 16.5]` `godaddy argentina` (`2` impr)

#### C. Métricas de Bing Webmaster Tools (API Oficial + IndexNow)
- **Páginas en el Índice de Bing (`InIndex`):** `6` páginas ya indexadas | **Rastreadas (últimos 7 días):** `13` páginas | **Errores de rastreo:** `0`.
- **Rendimiento en Bing (Primera Impresión Desbloqueada):** `1` impresión | **Posición `7.0`** para `'barras tropicale para eventos en san juan'`.
- **Cuota Oficial `SubmitUrlBatch`:** Ampliada por Bing a `2.200` envíos directos en el mes + protocolo `IndexNow` activo.

#### D. Métricas de Google Analytics 4 (Últimos 7 días)
- **Usuarios Activos:** `56` usuarios (`83` sesiones, `162` vistas de página).
- **Canales:** `Direct` (`23` usuarios), `Paid Social` (`22` usuarios), `Organic Search` (`5` usuarios / `24` sesiones / `17` engaged = **70,8% engagement**).

---

## 4. Plan de Ataque para Esta Semana (Lunes 9 al Sábado 14 de Noviembre de 2026)

> **Directriz de la Semana:** Cada día combina **1 Cirugía / Boost de optimización** sobre páginas con impresiones en GSC + **1 Guía Nueva 0% canibalizada con slug corto de 3 a 5 palabras** (Regla #18), alternando Lunes/Miércoles/Viernes (Diseño Web) y Martes/Jueves/Sábado (SEO).

### [x] Lunes 9/11 — Eje Diseño Web y Conversión (Completado)
1. **[x] Cirugía + Boost Striking Distance (Pos 8.7 y Pos 16.5):**
   - **Boost 1 (`/blog/paginas-web-para-inmobiliarias-argentina/` — Pos `8.7` en GSC):** `<title>` acortado de 81 a 57 caracteres (`Páginas Web para Inmobiliarias en Argentina: Precios 2026`), añadida la Sección 3 (*Diseño de página web para inmobiliarias vs. Portales y Plantillas lentas*) con tabla comparativa, corregidos los enlaces internos hacia `/blog/seo-para-inmobiliarias-desarrolladoras-argentina-google/` y `/demos/funnel/`, y sumadas las FAQs 3 y 4 con `<details name="faq-accordion">`.
   - **Boost 2 (`/blog/crear-pagina-web-godaddy-conviene-argentina/` — Pos `16.5` en GSC):** `<title>` optimizado a 56 caracteres (`GoDaddy Argentina 2026: Precios en Dólares y si Conviene`), añadida la Sección 4 (*Cómo migrar de GoDaddy sin perder tu dominio ni tus correos*) y FAQs 3 y 4 con `<details name="faq-accordion">`.
2. **[x] Artículo Nuevo Diseño Web (Slug corto de 4 palabras · 0% Canibalización):**
   - **Slug:** `/blog/paginas-web-distribuidoras-mayoristas/`
   - **Título:** *Páginas Web para Distribuidoras y Mayoristas en Argentina: Catálogo Ágil y Pedidos por WhatsApp* (154 guías activas en `/blog/` y 172 URLs en `sitemap.xml`).

### [x] Martes 10/11 — Eje Especialista SEO, Velocidad e IA (Completado)
1. **[x] Cirugía + Boost de Autoridad Técnica (Pos 8.0–14.7 en GSC):**
   - **Boost (`/blog/configurar-correo-corporativo-outlook-firma-profesional/` — Pos `8.0–14.7` en GSC):** `<title>` optimizado de 85 a 58 caracteres (`Correo Corporativo en Outlook: Cómo Configurarlo y Firma`), inyectadas las consultas exactas de la Radiografía de GSC (`'como abrir un correo empresarial en outlook'` en H2 #1, `'crear correo corporativo outlook gratis'` en la nueva Sección 3 con tabla comparativa frente a Microsoft 365 en dólares, y `'como configurar un correo corporativo en outlook'` en el bloque de Respuesta Directa), más 4 FAQs con `<details name="faq-accordion">` y Schema `FAQPage`.
2. **[x] Artículo Nuevo Autoridad SEO (Slug corto de 5 palabras · 0% Canibalización · 0 Enlaces Fantasma):**
   - **Slug:** `/blog/errores-google-search-console-seo/`
   - **Título:** *Errores de Google Search Console en Argentina: Cómo Solucionarlos y Subir Posiciones* (155 guías activas en `/blog/`, 13 en categoría SEO y 173 URLs en `sitemap.xml`).

### [x] Miércoles 11/11 — Eje Diseño Web y Localidades (Regla #16) (Completado)
1. **[x] Cirugía Geográfica de Alta Impresión (Usando datos de GSC sin pedir CSV):**
   - **Boost 1 (`/blog/diseno-web-mendoza/` — `55` impresiones en GSC para `'diseño web mendoza'` y `'diseño web en mendoza'`):** `<title>` acortado de 78 a 50 caracteres (`Diseño Web en Mendoza: Precios y Google Maps 2026`), `dateModified` actualizado al 11/11/2026, inyectado Google Tag GA4 en `<head>`, sumada la 4ta FAQ interactiva (`¿Cuánto tarda el desarrollo de una página web en Mendoza y qué necesito enviar?`) con `<details name="faq-accordion">` y `FAQPage` Schema, y reforzado el interlinking con San Rafael, San Luis y Auditoría SEO.
   - **Boost 2 (`/blog/diseno-web-san-luis/` — `25` impresiones en GSC para `'diseño web san luis'`):** `<title>` acortado de 77 a 52 caracteres (`Diseño Web en San Luis: Precios y Google Maps 2026`), `dateModified` actualizado al 11/11/2026, inyectado Google Tag GA4 en `<head>`, sumada la 4ta FAQ interactiva (`¿Cuánto demora hacer una página web en San Luis y qué incluye el mantenimiento?`) con `<details name="faq-accordion">` y `FAQPage` Schema.
2. **[x] Artículo Nuevo Ciudad Específica (Slug corto de 5 palabras · Regla #16 · 0% Canibalización · 0 Enlaces Fantasma):**
   - **Slug:** `/blog/diseno-web-villa-carlos-paz/`
   - **Título:** *Diseño Web en Villa Carlos Paz: Turismo, Hoteles y Comercios* (156 guías activas en `/blog/`, 40 en categoría Google Maps y 174 URLs en `sitemap.xml`).
   - **Enfoque de Negocio:** Valle de Punilla, reservas directas a WhatsApp sin pagar 15% a 22% a Booking/Airbnb, gastronomía en Costanera y San Martín, teatros y comercios locales. Imagen editorial propia (`guia_diseno_web_villa_carlos_paz.png`). Enlaces entrantes desde `/blog/diseno-web-cordoba/` y `/blog/diseno-web-villa-maria/`.

### [x] Miércoles 11/11 (Noche) — Kickoff del Sprint de Autoridad SEO (Batch 1: 6 Guías Técnicas Publicadas)
> **Sprint de Alta Velocidad (6 Guías Diarias hasta el Sábado):** Para acelerar el posicionamiento del sitio web y ganar autoridad temática masiva (Topical Authority) en Google y LLMs en Argentina, se publican 6 artículos diarios de especialidad técnica y estratégica canalizando autoridad hacia `/auditoria-seo/`.

1. **[x] Guía 1 (SEO Técnico / Datos Estructurados):**
   - **Slug:** `/blog/schema-markup-datos-estructurados-seo/` (5 palabras)
   - **Título:** *Schema Markup y Datos Estructurados: Guía Práctica 2026*
   - **Imagen:** `guia_schema_markup_datos_estructurados_seo.png` (438 KB). JSON-LD `LocalBusiness`, `FAQPage`, `Product`, rich snippets y citación en IA.
2. **[x] Guía 2 (SEO On-Page / Prevención de Canibalización):**
   - **Slug:** `/blog/canibalizacion-palabras-clave-seo/` (4 palabras)
   - **Título:** *Canibalización de Palabras Clave: Cómo Curarla en Google*
   - **Imagen:** `guia_canibalizacion_palabras_clave_seo.png` (355 KB). Detección en Search Console, técnica de *Keyword Absorbing* y redirección para consolidar rankings.
3. **[x] Guía 3 (SEO Off-Page / Autoridad y Prensa):**
   - **Slug:** `/blog/link-building-menciones-prensa-argentina/` (5 palabras)
   - **Título:** *Link Building y Menciones de Prensa en Argentina: Guía SEO*
   - **Imagen:** `guia_link_building_menciones_prensa_argentina.png` (439 KB). Digital PR, notas en medios provinciales/nacionales, directorios colegiados y Brand Mentions para GEO.
4. **[x] Guía 4 (SEO Técnico / Rastreo e Indexación):**
   - **Slug:** `/blog/robots-txt-sitemap-xml-seo/` (5 palabras)
   - **Título:** *Robots.txt y Sitemap XML en SEO: Guía Práctica 2026*
   - **Imagen:** `guia_robots_txt_sitemap_xml_seo.png` (406 KB). Directivas de User-agent, crawl budget, sitemap en producción y prevención de desindexación.
5. **[x] Guía 5 (SEO Técnico / Canónicas y Redirecciones):**
   - **Slug:** `/blog/etiqueta-canonica-redireccion-301-seo/` (5 palabras)
   - **Título:** *Etiqueta Canónica y Redirección 301 en SEO: Guía 2026*
   - **Imagen:** `guia_etiqueta_canonica_redireccion_301_seo.png` (385 KB). Resolución de "Página alternativa con canónica adecuada", cadenas 301 y prevención de duplicados.
6. **[x] Guía 6 (SEO On-Page / Arquitectura y Silos):**
   - **Slug:** `/blog/enlazado-interno-silos-seo/` (4 palabras)
   - **Título:** *Enlazado Interno y Silos en SEO: Cómo Guiar a Google 2026*
   - **Imagen:** `guia_enlazado_interno_silos_seo.png` (407 KB). Topic Clusters, distribución de PageRank, anchor text contextual y eliminación de páginas huérfanas.
- **Inventario Total Actualizado:** **162 guías activas** en `/blog/index.html` (19 en categoría Especialista SEO) y **180 URLs canónicas** en `sitemap.xml` / `public/sitemap.xml`. Notificadas con status `200 OK` en Google Indexing API v3, `202 Accepted` en IndexNow y `SubmitFeed OK` en Bing.

### Jueves 12/11 — Eje Especialista SEO por Rubro & Sprint Día 2 (COMPLETADO)
1. **Cirugía SEO E-Commerce (Pos 4.7–8.0 en GSC para 'tiendanube cobra comision por venta' - COMPLETADO):**
   - Boost aplicado a `/blog/precios-comisiones-tiendanube-alternativas-argentina/` con título acortado a 60 caracteres, inyección de la consulta exacta en H2 y meta description, 4ta FAQ interactiva y schema actualizado.
2. **Cirugía Diseño Web Bariloche (Pos 11.3 en GSC para 'desarrollo de sitios web profesionales bariloche' - COMPLETADO):**
   - Boost aplicado a `/blog/diseno-web-bariloche/` con título acortado a 55 caracteres, inyección de Google Tag GA4 faltante, 4ta FAQ interactiva y ajuste de contraste en acordeones.
3. **Sprint de Autoridad SEO Día 2 — 6 Nuevos Artículos Técnicos Publicados (COMPLETADO):**
   - `/blog/seo-medicos-clinicas-argentina/`
   - `/blog/seo-local-google-maps-argentina/`
   - `/blog/consultor-seo-vs-agencia-argentina/`
   - `/blog/seo-on-page-checklist-optimizacion/`
   - `/blog/keyword-research-palabras-clave-argentina/`
   - `/blog/optimizar-imagenes-seo-peso-webp/`
   - 6 fotos editoriales auténticas cuantizadas a 256 colores (&lt; 490 KB), dual-sync en `images/` y `public/images/`.
   - Contadores actualizados: 168 guías activas (25 en SEO) y 186 URLs canónicas en ambos sitemaps.
   - Notificadas las 10 URLs a Google Indexing API v3 (200 OK), GSC Sitemap, IndexNow (202 Accepted) y Bing Webmaster (200 OK).

### Viernes 13/11 — Eje Diseño Web, Demos y Embudos
1. **Cirugía de Conversión + Boost por Solapamiento (71%):**
   - **Boost 1 (Alta Impresión — 395 impr):** `/blog/como-registrar-dominio-com-ar-nic-argentina/` inyectando `'comprar dominio .ar'` y `'registro de dominios .ar'`.
   - **Boost 2 (Keyword Absorbing 71%):** `/blog/paginas-web-empresas-limpieza-finales-obra-tapizados/` sumando los H2 y FAQs de *limpieza de oficinas, consorcios y abonos corporativos*.
2. **Artículo Nuevo Diseño Web Rubro B2B (Slug corto de 4 palabras · 0% Canibalización):**
   - **Slug:** `/blog/paginas-web-logistica-transporte/`
   - **Título:** *Páginas Web para Empresas de Logística y Transporte de Carga en Argentina*

### Sábado 14/11 — Eje Especialista SEO Local, Maps y Analítica
1. **Artículo Nuevo SEO Local (Slug corto de 5 palabras · 0% Canibalización):**
   - **Slug:** `/blog/conseguir-resenas-google-maps-seo/`
   - **Título:** *Cómo Conseguir Más Reseñas en Google Maps con QR y Subir al Top 3 Local*

---

## 5. Próximo Comando Dominical Programado (Domingo 15 de Noviembre de 2026)
- Ejecutar `python scratch/sunday_seo_command.py` (GSC + Bing Webmaster Tools + GA4 + SerpBear).
- Evaluar la primera semana de conversiones con los 6 nuevos eventos de GA4 (`generate_lead`, `whatsapp_click`, `view_demo`, `faq_expand`, `article_read_75`).
- Definir el Plan de Ataque de la Semana 2 (16/11 al 21/11).
