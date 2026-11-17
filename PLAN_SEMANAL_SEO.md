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

### [ ] Miércoles 18/11 — Eje Diseño Web y Localidades (Boost Zona Sur GBA + Ciudad Nueva: Luján)

#### A. Paso 1 — Cirugía / Boost Geográfico en "Striking Distance" (Pos 9.0 a 19.5 en GSC)
- **URL a Optimizar:** `/blog/diseno-web-zona-sur/`
- **Diagnóstico GSC:** Acumula **5 consultas de altísima intención comercial en posiciones 9.0 a 19.5**:
  - `'diseño web profesional en zona sur'` (`Pos 9.0`, 1 imp)
  - `'diseño web landing page y hosting zona sur'` (`Pos 9.2`, 4 imp)
  - `'diseño web y hosting en zona sur'` (`Pos 9.7`, 3 imp)
  - `'diseño web hosting y seo zona sur'` (`Pos 11.8`, 4 imp)
  - `'diseño web posicionamiento seo zona sur'` (`Pos 19.5`, 2 imp)
  - `'diseño web landing page google ads zona sur'` (`Pos 21.0`, 2 imp)
- **Cirugía exacta a ejecutar en Paso 3:**
  1. Optimizar `<title>` a **56 caracteres**: `Diseño Web, Hosting y SEO en Zona Sur GBA: Precios 2026`
  2. Actualizar `<h2>` #2 a: `Diseño web, Landing Page, Hosting y Posicionamiento SEO en Zona Sur: Todo Resuelto en un Solo Lugar` e incluir las frases exactas `'diseño web landing page y hosting zona sur'`, `'diseño web para Google Ads en Zona Sur'` y enlace a la nueva demo `/demos/arquitectura/` para estudios y constructoras del corredor Canning / Lomitas / Quilmes.
  3. Ampliar de 3 a **6 FAQs interactivas** (`<details name="faq-accordion">` + GA4 `faq_expand` + Schema `FAQPage` + `dateModified: 2026-11-18T09:30:00-03:00`):
     - FAQ 4: `¿El servicio de diseño web en Zona Sur incluye el hosting rápido y el certificado SSL?`
     - FAQ 5: `¿Hacen Landing Pages optimizadas para campañas de Google Ads y Meta Ads en Zona Sur?`
     - FAQ 6: `¿Cómo funciona el posicionamiento SEO local para superar a mi competencia en Quilmes, Lomas, Avellaneda y Lanús?`

