# PLAN_SEMANAL_SEO.md — Comando Estratégico Dominical (`erikwebsite.com`)

> **Propósito:** Archivo maestro vivo donde cada domingo registramos la evolución real de `erikwebsite.com` (Google Search Console, GA4 con eventos de conversión a WhatsApp, SerpBear e inventario de URLs), auditamos qué funcionó tras la ventana de maduración de 14 días, prevenimos al 100% la canibalización de palabras clave y dejamos trazado el **Plan de Ataque de Lunes a Sábado**.

---

## 1. Reglas del Sistema Operativo Semanal (Cadencia 3 + 3 + 1)

| Día | Eje Estratégico | Objetivo Principal | Cuota Recomendada |
| :--- | :--- | :--- | :--- |
| **Lunes** | Diseño Web y Conversión | Rubros comerciales, comparativas BoFu o cirugía de páginas de Diseño Web en posiciones 4–20 | 1 a 2 páginas (nuevas o actualizadas) |
| **Martes** | Especialista SEO, Velocidad e IA | Posicionamiento en Google, casos técnicos, Core Web Vitals y sinergia Web + Redes | 1 a 2 páginas (nuevas o actualizadas) |
| **Miércoles** | Diseño Web y Localidades | Ciudades o zonas estratégicas (Regla #16: 1 sola ciudad o 1 zona reconocible por slug) | 1 a 2 páginas (nuevas o actualizadas) |
| **Jueves** | Especialista SEO por Rubro / CMS | SEO aplicado a industrias (inmobiliarias, abogados, salud, tiendas) y plataformas | 1 a 2 páginas (nuevas o actualizadas) |
| **Viernes** | Diseño Web, Demos y Embudos | Páginas conectadas a las 13 Demos Interactivas, cotizadores y Landings Modo Funnel | 1 a 2 páginas (nuevas o actualizadas) |
| **Sábado** | Especialista SEO Local, Maps y Analítica | Dominio de San Juan, Google Maps, Search Console, GA4 y citación en IA (AEO/GEO) | 1 a 2 páginas (nuevas o actualizadas) |
| **Domingo** | **Comando Estratégico y Auditoría** | Ejecución de `sunday_seo_command.py`, actualización de este archivo y Plan de la Semana | 1 Reporte Profundo + Hoja de Ruta |

### Por qué hacemos Reporte Profundo los Domingos (y no reportes pesados diarios)
1. **Latencia de Google Search Console (48 hs):** GSC consolida los datos definitivos con 2 días de retraso y las posiciones orgánicas tienen micro-fluctuaciones diarias normales. Analizar métricas todos los días genera ruido estadístico.
2. **Ventana de Maduración de 14 a 28 días:** Toda página nueva o cirugía SEO necesita mínimo 2 semanas desde su envío por Indexing API para mostrar su verdadera tracción de impresiones y clics.
3. **Agilidad de Lunes a Sábado:** De lunes a sábado no perdemos tiempo en reportes burocráticos; solo corremos el chequeo de 10 segundos (`python scratch/check_cannibalization.py "<keyword>"`) antes de crear o editar según lo dictado el domingo.

---

## 2. Protocolo Estricto Anti-Canibalización ("Actualizar antes que Duplicar")

Antes de aprobar cualquier tema en la planificación del domingo:
1. Ejecutar `python scratch/check_cannibalization.py "<keyword o título propuesto>"`.
2. **Si el solapamiento es >= 70% con una URL existente:** **PROHIBIDO crear un artículo nuevo.** Esa tarea se convierte en una **Cirugía de Optimización / Boost** sobre la URL que ya existe (mejorar `<title>` para subir CTR, agregar nuevas sub-preguntas H2 detectadas en GSC, enriquecer tablas comparativas y sumarle 3 enlaces internos entrantes).
3. **Si el solapamiento está entre 45% y 69%:** Solo se crea si la intención de búsqueda es claramente distinta (por ejemplo, *"cuánto cobra Tiendanube"* vs. *"cómo hacer SEO en Tiendanube"*), diferenciando el H1 y enlazando ambas páginas entre sí.
4. **Si el solapamiento es < 45%:** Luz verde total para crear la nueva guía.

---

## 3. Evolución Histórica de Domingos (Bitácora de Métricas)

### Semana 1 (Auditoría Integral y Baseline) — Domingo 8 de Noviembre de 2026

#### A. Estado del Inventario y Arquitectura Técnica
- **URLs Canónicas en `sitemap.xml` / `public/sitemap.xml`:** `171` URLs activas (`200 OK`, 0 redirecciones en sitemap).
- **Guías y Herramientas en `/blog/`:** `153` guías activas (`12` en la categoría *Auditoría SEO, Velocidad e IA*).
- **Inventario Indexable Detectado por Escáner Local:** `156` páginas canónicas principales auditadas.
- **Archivo `/llms.txt`:** Activo en raíz y `public/llms.txt` para descubrimiento por crawlers de ChatGPT, Perplexity, Claude y Gemini.
- **Regla Visual y Editorial:** `0` emojis decorativos en todo el sitio (Regla #17 de `MEMORY.md`) + pastillas de filtro con estado activo dinámico en `/blog/`.
- **Implementación de Eventos en GA4 (`G-KWD0WYVK4J` — Propiedad `554839707`):**
  - Desplegado en las 171 páginas del sitio mediante `src/js/whatsapp.js` y `src/js/main.js`.
  - Nuevos eventos de conversión activados en producción hoy:
    1. `generate_lead` (Evento oficial de conversión de GA4 con `service_intent`, `lead_source`, `cta_text`, `value`, `currency`).
    2. `whatsapp_click` (Evento detallado de clic a cualquier botón o link de WhatsApp).
    3. `view_demo` (Registro de qué Demo Interactiva abre el usuario y desde qué página).
    4. `use_interactive_calculator` (Uso de calculadoras de indemnización, cotizador de vajilla, catering, funnel o generador QR).
    5. `faq_expand` (Qué pregunta frecuente abre el usuario antes de consultar).
    6. `article_read_75` (Lectura humana profunda superior al 75% del artículo tras +8s en página).
  - *Nota técnica sobre eventos:* La ventana de los últimos 7 días previa al deploy registra eventos estándar (`page_view`: 162, `user_engagement`: 104, `session_start`: 83, `first_visit`: 55, `scroll`: 37). Los nuevos 6 eventos de negocio se consolidarán en los reportes de GA4 en las próximas 24 a 48 hs.

#### B. Métricas de Google Search Console (Últimos 28 días en vivo)
- **Impresiones Totales:** `1.434` impresiones.
- **Clics Orgánicos Totales:** `6` clics registrados en:
  - `/` (Home): `2` clics | `8` impr | **Posición media `3.0`**
  - `/blog/configurar-correo-corporativo-outlook-firma-profesional/`: `1` clic | `32` impr | **Posición media `10.3`**
  - `/blog/generador-link-qr-whatsapp-gratis/`: `1` clic | `17` impr | **Posición media `21.3`**
  - `/blog/hotmart-argentina-comisiones-impuestos-alternativa-funnel/`: `1` clic | `12` impr | **Posición media `6.3`**
  - `/blog/tiendanube-linktree-vs-web-propia-a-medida/`: `1` clic | `10` impr | **Posición media `4.7`**
- **Top 10 Páginas por Volumen de Impresiones (Tracción Temprana):**
  1. `/blog/como-registrar-dominio-com-ar-nic-argentina/` (`395` impr, Pos `76.1`)
  2. `/blog/dominio-com-vs-com-ar-cual-conviene-argentina/` (`239` impr, Pos `60.4`)
  3. `/blog/como-crear-correo-corporativo-dominio-propio-gmail/` (`201` impr, Pos `80.9`)
  4. `/blog/diseno-web-mendoza/` (`55` impr, Pos `80.2`)
  5. `/blog/cuanto-cuesta-una-pagina-web-argentina/` (`54` impr, Pos `79.5`)
  6. `/blog/configurar-correo-corporativo-outlook-firma-profesional/` (`32` impr, Pos `10.3` + `1` clic)
  7. `/blog/generador-link-qr-whatsapp-gratis/` (`17` impr, Pos `21.3` + `1` clic)
  8. `/blog/hotmart-argentina-comisiones-impuestos-alternativa-funnel/` (`12` impr, Pos `6.3` + `1` clic)
  9. `/blog/tiendanube-linktree-vs-web-propia-a-medida/` (`10` impr, Pos `4.7` + `1` clic)
  10. `/` (Home): (`8` impr, Pos `3.0` + `2` clics)
- **Top Consultas GSC (por volumen de impresiones):**
  - `comprar dominio .ar` (`50` impr, Pos `69.4`)
  - `comprar dominios .ar` (`37` impr, Pos `81.1`)
  - `correo con dominio propio` (`34` impr, Pos `87.2`)
  - `dominios argentina` (`32` impr, Pos `78.6`)
  - `registro de dominios .ar` (`26` impr, Pos `93.4`)
  - `diseño web san luis` (`25` impr, Pos `81.1`)
  - `registrar dominio .ar` (`25` impr, Pos `93.6`)
  - `diseño web mendoza` (`23` impr, Pos `83.8`)
  - `diseño web en mendoza` (`21` impr, Pos `86.5`)
  - `dominio .com .ar` (`21` impr, Pos `41.6`)
  - `dominios .ar` (`21` impr, Pos `49.7`)
  - `dominio .com` (`20` impr, Pos `57.0`)
- **Oportunidades en "Striking Distance" (23 consultas en Posiciones 4.0 a 20.0 — Candidatas a Top 3):**
  - `[Pos 8.7]` `pagina web inmobiliarias` (`3` impr, `0` clics)
  - `[Pos 14.7]` `outlook corporativo` (`3` impr, `0` clics)
  - `[Pos 6.0]` `erik site` (`2` impr, `0` clics)
  - `[Pos 10.5]` `correo corporativo outlook` (`2` impr, `0` clics)
  - `[Pos 11.0]` `diseño web quilmes` (`2` impr, `0` clics)
  - `[Pos 16.5]` `godaddy argentina` (`2` impr, `0` clics)
  - `[Pos 6.0]` `lumina pilates` (`1` impr, `0` clics)
  - `[Pos 7.0]` `"reposición vajilla"` (`1` impr, `0` clics)
  - `[Pos 8.0]` `.com.ar` (`1` impr, `0` clics)
  - `[Pos 8.0]` `crear correo corporativo outlook gratis` (`1` impr, `0` clics)
  - `[Pos 8.0]` `erik web` (`1` impr, `0` clics)
  - `[Pos 8.0]` `tiendanube cobra comision por venta` (`1` impr, `0` clics)

#### C. Métricas de Google Analytics 4 (Últimos 7 días en vivo)
- **Usuarios Activos:** `56` usuarios (`83` sesiones, `162` vistas de página).
- **Desglose por Canal:**
  - `Direct`: `23` usuarios | `29` sesiones | `9` engaged sessions
  - `Paid Social`: `22` usuarios | `22` sesiones | `4` engaged sessions
  - `Organic Search`: `5` usuarios | `24` sesiones | `17` engaged sessions (**70,8% de engagement rate**; promedio de 4,8 sesiones por usuario, confirmando alta calidad y retención de lectura).
  - `Unassigned`: `3` usuarios | `3` sesiones | `0` engaged sessions
  - `Organic Social`: `1` usuario | `1` sesión | `0` engaged sessions
  - `Referral`: `1` usuario | `1` sesión | `0` engaged sessions

#### D. Estado de SerpBear Local
- **Base de Datos SQLite (`C:\Users\erikl\serpbear\data\database.sqlite`):** Activa y accesible, actualmente sin keywords configuradas en la instancia local (`0` registros). Se recomienda sembrar las 12 keywords clave de Striking Distance de GSC en SerpBear para seguimiento posicional diario automatizado.

#### E. Auditoría de Canibalización de Nuevos Temas (`check_cannibalization.py`)
- **Hallazgo Crítico:** La propuesta preliminar *"Páginas Web para Empresas de Limpieza de Oficinas y Consorcios"* arrojó un **71% de solapamiento** con la URL existente `/blog/paginas-web-empresas-limpieza-finales-obra-tapizados/`. Siguiendo la regla de oro **"Actualizar antes que Duplicar"**, se canceló la creación de una URL nueva y se programó una **Cirugía de Boost** sobre la página existente, reemplazando el cupo nuevo de ese día por un rubro B2B con **0% de canibalización**: **Empresas de Logística, Transporte de Carga y Fletes** (43% máx tokens genéricos, 0% en términos de negocio).

---

## 4. Plan de Ataque para Esta Semana (Lunes 9 al Sábado 14 de Noviembre de 2026)

> **Directriz de la Semana:** Cada día combina **1 Cirugía de Optimización / Boost** sobre URLs con impresiones o en Striking Distance + **1 Guía Nueva 100% libre de canibalización** auditada con `check_cannibalization.py`. Se respeta rigurosamente la alternancia: Lunes/Miércoles/Viernes (Diseño Web) y Martes/Jueves/Sábado (SEO).

### Lunes 9/11 — Eje Diseño Web y Conversión
1. **Cirugías de Striking Distance en GSC:**
   - **Cirugía 1 (Pos 8.7):** `/blog/paginas-web-para-inmobiliarias-argentina/` (`pagina web inmobiliarias`). Inyectar bloque H2 de respuesta directa para consultas comerciales de inmobiliarias y enlazar bidireccionalmente con la nueva guía de SEO Inmobiliario.
   - **Cirugía 2 (Pos 16.5):** `/blog/crear-pagina-web-godaddy-conviene-argentina/` (`godaddy argentina`). Mejorar título y agregar comparativa de costos de renovación SSL en pesos vs. dólares.
2. **Artículo Nuevo Diseño Web (0% Canibalización — 50% máx genérico con indumentaria):**
   - **Slug propuesto:** `/blog/paginas-web-distribuidoras-mayoristas-alimentos-bebidas-argentina/`
   - **Título Sturm:** *Páginas Web para Distribuidoras Mayoristas de Alimentos y Bebidas: Catálogo Ágil y Pedidos por WhatsApp*
   - **Enfoque BoFu:** Preventa a comercios, listas de precios diferenciadas por volumen y envío directo de pedidos consolidados a WhatsApp sin comisiones.

### Martes 10/11 — Eje Especialista SEO, Velocidad e IA
1. **Cirugía de Autoridad Técnica (Pos 8.0 a 10.5 — Primer Clic Orgánico):**
   - **URL:** `/blog/configurar-correo-corporativo-outlook-firma-profesional/`
   - **Acción:** Incorporar capturas y micro-sección para resolver el error recurrente de sincronización IMAP/SMTP en Outlook móvil y desktop, empujándola del puesto 10.3 al Top 3 nacional.
2. **Artículo Nuevo Autoridad SEO (0% Canibalización — 46% con guía general de indexación):**
   - **Slug propuesto:** `/blog/auditoria-seo-google-search-console-errores-indexacion-argentina/`
   - **Título Sturm:** *Errores de Indexación en Google Search Console: Cómo Solucionarlos y Recuperar Tráfico en tu Empresa*
   - **Enfoque Técnico:** Diagnóstico de *"Rastreada: actualmente sin indexar"*, *"Página duplicada sin etiqueta canonical"* y cómo forzar inspección efectiva.

### Miércoles 11/11 — Eje Diseño Web y Localidades (Regla #16: 1 Ciudad por Slug)
1. **Cirugía Geográfica de Alta Impresión:**
   - **URLs:** `/blog/diseno-web-mendoza/` (`55` impr) y `/blog/diseno-web-san-luis/` (`25` impr).
   - **Acción:** Afilar los H2 para que coincidan con las búsquedas exactas registradas en GSC (*"diseño web en mendoza"*, *"diseño web san luis"*), agregando testimonios de Cuyo y enlaces desde `/san-juan/`.
2. **Artículo Nuevo Ciudad Específica (Regla #16 — 0% Canibalización con ciudades existentes):**
   - **Slug propuesto:** `/blog/diseno-web-villa-carlos-paz/`
   - **Título Sturm:** *Diseño de Páginas Web en Villa Carlos Paz (Córdoba): Precios 2026, Turismo y Comercios*
   - **Enfoque BoFu:** Hotelería, cabañas, gastronomía y espectáculos en el Valle de Punilla, enlazando a la guía provincial `/blog/diseno-web-cordoba/`.

### Jueves 12/11 — Eje Especialista SEO por Rubro / CMS
1. **Cirugía SEO E-Commerce (Pos 8.0 en GSC):**
   - **URL:** `/blog/precios-comisiones-tiendanube-alternativas-argentina/`
   - **Acción:** Optimizar para la consulta en Striking Distance *"tiendanube cobra comision por venta"*, aclarando la escala de comisiones según el medio de pago (Pago Nube vs. pasarelas externas).
2. **Artículo Nuevo SEO Vertical de Salud (0% Canibalización — 40% máx):**
   - **Slug propuesto:** `/blog/seo-para-medicos-clinicas-odontologos-argentina-google/`
   - **Título Sturm:** *SEO Médico y para Odontólogos en Argentina: Cómo Posicionar tu Consultorio en Google y Captar Pacientes Particulares*
   - **Enfoque BoFu:** Ficha de Google Maps médica, SEO local de especialidades, reputación y turnos online conectados a `/demos/medicina/` y `/demos/odontologia/`.

### Viernes 13/11 — Eje Diseño Web, Demos y Embudos
1. **Cirugías de Conversión y Boost Directo:**
   - **Cirugía 1 (Alta Impresión):** `/blog/cuanto-cuesta-una-pagina-web-argentina/` (`54` impr). Actualizar referencias de costos 2026 y enlaces a las 13 Demos Interactivas.
   - **Cirugía 2 (Boost Anti-Canibalización 71%):** `/blog/paginas-web-empresas-limpieza-finales-obra-tapizados/`. Sumar encabezados H2 específicos para *"Abonos de limpieza de consorcios y oficinas corporativas"* y *"Cotizador rápido de cuadrillas por WhatsApp"*, absorbiendo la intención de búsqueda sin crear URLs duplicadas.
2. **Artículo Nuevo B2B Logística (0% Canibalización — 43% máx):**
   - **Slug propuesto:** `/blog/paginas-web-empresas-logistica-transporte-carga-fletes-argentina/`
   - **Título Sturm:** *Páginas Web para Empresas de Logística y Transporte de Carga en Argentina: Cotizador de Fletes y Clientes Corporativos*
   - **Enfoque BoFu:** Cotizador rápido por WhatsApp (origen, destino, tipo de carga, m3), geolocalización en parques industriales y enlaces al cotizador interactivo.

### Sábado 14/11 — Eje Especialista SEO Local, Maps y Analítica
1. **Cirugía SEO Local (Pos 11.0 en GSC):**
   - **URL:** `/blog/diseno-web-quilmes/` (`diseño web quilmes`).
   - **Acción:** Reforzar el interlinking entrante desde `/blog/diseno-web-zona-sur/` y optimizar la respuesta directa para catapultarla al Top 3 de Zona Sur.
2. **Artículo Nuevo SEO Local y Reseñas (0% Canibalización — 57% máx con agregar negocio):**
   - **Slug propuesto:** `/blog/como-conseguir-resenas-google-maps-posicionar-negocio-local/`
   - **Título Sturm:** *Cómo Conseguir Más Reseñas en Google Maps: Estrategias Éticas con QR para Subir al Top 3 Local*
   - **Enfoque BoFu:** Sinergia entre nuestro Generador QR de WhatsApp/Google y la reputación local, plantillas de mensajes para pedir reseñas y prevención de penalizaciones de Google.

---

## 5. Próximo Comando Dominical Programado (Domingo 15 de Noviembre de 2026)
- Auditar los primeros datos registrados por los nuevos eventos de negocio en GA4 (`generate_lead`, `whatsapp_click`, `view_demo`, `use_interactive_calculator`, `faq_expand`, `article_read_75`).
- Evaluar el impacto de las cirugías en las consultas de Striking Distance (`pagina web inmobiliarias`, `outlook corporativo`, `diseño web quilmes`, `godaddy argentina`).
- Medir la tracción inicial de impresiones del Batch 16 de Autoridad SEO y las nuevas publicaciones de la semana.
- Trazar el Plan de Ataque para la Semana 2 (16 al 21 de Noviembre de 2026).
