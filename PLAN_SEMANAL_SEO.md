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
2. **Si el solapamiento es >= 70% con una URL existente:** **PROHIBIDO crear un artículo nuevo.** Esa tarea se convierte en una **Cirugía de Optimización** sobre la URL que ya existe (mejorar `<title>` para subir CTR, agregar nuevas sub-preguntas H2 detectadas en GSC, enriquecer tablas comparativas y sumarle 3 enlaces internos entrantes).
3. **Si el solapamiento está entre 45% y 69%:** Solo se crea si la intención de búsqueda es claramente distinta (por ejemplo, *"cuánto cobra Tiendanube"* vs. *"cómo hacer SEO en Tiendanube"*), diferenciando el H1 y enlazando ambas páginas entre sí.
4. **Si el solapamiento es < 45%:** Luz verde total para crear la nueva guía.

---

## 3. Evolución Histórica de Domingos (Bitácora de Métricas)

### Semana 1 (Baseline Inicial) — Domingo 8 de Noviembre de 2026

#### A. Estado del Inventario y Arquitectura Técnica
- **URLs Canónicas en `sitemap.xml` / `public/sitemap.xml`:** `171` URLs activas (`200 OK`, 0 redirecciones en sitemap).
- **Guías y Herramientas en `/blog/`:** `153` guías activas (`12` en la categoría *Auditoría SEO, Velocidad e IA*).
- **Archivo `/llms.txt`:** Activo en raíz y `public/llms.txt` para descubrimiento por crawlers de ChatGPT, Perplexity, Claude y Gemini.
- **Regla Visual y Editorial:** `0` emojis decorativos en todo el sitio (Regla #17) + pastillas de filtro con estado activo dinámico en `/blog/`.
- **Implementación en GA4 (`G-KWD0WYVK4J` — Propiedad `554839707`):**
  - Activado el seguimiento global en las 171 páginas del sitio mediante `src/js/whatsapp.js` y `src/js/main.js`.
  - Nuevos eventos en producción a partir de hoy:
    1. `generate_lead` (Evento oficial de conversión de GA4 con `service_intent`, `lead_source`, `cta_text`, `value`, `currency`).
    2. `whatsapp_click` (Evento detallado de clic a cualquier botón o link de WhatsApp).
    3. `view_demo` (Registro de qué Demo Interactiva abre el usuario y desde qué página).
    4. `use_interactive_calculator` (Uso de calculadoras de indemnización, cotizador de vajilla, catering, funnel o generador QR).
    5. `faq_expand` (Qué pregunta frecuente abre el usuario antes de consultar).
    6. `article_read_75` (Lectura humana profunda superior al 75% del artículo tras +8s en página).

#### B. Métricas de Google Search Console (Últimos 28 días)
- **Impresiones Totales:** `1.434` impresiones (en rápido ascenso a medida que Google indexa las nuevas camadas).
- **Clics Orgánicos:** `6` clics primeros registrados en:
  - `/` (Home): `2` clics, `8` impr, **Posición media `3.0`**
  - `/blog/configurar-correo-corporativo-outlook-firma-profesional/`: `1` clic, `32` impr, **Posición media `10.3`**
  - `/blog/generador-link-qr-whatsapp-gratis/`: `1` clic, `17` impr, **Posición media `21.3`**
  - `/blog/hotmart-argentina-comisiones-impuestos-alternativa-funnel/`: `1` clic, `12` impr, **Posición media `6.3`**
  - `/blog/tiendanube-linktree-vs-web-propia-a-medida/`: `1` clic, `10` impr, **Posición media `4.7`**
- **Páginas con Mayor Volumen de Impresiones (Tracción Temprana):**
  - `/blog/como-registrar-dominio-com-ar-nic-argentina/` (`395` impresiones)
  - `/blog/dominio-com-vs-com-ar-cual-conviene-argentina/` (`239` impresiones)
  - `/blog/como-crear-correo-corporativo-dominio-propio-gmail/` (`201` impresiones)
  - `/blog/diseno-web-mendoza/` (`55` impresiones)
  - `/blog/cuanto-cuesta-una-pagina-web-argentina/` (`54` impresiones)
- **Consultas en "Striking Distance" (Posiciones 4.0 a 20.0 — Candidatas a Cirugía de Subida a Top 3):**
  - `pagina web inmobiliarias` — **Posición `8.7`** (`3` impr)
  - `correo corporativo outlook` / `crear correo corporativo outlook gratis` — **Posición `8.0` a `10.5`** (`6` impr combinadas)
  - `tiendanube cobra comision por venta` — **Posición `8.0`**
  - `diseño web quilmes` — **Posición `11.0`** (ya optimizada ayer; monitorear subida en 14 días)
  - `godaddy argentina` — **Posición `16.5`**

#### C. Métricas de Google Analytics 4 (Últimos 7 días — Pre-Activación de Nuevos Eventos)
- **Usuarios Activos:** `56` usuarios (`83` sesiones, `162` vistas de página).
- **Desglose por Canal:**
  - `Direct`: `23` usuarios / `29` sesiones (`9` sesiones con interacción)
  - `Paid Social`: `22` usuarios / `22` sesiones (`4` sesiones con interacción)
  - `Organic Search`: `5` usuarios / `24` sesiones (`17` sesiones con interacción -> **70,8% de engagement**, el canal de mayor calidad de lectura).

---

## 4. Plan de Ataque para Esta Semana (Lunes 9 al Sábado 14 de Noviembre de 2026)

> **Directriz de la Semana:** Combinar **1 cirugía de optimización por día** sobre páginas que ya tienen impresiones en GSC con **1 guía nueva 0% canibalizada** respetando la alternancia Lunes/Miércoles/Viernes (Diseño Web) y Martes/Jueves/Sábado (SEO).

### Lunes 9/11 — Eje Diseño Web y Conversión
1. **Cirugía Striking Distance (Pos 8.7 y Pos 16.5):**
   - Optimizar `/blog/paginas-web-para-inmobiliarias-argentina/` (que ya asoma en posición `8.7` para `pagina web inmobiliarias`) sumando interlinking cruzado con la nueva guía de SEO Inmobiliario y bloque de preguntas reales de GSC.
   - Optimizar `/blog/crear-pagina-web-godaddy-conviene-argentina/` (posición `16.5` para `godaddy argentina`).
2. **Artículo Nuevo Diseño Web (0% Canibalización):**
   - `/blog/paginas-web-distribuidoras-mayoristas-alimentos-bebidas-argentina/` (*Páginas Web para Distribuidoras Mayoristas de Alimentos, Bebidas y Limpieza con Pedidos por WhatsApp*).

### Martes 10/11 — Eje Especialista SEO, Velocidad e IA
1. **Cirugía de Autoridad Técnica (Pos 8.0–10.3):**
   - Reforzar `/blog/configurar-correo-corporativo-outlook-firma-profesional/` (que ya logró su primer clic orgánico y promedia posición `10.3`) para meterla en el Top 3 nacional.
2. **Artículo Nuevo Autoridad SEO (0% Canibalización):**
   - `/blog/auditoria-seo-google-search-console-errores-indexacion-argentina/` (*Cómo Leer Google Search Console en tu Empresa: Guía para Detectar Páginas que Pierden Posiciones*).

### Miércoles 11/11 — Eje Diseño Web y Localidades (Regla #16)
1. **Cirugía Geográfica de Alta Impresión:**
   - Optimizar `/blog/diseno-web-mendoza/` (`55` impresiones en GSC) y `/blog/diseno-web-san-luis/` (`25` impresiones para `diseño web san luis`), ajustando encabezados H2 exactos y enlaces desde páginas vecinas de Cuyo (`/san-juan/`).
2. **Artículo Nuevo Ciudad Específica (Regla #16 — 1 sola ciudad por slug):**
   - `/blog/diseno-web-villa-carlos-paz/` (*Diseño de Páginas Web en Villa Carlos Paz (Córdoba): Turismo, Hoteles, Teatros y Comercios*).

### Jueves 12/11 — Eje Especialista SEO por Rubro
1. **Artículo Nuevo SEO Vertical (0% Canibalización):**
   - `/blog/seo-para-medicos-clinicas-odontologos-argentina-google/` (*SEO Médico y para Odontólogos en Argentina: Cómo Posicionar tu Consultorio en Google y Captar Pacientes Particulares*, conectado directo a `/demos/medicina/` y `/demos/odontologia/`).

### Viernes 13/11 — Eje Diseño Web, Demos y Embudos
1. **Cirugía de Conversión en Páginas Top:**
   - Optimizar `/blog/cuanto-cuesta-una-pagina-web-argentina/` (`54` impresiones en GSC) enriqueciendo la tabla de precios 2026 y enlaces directos a las 13 Demos.
2. **Artículo Nuevo Diseño Web Rubro B2B (0% Canibalización):**
   - `/blog/paginas-web-empresas-limpieza-mantenimiento-consorcios-oficinas/` (*Páginas Web para Empresas de Limpieza de Oficinas, Consorcios y Final de Obra en Argentina*).

### Sábado 14/11 — Eje Especialista SEO Local, Maps y Analítica
1. **Artículo Nuevo SEO Local (0% Canibalización):**
   - `/blog/como-conseguir-resenas-google-maps-posicionar-negocio-local/` (*Cómo Conseguir Más Reseñas en Google Maps con QR y Subir al Top 3 Local en tu Ciudad*, enlazando a nuestro Generador QR de WhatsApp y al servicio de Auditoría SEO Local).

### Domingo 15/11 — Próximo Comando Dominical Programado
- Evaluar los primeros 7 días de datos de los nuevos eventos de GA4 (`generate_lead`, `whatsapp_click`, `view_demo`, `faq_expand`, `article_read_75`).
- Medir el impacto de los 12 artículos de Autoridad SEO publicados en los Batches 15 y 16.
- Definir el Plan de Ataque de la Semana 2 (16/11 al 21/11).