#### B. Paso 2 — Outline Maestro de Artículo Nuevo (Regla #16: 1 Sola Ciudad · 0% Canibalización)
- **Main Keyword:** `Diseño web en Luján`
- **Slug (Regla #18 — 4 palabras naturales):** `/blog/diseno-web-lujan/`
- **`<title>` (55 caracteres):** `Diseño Web en Luján: Páginas para Empresas y Comercios`
- **`<h1>`:** `Diseño de Páginas Web en Luján (Buenos Aires): Desarrollo Rápido y Google Maps para Empresas, Turismo y Profesionales`
- **`meta description` (155 caracteres):** `Diseño web en Luján (Provincia de Buenos Aires). Páginas web rápidas desde $150.000 ARS para empresas del corredor Acceso Oeste, turismo, agro y comercios.`
- **Direct Answer Sturm (Primeras 5–10 palabras con Main Keyword exacta):**
  > **El servicio de diseño web en Luján (Provincia de Buenos Aires)** permite a empresas industriales del corredor Acceso Oeste y Ruta 6, alojamientos turísticos, comercios del centro y profesionales independientes captar clientes todos los días desde Google y Google Maps con una Landing Page en código a medida por $150.000 ARS finales.
- **Categoría en `blog/index.html`:** `maps` (*SEO Local & Google Maps*)
- **Imagen Editorial (`1200x675`, PIL `< 490 KB`):** `images/guia_diseno_web_lujan.png` — Vista editorial luminosa de estudio profesional/comercio moderno en Luján con referencia arquitectónica sutil del centro histórico/corredor productivo del Oeste bonaerense y laptop mostrando sitio web corporativo con mapa local y botón de WhatsApp; pastilla `"DISEÑO WEB LUJÁN"` y sello `erikwebsite.com`.
- **Estructura de Subtítulos `<h2>`:**
  - `<h2>1. Por qué las empresas, cabañas y comercios de Luján tienen una oportunidad única en Google hoy</h2>` (Polo industrial Ruta 6 / Acceso Oeste, desarrollos urbanísticos y estudios de arquitectura en clubes de campo, turismo en Carlos Keen / Cortínez / Open Door, y servicios profesionales en el centro de Luján).
  - `<h2>2. Qué incluye nuestra propuesta de diseño web en Luján por $150.000 ARS finales</h2>` (Tabla comparativa: Agencia tradicional / WordPress lento vs. Desarrollo en Código Limpio en 3 a 5 días hábiles).
  - `<h2>3. Posicionamiento en Google Maps para negocios de Luján, Jáuregui, Pueblo Nuevo y Carlos Keen</h2>`
  - `<h2>4. Cómo convertir las búsquedas de turistas y empresas del corredor Oeste en consultas de WhatsApp</h2>`
- **Interlinking Obligatorio (Regla #19 — Solo URLs reales verificadas):**
  - `/blog/diseno-web-zona-oeste/`
  - `/blog/diseno-web-pilar/`
  - `/demos/arquitectura/` (para desarrolladoras, arquitectos y constructoras de barrios privados en Luján / Open Door)
  - `/blog/como-poner-agregar-negocio-local-google-maps-gratis/`
  - `/auditoria-seo/` (además de añadir enlace entrante desde `/blog/diseno-web-zona-oeste/` hacia `/blog/diseno-web-lujan/`).
- **6 FAQs Interactivas (`<details name="faq-accordion">` + GA4 `faq_expand` + Schema `FAQPage`):**
  1. `¿Cuánto cuesta hacer una página web profesional en Luján en 2026?`
  2. `¿Cuánto demora la entrega de la página web y qué material tengo que enviar?`
  3. `¿Sirve para restaurantes de campo en Carlos Keen, quintas y hoteles en Luján?`
  4. `¿Cómo hacen para que mi empresa o estudio de arquitectura del corredor Ruta 6 / Acceso Oeste aparezca en Google?`
  5. `¿El pago de $150.000 ARS es único o estoy obligado a pagar una mensualidad?`
  6. `¿Me ayudan a registrar el dominio .com.ar en NIC Argentina y configurar el correo corporativo?`

---

### [ ] Jueves 19/11 — Eje Especialista SEO por Rubro / CMS (Boost Diseño Web Comparativas Maduras: Shopify + Canva + Nuevo Artículo SEO: Hoteles y Cabañas)

#### A. Paso 1 — Doble Cirugía / Boost en Comparativas de Diseño Web Maduras (>15 días en GSC)
1. **Boost 1 (`/blog/precios-shopify-argentina-conviene/` — `34` impresiones en GSC, Pos `22.4`, 15 días de antigüedad):**
   - **Diagnóstico GSC:** Acumula `34` impresiones al borde de entrar al Top 20, pero su `<title>` actual tiene **85 caracteres** y solo cuenta con **2 FAQs**.
   - **Cirugía exacta a ejecutar en Paso 3:**
     - Acortar `<title>` de 85 a **55 caracteres**: `Precios de Shopify en Argentina 2026: ¿Conviene o No?`
     - Ampliar de 2 a **6 FAQs interactivas** (`<details name="faq-accordion">` + GA4 `faq_expand` + Schema `FAQPage` + `dateModified: 2026-11-19T09:30:00-03:00`) sobre dólar tarjeta, comisiones por pasarela local y alternativa en código propio.
2. **Boost 2 (`/blog/hacer-landing-page-canva-sirve-para-vender/` — `22` impresiones en GSC, Posición `6.0`, 18 días de antigüedad):**
   - **Diagnóstico GSC:** Ya está en **Puesto `6.0`** en la primera página de Google, pero tiene un `<title>` de **87 caracteres** y solo **2 FAQs**.
   - **Cirugía exacta a ejecutar en Paso 3:**
     - Acortar `<title>` de 87 a **56 caracteres**: `Hacer una Página Web en Canva: ¿Sirve para Vender 2026?`
     - Sumar enlace comparativo hacia nuestras demos reales (incluyendo `/demos/arquitectura/` y `/demos/estetica/`) para mostrar la diferencia visual entre un enlace de Canva y una web profesional.
     - Ampliar de 2 a **6 FAQs interactivas** con Schema `FAQPage` y `dateModified`.

#### B. Paso 2 — Outline Maestro de Artículo Nuevo SEO (0% Canibalización Verificada)
- **Main Keyword:** `SEO para hoteles y cabañas en Argentina`
- **Slug (Regla #18 — 6 palabras naturales):** `/blog/seo-hoteles-cabanas-turismo-argentina/`
- **`<title>` (56 caracteres):** `SEO para Hoteles y Cabañas en Argentina: Más Reservas`
- **`<h1>`:** `SEO para Hoteles, Cabañas y Alojamientos en Argentina: Cómo Conseguir Reservas Directas en Google sin Comisiones`
- **`meta description` (156 caracteres):** `SEO para hoteles y cabañas en Argentina. Posicioná tu alojamiento en Google y Google Maps para recibir reservas directas por WhatsApp sin pagar 18% a OTAs.`
- **Direct Answer Sturm (Primeras 5–10 palabras con Main Keyword exacta):**
  > **Una estrategia de SEO para hoteles y cabañas en Argentina** permite que tu complejo turístico aparezca en los primeros lugares de Google y Google Maps cuando un viajero busca alojamiento en tu destino, captando reservas directas por WhatsApp y ahorrando entre el 15% y el 22% de comisión por estadía que cobran las plataformas intermediarias.
- **Categoría en `blog/index.html`:** `seo` (*Auditoría SEO, Velocidad e IA*)
- **Imagen Editorial (`1200x675`, PIL `< 490 KB`):** `images/guia_seo_hoteles_cabanas_turismo_argentina.png` — Recepción cálida de hotel boutique / complejo de cabañas en destino turístico argentino (madera y piedra con vista a montañas) donde el dueño revisa en su notebook el posicionamiento en Google Maps y mensajes de reserva directa en WhatsApp; pastilla `"SEO TURISMO & HOTELES"` y sello `erikwebsite.com`.
- **Estructura de Subtítulos `<h2>`:**
  - `<h2>1. Cómo buscan alojamiento los turistas argentinos hoy (Google Maps, búsquedas por destino e IA)</h2>`
  - `<h2>2. SEO Local en Google Business Profile vs. Comisiones de Booking y Airbnb: Matemática de Rentabilidad</h2>` (Tabla comparativa HTML de 100 estadías anuales: margen neto con OTAs vs. reserva directa SEO + WhatsApp).
  - `<h2>3. Los 5 pilares técnicos del SEO para hoteles, complejos de cabañas y aparts en Argentina</h2>` (Velocidad móvil en ruta con 4G, Schema `LodgingBusiness` / `Hotel`, páginas de destino local y fotos optimizadas en WebP).
  - `<h2>4. Cómo usar el Efecto Billboard: cuando el turista te descubre en una app pero te busca por tu nombre en Google</h2>`
- **Interlinking Obligatorio (Regla #19 — Solo URLs reales verificadas):**
  - `/blog/paginas-web-cabanas-hoteles-turismo/`
  - `/blog/sistema-reservas-whatsapp-hoteles-cabanas-sin-comisiones/`
  - `/blog/conseguir-resenas-google-maps-seo/`
  - `/blog/diseno-web-bariloche/` y `/blog/diseno-web-villa-carlos-paz/`
  - `/auditoria-seo/`
- **6 FAQs Interactivas (`<details name="faq-accordion">` + GA4 `faq_expand` + Schema `FAQPage`):**
  1. `¿Cómo hago para que mi hotel o complejo de cabañas aparezca antes que Booking cuando buscan el nombre de mi alojamiento?`
  2. `¿Cuánto tarda en hacer efecto el posicionamiento SEO para una temporada de verano o vacaciones de invierno?`
  3. `¿Qué palabras clave buscan los viajeros argentinos antes de reservar una cabaña o hotel?`
  4. `¿Cómo influyen las reseñas de los huéspedes en Google Maps para aparecer en el Top 3 de mi ciudad turística?`
  5. `¿Puedo mantener mi perfil en plataformas turísticas y al mismo tiempo potenciar mi canal de reservas directas con SEO?`
  6. `¿Qué datos estructurados (Schema.org) necesita la web de un hotel o cabaña para ser recomendada por ChatGPT y Google AI?`

---

### [ ] Viernes 20/11 — Eje Diseño Web, Demos y Embudos (Boost QR WhatsApp + Boost Cotizador Online con Demo Arquitectura + Nuevo Artículo: Administración de Consorcios y Countries)

#### A. Paso 1 — Doble Cirugía / Boost en Herramientas, Embudos y Cotizador Interactivo
1. **Boost 1 (`/blog/generador-link-qr-whatsapp-gratis/` — `1` clic, `50` impr (+194%), Pos `16.1`, 20 días de antigüedad):**
   - **Consultas reales en GSC:** `'generar codigo qr para whatsapp'` (Pos 17.0, 11 imp), `'generador de qr whatsapp'` (Pos 16.0, 5 imp), `'codigo qr para whatsapp'` (Pos 28.0).
   - **Cirugía exacta a ejecutar en Paso 3:**
     - Acortar `<title>` de 72 a **56 caracteres**: `Generador de QR y Link de WhatsApp Gratis (Sin Vencer)`
     - Ajustar `<h2>` #1 a: `1. Cómo Generar un Código QR para WhatsApp Gratis y Sin Caducidad` inyectando las frases exactas de GSC (`generar codigo qr para whatsapp` y `generador de qr whatsapp`).
     - Ampliar de 3 a **6 FAQs interactivas** (`<details name="faq-accordion">` + GA4 `faq_expand` + Schema `FAQPage` + `dateModified`).
2. **Boost 2 (`/blog/cotizador-online-whatsapp-vs-carrito-compras-tradicional/` — Posición `10.0` en GSC + Integración Demo Arquitectura):**
   - **Diagnóstico GSC:** Ya existe y posiciona en **Puesto `10.0`**, pero tiene un `<title>` de **78 caracteres**, solo **2 FAQs** y todavía no muestra el nuevo **Cotizador de Obra por m² de `/demos/arquitectura/`**.
   - **Cirugía exacta a ejecutar en Paso 3:**
     - Acortar `<title>` de 78 a **56 caracteres**: `Cotizador Online y Calculadora de Presupuestos WhatsApp` (absorbiendo también la intención `'calculadora de presupuestos interactiva para páginas web'` sin canibalizar).
     - Agregar en la sección de Demos en Vivo la tarjeta y enlace directo al **Cotizador de Obra de `/demos/arquitectura/`** (junto a `/demos/abogados/`, `/demos/fitness/`, `/demos/eventos/` y `/demos/urgencias-hogar/`).
     - Ampliar de 2 a **6 FAQs interactivas** con Schema `FAQPage` y `dateModified`.

#### B. Paso 2 — Outline Maestro de Artículo Nuevo Conectado a `/demos/arquitectura/` (0% Canibalización Verificada)
- **Main Keyword:** `Páginas web para administración de consorcios y countries`
- **Slug (Regla #18 — 6 palabras naturales):** `/blog/paginas-web-administracion-consorcios-countries/`
- **`<title>` (56 caracteres):** `Páginas Web para Administración de Consorcios y Barrios`
- **`<h1>`:** `Páginas Web para Administración de Consorcios y Barrios Privados en Argentina: Cómo Captar Edificios y Mostrar Solvencia`
- **`meta description` (155 caracteres):** `Páginas web para administración de consorcios, edificios y barrios privados en Argentina. Captá nuevos consejos de propietarios por Google y WhatsApp.`
- **Direct Answer Sturm (Primeras 5–10 palabras con Main Keyword exacta):**
  > **Las páginas web para administración de consorcios y countries** permiten a administradores matriculados (RPA en CABA, GBA e interior del país) demostrar transparencia en liquidación de expensas, mantenimiento edilicio (Ley 257) y auditorías contables para captar nuevos edificios y barrios cerrados desde Google.
- **Categoría en `blog/index.html`:** `diseno` (*Diseño Web & Conversión*)
- **Imagen Editorial (`1200x675`, PIL `< 490 KB`):** `images/guia_paginas_web_administracion_consorcios_countries.png` — Administrador de consorcios profesional frente a edificio residencial moderno en Buenos Aires revisando en su tablet la página web institucional del estudio con formulario de cotización por cantidad de unidades funcionales; pastilla `"CONSORCIOS & COUNTRIES"` y sello `erikwebsite.com`.
- **Estructura de Subtítulos `<h2>`:**
  - `<h2>1. Cómo eligen nuevo administrador los Consejos de Propietarios cuando están cansados de la gestión anterior</h2>`
  - `<h2>2. Qué debe mostrar la página web de una Administración de Consorcios y Barrios Cerrados para generar confianza inmediata</h2>` (Matrícula RPA, sistemas de liquidación claros, proveedores matriculados de obra/fachadas Ley 257 —enlazando a `/demos/arquitectura/`— y canal de emergencias).
  - `<h2>3. Comparativa: Depender solo del boca en boca vs. Captar Edificios y Countries con una Landing Page con Pre-Cotizador</h2>` (Tabla comparativa HTML filtrando por cantidad de departamentos/lotes, amenities y localidad).
  - `<h2>4. Posicionamiento en Google Maps para Administradores de Consorcios por barrio o zona</h2>`
- **Interlinking Obligatorio (Regla #19 — Solo URLs reales verificadas):**
  - `/demos/arquitectura/` (conectando directamente con el bloque *Consorcios, Edificios & Ley 257*)
  - `/demos/contable/`
  - `/blog/paginas-web-empresas-limpieza-finales-obra-tapizados/`
  - `/blog/paginas-web-seguridad-privada-alarmas-monitoreo/`
  - `/blog/paginas-web-estudios-contables-argentina/`
- **6 FAQs Interactivas (`<details name="faq-accordion">` + GA4 `faq_expand` + Schema `FAQPage`):**
  1. `¿Cuánto cuesta una página web profesional para una administración de consorcios en Argentina?`
  2. `¿Cómo filtrar en la web a los miembros del Consejo de Propietarios que buscan cambiar de administrador?`
  3. `¿Qué datos conviene pedir en el cotizador antes de pasar a WhatsApp (cantidad de unidades funcionales, seguridad, amenities)?`
  4. `¿Puedo enlazar en mi página web el acceso al sistema de liquidación de expensas que ya uso?`
  5. `¿Cómo ayuda tener una web propia a conseguir consorcios en barrios específicos de CABA, Zona Norte, Zona Sur o ciudades del interior?`
  6. `¿Cuánto demora el armado de la página web y qué información necesito enviar?`

---

### [ ] Sábado 21/11 — Eje Especialista SEO Local, Maps y Analítica (Boost Diseño Web Ciudades Maduras: Rosario y Santa Fe + Nuevo Artículo SEO: Estadísticas de Google Business Profile)

#### A. Paso 1 — Doble Cirugía / Boost en Páginas de Diseño Web Maduras (>16 días en GSC)
1. **Boost 1 (`/blog/diseno-web-rosario/` — `35` impresiones en GSC, 16 días de antigüedad, solo 2 FAQs):**
   - **Diagnóstico GSC:** Es la segunda ciudad con más impresiones del país después de Mendoza (`35` impr), pero su `<title>` tiene 61 caracteres y solo cuenta con **2 FAQs**.
   - **Cirugía exacta a ejecutar en Paso 3:**
     - Acortar `<title>` a **54 caracteres**: `Diseño Web en Rosario: Páginas y Google Maps (2026)`
     - Incorporar enlace contextual a la nueva demo `/demos/arquitectura/` para estudios de arquitectura, constructoras y desarrolladoras de Rosario (Puerto Norte, Centro, Fisherton y Funes).
     - Ampliar de 2 a **6 FAQs interactivas** (`<details name="faq-accordion">` + GA4 `faq_expand` + Schema `FAQPage` + `dateModified: 2026-11-21T09:30:00-03:00`).
2. **Boost 2 (`/blog/diseno-web-santa-fe/` — `32` impresiones en GSC, 16 días de antigüedad, `<title>` 70 chars y 2 FAQs):**
   - **Diagnóstico GSC:** Acumula `32` impresiones, con `<title>` de 70 caracteres y solo **2 FAQs**.
   - **Cirugía exacta a ejecutar en Paso 3:**
     - Acortar `<title>` de 70 a **55 caracteres**: `Diseño Web en Santa Fe Capital: Precios y Maps 2026`
     - Incorporar enlace contextual a `/demos/arquitectura/` y ampliar de 2 a **6 FAQs interactivas** con Schema `FAQPage` y `dateModified`.

#### B. Paso 2 — Outline Maestro de Artículo Nuevo SEO Local / Maps (0% Canibalización Verificada)
- **Main Keyword:** `Estadísticas de Google Business Profile`
- **Slug (Regla #18 — 5 palabras exactas):** `/blog/estadisticas-google-business-profile-maps/`
- **`<title>` (57 caracteres):** `Estadísticas de Google Business Profile: Medir Google Maps`
- **`<h1>`:** `Estadísticas de Google Business Profile: Cómo Medir Llamadas, Clics a tu Web y Rutas en Google Maps`
- **`meta description` (156 caracteres):** `Estadísticas de Google Business Profile (ex Google Mi Negocio): cómo leer el panel de rendimiento en Google Maps, medir clics a tu web y sumar etiquetas UTM.`
- **Direct Answer Sturm (Primeras 5–10 palabras con Main Keyword exacta):**
  > **Las estadísticas de Google Business Profile (el panel de Rendimiento de Google Maps)** muestran exactamente cuántas personas buscaron tu rubro en tu ciudad, cuántas tocaron el botón de llamar, cuántas pidieron indicaciones para llegar a tu local y cuántas entraron a tu página web durante los últimos 6 meses.
- **Categoría en `blog/index.html`:** `maps` (*SEO Local & Google Maps*)
- **Imagen Editorial (`1200x675`, PIL `< 490 KB`):** `images/guia_estadisticas_google_business_profile_maps.png` — Dueño de negocio / consultor en Argentina analizando en laptop el panel de Rendimiento de Google Business Profile (gráficos de llamadas, solicitudes de cómo llegar, clics al sitio web y términos de búsqueda locales en Google Maps); pastilla `"MÉTRICAS GOOGLE MAPS"` y sello `erikwebsite.com`.
- **Estructura de Subtítulos `<h2>`:**
  - `<h2>1. Dónde ver las estadísticas de Google Business Profile en 2026 y qué significa cada métrica</h2>`
  - `<h2>2. Las 4 métricas que importan para tu facturación: Términos de búsqueda, Llamadas, Cómo llegar y Clics al sitio web</h2>` (Tabla comparativa HTML explicando qué mide cada indicador, qué problema revela si está bajo y cómo mejorarlo).
  - `<h2>3. El punto ciego de Google Maps: cómo agregar parámetros UTM al enlace de tu web para ver los clics de Maps dentro de GA4</h2>`
  - `<h2>4. Cómo usar el informe de "Búsquedas" de tu ficha para descubrir nuevas palabras clave locales en tu ciudad</h2>`
- **Interlinking Obligatorio (Regla #19 — Solo URLs reales verificadas):**
  - `/blog/como-poner-agregar-negocio-local-google-maps-gratis/`
  - `/blog/por-que-mi-negocio-no-aparece-en-google-maps/`
  - `/blog/conseguir-resenas-google-maps-seo/`
  - `/blog/como-instalar-google-analytics-4-ga4-medir-clics-whatsapp/`
  - `/auditoria-seo/`
- **6 FAQs Interactivas (`<details name="faq-accordion">` + GA4 `faq_expand` + Schema `FAQPage`):**
  1. `¿Cómo entro a ver las estadísticas de mi ficha de Google Maps desde el celular o la computadora?`
  2. `¿Por qué Google Analytics 4 muestra como tráfico "Directo" u "Orgánico" las visitas que vienen desde Google Maps?`
  3. `¿Cómo se arma un enlace con código UTM para el botón de "Sitio web" de Google Business Profile?`
  4. `¿Google Maps mide cuando alguien hace clic en mi enlace de WhatsApp dentro de la ficha?`
  5. `¿Qué significa que mi negocio tenga muchas "Visualizaciones en Maps" pero pocos clics a llamadas o sitio web?`
  6. `¿Cada cuánto tiempo actualiza Google Business Profile el listado de palabras clave con las que me encontraron?`

---

## 6. Próximo Comando Dominical Programado (Domingo 22 de Noviembre de 2026)
- **Ejecución de Auditoría Integral (Semana 3):** Correr `python scratch/sunday_seo_command.py` con **Argon (High)** para contrastar la evolución de impresiones, clics orgánicos, páginas en Bing (`InIndex`), conversiones GA4 (`generate_lead` / `whatsapp_click`) y el impacto de las 27 guías del Sprint + los 6 nuevos artículos y 8 Boosts de la Semana 2.
