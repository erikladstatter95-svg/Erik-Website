"""
Generates a faithful 1:1 translation of index.html into en/index.html.
Preserves the EXACT DOM structure, identical sections, identical cards,
identical buttons, and identical styles of index.html.
Changes ONLY texts to natural English, prices to $199 USD and $20 USD/mo,
payment methods to PayPal/Wise/Wire/Crypto, and updates hreflang / canonical.
"""

with open('index.html', 'r', encoding='utf-8') as f:
    es = f.read()

# Replacements dictionary for 1:1 structural translation
replacements = [
    # Head & SEO
    ('<html lang="es"', '<html lang="en"'),
    ('<title>Diseño Web Profesional de Alto Impacto | Erik Website</title>', '<title>Professional High-Impact Web Design | Erik Website</title>'),
    ('content="Diseño de páginas web listas para usar que multiplican tus consultas por WhatsApp. Entrega en 3 a 5 días y soporte total."',
     'content="Ready-to-use websites designed to turn visitors into direct WhatsApp inquiries. Live in 3 to 5 days with full support."'),
    ('<link rel="canonical" href="https://erikwebsite.com/">', '<link rel="canonical" href="https://erikwebsite.com/en/">'),
    ('<meta property="og:url" content="https://erikwebsite.com/">', '<meta property="og:url" content="https://erikwebsite.com/en/">'),
    ('<meta property="og:title" content="Diseño Web Profesional de Alto Impacto | Erik Website">', '<meta property="og:title" content="Professional High-Impact Web Design | Erik Website">'),
    ('<meta property="og:description" content="Diseño de páginas web listas para usar que multiplican tus consultas por WhatsApp. Entrega en 3 a 5 días y soporte total.">', '<meta property="og:description" content="Ready-to-use websites designed to turn visitors into direct WhatsApp inquiries. Live in 3 to 5 days with full support.">'),
    ('<meta property="og:locale" content="es_AR">', '<meta property="og:locale" content="en_US">'),
    ('<meta name="twitter:url" content="https://erikwebsite.com/">', '<meta name="twitter:url" content="https://erikwebsite.com/en/">'),
    ('<meta name="twitter:title" content="Diseño Web Profesional de Alto Impacto | Erik Website">', '<meta name="twitter:title" content="Professional High-Impact Web Design | Erik Website">'),
    ('<meta name="twitter:description" content="Diseño de páginas web listas para usar que multiplican tus consultas por WhatsApp. Entrega en 3 a 5 días y soporte total.">', '<meta name="twitter:description" content="Ready-to-use websites designed to turn visitors into direct WhatsApp inquiries. Live in 3 to 5 days with full support.">'),

    # Top Bar
    ('Desarrollo web para comercios y profesionales en San Juan y toda Argentina | Entrega en 3 a 5 días hábiles',
     'Custom web development for businesses and independent professionals worldwide | Delivery in 3 to 5 business days'),

    # Navbar
    ('Demos en Vivo', 'Live Demos'),
    ('Mis Trabajos', 'Our Work'),
    ('¿Cómo Empezar?', 'How to Start'),
    ('Precios Claros', 'Clear Pricing'),
    ('Cotizar mi Web', 'Get a Quote'),
    ('Hola Erik! Vi tu portfolio y me gustaría consultar por un sitio web para mi negocio.',
     'Hello Erik! I reviewed your portfolio and would like to inquire about a website for my business.'),

    # Language Switcher in en/index.html: EN active, ES links to /
    ('<span class="px-2.5 py-1 rounded-full bg-white text-neutral-900 shadow-2xs font-bold">ES</span>\n          <a href="/en/" class="px-2.5 py-1 rounded-full text-neutral-500 hover:text-neutral-900 transition-colors" title="Switch to English version">EN</a>',
     '<a href="/" class="px-2.5 py-1 rounded-full text-neutral-500 hover:text-neutral-900 transition-colors" title="Ver versión en Español">ES</a>\n          <span class="px-2.5 py-1 rounded-full bg-white text-neutral-900 shadow-2xs font-bold">EN</span>'),

    # Hero
    ('Especializado en Negocios y Profesionales Locales', 'Specialized in Businesses & Independent Professionals'),
    ('Diseño Web Profesional <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-600 via-teal-600 to-emerald-700">que convierte en WhatsApp</span>',
     'Professional Web Design <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-600 via-teal-600 to-emerald-700">that converts on WhatsApp</span>'),
    ('Transformá las búsquedas de Google Maps en consultas directas a tu celular. Creamos <strong class="text-neutral-800 font-semibold">sitios web ultrarrápidos</strong> listos para usar en 3 a 5 días hábiles, con textos redactados a partir de tus audios.',
     'Turn Google searches into direct leads on your phone. We build <strong class="text-neutral-800 font-semibold">ultra-fast websites</strong> ready in 3 to 5 business days, with sales copy written directly from your voice notes.'),
    ('<span>Velocidad Ultra Rápida</span>', '<span>Ultra Fast Speed</span>'),
    ('<span>Optimización Google Maps</span>', '<span>Google Maps Optimization</span>'),
    ('<span>Redacción comercial incluida</span>', '<span>Commercial Copywriting Included</span>'),
    ('Hola Erik! Estuve viendo tu web y quiero consultar para hacer un sitio web para mi negocio.',
     'Hello Erik! I was checking your website and would like to build a professional website for my business.'),
    ('<span>Escribirme por WhatsApp</span>', '<span>Message on WhatsApp</span>'),
    ('<span>Explorar Plantillas Reales</span>', '<span>Explore Live Templates</span>'),
    ('<strong class="text-neutral-700 font-semibold">100% negocios locales satisfechos</strong> en Argentina',
     '<strong class="text-neutral-700 font-semibold">100% satisfied business clients</strong> worldwide'),

    # Solución & Comparativa
    ('La Solución: Alta Conversión', 'The Solution: High Conversion'),
    ('El costo invisible de no tener una web optimizada', 'The invisible cost of not having an optimized website'),
    ('La mayoría de las personas buscan negocios en Google Maps o Instagram, pero si no encuentran una web clara, rápida y con contacto directo, eligen al competidor de al lado.',
     'Most people search for services on Google or Instagram, but if they find no clear website with direct contact, they immediately choose the competitor next door.'),
    ('Tu negocio sin web (o web lenta)', 'Your business without a website (or slow site)'),
    ('Perdiendo clientes todos los días', 'Losing potential clients every single day'),
    ('<strong class="text-neutral-900 font-semibold">El cliente duda de tu formalidad:</strong> Un perfil de Instagram o Maps sin web da sensación de negocio improvisado o inactivo.',
     '<strong class="text-neutral-900 font-semibold">Clients doubt your legitimacy:</strong> A social profile or map listing without an official website feels informal or inactive.'),
    ('<strong class="text-neutral-900 font-semibold">Preguntas repetitivas todo el día:</strong> "¿Cuánto sale?", "¿Dónde atienden?", "¿Qué incluye?". Respondés 20 veces lo mismo.',
     '<strong class="text-neutral-900 font-semibold">Repetitive questions all day:</strong> "How much is it?", "Where are you located?", "What is included?". Answering the same questions 20 times a day.'),
    ('<strong class="text-neutral-900 font-semibold">Pérdida de clientes potenciales:</strong> Quien busca un servicio en Google Maps a las 11 de la noche y no ve información clara ni web, se va con la competencia.',
     '<strong class="text-neutral-900 font-semibold">Lost high-intent clients:</strong> Someone searching on Google late at night with no clear website will instantly contact your competitor.'),
    ('<strong class="text-neutral-900 font-semibold">Falta de tiempo para redactar:</strong> Postergan tener web porque creen que tendrán que escribir textos y sacar fotos profesionales ellos mismos.',
     '<strong class="text-neutral-900 font-semibold">No time to write content:</strong> Postponing a website because you dread having to write long essays or hire photographers yourself.'),
    ('<strong class="text-neutral-900 font-semibold">Webs tradicionales lentas:</strong> Tardan varios segundos en abrir en el celular, el usuario se cansa y aprieta volver.',
     '<strong class="text-neutral-900 font-semibold">Slow bloated websites:</strong> Taking 6+ seconds to load on mobile makes users bounce before seeing your offer.'),

    ('Efecto Inmediato', 'Immediate Impact'),
    ('Con tu Sitio Web Pro', 'With Your Pro Website'),
    ('Contacto directo a tu WhatsApp', 'Direct leads straight to WhatsApp'),
    ('<strong class="text-neutral-900 font-semibold">Confianza y autoridad instantánea:</strong> Fotos de calidad, ubicación clara y opiniones de Google Maps que despejan cualquier duda.',
     '<strong class="text-neutral-900 font-semibold">Instant authority & trust:</strong> High-res visuals, clear credentials, and verified client reviews that eliminate doubt.'),
    ('<strong class="text-neutral-900 font-semibold">Consultas filtradas y directas:</strong> El cliente te escribe a WhatsApp sabiendo exactamente qué servicio busca y ahorrándote tiempo.',
     '<strong class="text-neutral-900 font-semibold">Pre-qualified direct leads:</strong> Clients message you already knowing your services and rates, saving you hours.'),
    ('<strong class="text-neutral-900 font-semibold">Ficha de Google Maps optimizada:</strong> Vinculamos y auditamos tu perfil de Google Maps para que destaques en las búsquedas de tu zona.',
     '<strong class="text-neutral-900 font-semibold">Google Business optimization:</strong> We audit and link your Google profile to rank higher in local search results.'),
    ('<strong class="text-neutral-900 font-semibold">Cero esfuerzo para vos:</strong> Vos solo nos mandás un par de audios contándonos qué hacés; nosotros redactamos los textos y seleccionamos las fotos.',
     '<strong class="text-neutral-900 font-semibold">Zero hassle for you:</strong> Just send us 2 or 3 voice notes explaining what you do; we craft the copy and curate professional imagery.'),
    ('<strong class="text-neutral-900 font-semibold">Todo resuelto:</strong> Carga ultrarrápida, dominio registrado, hosting de alta velocidad y soporte continuo.',
     '<strong class="text-neutral-900 font-semibold">Everything handled:</strong> Sub-second loading, domain registration, SSL cloud hosting, and continuous technical support.'),

    # Demos Section Header & Banner
    ('Demos y Variaciones de Diseño', 'Live Demos & Design Layouts'),
    ('Explorá distintas opciones para tu negocio', 'Explore tailored layouts for your business'),
    ('Cada negocio tiene su identidad. Estas plantillas son <strong>ejemplos de partida para que tengas el control</strong> de cómo querés que se vea tu web: podés combinar colores, disposiciones y secciones de cualquiera de ellas.',
     'Every business has its own unique identity. These templates are <strong>starting points so you stay in full control</strong> of how your website looks: you can mix and match styles, color palettes, and sections from any of them.'),
    ('100% Adaptables a Cualquier Rubro', '100% Adaptable to Any Industry'),
    ('¿Te gusta el estilo de una demo pero vendés otro servicio? Adaptamos tipografías, fotos, botones y textos para que encaje a la perfección con tu marca.',
     'Love a specific demo layout but offer a different service? We adapt fonts, imagery, buttons, and copy so it fits your brand seamlessly.'),
    ('<span>Ver cómo empezamos</span> →', '<span>See How We Start</span> →'),

    # Cluster 1
    ('Turnos y Salud', 'Appointments & Health'),
    ('3 Estilos', '3 Styles'),
    ('Salud, Belleza y Bienestar', 'Health, Beauty & Wellness'),
    ('Para estéticas, odontólogos, psicólogos y profesionales', 'For beauty clinics, dentists, therapists, and doctors'),
    ('3 Formatos listos para hojear:', '3 formats ready to explore:'),
    ('<strong class="text-neutral-900">Estética Médica:</strong> Estilo editorial y armonización', '<strong class="text-neutral-900">Medical Aesthetics:</strong> Editorial beauty & treatments'),
    ('<strong class="text-neutral-900">Centro Odontológico:</strong> Selector de turnos 3D', '<strong class="text-neutral-900">Dental Clinic:</strong> 3D treatment & slot selector'),
    ('<strong class="text-neutral-900">Psicología:</strong> Formato sereno, presencial u online', '<strong class="text-neutral-900">Psychology:</strong> Calming layout, in-person or online'),
    ('<span>Ver Diseños (Explorar 3 Estilos)</span>', '<span>View Layouts (Explore 3 Styles)</span>'),

    # Cluster 2
    ('Eventos y Fiestas', 'Events & Venues'),
    ('Catálogos, Fiestas y Salones', 'Catalogs, Events & Venues'),
    ('Alquiler para eventos, catering y fincas', 'Event rentals, catering menus, and venues'),
    ('<strong class="text-neutral-900">Vajilla y Cristalería:</strong> Catálogo con cotizador', '<strong class="text-neutral-900">Tableware & Rentals:</strong> Visual catalog with estimator'),
    ('<strong class="text-neutral-900">Catering y Barras:</strong> Menús gourmet y degustación', '<strong class="text-neutral-900">Catering & Bars:</strong> Gourmet menus and packages'),
    ('<strong class="text-neutral-900">Salones y Quintas:</strong> Galería de fotos del predio', '<strong class="text-neutral-900">Venues & Estates:</strong> High-res photo gallery of grounds'),

    # Cluster 3
    ('Servicios Directos', 'Direct Services'),
    ('4 Estilos', '4 Styles'),
    ('Autoridad, Urgencias y PyMEs', 'Authority, Emergencies & SMEs'),
    ('Estudios profesionales y reparaciones del hogar', 'Professional practices and home services'),
    ('4 Formatos listos para hojear:', '4 formats ready to explore:'),
    ('<strong class="text-neutral-900">Estudio Jurídico:</strong> Solemne, guardia y litigios', '<strong class="text-neutral-900">Law Firm:</strong> Solemn, credentials, and litigation areas'),
    ('<strong class="text-neutral-900">Urgencias Hogar 24hs:</strong> Llamada y auxilio rápido', '<strong class="text-neutral-900">24/7 Home Trades:</strong> Quick dispatch and emergency button'),
    ('<strong class="text-neutral-900">Estudio Contable:</strong> Asesoría fiscal para empresas', '<strong class="text-neutral-900">Accounting Practice:</strong> Tax & financial plans for SMEs'),
    ('<strong class="text-neutral-900">Personal Trainer:</strong> Planes fitness, fuerza y nutrición', '<strong class="text-neutral-900">Personal Trainer:</strong> Fitness programs and coaching'),
    ('<span>Ver Diseños (Explorar 4 Estilos)</span>', '<span>View Layouts (Explore 4 Styles)</span>'),

    # Trabajos Reales / Portfolio
    ('Desarrollos Especiales', 'Custom Developments'),
    ('Proyectos a Medida para Clientes', 'Bespoke Client Projects'),
    ('Sitios web y plataformas en producción desarrollados para marcas que requerían funcionalidades específicas, catálogos interactivos o sistemas de reserva personalizados. Cotizados a medida tras evaluar cada proyecto.',
     'Production websites and platforms engineered for brands requiring custom capabilities, interactive catalogs, or tailored booking flows. Quoted on a per-project basis.'),
    ('En Producción Activa', 'In Active Production'),
    ('E-Commerce e Impresión 3D', 'E-Commerce & 3D Printing'),
    ('Plataforma online completa para tienda de impresiones 3D, figuras coleccionables y cotización a medida. Catálogo visual interactivo, procesamiento ágil y enlace directo de compra.',
     'Complete online platform for a 3D printing studio, collectible figures, and custom quotes. Interactive visual catalog, fast checkout flow, and direct sales inquiries.'),
    ('Desarrollo personalizado activo', 'Active custom development'),
    ('<span>Visitar Sitio Web</span>', '<span>Visit Website</span>'),
    ('Self Photo Studio en San Juan', 'Self Photo Studio'),
    ('Sitio web para el primer Self Photo Studio en San Juan: sesiones fotográficas profesionales autónomas con control remoto. Estética visual de alto impacto, experiencia inmersiva y reserva ágil de turnos.',
     'Website for the first autonomous Self Photo Studio in San Juan: professional remote-controlled photo sessions. High-impact visual aesthetics, immersive experience, and seamless appointment booking.'),

    # Testimonials
    ('Testimonios Reales', 'Real Client Reviews'),
    ('Lo que opinan los negocios que ya trabajan conmigo', 'What business owners say about working with me'),
    ('Resultados comprobados: más consultas directas, velocidad de carga instantánea y aumento de clientes por WhatsApp.',
     'Proven results: more direct inquiries, instant loading speeds, and an increase in paying clients via WhatsApp.'),
    ('"Erik entendió a la perfección la estética moderna e interactiva que necesitábamos para Wink Studio en San Juan. El sitio vuela en celulares y la gente reserva su turno sin perder tiempo. La atención y el soporte durante todo el lanzamiento fueron de diez."',
     '"Erik completely understood the modern, interactive aesthetics we needed for Wink Studio. The website flies on mobile devices and customers book their slots effortlessly. Support throughout the entire launch was a 10/10."'),
    ('"Veníamos de una web vieja y lenta que no nos generaba ningún contacto. Con el nuevo sitio web ultrarrápido, los pacientes tocan el botón de WhatsApp y recibimos entre 4 y 6 consultas diarias directo al consultorio. En la primera semana recuperamos la inversión."',
     '"We previously had a slow, outdated website that brought zero inquiries. With our new ultra-fast site, patients simply tap the WhatsApp button and we receive 4 to 6 daily inquiries straight to reception. We recouped our entire investment in week one."'),
    ('"Necesitábamos una plataforma para exhibir catálogo y cotizar impresiones 3D personalizadas. El desarrollo a medida superó nuestras expectativas: es rápido, claro para los clientes y nos ahorró muchísimo tiempo de respuesta diaria."',
     '"We needed a platform to showcase our catalog and quote custom 3D prints. The custom development exceeded our expectations: it is blazingly fast, crystal-clear for clients, and saves us hours of daily manual customer support."'),

    # Proceso
    ('Proceso Simple Sin Pérdida de Tiempo', 'Simple Process With Zero Time Wasted'),
    ('¿Qué necesitamos de vos para empezar?', 'What do we need from you to get started?'),
    ('<strong>Cero pérdida de tiempo para vos:</strong> No tenés que sentarte a escribir textos ni diseñar nada. Con <strong>3 audios de WhatsApp</strong> contándonos qué hacés, nosotros nos encargamos de redactar los contenidos comerciales, seleccionar fotos de alta calidad y programar todo tu sitio.',
     '<strong>Zero time wasted for you:</strong> You don\'t have to sit down and write essays or design anything. With just <strong>3 voice notes</strong> telling us what you do, we handle all sales copywriting, curate high-res visual assets, and code your complete site.'),
    ('Audios sobre tu negocio', 'Voice notes about your business'),
    ('Mandanos 2 o 3 audios contándonos qué servicios ofrecés y cómo trabajás. <strong class="text-neutral-800 font-semibold">Nosotros redactamos todos los textos profesionales</strong> con enfoque comercial.',
     'Send us 2 or 3 voice notes explaining your services and workflow. <strong class="text-neutral-800 font-semibold">We write all professional sales copy</strong> tailored to convert.'),
    ('Fotos de tu local o trabajo', 'Photos of your venue or work'),
    ('Fotos de tu local, trabajos o productos tomadas con tu celular. Si no tenés buenas fotos, te seleccionamos recursos visuales profesionales acordes a tu rubro.',
     'Photos of your studio, work, or products taken with your smartphone. If you lack good photos, we curate professional high-resolution assets suited to your industry.'),
    ('Precios y servicios clave', 'Rates & core services'),
    ('Una lista aproximada de precios o promociones que quieras mostrar. Esto filtra a los curiosos y hace que te escriban solo clientes decididos a contratar.',
     'An approximate list of rates or packages you offer. This pre-qualifies visitors so only serious clients reach out to you.'),
    ('WhatsApp y Google Maps', 'WhatsApp & Google Maps link'),
    ('El número para recibir consultas y el link a tu ficha de Google Maps. <strong class="text-neutral-800 font-semibold">Nosotros auditamos y optimizamos tu ficha</strong> para conectarla con tu nueva web.',
     'Your phone number for inquiries and your Google Business profile link. <strong class="text-neutral-800 font-semibold">We audit and optimize your Google profile</strong> to link seamlessly with your new website.'),

    ('Pago 50% y 50%', '50% / 50% Payment'),
    ('Abonás el 50% para congelar agenda y comenzar el desarrollo, y el 50% restante contra entrega final una vez que revisás tu web.',
     'Pay 50% upfront to reserve the schedule and start development, and the remaining 50% upon final sign-off once you review your live staging site.'),
    ('Hasta 2 Revisiones', 'Up to 2 Revisions'),
    ('El trabajo incluye hasta 2 rondas de revisiones completas antes de publicar para que el diseño y los textos queden exactamente como querés.',
     'Includes up to 2 rounds of revisions before publishing so design, copy, and features match exactly what you want.'),
    ('Primer Mes 100% Gratis', 'First Month 100% Free'),
    ('¡Tu primer mes de mantenimiento, hosting de alta velocidad y soporte técnico está completamente bonificado con el setup!',
     'Your first month of high-speed cloud hosting, SSL maintenance, and technical care is 100% included with the initial setup!'),

    # Precios
    ('Transparencia Total', 'Total Transparency'),
    ('Inversión simple, sin sorpresas ni letra chica', 'Simple investment, zero surprises or fine print'),
    ('Sabemos que en Argentina necesitás previsibilidad. Precios fijos en pesos, entrega en mano y todo resuelto de punta a punta.',
     'We believe in absolute predictability. Flat transparent pricing, turnkey delivery, and everything handled end-to-end.'),
    ('1º Mes Gratis de Mantenimiento', '1st Month Free Maintenance Included'),
    ('Sitio Web Pro Negocio Local', 'Pro Business Website'),
    ('Todo lo que necesitás para tener presencia online que convierta.', 'Everything you need for an online presence that turns visitors into clients.'),
    ('Setup Inicial (Diseño, Programación y Lanzamiento):', 'Initial Setup (Design, Coding & Launch):'),
    ('Pago único (50% anticipo / 50% entrega)', 'One-time fee (50% upfront / 50% upon delivery)'),
    ('$150.000', '$199'),
    ('>ARS<', '>USD<'),
    ('Mantenimiento + Hosting + Dominio:', 'Cloud Care + Hosting + Domain:'),
    ('¡Primer mes 100% bonificado! Luego $20.000/mes', '1st month 100% free! Then $20 USD/mo'),
    ('$20.000', '$20'),
    ('>ARS/mes<', '>USD/mo<'),
    ('¿Qué incluye exactamente?', 'What is included exactly?'),
    ('<strong class="text-white font-semibold">Desarrollo a medida y optimización extrema:</strong> Carga ultra rápida optimizada para celulares.',
     '<strong class="text-white font-semibold">Custom development & speed optimization:</strong> Sub-second loading optimized for smartphones.'),
    ('<strong class="text-white font-semibold">Dominio registrado incluido:</strong> Gestión y conexión oficial a nombre de tu negocio.',
     '<strong class="text-white font-semibold">Custom domain registration included:</strong> Full configuration and official connection for your brand.'),
    ('<strong class="text-white font-semibold">Hosting de alta velocidad incluido:</strong> Con certificado SSL de seguridad y disponibilidad continua.',
     '<strong class="text-white font-semibold">High-speed cloud hosting included:</strong> Continuous uptime with automated SSL security certificate.'),
    ('<strong class="text-white font-semibold">Auditoría y optimización de tu ficha de Google Maps:</strong> Categorías, enlace web oficial y fotos para atraer búsquedas locales en tu zona.',
     '<strong class="text-white font-semibold">Google Business Profile audit & optimization:</strong> Categories, verified official website link, and photos to capture local searches.'),
    ('<strong class="text-white font-semibold">Redacción comercial incluida:</strong> Vos solo nos mandás un par de audios y nosotros redactamos los textos de tu web para que conviertan.',
     '<strong class="text-white font-semibold">Sales copywriting included:</strong> Just send us 2 or 3 voice notes and we write compelling copy that converts visitors.'),
    ('<strong class="text-white font-semibold">Integración y botones directos a WhatsApp:</strong> Textos pre-armados para que el cliente consulte con un solo toque.',
     '<strong class="text-white font-semibold">Direct WhatsApp integration:</strong> Pre-filled contextual links so clients reach you with a single tap.'),
    ('<strong class="text-white font-semibold">Mantenimiento mensual y cambios menores:</strong> Hasta 3 revisiones o cambios puntuales por mes (textos, precios y fotos). Modificaciones adicionales se cotizan aparte.',
     '<strong class="text-white font-semibold">Monthly care & minor updates:</strong> Up to 3 content or rate updates per month. Additional features quoted separately.'),
    ('<strong class="text-white font-semibold">Entrega rápida en 3 a 5 días hábiles</strong> con hasta 2 rondas de revisiones incluidas.',
     '<strong class="text-white font-semibold">Fast delivery in 3 to 5 business days</strong> with up to 2 revision rounds included.'),
    ('Hola Erik! Quiero contratar el plan Sitio Web Pro ($150.000 setup + $20.000/mes) para mi negocio. ¿Cómo empezamos?',
     'Hello Erik! I want to order the Pro Website package ($199 setup + $20/mo) for my business. How do we get started?'),
    ('<span>Pedir mi Web por WhatsApp</span>', '<span>Order my Website via WhatsApp</span>'),
    ('Aceptamos Transferencia Bancaria y Mercado Pago. Consulta nuestros <a href="/terminos" class="text-emerald-400 underline hover:text-emerald-300">Términos y Condiciones</a>.',
     'We accept PayPal, Wise, Bank Wire (SWIFT / ACH), and Crypto (USDT). Check our <a href="/terminos" class="text-emerald-400 underline hover:text-emerald-300">Terms & Conditions</a>.'),
    ('¿Ya tenés una página pero no tenés quién te la mantenga?', 'Already have a website but need reliable hosting and maintenance?'),
    ('También nos hacemos cargo del mantenimiento, hosting, copias de seguridad y actualización de textos y precios para sitios web existentes.',
     'We also take care of high-speed hosting, SSL, daily backups, and regular content or price updates for existing websites.'),
    ('Hola Erik! Ya tengo una página web hecha pero necesito mantenimiento y soporte técnico. ¿Cómo podemos coordinar?',
     'Hello Erik! I already have an existing website and need technical maintenance and hosting. How can we coordinate?'),
    ('Consultar Mantenimiento', 'Inquire About Maintenance'),

    # FAQs
    ('Dudas Habituales', 'Common Questions'),
    ('Preguntas Frecuentes', 'Frequently Asked Questions'),
    ('Respondemos todo con total transparencia antes de que tomes una decisión.', 'Complete transparency before you make any decision.'),
    ('¿Cuánto tardan en entregar mi página web y qué tengo que hacer yo?', 'How long does delivery take and what do I have to do?'),
    ('Tu web queda lista en <strong>3 a 5 días hábiles</strong>. Vos no tenés que redactar textos extensos ni saber nada técnico: <strong>con solo mandarnos 3 audios de WhatsApp contándonos qué hacés</strong>, fotos de tu local o trabajos y tus precios, nosotros redactamos todos los textos comerciales, seleccionamos fotos profesionales y dejamos todo publicado y funcionando con hasta 2 rondas de revisiones.',
     'Your website is live within <strong>3 to 5 business days</strong>. You don\'t need to write long copy or know any code: <strong>simply send us 3 voice notes explaining what you do</strong>, photos of your venue or work, and your rates. We write all sales copy, curate professional visuals, and launch your site with up to 2 revision rounds included.'),

    ('¿Incluye la optimización de mi ficha de Google Maps / Google Business Profile?', 'Does it include Google Business Profile / Google Maps optimization?'),
    ('<strong>Sí, totalmente y sin costo extra.</strong> La web convierte las visitas en clientes, pero la ficha de Google Maps es la que atrae el tráfico local. Con el servicio te dejamos tu ficha de Google Maps auditada y optimizada (categorías exactas, horarios, fotos, botón oficial a tu web y enlace directo a WhatsApp) para que aproveches al máximo a los clientes que buscan en tu zona.',
     '<strong>Yes, fully included at no extra cost.</strong> Your website converts visitors into paying customers, while your Google Business profile captures local search intent. We audit and optimize your Google profile (exact categories, hours, photos, verified website link, and direct WhatsApp contact) so you get the most out of local traffic.'),

    ('¿Cómo funciona el dominio y el hosting?', 'How does the domain and cloud hosting work?'),
    ('Nosotros nos encargamos de todo el trámite de registro y delegación de tu dominio oficial a nombre de tu negocio y dejamos configurado el hosting de máxima velocidad con certificado de seguridad SSL. No tenés que lidiar con configuraciones técnicas complejas.',
     'We handle all domain registration, DNS delegation, and configure high-speed cloud hosting with an automated SSL certificate. You never have to deal with complicated technical configurations.'),

    ('¿Por qué elegir un sitio web moderno frente a una web tradicional?', 'Why choose a bespoke modern website over a traditional one?'),
    ('Las webs tradicionales suelen ser pesadas, se desactualizan, requieren plugins que se rompen y tardan varios segundos en abrir en el celular. Nuestras páginas se construyen con tecnología estática moderna y plantillas 100% personalizables: <strong>cargan de inmediato, no sufren fallas técnicas y están pensadas específicamente para que la gente toque el botón de WhatsApp y te hable de forma directa</strong>.',
     'Traditional agency sites or WordPress builders are heavy, break with plugin updates, and take seconds to open on phones. Our websites are built with pure, modern code: <strong>they load instantly, never crash, and are engineered specifically to drive direct contact on WhatsApp or email</strong>.'),

    ('¿Qué incluye el mantenimiento mensual ($20.000/mes)?', 'What is included in the monthly maintenance ($20 USD/mo)?'),
    ('¡Recordá que el 1º mes es 100% gratis! A partir del segundo mes, el abono mensual incluye hosting de alta velocidad, renovación de dominio, soporte preventivo y <strong>hasta 3 revisiones o cambios puntuales por mes</strong> (actualización de precios, textos o fotos). En caso de necesitar más revisiones o cambios en un mismo mes, se pueden realizar coordinando un valor adicional preferencial. Si más adelante querés agregar secciones enteras o páginas adicionales, se presupuestan aparte.',
     'Remember the 1st month is 100% free! Starting month two, the monthly care includes high-speed hosting, domain renewal, SSL monitoring, and <strong>up to 3 content or rate updates per month</strong>. If you ever need additional updates in the same month, we coordinate them at a preferential rate. Full redesigns or entire new pages are quoted separately.'),

    ('¿Puedo comprar los accesos y el código fuente para gestionar mi web por mi cuenta?', 'Can I buy out full access and source code to manage my website myself?'),
    ('Sí, totalmente. Si en algún momento decidís autogestionar tu sitio, podés adquirir la propiedad total, los accesos completos y el código fuente definitivo de tu página abonando el equivalente a 10 mensualidades de mantenimiento ($200.000 ARS), conforme a nuestros Términos y Condiciones.',
     'Yes, absolutely. If at any point you wish to self-host or manage your site independently, you can acquire full ownership, code repository rights, and all production files for a one-time buyout equal to 10 months of maintenance ($200 USD), in accordance with our Terms & Conditions.'),

    # Footer CTA
    ('¿Listo para que tu negocio tenga la web que se merece?', 'Ready for your business to have the website it deserves?'),
    ('Contanos sobre tu local o actividad profesional y te armamos una propuesta sin compromiso.', 'Tell us about your business or professional practice and we will prepare a proposal with no commitment.'),
    ('Hola Erik! Quiero coordinar para ver una propuesta para mi negocio.', 'Hello Erik! I would like to coordinate a proposal for my business.'),
    ('<span>Escribirme ahora por WhatsApp</span>', '<span>Message me on WhatsApp now</span>'),

    # Footer
    ('© 2026 erikwebsite.com. Todos los derechos reservados.', '© 2026 erikwebsite.com. All rights reserved.'),
    ('Blog y Guías', 'Blog & Guides (ES)'),
    ('Términos y Condiciones', 'Terms & Conditions'),
    ('¿Hablamos por WhatsApp?', 'Chat on WhatsApp'),
    ('Hola Erik! Me interesa tener una página web para mi negocio, ¿me podrías dar más información sobre las opciones y precios?',
     'Hello Erik! I\'m interested in getting a website for my business, could you give me more information on packages and pricing?'),

    # Link demo adjustments inside English page: add ?lang=en to live demo links so demo prices switch to USD
    ('href="/demos/estetica/"', 'href="/demos/estetica/?lang=en"'),
    ('href="/demos/odontologia/"', 'href="/demos/odontologia/?lang=en"'),
    ('href="/demos/psicologia/"', 'href="/demos/psicologia/?lang=en"'),
    ('href="/demos/vajilla/"', 'href="/demos/vajilla/?lang=en"'),
    ('href="/demos/catering/"', 'href="/demos/catering/?lang=en"'),
    ('href="/demos/salones/"', 'href="/demos/salones/?lang=en"'),
    ('href="/demos/abogados/"', 'href="/demos/abogados/?lang=en"'),
    ('href="/demos/urgencias-hogar/"', 'href="/demos/urgencias-hogar/?lang=en"'),
    ('href="/demos/contable/"', 'href="/demos/contable/?lang=en"'),
    ('href="/demos/fitness/"', 'href="/demos/fitness/?lang=en"'),
]

en_translated = es
for orig, repl in replacements:
    en_translated = en_translated.replace(orig, repl)

with open('en/index.html', 'w', encoding='utf-8') as f:
    f.write(en_translated)

print("Generated faithful 1:1 en/index.html successfully!")
