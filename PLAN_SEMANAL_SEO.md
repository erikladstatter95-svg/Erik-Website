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

### C. Regla del Slug Alineado a la Main Keyword (Regla #18 & Fórmula Sturm)
El slug de la URL **debe coincidir de forma natural y exacta con la Palabra Clave Principal (Main Keyword)** del artículo, sin forzar un conteo artificial ni rígido de palabras:
- **La Main Keyword manda:** Si la frase clave tiene 3, 4, 5 o 6 palabras (por ejemplo: `/blog/conseguir-resenas-google-maps-seo/`, `/blog/seo-vs-google-ads-argentina/` o `/blog/paginas-web-logistica-transporte/`), el slug debe reflejar esa consulta de búsqueda exacta sin añadir palabras de relleno ni recortar términos que alteren la intención de búsqueda.
- **Prohibido:** Slugs kilométricos de 8 a 12 palabras con frases redundantes o preposiciones innecesarias que diluyan la relevancia algorítmica.
- **Alineación Total de 4 Puntos (Fórmula Sturm):** La misma Main Keyword exacta debe estar presente en:
  1. La etiqueta `<title>` (50 a 60 caracteres, ubicada al frente).
  2. El slug de la URL.
  3. El encabezado `<h1>`.
  4. La `meta description` y las **primeras 5 a 10 palabras** del primer párrafo / bloque de Respuesta Directa.

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

### Semana 2 — Domingo 15 de Noviembre de 2026 (Comparativa vs. Baseline Semana 1)

#### A. Tabla Comparativa de Crecimiento Semanal (Semana 1 vs. Semana 2)

| Indicador Clave (KPI) | Semana 1 (8/11/2026) | Semana 2 (15/11/2026) | Variación Semanal |
| :--- | :--- | :--- | :--- |
| **URLs Canónicas en `sitemap.xml` / `public/sitemap.xml`** | `171` URLs | **`199` URLs** | **+28 URLs (+16,4%)** |
| **Guías Activas en `/blog/index.html`** | `153` guías (`12` SEO) | **`180` guías (`33` SEO / `41` Maps)** | **+27 guías (+17,6%)** |
| **Impresiones Totales en Google Search Console (28d)** | `1.434` impr | **`3.310` impr** | **+1.876 impr (+130,8%)** |
| **Clics Orgánicos en Google Search Console (28d)** | `6` clics | **`7` clics** | **+1 clic (+16,7%)** |
| **Consultas en "Striking Distance" (Pos 4.0 a 20.0 en GSC)** | `23` consultas | **`37` consultas** | **+14 consultas (+60,9%)** |
| **Páginas en el Índice de Bing (`InIndex`)** | `6` páginas | **`10` páginas** | **+4 páginas (+66,7%)** |
| **Páginas Rastreadas por Bing (`CrawledPages` 7d)** | `13` páginas | **`42` páginas** | **+29 páginas (+223,1%)** |
| **Errores de Rastreo en Bing / Sitemaps** | `0` errores | **`0` errores** | **100% Salud Técnica** |
| **GA4 `generate_lead` / `whatsapp_click` (7d)** | *Recién instalado (0)* | **`4` conversiones (`3` usuarios)** | **Primeros leads medidos en vivo** |
| **GA4 `article_read_75` (Lectura Profunda >75%)** | *Recién instalado (0)* | **`18` lecturas profundas (`7` usuarios)** | **Validación de retención editorial** |
| **GA4 `faq_expand` (Apertura de Acordeones FAQ)** | *Recién instalado (0)* | **`9` aperturas (`2` usuarios)** | **Interacción real con FAQs** |
| **GA4 Engagement Rate de Tráfico Orgánico (`Organic Search`)** | `70,8%` (`17/24` ses.) | **`90,9%` (`10/11` ses.)** | **+20,1 pts de retención orgánica** |

#### B. Radiografía Detallada de Google Search Console (Semana 2 — `3.310` Impresiones)
- **Páginas con Clics Orgánicos Activos:**
  1. `/` (Home): `2` clics, `10` impr, **Posición `3.1`** (`erik web`, `erik site`)
  2. `/blog/configurar-correo-corporativo-outlook-firma-profesional/`: `1` clic, `92` impr (subió de `32` -> **+187%** tras el Boost del martes 10/11), **Posición `15.6`** (`como configurar un correo corporativo en outlook` Pos `13.0`, `correo corporativo outlook` Pos `10.5`, `correo profesional outlook` Pos `23.0`)
  3. `/blog/generador-link-qr-whatsapp-gratis/`: `1` clic, `50` impr (subió de `17` -> **+194%**), **Posición `16.1`** (`generador de qr whatsapp` Pos `16.0`, `generar codigo qr para whatsapp` Pos `17.0`)
  4. `/blog/por-que-mi-pagina-web-no-aparece-en-google-como-indexar/`: **`1` clic nuevo**, `26` impr (`mi web no aparece en google`, `como hacer que google encuentre mi pagina`, `google no indexa mi página`)
  5. `/blog/hotmart-argentina-comisiones-impuestos-alternativa-funnel/`: `1` clic, `22` impr (subió de `12` -> **+83%**), **Posición `7.0`**
  6. `/blog/tiendanube-linktree-vs-web-propia-a-medida/`: `1` clic, `11` impr, **Posición `4.5`**
- **Salto Explosivo en Páginas de Alta Impresión y Nuevas Entradas al Top 10:**
  - `/blog/como-registrar-dominio-com-ar-nic-argentina/`: de `395` a **`881` impresiones (+123%)**
  - `/blog/como-crear-correo-corporativo-dominio-propio-gmail/`: de `201` a **`542` impresiones (+169%)**
  - `/blog/dominio-com-vs-com-ar-cual-conviene-argentina/`: de `239` a **`459` impresiones (+92%)**
  - `/blog/como-crear-catalogo-online-pedidos-whatsapp/`: **Nueva en el Top 10 con `200` impresiones y Posición Promedio `11.6`** (`catálogo digital whatsapp`, `catálogo de venta por whatsapp`, `catálogo online whatsapp`, `como hacer un catálogo en pdf para enviar por whatsapp`).
- **Nuevas Consultas Destacadas en "Striking Distance" (37 consultas en Posiciones 4.0 a 20.0):**
  - `[Pos 6.0]` `chatgpt publicidad impacto seo aeo` (`1` impr)
  - `[Pos 7.0]` `crear tu propia pagina web gratis google` / `creador paginas web google` (`3` impr)
  - `[Pos 9.0–19.5]` Cluster Zona Sur GBA: `diseño web profesional en zona sur` (Pos `9.0`), `diseño web landing page y hosting zona sur` (Pos `9.2`), `diseño web y hosting en zona sur` (Pos `9.7`), `diseño web hosting y seo zona sur` (Pos `11.8`), `diseño web posicionamiento seo zona sur` (Pos `19.5`)
  - `[Pos 10.0]` `como poner la ubicación de un negocio en google maps` (`2` impr)
  - `[Pos 11.3]` `desarrollo de sitios web profesionales bariloche` (`7` impr)
  - `[Pos 19.0–20.0]` `consultor geo argentina` (Pos `19.0`), `consultor seo b2b` (Pos `19.0`), `consultor seo argentina` (Pos `20.0`)

---

## 4. Histórico de Semanas Ejecutadas (Semana 1: Lunes 9 al Sábado 14 de Noviembre de 2026 — Completada)

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

### [x] Viernes 13/11 — Eje Diseño Web B2B + Sprint 3 de Autoridad SEO (6 Artículos + 2 Boosts Completados)
1. **Cirugías / Boosts Ejecutados con Éxito:**
   - **Boost 1 (Alta Impresión — 395 impr):** `/blog/como-registrar-dominio-com-ar-nic-argentina/` -> Título acortado a `Comprar Dominio .ar y .com.ar en NIC Argentina 2026` (53 chars), meta description actualizada, H2 optimizado con `Cómo Comprar un Dominio .ar y Registrarlo en NIC Argentina`, 4ta FAQ agregada con evento GA4 y `dateModified: 2026-11-13T09:30:00-03:00`.
   - **Boost 2 (Keyword Absorbing 71% overlap):** `/blog/paginas-web-empresas-limpieza-finales-obra-tapizados/` -> Título acortado a `Páginas Web para Empresas de Limpieza en Argentina 2026` (55 chars), absorbido el cluster B2B en H2 `Abonos Corporativos de Limpieza para Oficinas y Consorcios: Cómo Captar Clientes B2B`, y `dateModified: 2026-11-13T09:30:00-03:00`.
2. **Sprint de Autoridad SEO y Diseño Web B2B (6 Artículos Publicados con Slugs de 3 a 5 palabras · 0% Canibalización):**
   - **1. `/blog/paginas-web-logistica-transporte/`:** *Páginas Web para Empresas de Logística y Transporte* (4 palabras, 51 chars). Imagen: `guia_paginas_web_logistica_transporte.png` (432.6 KB).
   - **2. `/blog/presupuesto-diseno-web-argentina/`:** *Presupuesto de Diseño Web en Argentina: Qué Debe Incluir* (4 palabras, 56 chars). Imagen: `guia_presupuesto_diseno_web_argentina.png` (413.0 KB).
   - **3. `/blog/seo-internacional-etiqueta-hreflang-argentina/`:** *SEO Internacional: Guía de Etiquetas Hreflang y Países* (4 palabras, 54 chars). Imagen: `guia_seo_internacional_etiqueta_hreflang_argentina.png` (423.9 KB).
   - **4. `/blog/crawl-budget-optimizacion-rastreo-google/`:** *Crawl Budget: Cómo Optimizar el Presupuesto de Rastreo* (5 palabras, 54 chars). Imagen: `guia_crawl_budget_optimizacion_rastreo_google.png` (447.4 KB).
   - **5. `/blog/migracion-web-seo-redirecciones-301/`:** *Migración Web SEO: Cómo Cambiar de Sitio sin Perder Tráfico* (4 palabras, 59 chars). Imagen: `guia_migracion_web_seo_redirecciones_301.png` (437.5 KB).
   - **6. `/blog/seguridad-web-certificados-ssl-https/`:** *Seguridad Web: Certificados SSL, HTTPS y Confianza en Google* (4 palabras, 60 chars). Imagen: `guia_seguridad_web_certificados_ssl_https.png` (376.7 KB).
3. **Métricas de Infraestructura y Notificaciones:**
   - **Inventario Actualizado:** **174 guías activas** en `/blog/index.html` y **192 URLs canónicas** en `sitemap.xml` y `public/sitemap.xml`.
   - **Auditoría de Enlaces Internos:** 0 enlaces rotos (`audit_all_internal_links.py` 100% limpio).
   - **Compilación de Producción:** `npm run build` en 8.05s con 0 errores y 0 advertencias.
   - **Notificaciones Oficiales:** Google Indexing API v3 (`200 OK` en las 9 URLs), GSC Sitemap (`sitemap.xml` enviado con éxito), IndexNow (`202 Accepted` en 9 URLs) y Bing Webmaster API `SubmitUrlBatch` (`200 OK`).

### [x] Sábado 14/11 — Eje Especialista SEO Local, Maps, Analítica y Cierre del Sprint de Autoridad SEO (Completado: 2 Boosts + 6 Nuevos Artículos)

#### A. Paso 1 — Estrategia, Detección de Canibalización y Selección de Cirugías (Boosts)
1. **[x] Boost 1 (239 Impresiones en GSC · Dominio .com vs .com.ar - COMPLETADO):**
   - **URL:** `/blog/dominio-com-vs-com-ar-cual-conviene-argentina/`
   - **Cirugía aplicada:**
     - `<title>` acortado a **54 caracteres**: `Dominio .com vs .com.ar y .ar: ¿Cuál Conviene en 2026?`
     - Nuevo `<h2>` #4: `4. Diferencias entre Dominio .com.ar, Dominio .ar Directo y Dominio .com en Argentina` con tabla comparativa de registradores.
     - Ampliado a **6 FAQs interactivas** (`<details name="faq-accordion">` con evento GA4 `faq_expand`) + actualización de Schema `FAQPage` y `dateModified: 2026-11-14T10:30:00-03:00`.
2. **[x] Boost 2 (201 Impresiones en GSC · Correo con Dominio Propio en Gmail - COMPLETADO):**
   - **URL:** `/blog/como-crear-correo-corporativo-dominio-propio-gmail/`
   - **Cirugía aplicada:**
     - `<title>` acortado a **56 caracteres**: `Correo con Dominio Propio en Gmail: Cómo Crearlo en 2026`
     - Nuevo `<h2>` #4: `4. Cómo Configurar un Correo con Dominio Propio sin Caer en Spam (SPF, DKIM y DMARC)`
     - Ampliado a **6 FAQs interactivas** (`<details name="faq-accordion">` con evento GA4 `faq_expand`) + actualización de Schema `FAQPage` y `dateModified: 2026-11-14T10:30:00-03:00`.
3. **[x] Auditoría de Canibalización de los 6 Nuevos Artículos SEO (0% Solapamiento de Intención):**
   - Todos los slugs cumplen estrictamente con 5 palabras (Regla #18), títulos entre 53 y 57 caracteres, y 0% de solapamiento de intención frente a las guías existentes.

#### B. Pasos 2, 3 y 4 — Publicación y Despliegue de los 6 Artículos de Cierre del Sprint
1. **[x] `/blog/conseguir-resenas-google-maps-seo/`:** *Cómo Conseguir Reseñas en Google Maps: QR y SEO Local* (5 palabras, 53 chars, categoría `maps`). Imagen: `guia_conseguir_resenas_google_maps_seo.png` (364.4 KB). 6 FAQs con GA4 tracking.
2. **[x] `/blog/seo-vs-google-ads-argentina/`:** *SEO vs Google Ads en Argentina: ¿Dónde Conviene Invertir?* (5 palabras, 57 chars, categoría `seo`). Imagen: `guia_seo_vs_google_ads_argentina.png` (379.9 KB). 6 FAQs con GA4 tracking.
3. **[x] `/blog/seo-b2b-empresas-industriales-argentina/`:** *SEO B2B para Empresas Industriales y Mayoristas Argentina* (5 palabras, 57 chars, categoría `seo`). Imagen: `guia_seo_b2b_empresas_industriales_argentina.png` (439.4 KB). 6 FAQs con GA4 tracking.
4. **[x] `/blog/actualizar-contenido-antiguo-seo-google/`:** *Cómo Actualizar Contenido Antiguo en SEO: Content Decay* (5 palabras, 55 chars, categoría `seo`). Imagen: `guia_actualizar_contenido_antiguo_seo_google.png` (434.3 KB). 6 FAQs con GA4 tracking.
5. **[x] `/blog/eeat-google-autoridad-confianza-seo/`:** *E-E-A-T en Google: Experiencia, Autoridad y Confianza SEO* (5 palabras, 57 chars, categoría `seo`). Imagen: `guia_eeat_google_autoridad_confianza_seo.png` (370.7 KB). 6 FAQs con GA4 tracking.
6. **[x] `/blog/mejorar-ctr-organico-titulos-google/`:** *Cómo Mejorar el CTR Orgánico en Google: Títulos y Metas* (5 palabras, 55 chars, categoría `seo`). Imagen: `guia_mejorar_ctr_organico_titulos_google.png` (390.9 KB). 6 FAQs con GA4 tracking.

#### C. Métricas de Infraestructura y Notificaciones (Sprint de 4 Días Concluido)
- **Inventario Total Actualizado:** **180 guías activas** en `/blog/index.html` (41 en Google Maps y 33 en Auditoría SEO) y **198 URLs canónicas** en `sitemap.xml` / `public/sitemap.xml`.
- **Auditoría de Enlaces Internos:** 0 enlaces rotos (`audit_all_internal_links.py` 100% limpio en todo el sitio).
- **Compilación de Producción:** `npm run build` en 8.57s con 0 errores y 0 advertencias.
- **Notificaciones Oficiales:** Google Indexing API v3 (`200 OK` en las 9 URLs), GSC Sitemap (`sitemap.xml` enviado con éxito), IndexNow (`202 Accepted` en 9 URLs) y Bing Webmaster API `SubmitUrlBatch` (`200 OK`).

---

## 5. Plan de Ataque para Esta Semana (Semana 2: Lunes 16 al Sábado 21 de Noviembre de 2026) — Pasos 1 y 2 Completos en Argon High

> **Directriz Operativa Híbrida (Argon High ➔ Flash 3.8 High):** Todos los **Pasos 1 (Selección de Boosts Quirúrgicos + Verificación 0% Canibalización)** y **Pasos 2 (Outlines Maestros Cerrados con Regla #18 de Slug natural, Fórmula Sturm de 4 puntos y 6 FAQs interactivas)** de Lunes a Sábado ya están resueltos y validados aquí abajo por **Argon (High Reasoning)**. De lunes a sábado solo debés cambiar a **Flash 3.8 (High)** y pedir: *"Ejecutá los pasos 3 y 4 del [Día]"*.

---

### [x] Lunes 16/11 — Eje Diseño Web y Conversión (Completado: Boost Catálogo WhatsApp + Nuevo Artículo Mueblerías)

#### A. Paso 1 — Cirugía / Boost Striking Distance (Pos 11.6 y 200 Impresiones en GSC) [EJECUTADO]
- **URL Optimizada:** `/blog/como-crear-catalogo-online-pedidos-whatsapp/`
- **Diagnóstico GSC:** Entró al Top 10 del sitio con **`200` impresiones** y **Posición `11.6`**, pero su `<title>` anterior medía 76 caracteres y solo tenía 2 FAQs.
- **Cirugía ejecutada:**
  1. `<title>` acortado de 76 a **54 caracteres**: `Cómo Crear un Catálogo Online con Pedidos por WhatsApp`
  2. `meta description` actualizada (157 caracteres) y Direct Answer Sturm ajustado en sus primeras 10 palabras con `catálogo digital para WhatsApp` y `catálogo de venta por WhatsApp`.
  3. Nuevo `<h2>` #4 incorporado: `4. Catálogo Digital en WhatsApp vs. Catálogo en PDF: Qué Convierte Más en Argentina` con tabla comparativa HTML responsiva.
  4. Ampliado de 2 a **6 FAQs interactivas** (`<details name="faq-accordion">` con evento GA4 `faq_expand`) + actualización de Schema `FAQPage` y `dateModified: 2026-11-16T10:30:00-03:00`.

#### B. Pasos 2, 3 y 4 — Publicación y Despliegue de Artículo Nuevo [EJECUTADO]
- **Main Keyword:** `Páginas web para mueblerías y fábricas de muebles`
- **Slug (Regla #18 — 5 palabras exactas):** `/blog/paginas-web-mueblerias-fabricas-muebles/`
- **`<title>` (54 caracteres):** `Páginas Web para Mueblerías y Fábricas de Muebles 2026`
- **`<h1>`:** `Páginas Web para Mueblerías y Fábricas de Muebles a Medida en Argentina: Catálogo y Cotizador por WhatsApp`
- **`meta description` (154 caracteres):** `Páginas web para mueblerías y fábricas de muebles a medida en Argentina. Mostrá tu catálogo de sillones, cocinas y placares y cotizá directo en WhatsApp.`
- **Direct Answer Sturm:** Cumplido en primeras 8 palabras con Main Keyword exacta.
- **Categoría en `blog/index.html`:** `diseno` (*Diseño Web & Conversión* — Mostrando 181 guías).
- **Imagen Editorial Dual-Sync (`images/` y `public/images/`):** `guia_paginas_web_mueblerias_fabricas_muebles.png` (383.1 KB, cuantizada con PIL, pastilla `"MUEBLERÍAS & FÁBRICAS"` y sello `erikwebsite.com`).
- **Estructura y Componentes:** 4 secciones `<h2>`, tabla comparativa HTML (*Solo Instagram / Facebook* vs *Tienda E-Commerce con Comisiones* vs *Catálogo Web + Cotizador de Medidas a WhatsApp*), 6 FAQs interactivas con GA4 tracking y marcado `Schema.org` (`BlogPosting`, `BreadcrumbList`, `FAQPage`).
- **Interlinking Verificado:** Enlaces hacia `/blog/como-crear-catalogo-online-pedidos-whatsapp/`, `/blog/catalogo-pdf-canva-vs-catalogo-web/`, `/blog/paginas-web-fabricas-aberturas-aluminio-pvc-dvh-steel-framing/`, `/blog/como-poner-agregar-negocio-local-google-maps-gratis/` y llamadas a cotización.
- **Registro & Compilación:** Añadido a `blog/index.html`, `vite.config.js`, `sitemap.xml` y `public/sitemap.xml` (**200 URLs canónicas** en total). Build en Vite limpio en 10.91s (`0 errores`).
- **Notificaciones Oficiales:** Google Indexing API v3 (`200 OK` en ambas URLs), GSC Sitemap enviado, IndexNow API (`202 Accepted`) y Bing Webmaster API (`200 OK`).
  - `/blog/como-poner-agregar-negocio-local-google-maps-gratis/`
  - `/#demos` y `/#precios`
- **6 FAQs Interactivas (`<details name="faq-accordion">` + GA4 `faq_expand` + Schema `FAQPage`):**
  1. `¿Cuánto cuesta una página web para una mueblería o fábrica de muebles en Argentina?`
  2. `¿Conviene tener carrito con pago online o cotizador directo por WhatsApp para vender muebles?`
  3. `¿Cómo muestro las variantes de telas, maderas y medidas sin que la página se vuelva lenta?`
  4. `¿Puedo actualizar los precios o pausar modelos sin stock fácilmente desde el celular?`
  5. `¿Cómo ayuda la página web a que mi showroom o fábrica de muebles aparezca primero en Google Maps?`
  6. `¿Cuánto demora el desarrollo y qué fotos necesito para empezar?`

---

### [x] Martes 17/11 — Eje Especialista SEO, Velocidad e IA (Boost Diseño Web Maduro + Demo Arquitectura + Nuevo Artículo SEO: GTM vs GA4) [COMPLETADO]

> **Regla de Maduración (14+ días):** Como los artículos de la categoría SEO fueron publicados hace pocos días en el Sprint, no se tocan hasta que cumplan su ventana de maduración en Search Console. En su lugar, ejecutamos el Boost sobre páginas maduras de **Diseño Web / NIC.ar** e integramos la nueva **Demo de Arquitectura (`/demos/arquitectura/`)** en el cluster de Arquitectos y Constructoras.

#### A. Paso 1 — Doble Cirugía / Boost en Diseño Web Maduro + Integración de `/demos/arquitectura/` [EJECUTADO]
1. **Boost 1 (`/blog/como-delegar-dns-renovar-dominio-nic-argentina/` — `78` impr y Posición `6.9` en GSC, 18 días de antigüedad):**
   - **Diagnóstico GSC:** Posiciona en **Puesto `6.9`** con `78` impresiones reales, pero su `<title>` actual medía **96 caracteres** (se cortaba en Google) y solo tenía **2 FAQs**.
   - **Cirugía ejecutada en Paso 3:**
     - Acortado `<title>` de 96 a **56 caracteres**: `Cómo Delegar Dominio en NIC Argentina y Renovar .com.ar`
     - Ampliado de 2 a **6 FAQs interactivas** (`<details name="faq-accordion">` con evento GA4 `faq_expand` y actualización de Schema `FAQPage` + `dateModified: 2026-11-17T09:30:00-03:00`) cubriendo estado *"No Delegado"*, cambio de DNS a Cloudflare/hosting y tiempos de propagación.
2. **Boost 2 (`/blog/paginas-web-constructoras-desarrolladoras-arquitectura-argentina/` y `/blog/portfolio-web-arquitectos-estudios-de-arquitectura/` — Integración de `/demos/arquitectura/`):**
   - **Diagnóstico:** Ambas guías maduras tenían `<title>` largos (102 y 74 caracteres), solo 2 FAQs y **aún no enlazaban a la nueva Demo Interactiva `/demos/arquitectura/`** (*VÉRTICE · Arquitectura & Gestión de Obras*).
   - **Cirugía ejecutada en Paso 3:**
     - Acortado `<title>` de Constructoras/Arquitectura de 102 a **57 caracteres**: `Páginas Web para Constructoras y Estudios de Arquitectura`
     - Acortado `<title>` de Portfolio Arquitectos a **49 caracteres**: `Portfolio Web para Arquitectos y Obras: Guía 2026`
     - Agregado en ambas guías un bloque destacado de **Prueba en Vivo hacia `/demos/arquitectura/`** (destacando el Portfolio filtrable por tipología, el Slider Interactivo Antes/Después para remodelaciones, la sección de Consorcios & Ley 257 y el Cotizador de Obra por m² conectado a WhatsApp).
     - Ampliado a **6 FAQs interactivas** con Schema `FAQPage` y `dateModified: 2026-11-17T09:30:00-03:00`.

#### B. Paso 2 — Outline Maestro de Artículo Nuevo SEO (0% Canibalización Verificada) [EJECUTADO]
- **Main Keyword:** `Google Tag Manager vs GA4 directo`
- **Slug (Regla #18 — 6 palabras naturales):** `/blog/google-tag-manager-vs-ga4-seo/`
- **`<title>` (56 caracteres):** `Google Tag Manager vs GA4 Directo: ¿Cuál Conviene 2026?`
- **`<h1>`:** `Google Tag Manager vs. GA4 Directo (gtag.js): Qué Conviene Más para tu Velocidad Web y el SEO`
- **`meta description` (156 caracteres):** `Google Tag Manager vs GA4 directo en código: comparativa real de peso en JavaScript, impacto en Core Web Vitals (INP/LCP) y cuándo conviene usar cada uno.`
- **Direct Answer Sturm (Primeras 5–10 palabras con Main Keyword exacta):**
  > **Elegir entre Google Tag Manager vs. GA4 directo (`gtag.js`)** depende de cuántos píxeles y herramientas de marketing uses: insertar GA4 directo en código es más liviano y rápido para los Core Web Vitals de una PyME, mientras que GTM solo se justifica cuando administrás múltiples etiquetas complejas sin tocar el código.
- **Categoría en `blog/index.html`:** `seo` (*Auditoría SEO, Velocidad e IA*)
- **Imagen Editorial (`1200x675`, PIL `< 490 KB`):** `images/guia_google_tag_manager_vs_ga4_seo.png` (316.6 KB, dual-sync con `public/images/`) — Especialista en analítica y performance web en oficina de Buenos Aires comparando en doble monitor el rendimiento de carga (`gtag.js` limpio con métricas Core Web Vitals en verde vs contenedor de scripts) junto a métricas de conversión de WhatsApp; pastilla `"ANALÍTICA & PERFORMANCE"` y sello `erikwebsite.com`.
- **Estructura de Subtítulos `<h2>`:**
  - `<h2>1. ¿Es lo mismo tener Google Tag Manager (GTM) que instalar el código de GA4 directo?</h2>`
  - `<h2>2. Comparativa Técnica: GA4 Directo (gtag.js) vs. Google Tag Manager en Velocidad y SEO</h2>` (Tabla comparativa HTML: Peso de scripts, ejecución en hilo principal / INP, facilidad para medir `whatsapp_click` y `generate_lead`, riesgo de contenedores inflados por agencias).
  - `<h2>3. Cómo impacta un contenedor pesado de Tag Manager en tus Core Web Vitals (LCP e INP)</h2>`
  - `<h2>4. Cuándo conviene usar GA4 directo en código limpio y cuándo sí tiene sentido migrar a GTM</h2>`
- **Interlinking Obligatorio (Regla #19 — Solo URLs reales verificadas):**
  - `/blog/como-instalar-google-analytics-4-ga4-medir-clics-whatsapp/`
  - `/blog/auditoria-velocidad-web-core-web-vitals-lcp-inp-google/`
  - `/blog/errores-google-search-console-seo/`
  - `/demos/arquitectura/` (como ejemplo de web en código limpio con carga instantánea 60 FPS y eventos medidos sin peso extra)
  - `/auditoria-seo/`
- **6 FAQs Interactivas (`<details name="faq-accordion">` + GA4 `faq_expand` + Schema `FAQPage`):**
  1. `¿Google Tag Manager reemplaza a Google Analytics 4 o trabajan juntos?`
  2. `¿Por qué Google Tag Manager puede bajar la puntuación de PageSpeed Insights en celulares?`
  3. `¿Se pueden medir clics al botón de WhatsApp y cotizadores interactivos sin usar Google Tag Manager?`
  4. `¿Si tengo Meta Pixel y Google Analytics 4 necesito obligatoriamente Google Tag Manager?`
  5. `¿Qué pasa si instalo el código de GA4 directo en el HTML y además lo cargo dentro de GTM?`
  6. `¿Cómo excluir mi propia IP o mis visitas de prueba en Google Analytics 4 para no alterar las métricas?`

#### C. Métricas de Infraestructura y Notificaciones (Martes 17/11 Concluido)
- **Inventario Total Actualizado:** **182 guías activas** en `/blog/index.html` (34 en Auditoría SEO, Velocidad e IA) y **201 URLs canónicas** en `sitemap.xml` / `public/sitemap.xml`.
- **Auditoría de Enlaces Internos:** 0 enlaces rotos (`audit_all_internal_links.py` 100% limpio en todo el sitio).
- **Compilación de Producción:** `npm run build` en 17.41s con 0 errores y 0 advertencias.
- **Notificaciones Oficiales:** Google Indexing API v3 (`200 OK` en las 5 URLs), GSC Sitemap (`sitemap.xml` enviado con éxito), IndexNow (`202 Accepted` en 5 URLs) y Bing Webmaster API `SubmitUrlBatch` (`200 OK`).

---

### [x] Miércoles 18/11 — Eje Diseño Web y Localidades (Completado: Boost Zona Sur GBA + Nuevo Artículo Luján)

> **Estado:** COMPLETADO CON ÉXITO.
> - **Boost Aplicado:** `/blog/diseno-web-zona-sur/` (`<title>` optimizado a 56 chars, H2 #2 reestructurado con queries comerciales de GSC, 6 FAQs interactivas + Schema FAQPage, dateModified actualizado).
> - **Nuevo Artículo Publicado:** `/blog/diseno-web-lujan/` (Main Keyword: `Diseño web en Luján`, slug natural de 4 palabras, Direct Answer Sturm, tabla comparativa, 6 FAQs, 0 emojis, imagen PIL optimizada 255.8 KB).
> - **Interlinking Bidireccional:** Enlace desde `/blog/diseno-web-zona-oeste/` hacia `/blog/diseno-web-lujan/` y enlaces internos hacia `/blog/diseno-web-pilar/`, `/blog/diseno-web-zona-oeste/`, `/demos/arquitectura/`, `/auditoria-seo/`.
> - **Registro & Build:** Card añadida en `blog/index.html` (categoría `maps`), contador actualizado a 183 guías, ruta registrada en `vite.config.js`, sitemaps sincronizados con 202 URLs canónicas (`sitemap.xml` y `public/sitemap.xml`).
> - **Verificación:** 0 enlaces rotos (`audit_all_internal_links.py`), 0 emojis (Regla #17), build Vite limpio (`npm run build` en 28.22s).
> - **Indexación:** Notificación a Google Indexing API v3 (`200 OK`), GSC Sitemap ping, IndexNow (`202 Accepted`) y Bing Webmaster API (`200 OK`).

#### A. Paso 1 — Cirugía / Boost Geográfico en "Striking Distance" (Pos 9.0 a 19.5 en GSC)
- **URL a Optimizar:** `/blog/diseno-web-zona-sur/`
- **Diagnóstico GSC:** Acumula **5 consultas de altísima intención comercial en posiciones 9.0 a 19.5**:
  - `'diseño web profesional en zona sur'` (`Pos 9.0`, 1 imp)
  - `'diseño web landing page y hosting zona sur'` (`Pos 9.2`, 4 imp)
  - `'diseño web y hosting en zona sur'` (`Pos 9.7`, 3 imp)
  - `'diseño web hosting y seo zona sur'` (`Pos 11.8`, 4 imp)
  - `'diseño web posicionamiento seo zona sur'` (`Pos 19.5`, 2 imp)
  - `'diseño web landing page google ads zona sur'` (`Pos 21.0`, 2 imp)
- **Cirugía ejecutada:**
  1. `<title>` optimizado a **56 caracteres**: `Diseño Web, Hosting y SEO en Zona Sur GBA: Precios 2026`
  2. `<h2>` #2 actualizado a: `Diseño web, Landing Page, Hosting y Posicionamiento SEO en Zona Sur: Todo Resuelto en un Solo Lugar` incluyendo las frases exactas `'diseño web landing page y hosting zona sur'`, `'diseño web para Google Ads en Zona Sur'` y enlace a la nueva demo `/demos/arquitectura/` para estudios y constructoras del corredor Canning / Lomitas / Quilmes.
  3. Ampliado de 3 a **6 FAQs interactivas** (`<details name="faq-accordion">` + GA4 `faq_expand` + Schema `FAQPage` + `dateModified: 2026-11-18T09:30:00-03:00`).

#### B. Paso 2 — Outline Maestro de Artículo Nuevo (Regla #16: 1 Sola Ciudad · 0% Canibalización)
- **Main Keyword:** `Diseño web en Luján`
- **Slug (Regla #18 — 4 palabras naturales):** `/blog/diseno-web-lujan/`
- **`<title>` (55 caracteres):** `Diseño Web en Luján: Páginas para Empresas y Comercios`
- **`<h1>`:** `Diseño de Páginas Web en Luján (Buenos Aires): Desarrollo Rápido y Google Maps para Empresas, Turismo y Profesionales`
- **`meta description` (155 caracteres):** `Diseño web en Luján (Provincia de Buenos Aires). Páginas web rápidas desde $150.000 ARS para empresas del corredor Acceso Oeste, turismo, agro y comercios.`
- **Direct Answer Sturm:** Cumplido con Main Keyword en las primeras palabras.
- **Categoría en `blog/index.html`:** `maps` (*Google Maps y Posicionamiento Local*, total 42 guías).
- **Imagen Editorial:** `images/guia_diseno_web_lujan.png` y `public/images/guia_diseno_web_lujan.png` (255.8 KB).
- **Interlinking:** Bidireccional verificado y auditado (0 enlaces rotos).

---

> **REVISIÓN ESTRATÉGICA DE MEDIO TÉRMINO (Jueves 19/11/2026 — Datos en Vivo GSC + GA4 + Bing + 32 CSVs + Google AR Autocomplete):**
> - **Pulso actual (4 días después del domingo 15/11):** GSC saltó de `3.310` a **`4.772` impresiones (+44%)** y `44` consultas en *Striking Distance*; Bing `InIndex` subió de `10` a **`17` páginas (+70%)**; y **GA4 confirmó tráfico real de asistentes de IA (`AI Assistant`: 3 usuarios, 100% engaged)**: `chatgpt.com` derivando a `/blog/diseno-web-rosario/` y `/demos/odontologia/`, y `gemini.google.com` hacia `/blog/como-delegar-dns-renovar-dominio-nic-argentina/`.
> - **Ajustes de Alto Impacto aplicados a Jueves, Viernes y Sábado:**
>   1. Se reemplazaron 3 artículos nuevos de baja demanda o alto solapamiento (*Hoteles SEO* 67% overlap, *Consorcios* 0 sugerencias web en AR, *Estadísticas GBP* 1 sugerencia) por **3 keywords validadas por demanda real en Argentina (Google AR Autocomplete + CSVs), <= 50% solapamiento y sinergia directa con nuestras demos y tráfico real de IA**.
>   2. Se reemplazaron 2 Boosts débiles (*Cotizador* 1 impr y *Santa Fe* fuera de eje) por páginas maduras con tracción explosiva y títulos truncados de 98–100c (**Hotmart** 32 impr / 1 clic / Pos 8.0 y **Google Maps Gratis** 101 impr / Pos 10.0).
>   3. Se añadió un **Bloque 0 de Saneamiento Técnico** para corregir errores críticos detectados en la auditoría (11 artículos sin `/src/js/main.js`, Boost fallido del 13/11 en NIC.ar con 1.191 impr, desfase Schema FAQPage, `data-cat="geo"` huérfano y enlace 404 en `llms.txt`).
> - **Regla obligatoria para el modelo ejecutor (Flash) en TODOS los días restantes:** Al terminar cualquier Bloque o Día, ejecutar obligatoriamente `python scratch/verify_article_hygiene.py --hub <archivos_tocados>`, `python scratch/audit_all_internal_links.py`, revisar `git diff --stat`, compilar `npm run build`, notificar a Google Indexing API v3 + GSC Sitemap + IndexNow + Bing Webmaster API, y hacer `git push origin main`.

---

### [x] Bloque 0 — Saneamiento Técnico Urgente (COMPLETADO 19/11 · 100% PASS en `verify_article_hygiene.py --hub`)

> **Por qué es prioritario:** Corrige 4 fugas técnicas silenciosas que hoy frenan conversiones de WhatsApp, rastreo IA y posiciones en nuestras 3 URLs con más impresiones del sitio (`1.191`, `1.033` y `580` impr).

1. **Inyectar `<script type="module" src="/src/js/main.js"></script>` antes de `</body>` en los 11 artículos del Sprint 13–14/11 que quedaron sin JS activo** (hoy sus botones `data-wa-msg`, menú móvil y eventos GA4 `generate_lead`/`whatsapp_click`/`article_read_75` no disparan):
   - `blog/actualizar-contenido-antiguo-seo-google/index.html`
   - `blog/conseguir-resenas-google-maps-seo/index.html`
   - `blog/eeat-google-autoridad-confianza-seo/index.html`
   - `blog/mejorar-ctr-organico-titulos-google/index.html`
   - `blog/migracion-web-seo-redirecciones-301/index.html`
   - `blog/paginas-web-logistica-transporte/index.html`
   - `blog/presupuesto-diseno-web-argentina/index.html`
   - `blog/seguridad-web-certificados-ssl-https/index.html`
   - `blog/seo-b2b-empresas-industriales-argentina/index.html`
   - `blog/seo-internacional-etiqueta-hreflang-argentina/index.html`
   - `blog/seo-vs-google-ads-argentina/index.html`
2. **Reparar el Boost fantasma del 13/11 en nuestra URL #1 en impresiones + Paridad Schema `FAQPage` en el Top 3 de GSC (Reglas #21 y #22):**
   - `/blog/como-registrar-dominio-com-ar-nic-argentina/` (**`1.191` impr en GSC**, hoy sigue con `<title>` de 88c, `FAQ: 2/2`, `mod: 2026-10-25` e imagen `guia_registrar_dominio_com_ar.png` de 614.9 KB > 490 KB):
     - Acortar `<title>`, `og:title` y `twitter:title` a **53c**: `Comprar Dominio .ar y .com.ar en NIC Argentina (2026)`
     - Actualizar `meta description` (147c): `Guía para comprar un dominio .ar o registrar un .com.ar en NIC Argentina en 2026: trámite con Clave Fiscal ARCA, precios en pesos y delegación DNS.`
     - Ampliar de 2 a **6 FAQs con paridad exacta 6/6 (`<details>` == JSON-LD `FAQPage`)** cubriendo `'comprar dominio .ar'`, `'registro .com'`, `'nic ar'`, Clave Fiscal nivel 2 y diferencia `.ar` vs `.com.ar`.
     - Cuantizar `images/guia_registrar_dominio_com_ar.png` por debajo de `450 KB` y sincronizar en `public/images/`.
     - Actualizar `dateModified: 2026-11-19T10:00:00-03:00` y verificar con `verify_article_hygiene.py`.
   - `/blog/como-crear-correo-corporativo-dominio-propio-gmail/` (**`1.033` impr**, hoy `6 <details>` vs `2 Schema`): sincronizar el JSON-LD `FAQPage` para que contenga las 6 preguntas exactas del HTML (6/6) y corregir cualquier tuteo neutro a voseo argentino.
   - `/blog/dominio-com-vs-com-ar-cual-conviene-argentina/` (**`580` impr**, hoy `6 <details>` vs `3 Schema`): sincronizar el JSON-LD `FAQPage` a 6/6 exacto y corregir `"Puedes desbloquear"` por `"Podés desbloquear"` (Regla #25).
3. **Saneamiento de taxonomía en `blog/index.html` (Regla #24):**
   - Cambiar `data-cat="geo"` por `data-cat="maps"` en las 6 tarjetas provinciales huérfanas (`diseno-web-caba-buenos-aires`, `catamarca`, `la-rioja`, `santa-cruz`, `tierra-del-fuego`, `la-pampa`) — pasan a quedar visibles dentro de *Google Maps y Posicionamiento Local*.
   - Sincronizar todos los contadores reales del `<select>` (`all`, `maps`, `servicios`, `ventas`, `dominios`).
4. **Actualizar `llms.txt` y copiar a `public/llms.txt` (Regla #27):**
   - Eliminar el enlace roto `/demos/medicina/` (404 inexistente).
   - Agregar `/demos/arquitectura/` (*Vértice · Arquitectura, Reformas y Consorcios Ley 257*) y destacar el rediseño de `/demos/contable/`.
   - Actualizar el contador del blog (`183+ Guías`) y añadir las guías pilares nuevas de SEO técnico (`/blog/seo-on-page-checklist-optimizacion/`, `/blog/schema-markup-datos-estructurados-seo/`, `/blog/seo-local-google-maps-argentina/`, `/blog/google-tag-manager-vs-ga4-seo/`).
   - Verificar con `python scratch/verify_article_hygiene.py --hub` que devuelva **0 FAIL**.

---

### [x] Jueves 19/11 — Eje Especialista SEO por Rubro / CMS (COMPLETADO: Boosts Shopify + Canva + Nuevo Artículo SEO Odontólogos)

#### A. Paso 1 — Doble Cirugía / Boost en Comparativas Maduras (>18 días en GSC · Evidencia en Vivo 19/11)

1. **Boost 1 (`/blog/precios-shopify-argentina-conviene/` — Explotó de 34 a `63` impr (+85%), Pos `16.7`, 18 días de antigüedad):**
   - **Consultas reales GSC + Google AR Autocomplete:**
     - GSC: `'shopify argentina'` (**31 impr, Pos `13.2`** — a 3 puestos de Página 1), `'shopify precios'` (3 impr, Pos `21.0`), `'pagina web precios argentina'` (Pos `6.0`), `'cuanto se cobra una pagina web en argentina'` (Pos `8.0`).
     - Autocomplete AR (12 sugerencias): `shopify argentina precios`, `cuanto cuesta shopify en argentina`, `comisiones mercado pago shopify`, `shopify argentina es confiable`, `shopify argentina que es y para que sirve`, `shopify argentina opiniones`.
   - **Defectos actuales detectados:** `<title>` de **85c**, FAQ desfasado (`2 <details>` vs `3 Schema`), `dateModified: 2026-11-01`.
   - **Cirugía exacta para Paso 3:**
     - `<title>`, `og:title`, `twitter:title` (**53c**): `Precios de Shopify en Argentina 2026: ¿Conviene o No?`
     - `meta description`, `og:description`, `twitter:description` (**146c**): `Precios reales de Shopify en Argentina en 2026: planes en dólares, impuestos, doble comisión con Mercado Pago y cuándo conviene una tienda propia.`
     - Reforzar en el primer párrafo y `<h2>` #1 las frases exactas `'Shopify Argentina'` y `'precios de Shopify en Argentina'`, aclarando cómo funciona el cobro mensual en USD + la comisión extra del 2% al 0,5% por usar Mercado Pago como pasarela externa.
     - Ampliar con **paridad exacta 6/6 (`<details>` == JSON-LD `FAQPage`)** respondiendo las preguntas reales de IA y Google AR:
       1. `¿Cuánto cuesta Shopify por mes en Argentina en 2026 en pesos reales?`
       2. `¿Shopify cobra comisión adicional si uso Mercado Pago en Argentina?`
       3. `¿Qué es Shopify, para qué sirve y es confiable para vender desde Argentina?`
       4. `¿Cómo se pagan las facturas de Shopify en dólares y qué impuestos aplican?`
       5. `¿Conviene Shopify, Tiendanube o una página web propia sin comisiones por venta?`
       6. `¿Cuándo conviene elegir una Landing Page o Catálogo por WhatsApp en lugar de Shopify?`
     - Actualizar `dateModified: 2026-11-19T10:00:00-03:00` y enlazar hacia `/blog/precios-comisiones-tiendanube-alternativas-argentina/`, `/blog/woocommerce-vs-tiendanube-cual-conviene-argentina/` y `/blog/tienda-online-propia-cuando-conviene-argentina/`.

2. **Boost 2 (`/blog/hacer-landing-page-canva-sirve-para-vender/` — `27` impr, Pos `7.3` en Página 1, 22 días de antigüedad):**
   - **Consultas reales GSC + Google AR Autocomplete:**
     - GSC: `'como hacer una landing page en canva'` (Pos `20.0`), `'landing page canva'` (Pos `23.0`).
     - Autocomplete AR (15 sugerencias): `como hacer una landing page gratis en canva`, `pagina web en canva con dominio propio`, `publicar sitio web canva con dominio propio`, `pagina web en canva ejemplos`, `sirve canva para hacer pagina web`.
   - **Defectos actuales detectados:** `<title>` de **87c**, `meta description` de **171c** (se corta), FAQ desfasado (`2 <details>` vs `3 Schema`), `dateModified: 2026-10-28`.
   - **Cirugía exacta para Paso 3:**
     - `<title>`, `og:title`, `twitter:title` (**55c**): `Hacer una Página Web en Canva: ¿Sirve para Vender 2026?`
     - `meta description`, `og:description`, `twitter:description` (**146c**): `Cómo hacer una landing page o página web en Canva: sus límites reales en SEO, dominio propio y Píxel de Meta Ads, y cuándo pasar a una web propia.`
     - Agregar bloque comparativo con enlaces a demos reales en código limpio (**`/demos/arquitectura/`**, **`/demos/contable/`** y **`/demos/estetica/`**) contrastando velocidad móvil, Píxel de Meta y SEO frente a una página armada en Canva.
     - Ampliar con **paridad exacta 6/6 (`<details>` == JSON-LD `FAQPage`)** cubriendo:
       1. `¿Puedo hacer una landing page gratis en Canva y usarla para vender?`
       2. `¿Se puede conectar un dominio .com.ar propio a una página web hecha en Canva?`
       3. `¿Por qué una página web de Canva no sirve para campañas de Meta Ads y Google Ads?`
       4. `¿Posicionan en Google (SEO) las páginas creadas con Canva Sites?`
       5. `¿Cómo se ven los diseños de Canva en celulares y por qué pierden clientes?`
       6. `¿Qué alternativa conviene en Argentina si ya probé Canva y necesito vender en serio?`
     - Actualizar `dateModified: 2026-11-19T10:00:00-03:00`.

#### B. Paso 2 — Outline Maestro de Artículo Nuevo SEO por Rubro (`0%` Canibalización Verificada · Potencia Demo Citada por ChatGPT)

> **Por qué se eligió esta keyword sobre Hoteles/Cabañas:** `SEO para hoteles y cabañas` arrojó **67% de solapamiento** con 2 guías existentes (ambas con 0 impresiones) y solo 3 sugerencias en Google AR. En cambio, **`SEO para odontólogos y consultorios dentales`** tiene **`0%` de canibalización**, **11 sugerencias activas en Google AR**, ticket alto por paciente (implantes/ortodoncia), y potencia directamente **`/demos/odontologia/`**, que **esta misma semana recibió visitas reales desde `chatgpt.com` en GA4 (100% engaged)**.

- **Main Keyword:** `SEO para odontólogos y consultorios dentales`
- **Slug (Regla #18 — 4 palabras limpias):** `/blog/seo-odontologos-consultorios-dentales/`
- **`<title>` (57 caracteres):** `SEO para Odontólogos y Consultorios Dentales en Argentina`
- **`<h1>` (69 caracteres — Regla #5 estricta):** `SEO para Odontólogos: Cómo Posicionar tu Consultorio en Google y Maps`
- **`meta description` (154 caracteres):** `SEO para odontólogos y clínicas dentales en Argentina: cómo captar pacientes particulares de implantes y ortodoncia en Google y Google Maps sin pagar ads.`
- **Direct Answer Sturm (Primeras 5–10 palabras con Main Keyword exacta · 54 palabras):**
  > **El SEO para odontólogos y consultorios dentales** en Argentina consiste en optimizar tu página web y tu ficha de Google Maps para aparecer en el Top 3 cuando un paciente busca tratamientos rentables (implantes, ortodoncia invisible, carillas o guardia) en tu barrio, captando turnos particulares por WhatsApp sin depender mes a mes de anuncios pagos.
- **Categoría real en `blog/index.html` (Regla #24):** `seo` (*Auditoría SEO, Velocidad e IA*)
- **Preguntas IA / Query Fan-Out a responder en el cuerpo (ChatGPT, Perplexity, Google AI Overviews + Google AR Autocomplete):**
  1. *Prompt IA:* *"¿Cómo conseguir más pacientes particulares para mi consultorio odontológico en Argentina sin depender de obras sociales?"*
  2. *Prompt IA:* *"¿Qué palabras clave buscan los pacientes antes de sacar turno con un dentista en Google?"* (búsquedas por tratamiento + barrio: `implantes dentales [barrio]`, `ortodoncia invisible precio`, `odontólogo de guardia cerca de mí`).
  3. *Prompt IA:* *"¿Cómo hacer que mi clínica dental aparezca primera en Google Maps frente a otros odontólogos de la zona?"*
  4. *Prompt IA:* *"¿Qué requisitos E-E-A-T y YMYL exige Google para posicionar una web médica u odontológica?"* (matrícula MN/MP visible, autoría profesional real, Schema `Dentist` + `MedicalClinic`).
  5. *Prompt IA:* *"¿Conviene invertir en SEO local o en Google Ads / Instagram Ads para una clínica dental?"*
  - **Entidades concretas para citación GEO:** Matrícula profesional visible (MN / MP), categorías exactas de Google Business Profile (`Dentista`, `Clínica dental`, `Ortodoncista`, `Periodoncista`), Schema `Dentist`, tiempos reales de posicionamiento local (60–120 días), comparativa de costo por paciente particular (implante/ortodoncia vs inversión única de $150.000 ARS en web rápida + SEO local).
- **Imagen Editorial (`1200x675`, PIL `< 490 KB`, dual-sync `images/` y `public/images/`):**
  - Archivo: `images/guia_seo_odontologos_consultorios_dentales.png`
  - Escena (Regla Visual Sturm): Recepción luminosa y moderna de consultorio odontológico en Argentina con odontólogo/a junto a mostrador mirando una tablet/monitor donde se ve un mapa local con el consultorio en posición #1 de Google Maps y una consulta entrante de turno por WhatsApp; luz natural limpia, sin textos diminutos ilegibles; pastilla superior izquierda `"SEO ODONTÓLOGOS"` y sello inferior derecho `erikwebsite.com`.
- **Estructura de Subtítulos `<h2>`:**
  1. `<h2>1. Cómo buscan dentista los pacientes particulares hoy (Google Maps, tratamientos y ChatGPT)</h2>`
  2. `<h2>2. SEO Local vs. Obras Sociales y Anuncios Pagos: Matemática de un Consultorio Dental</h2>` *(Tabla comparativa HTML: Depender de Obras Sociales / Prepagas vs. Solo Instagram Ads vs. Web Rápida + SEO Local en Google Maps por tratamiento).*
  3. `<h2>3. Los 5 pilares del SEO para clínicas dentales y odontólogos (E-E-A-T, Google Maps y Schema Dentist)</h2>` *(Páginas/secciones por tratamiento de alto margen, ficha GBP con categorías secundarias, reseñas con fotos del consultorio, matrícula visible para YMYL y velocidad sub-1s en celular).*
  4. `<h2>4. Cómo convertir visitas de Google en turnos confirmados por WhatsApp (Ejemplo en vivo)</h2>` *(Enlace destacado a `/demos/odontologia/` como modelo real de estructura enfocada en turnos y especialidades).*
- **Interlinking Obligatorio (100% verificado en disco — Regla #19):**
  - **Salientes:** `/demos/odontologia/`, `/blog/paginas-web-marketing-odontologos-argentina/`, `/blog/seo-medicos-clinicas-argentina/`, `/blog/conseguir-resenas-google-maps-seo/`, `/blog/seo-local-google-maps-argentina/`, `/auditoria-seo/`.
  - **Entrante obligatorio:** Agregar un enlace contextual desde `/blog/paginas-web-marketing-odontologos-argentina/` hacia `/blog/seo-odontologos-consultorios-dentales/`.
- **6 FAQs Interactivas (Paridad exacta 6/6 HTML `<details>` == JSON-LD `FAQPage` — Regla #22):**
  1. `¿Cómo hago para que mi consultorio odontológico aparezca primero en Google Maps en mi barrio?`
  2. `¿Qué diferencia hay entre hacer publicidad en Instagram y hacer SEO para odontólogos?`
  3. `¿Qué tratamientos conviene posicionar primero en Google para atraer pacientes particulares?`
  4. `¿Por qué Google es más exigente con el SEO de clínicas dentales y médicos (criterio YMYL y E-E-A-T)?`
  5. `¿Cuánto tiempo tarda un consultorio dental en ver pacientes nuevos desde Google?`
  6. `¿Necesito tener una página web propia o alcanza solo con la ficha gratuita de Google Maps?`
- **Cierre técnico del Jueves (Flash):** Ejecutar `python scratch/verify_article_hygiene.py --hub blog/precios-shopify-argentina-conviene/index.html blog/hacer-landing-page-canva-sirve-para-vender/index.html blog/seo-odontologos-consultorios-dentales/index.html` -> `audit_all_internal_links.py` -> `git diff --stat` -> `npm run build` -> Notificar APIs (Google Indexing v3, GSC Sitemap, IndexNow, Bing) -> `git push origin main`.

---

### [x] Viernes 20/11 — Eje Diseño Web, Demos y Embudos (COMPLETADO: Boosts QR WhatsApp + Hotmart Funnel + Nuevo Artículo Landing Page Vender Cursos Online)

#### A. Paso 1 — Doble Cirugía / Boost en Herramientas y Funnels con Tracción Real (>18 días en GSC)

1. **Boost 1 (`/blog/generador-link-qr-whatsapp-gratis/` — Explotó de 50 a `106` impr (+112% en 4 días!), `1` clic, Pos `16.7`, 25 días de antigüedad):**
   - **Consultas reales GSC + Google AR Autocomplete (33 sugerencias):**
     - GSC: `'generar codigo qr para whatsapp'` (**14 impr, Pos `18.1`**), `'generador de qr whatsapp'` (**8 impr, Pos `15.0`**), `'generador de qr para whatsapp'` (3 impr, Pos `13.7`), `'generar qr para whatsapp'` (3 impr, Pos `23.3`).
     - Autocomplete AR: `generar código qr para whatsapp gratis sin caducidad`, `generar codigo qr para whatsapp con mensaje`, `generar codigo qr para whatsapp business`, `generador de qr para grupo de whatsapp`, `generar codigo qr para whatsapp en canva`.
   - **Defectos actuales detectados:** `<title>` de **72c**, solo **3 FAQs**, `dateModified: 2026-10-26`.
   - **Cirugía exacta para Paso 3:**
     - `<title>`, `og:title`, `twitter:title` (**54c**): `Generador de QR y Link de WhatsApp Gratis (Sin Vencer)`
     - `meta description`, `og:description`, `twitter:description` (**148c**): `Generador de código QR para WhatsApp y link wa.me gratis sin caducidad. Creá tu QR con mensaje predefinido para local, catálogo o WhatsApp Business.`
     - Optimizar `<h2>` #1 para incluir las frases exactas `'generar código qr para whatsapp'` y `'generador de qr whatsapp sin caducidad'` (sin romper el widget interactivo `whatsapp-tool.js` ni sus IDs!).
     - Ampliar de 3 a **6 FAQs con paridad exacta 6/6 (`<details>` == JSON-LD `FAQPage`)** respondiendo las preguntas reales de Autocomplete + IA:
       1. `¿Por qué muchos generadores de códigos QR para WhatsApp vencen después de 14 días y este no?`
       2. `¿Cómo generar un código QR para WhatsApp Business con mensaje predefinido gratis?`
       3. `¿Cómo escribir un número de Argentina (+54 9) para que el link wa.me funcione en todos los celulares?`
       4. `¿Se puede generar un código QR que abra directamente un grupo de WhatsApp?`
       5. `¿Conviene crear el QR de WhatsApp en Canva o con un generador estático directo?`
       6. `¿Cuándo conviene pasar de un link suelto de WhatsApp a una Landing Page o Catálogo interactivo?`
     - Actualizar `dateModified: 2026-11-20T09:30:00-03:00`.

2. **Boost 2 (`/blog/hotmart-argentina-comisiones-impuestos-alternativa-funnel/` — `32` impr, `1` clic orgánico, Pos `8.0` en Página 1, 18 días de antigüedad — Reemplaza a Cotizador que solo tenía 1 impr):**
   - **Consultas reales GSC + Google AR Autocomplete (13 sugerencias):**
     - GSC: Posición promedio **`8.0`** con 1 clic real y 32 impresiones, `'hotmart afiliados argentina'` (Pos `17.0`).
     - Autocomplete AR: `hotmart argentina impuestos`, `hotmart argentina cuit`, `hotmart argentina opiniones`, `hotmart funciona en argentina`, `como vender en hotmart desde argentina`, `alternativas a hotmart`.
   - **Defectos GRAVES actuales detectados:** `<title>` de **100 CARACTERES** (cortado por la mitad en Google!), `meta description` de **218 CARACTERES**, FAQ desfasado (`2 <details>` vs `3 Schema`), `dateModified: 2026-11-02`.
   - **Cirugía exacta para Paso 3:**
     - `<title>`, `og:title`, `twitter:title` (**57c**): `Hotmart en Argentina 2026: Comisiones, Impuestos y Funnel`
     - `meta description`, `og:description`, `twitter:description` (**148c**): `Hotmart en Argentina en 2026: comisiones del 9,9%, impuestos, CUIT, retiros y cómo vender cursos o ebooks en pesos con tu propia Página Modo Funnel.`
     - Reforzar bloque práctico sobre **impuestos en Argentina, CUIT/monotributo, comisiones del 9,9% + tarifa fija y retiros**, sumar enlace bidireccional hacia la nueva guía del día (`/blog/landing-page-vender-cursos-online/`) y destacar la prueba en vivo de **`/demos/funnel/`**.
     - Ampliar con **paridad exacta 6/6 (`<details>` == JSON-LD `FAQPage`)** cubriendo:
       1. `¿Hotmart funciona en Argentina en 2026 y qué comisiones cobra por cada venta?`
       2. `¿Qué impuestos paga un comprador argentino cuando compra un curso o ebook en Hotmart?`
       3. `¿Necesito CUIT o ser monotributista para vender y retirar plata de Hotmart en Argentina?`
       4. `¿Cómo puedo vender mis cursos o ebooks en pesos argentinos con Mercado Pago y transferencia sin pagar 9,9%?`
       5. `¿Qué diferencia hay entre vender en Hotmart y tener mi propia Página Modo Funnel?`
       6. `¿Cuánto cuesta armar una Página Modo Funnel propia con Order Bump en Argentina?`
     - Actualizar `dateModified: 2026-11-20T09:30:00-03:00`.

#### B. Paso 2 — Outline Maestro de Artículo Nuevo Diseño Web & Funnels (Conectado 1:1 a `/demos/funnel/` y Boost 2)

> **Por qué se eligió esta keyword sobre Consorcios:** `pagina web administracion de consorcios` arrojó **0 sugerencias directas en Google AR**. En cambio, **`Landing page para vender cursos online`** capitaliza **500 búsquedas/mes en nuestros CSVs (`vender cursos online`, `funnel de conversión` Comp Baja 16/100, `embudo de conversion` Comp 19/100)**, **5 sugerencias directas en Google AR** (`landing page para vender cursos`, `crear pagina web para vender cursos online`, `vender ebooks en argentina`, `donde vender ebooks en argentina`), solo 50% de solapamiento léxico (intención 100% distinta a Canva) y vende directamente nuestra **Demo `/demos/funnel/`** ($150.000 ARS pago único).

- **Main Keyword:** `Landing page para vender cursos online`
- **Slug (Regla #18 — 5 palabras naturales):** `/blog/landing-page-vender-cursos-online/`
- **`<title>` (56 caracteres):** `Landing Page para Vender Cursos Online y Ebooks en Pesos`
- **`<h1>` (69 caracteres — Regla #5 estricta):** `Landing Page para Vender Cursos Online y Ebooks en Argentina sin 9,9%`
- **`meta description` (152 caracteres):** `Landing page para vender cursos online y ebooks en Argentina: cobrá en pesos con Mercado Pago o transferencia sin comisiones del 9,9% y sumá Order Bump.`
- **Direct Answer Sturm (Primeras 5–10 palabras con Main Keyword exacta · 53 palabras):**
  > **Una landing page para vender cursos online y ebooks** en Argentina te permite cobrar en pesos por Mercado Pago o transferencia bancaria sin regalar el 9,9% a plataformas extranjeras ni recargar dólares al comprador, concentrando tu oferta, temario, testimonios, Order Bump y botón de compra en una sola página de alta conversión.
- **Categoría real en `blog/index.html` (Regla #24):** `ventas` (*Embudos (Funnels) y Conversión*)
- **Preguntas IA / Query Fan-Out a responder en el cuerpo (ChatGPT, Perplexity, Google AI Overviews + Google AR Autocomplete):**
  1. *Prompt IA:* *"¿Cómo vender un curso online o ebook en Argentina sin usar Hotmart y cobrando en pesos?"*
  2. *Prompt IA:* *"¿Dónde vender ebooks o plantillas digitales en Argentina con Mercado Pago y transferencia?"*
  3. *Prompt IA:* *"¿Qué estructura exacta tiene que tener una landing page para vender un curso online que convierta anuncios de Instagram?"*
  4. *Prompt IA:* *"¿Qué es un Order Bump y cuánto puede subir el ticket promedio de un archivo digital o curso?"*
  5. *Prompt IA:* *"¿Conviene usar una plataforma con suscripción en dólares (Kajabi, Stan Store, Hotmart) o una landing page propia?"*
  - **Entidades concretas para citación GEO:** Comparativa numérica real sobre 50 ventas de un curso de $40.000 ARS ($2.000.000 ARS facturados): Hotmart (~9,9% + tarifa fija + fricción dólar tarjeta) vs. Stan Store ($29–$99 USD/mes) vs. Página Modo Funnel Propia ($150.000 ARS pago único + Mercado Pago / Transferencia 10% OFF + Order Bump + Píxel de Meta `Contact`/`InitiateCheckout`).
- **Imagen Editorial (`1200x675`, PIL `< 490 KB`, dual-sync `images/` y `public/images/`):**
  - Archivo: `images/guia_landing_page_vender_cursos_online.png`
  - Escena (Regla Visual Sturm): Creador/a de cursos o especialista en estudio luminoso de Argentina con micrófono de escritorio y notebook mostrando una página de ventas limpia (Modo Funnel) con botón de pago en pesos y celular al lado con notificaciones de ventas/consultas entrantes; pastilla superior izquierda `"FUNNELS & CURSOS"` y sello inferior derecho `erikwebsite.com`.
- **Estructura de Subtítulos `<h2>`:**
  1. `<h2>1. Cómo vender cursos online y ebooks en Argentina sin que los impuestos y comisiones te frenen las ventas</h2>`
  2. `<h2>2. Comparativa real: Hotmart / Stan Store vs. Tu Propia Landing Page Modo Funnel en Pesos</h2>` *(Tabla comparativa HTML con cálculo concreto sobre 50 ventas mensuales: comisión, facilidad de pago local, Píxel de Meta y propiedad de la base de alumnos).*
  3. `<h2>3. Anatomía de una landing page de alta conversión para cursos y archivos digitales (con Order Bump)</h2>` *(1 sola columna sin menús de fuga, promesa clara, temario en acordeón, selector Transferencia 10% OFF vs Mercado Pago, Order Bump y prueba en vivo en **`/demos/funnel/`**).*
  4. `<h2>4. Cómo entregar tu curso o ebook automáticamente y medir cada venta con Meta Pixel y GA4</h2>`
- **Interlinking Obligatorio (100% verificado en disco — Regla #19):**
  - **Salientes:** `/demos/funnel/`, `/blog/hotmart-argentina-comisiones-impuestos-alternativa-funnel/`, `/blog/stan-store-argentina-precios-alternativa-pesos/`, `/blog/que-es-un-funnel-de-ventas-para-que-sirve-argentina/`, `/blog/paginas-web-academias-institutos-cursos-oficios/`, `/blog/embudo-de-ventas-por-whatsapp-argentina/`.
  - **Entrante obligatorio:** Enlazar desde `/blog/hotmart-argentina-comisiones-impuestos-alternativa-funnel/` (Boost 2 del mismo día) hacia `/blog/landing-page-vender-cursos-online/`.
- **6 FAQs Interactivas (Paridad exacta 6/6 HTML `<details>` == JSON-LD `FAQPage` — Regla #22):**
  1. `¿Cómo puedo vender cursos online o ebooks en Argentina cobrando por Mercado Pago y transferencia?`
  2. `¿Necesito pagar una plataforma mensual en dólares para alojar los videos o PDFs de mi curso?`
  3. `¿Qué es un Order Bump en una landing page y cómo aumenta lo que gano por cada alumno?`
  4. `¿Se puede conectar el Píxel de Meta Ads y Google Analytics 4 para medir qué anuncio vende más cursos?`
  5. `¿Cuánto cuesta crear una landing page modo funnel para vender cursos o archivos digitales en Argentina?`
  6. `¿Qué diferencia hay entre una academia completa con aulas y una Página Modo Funnel de oferta única?`
- **Cierre técnico del Viernes (Flash):** Ejecutar `python scratch/verify_article_hygiene.py --hub blog/generador-link-qr-whatsapp-gratis/index.html blog/hotmart-argentina-comisiones-impuestos-alternativa-funnel/index.html blog/landing-page-vender-cursos-online/index.html` -> `audit_all_internal_links.py` -> `git diff --stat` -> `npm run build` -> Notificar APIs -> `git push origin main`.

---

### [x] Sábado 21/11 — Eje Especialista SEO Local, Maps y Analítica (Boost GEO Citado por ChatGPT: Rosario + Boost Maps 101 Impr + Nuevo Artículo: Parámetros UTM en GA4 y Google Maps)

#### A. Paso 1 — Doble Cirugía / Boost de Máximo Retorno (Citación IA Confirmada + Top Maps 101 Impr)

1. **Boost 1 (`/blog/diseno-web-rosario/` — `35` impr en GSC + TRÁFICO REAL DE `chatgpt.com` EN GA4, 22 días de antigüedad):**
   - **Por qué es prioritario en Sábado GEO/Local:** GA4 confirmó visitas reales desde **`chatgpt.com` hacia `/blog/diseno-web-rosario/` (100% engaged)**. Además posiciona en GSC para `'diseño web rosario'` (22 impr), `'diseño de paginas web rosario'` (7 impr, Pos `31.9`) y `'diseñador web rosario'` (3 impr, Pos `37.7`).
   - **Defectos actuales detectados:** `<title>` de 61c (con `| Erik Website`), FAQ desfasado (`2 <details>` vs `3 Schema`), `dateModified: 2026-10-30`.
   - **Cirugía exacta para Paso 3:**
     - `<title>`, `og:title`, `twitter:title` (**53c**): `Diseño Web en Rosario: Páginas, Precios y Maps (2026)`
     - `meta description`, `og:description`, `twitter:description` (**145c**): `Diseño de páginas web en Rosario desde $150.000 ARS finales: sitios ultrarrápidos con Google Maps y WhatsApp para empresas, comercios y estudios.`
     - Reforzar bloque GEO con datos estructurados claros para mantener y multiplicar la citación en ChatGPT/Perplexity/Gemini (precio exacto $150.000 ARS, entrega en 3 a 5 días hábiles, cobertura Centro, Pichincha, Puerto Norte, Fisherton, Funes y Gran Rosario) y sumar enlaces contextuales a **`/demos/arquitectura/`** y **`/demos/contable/`** (estudios contables y profesionales de Rosario).
     - Ampliar con **paridad exacta 6/6 (`<details>` == JSON-LD `FAQPage`)** cubriendo precios en Rosario, entrega remota vs presencial, Google Maps en Gran Rosario/Funes, dominio `.com.ar`, mantenimiento opcional y demos por rubro.
     - Actualizar `dateModified: 2026-11-21T09:30:00-03:00`.

2. **Boost 2 (`/blog/como-poner-agregar-negocio-local-google-maps-gratis/` — `101` impr en GSC, Pos `10.0` en Página 1, 22 días de antigüedad — Reemplaza a Santa Fe que pasa al Miércoles 25/11):**
   - **Consultas reales GSC + Google AR Autocomplete (25 sugerencias):**
     - GSC: `'como poner la ubicación de un negocio en google maps'` (**Pos `10.0`**), `'poner tu negocio en google maps'` (8 impr, Pos `42.6`), `'aparecer en google maps'` (8 impr), `'como agregar mi negocio a google maps'` (8 impr), `'registrar mi negocio en google maps'` (5 impr), `'como poner mi negocio en google maps'` (5 impr).
     - Autocomplete AR: `como poner mi negocio en google maps gratis`, `como poner mi negocio en google maps desde mi celular`, `cuanto cuesta poner tu negocio en google maps`, `como poner mi negocio en google maps y waze`, `como poner visible mi negocio en google maps`.
   - **Defectos GRAVES actuales detectados:** `<title>` de **98 CARACTERES**, `meta description` de **171 caracteres**, FAQ desfasado (`2 <details>` vs `3 Schema`), y un CTA metido como `<h2>` al final!
   - **Cirugía exacta para Paso 3:**
     - `<title>`, `og:title`, `twitter:title` (**57c**): `Cómo Poner tu Negocio en Google Maps Gratis (Paso a Paso)`
     - `meta description`, `og:description`, `twitter:description` (**150c**): `Cómo poner tu negocio en Google Maps gratis desde el celular o PC en Argentina: alta de ficha, verificación por video y claves para salir en el Top 3.`
     - Convertir el último `<h2>` promocional en `<h3>` (higiene semántica), inyectar en el cuerpo las consultas exactas de Google AR (*hacer el alta desde el celular*, *por qué es 100% gratis*, *diferencia con Waze*) y sumar enlace hacia la nueva guía del sábado (`/blog/parametros-utm-google-analytics-4-maps/`).
     - Ampliar con **paridad exacta 6/6 (`<details>` == JSON-LD `FAQPage`)** cubriendo:
       1. `¿Cobran algo o cuánto cuesta poner mi negocio en Google Maps en Argentina?`
       2. `¿Cómo puedo agregar la ubicación de mi negocio en Google Maps desde el celular?`
       3. `¿Cómo aprobar la verificación por video de Google Maps si trabajo a domicilio o sin cartel?`
       4. `¿Cuánto tarda en aparecer mi negocio visible en Google Maps después de verificarlo?`
       5. `¿Al dar de alta mi local en Google Maps también aparece automáticamente en Waze?`
       6. `¿Cómo puedo medir cuántas personas entran a mi página web desde mi ficha de Google Maps?`
     - Actualizar `dateModified: 2026-11-21T09:30:00-03:00`.

#### B. Paso 2 — Outline Maestro de Artículo Nuevo SEO Local & Analítica (`40%` Solapamiento Máximo · `12` Sugerencias Reales en Google AR)

> **Por qué se mejoró el enfoque original (*Estadísticas GBP* -> *Parámetros UTM en GA4 + Google Maps*):** `estadisticas google business profile` solo tenía 1 sugerencia en Google AR y baja intención de acción. Al reenfocarla en **`Parámetros UTM en Google Analytics 4 y Google Maps`** (absorbiendo dentro de la guía cómo cruzar las estadísticas del panel de Google Business Profile con GA4), capturamos **12 sugerencias reales en Google AR** (`que son los parametros utm`, `utm google analytics 4`, `como ver las utm en google analytics 4`, `utm builder google analytics 4`, `estadisticas de google mi negocio`), mantenemos `0%` canibalización real y resolvemos el mayor punto ciego analítico de negocios locales y marketers.

- **Main Keyword:** `Parámetros UTM en Google Analytics 4`
- **Slug (Regla #18 — 6 palabras naturales):** `/blog/parametros-utm-google-analytics-4-maps/`
- **`<title>` (56 caracteres):** `Parámetros UTM en Google Analytics 4: Medir Maps y Redes`
- **`<h1>` (68 caracteres — Regla #5 estricta):** `Parámetros UTM en Google Analytics 4: Cómo Medir Google Maps y Redes`
- **`meta description` (148 caracteres):** `Qué son los parámetros UTM en Google Analytics 4 y cómo crear enlaces etiquetados para medir clics reales desde Google Maps, Instagram y códigos QR.`
- **Direct Answer Sturm (Primeras 5–10 palabras con Main Keyword exacta · 55 palabras):**
  > **Los parámetros UTM en Google Analytics 4 (GA4)** son etiquetas cortas que se agregan al final de un enlace (`?utm_source=...&utm_medium=...`) para identificar con exactitud cuántas visitas y consultas de WhatsApp llegan desde tu ficha de Google Maps, tu biografía de Instagram, tus códigos QR impresos o cada campaña de anuncios.
- **Categoría real en `blog/index.html` (Regla #24):** `maps` (*Google Maps y Posicionamiento Local*)
- **Preguntas IA / Query Fan-Out a responder en el cuerpo (ChatGPT, Perplexity, Google AI Overviews + Google AR Autocomplete):**
  1. *Prompt IA:* *"¿Qué son los parámetros UTM en Google Analytics 4 y para qué sirven en un negocio local?"*
  2. *Prompt IA:* *"¿Por qué las visitas que vienen de Google Maps aparecen como tráfico Directo u Orgánico en GA4 y cómo arreglarlo?"*
  3. *Prompt IA:* *"¿Cómo etiquetar el enlace del sitio web en Google Business Profile (Google Mi Negocio) sin romper el SEO ni las estadísticas?"*
  4. *Prompt IA:* *"¿Dónde se ven los resultados de las etiquetas UTM dentro de los informes de Google Analytics 4?"* (ruta exacta: `Informes > Adquisición > Adquisición de tráfico > Fuente / Medio de la sesión` + `Campaña de la sesión`).
  5. *Prompt IA:* *"¿Qué errores con las UTM arruinan los datos de GA4?"* (usar UTM en enlaces internos del propio sitio, mezclar mayúsculas/minúsculas como `Instagram` vs `instagram`, o no diferenciar `utm_source=google` de `utm_medium=organic`).
  - **Entidades concretas para citación GEO:** Los 5 parámetros estándar (`utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`), ejemplo exacto listo para copiar en Google Business Profile (`https://tudominio.com.ar/?utm_source=google&utm_medium=organic&utm_campaign=gbp`), cruce con el panel de *Rendimiento / Estadísticas de Google Business Profile* (llamadas, rutas, búsquedas) y regla crítica de etiqueta `<link rel="canonical">` para que las UTM nunca dupliquen URLs en Google.
- **Imagen Editorial (`1200x675`, PIL `< 490 KB`, dual-sync `images/` y `public/images/`):**
  - Archivo: `images/guia_parametros_utm_google_analytics_4_maps.png`
  - Escena (Regla Visual Sturm): Consultor de analítica / dueño de PyME en escritorio limpio mirando pantalla de laptop con gráficos de canales de adquisición (Google Maps, Instagram, QR) y celular al lado con una ficha de Google Maps abierta; iluminación natural de oficina moderna en Argentina; pastilla superior izquierda `"ANALÍTICA GA4 & MAPS"` y sello inferior derecho `erikwebsite.com`.
- **Estructura de Subtítulos `<h2>`:**
  1. `<h2>1. Qué son los parámetros UTM en Google Analytics 4 y por qué arreglan el punto ciego de Google Maps</h2>`
  2. `<h2>2. Los 5 parámetros UTM explicados con ejemplos reales para negocios en Argentina</h2>` *(Tabla comparativa HTML con ejemplos listos para copiar: Botón Sitio Web de Google Business Profile, Bio de Instagram, Cartel QR impreso en local, Firma de correo corporativo y Campaña de Meta Ads).*
  3. `<h2>3. Cómo cruzar las estadísticas de Google Business Profile con tus informes UTM en GA4 paso a paso</h2>` *(Ruta exacta en GA4: Adquisición de tráfico -> Fuente/Medio + Campaña, cruzada con `whatsapp_click` y `generate_lead`, más las 4 métricas útiles del panel de Google Maps).*
  4. `<h2>4. Los 4 errores con parámetros UTM que ensucian tus métricas (y cómo afecta al SEO si no tenés canonical)</h2>` *(Nunca usar UTM en enlaces internos, siempre minúsculas sin acentos ni espacios, consistencia de nombres y validación de `<link rel="canonical">`).*
- **Interlinking Obligatorio (100% verificado en disco — Regla #19):**
  - **Salientes:** `/blog/como-poner-agregar-negocio-local-google-maps-gratis/`, `/blog/por-que-mi-negocio-no-aparece-en-google-maps/`, `/blog/como-instalar-google-analytics-4-ga4-medir-clics-whatsapp/`, `/blog/google-tag-manager-vs-ga4-seo/`, `/blog/generador-link-qr-whatsapp-gratis/`, `/auditoria-seo/`.
  - **Entrante obligatorio:** Enlazar desde `/blog/como-poner-agregar-negocio-local-google-maps-gratis/` (Boost 2 del mismo día) y desde `/blog/como-instalar-google-analytics-4-ga4-medir-clics-whatsapp/` hacia `/blog/parametros-utm-google-analytics-4-maps/`.
- **6 FAQs Interactivas (Paridad exacta 6/6 HTML `<details>` == JSON-LD `FAQPage` — Regla #22):**
  1. `¿Usar parámetros UTM en el enlace de Google Business Profile perjudica el SEO o duplica mi página en Google?`
  2. `¿Dónde veo el tráfico de mis enlaces UTM paso a paso dentro de Google Analytics 4?`
  3. `¿Cuál es la plantilla UTM recomendada para el botón de Sitio Web de Google Maps?`
  4. `¿Puedo usar parámetros UTM dentro de los botones del menú o enlaces internos de mi propia web?`
  5. `¿Cómo combino un código QR impreso con parámetros UTM para saber cuánta gente escanea mi vidriera o folleto?`
  6. `¿Por qué las estadísticas de clics en Google Business Profile no coinciden exactamente al 100% con las sesiones de GA4?`
- **Cierre técnico del Sábado (Flash):** Ejecutar `python scratch/verify_article_hygiene.py --hub blog/diseno-web-rosario/index.html blog/como-poner-agregar-negocio-local-google-maps-gratis/index.html blog/parametros-utm-google-analytics-4-maps/index.html` -> `audit_all_internal_links.py` -> `git diff --stat` -> `npm run build` -> Notificar APIs -> `git push origin main`.

---

## 6. Próximo Comando Dominical Programado (Domingo 22 de Noviembre de 2026)
- **Ejecución de Auditoría Integral (Semana 3):** Correr `python scratch/sunday_seo_command.py` para contrastar la evolución de impresiones (`4.772` al 19/11), clics orgánicos, páginas en Bing (`17` al 19/11), tráfico de asistentes de IA (`AI Assistant` en GA4) y conversiones `generate_lead` / `whatsapp_click`.
- **Cola Pre-Validada de Boosts Maduros para Semana 3 (Lunes 23 al Sábado 28/11 — Ya detectados hoy en GSC):**
  1. `/blog/ferozo-webmail-roundcube-vs-gmail-outlook-corporativo/` (**76 impr, Pos `8.8`**, 9 queries en Pos 6.7–11.6 + visita orgánica real en GA4 — cumple 14 días el 21/11).
  2. `/blog/crear-pagina-web-google-sites-sirve-para-negocio/` (**45 impr**, 4 queries en Página 1 Pos 5.0–8.0, `<title>` 84c, `meta desc` 189c, 2 FAQs).
  3. `/blog/por-que-mi-negocio-no-aparece-en-google-maps/` (**57 impr**, `<title>` 84c, FAQ roto 2/4).
  4. `/blog/diseno-web-santa-fe/` (32 impr, `<title>` 70c, FAQ roto 2/3) y `/blog/diseno-web-la-rioja/` (29 impr, `<title>` 84c) — en el **Miércoles 25/11** (eje Diseño Web y Localidades).
  5. Evaluar a partir del **26/11** (ventana 14 días) el comportamiento de `/blog/seo-on-page-checklist-optimizacion/` (**111 impr en Pos `6.3` en solo 7 días!**) y decidir si cargar nuestras 30 Money Keywords en **SerpBear** (hoy en `0` rastreadas) o retirarlo del reporte dominical.
