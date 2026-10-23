import re
import os

def update_article_7_new():
    # Update the 7 new articles with the 4 responsive cards in HTML right after the cover banner!
    summary_cards_by_slug = {
        'paginas-web-para-psicologos-argentina': [
            {
                'num': '01',
                'badge': 'LEGALIDAD Y ÉTICA',
                'title': 'Confianza y Matrícula',
                'points': [
                    'Exhibición visible del número de matrícula provincial o nacional.',
                    'Corriente clínica clara (TCC, Psicoanálisis, Sistémica).',
                    'Aclaración de aranceles y emisión de factura para reintegro.'
                ]
            },
            {
                'num': '02',
                'badge': 'ALCANCE NACIONAL',
                'title': 'Terapia Online y Presencial',
                'points': [
                    'Atención a pacientes de todo el país y argentinos en el exterior.',
                    'Plataformas seguras y directas (Google Meet o Zoom).',
                    'Mapa y fotos del consultorio físico si atendés presencial.'
                ]
            },
            {
                'num': '03',
                'badge': 'WHATSAPP DIRECTO',
                'title': 'Turnos sin Fricción',
                'points': [
                    'El paciente no tiene que crearse usuarios ni bajar apps.',
                    'Mensaje estructurado con nombre, modalidad y horario.',
                    'Respondés a tu ritmo entre sesiones sin interrupciones.'
                ]
            },
            {
                'num': '04',
                'badge': 'INDEPENDENCIA',
                'title': '0% Comisiones a Directorios',
                'points': [
                    'Dejá de pagar mensualidades para figurar en listas colectivas.',
                    'Cobros directos a tu CBU, CVU o cuenta de Mercado Pago.',
                    'Tu propio posicionamiento en Google te pertenece 100%.'
                ]
            }
        ],
        'paginas-web-oficios-servicios-hogar': [
            {
                'num': '01',
                'badge': 'LOCAL PACK',
                'title': 'Google Maps en tu Barrio',
                'points': [
                    'Aparecé primero cuando un vecino busca "electricista urgente".',
                    'Radio de servicio personalizado según los barrios que cubrís.',
                    'Botón de llamada directa al toque sin perder tiempo.'
                ]
            },
            {
                'num': '02',
                'badge': 'SEGURIDAD',
                'title': 'Matrícula y Respaldo',
                'points': [
                    'Constancia de técnico electricista o gasista matriculado.',
                    'Fotos reales de tableros prolijos e instalaciones terminadas.',
                    'Generá la tranquilidad necesaria para entrar a un hogar.'
                ]
            },
            {
                'num': '03',
                'badge': 'COTIZACIÓN ÁGIL',
                'title': 'Presupuestos por WhatsApp',
                'points': [
                    'El cliente te envía foto o video de la falla técnica.',
                    'Filtrás curiosos desde tu taller sin viajar al vicio.',
                    'Aclarás el costo de visita técnica o diagnóstico previo.'
                ]
            },
            {
                'num': '04',
                'badge': 'ORGANIZACIÓN',
                'title': 'Formalidad Comercial',
                'points': [
                    'Factura de Monotributo y presupuesto formal en PDF.',
                    'Cobro con transferencia bancaria o tarjeta en obra.',
                    'Tu reputación con reseñas verificadas de clientes reales.'
                ]
            }
        ],
        'paginas-web-estudios-contables-argentina': [
            {
                'num': '01',
                'badge': 'SEGMENTACIÓN',
                'title': 'PyMEs y Monotributistas',
                'points': [
                    'Páginas orientadas a lo que cada cliente necesita resolver.',
                    'Altas impositivas, recategorizaciones y convenios multilaterales.',
                    'Liquidación de sueldos (F. 931), Ganancias e IVA mensual.'
                ]
            },
            {
                'num': '02',
                'badge': '100% DIGITAL',
                'title': 'Atención Online al País',
                'points': [
                    'Presentaciones digitales sin necesidad de carpetas de papel.',
                    'Asesoramiento continuo por WhatsApp y reuniones por Meet.',
                    'Captá empresas de Buenos Aires, Córdoba, Rosario o San Juan.'
                ]
            },
            {
                'num': '03',
                'badge': 'PRESTIGIO',
                'title': 'Autoridad y Matrícula CPCE',
                'points': [
                    'Respaldo institucional de contadores matriculados.',
                    'Cero jerga técnica incomprensible: comunicación directa.',
                    'Respuestas garantizadas en menos de 24 horas hábiles.'
                ]
            },
            {
                'num': '04',
                'badge': 'LEADS CALIFICADOS',
                'title': 'Abonos Mensuales Sólidos',
                'points': [
                    'Formulario breve de diagnóstico fiscal en tu web.',
                    'Presupuestos mensuales transparentes según volumen de ventas.',
                    'Dejá de depender del boca a boca para sumar nuevas empresas.'
                ]
            }
        ],
        'paginas-web-salones-belleza-estetica': [
            {
                'num': '01',
                'badge': 'IMPACTO VISUAL',
                'title': 'Antes y Después Real',
                'points': [
                    'Galería con resultados reales de tratamientos en alta definición.',
                    'Lifting de pestañas, depilación láser, masajes y estética facial.',
                    'Marcas de productos dermatológicos y aparatología aprobada.'
                ]
            },
            {
                'num': '02',
                'badge': 'TRANSPARENCIA',
                'title': 'Precios Claros Visibles',
                'points': [
                    'Basta de perder horas respondiendo "precio por privado".',
                    'Precios por sesión y paquetes promocionales destacados.',
                    'Medios de pago disponibles: transferencias y cuotas.'
                ]
            },
            {
                'num': '03',
                'badge': 'AGENDA LLENA',
                'title': 'Turnos con Seña Previa',
                'points': [
                    'Botón a WhatsApp preconfigurado con el servicio elegido.',
                    'Cobro de seña previa del 30% o 50% por Mercado Pago.',
                    'Reducción drástica del ausentismo y cancelaciones sobre la hora.'
                ]
            },
            {
                'num': '04',
                'badge': 'MAPS LOCAL',
                'title': 'Clientas de tu Zona',
                'points': [
                    'Posicionamiento en Google Maps para "estética cerca de mí".',
                    'Fotos luminosas del salón y botón directo de cómo llegar.',
                    'Reseñas de 5 estrellas de clientas habituales de tu barrio.'
                ]
            }
        ],
        'paginas-web-salones-eventos-catering': [
            {
                'num': '01',
                'badge': 'GALERÍA INMERSIVA',
                'title': 'Parque de Día y Noche',
                'points': [
                    'Fotos de bodas y 15s con ambientación luminosa real.',
                    'Piscina con livings lounge, pista de baile climatizada y suite vip.',
                    'Demostración de capacidad en mesas formales o formato cóctel.'
                ]
            },
            {
                'num': '02',
                'badge': 'COTIZADOR INTELIGENTE',
                'title': 'Presupuestos por Invitados',
                'points': [
                    'El cliente selecciona tipo de fiesta y cantidad de personas.',
                    'Opciones de catering (finger food, asado criollo o menú formal).',
                    'Recibís el pedido completo en tu WhatsApp ya prefiltrado.'
                ]
            },
            {
                'num': '03',
                'badge': 'SEGURIDAD TOTAL',
                'title': 'Tranquilidad para la Familia',
                'points': [
                    'Grupo electrógeno propio de alta potencia garantizado.',
                    'Seguro de responsabilidad civil y emergencias médicas.',
                    'Estacionamiento privado interno vigilado durante el evento.'
                ]
            },
            {
                'num': '04',
                'badge': 'VENTAS ANTICIPADAS',
                'title': 'Cierre de Fechas con Seña',
                'points': [
                    'Condiciones claras de congelamiento de tarifa.',
                    'Cierre de contratos con 6 a 14 meses de anticipación.',
                    'Evitá visitas de curiosos que no tienen definida la fecha.'
                ]
            }
        ],
        'paginas-web-personal-trainers-gimnasios': [
            {
                'num': '01',
                'badge': 'MODELOS ESCALABLES',
                'title': 'Presencial vs Online',
                'points': [
                    'Cupos limitados para clases presenciales personalizadas.',
                    'Asesorías remotas a alumnos de todo el país y el exterior.',
                    'Planes adaptados al equipamiento del gimnasio o casa del alumno.'
                ]
            },
            {
                'num': '02',
                'badge': 'PRUEBA SOCIAL',
                'title': 'Transformaciones Reales',
                'points': [
                    'Fotos de cambios físicos reales y testimonios verificados.',
                    'Especialidades: fuerza, descenso de grasa, salud postural.',
                    'Matrícula o certificación de profesor de educación física.'
                ]
            },
            {
                'num': '03',
                'badge': 'INGRESOS RECURRENTES',
                'title': 'Suscripciones Automáticas',
                'points': [
                    'Cobros mensuales con débito automático por Mercado Pago.',
                    'Paquetes trimestrales o semestrales con beneficios.',
                    'Menos tiempo persiguiendo pagos a fin de mes.'
                ]
            },
            {
                'num': '04',
                'badge': 'FILTRO PREVIO',
                'title': 'Cuestionario de Salud Inicial',
                'points': [
                    'El alumno completa sus objetivos y lesiones previas en la web.',
                    'Demuestra seriedad profesional y justifica tus tarifas altas.',
                    'Llega a tu WhatsApp listo para arrancar el primer día.'
                ]
            }
        ],
        'por-que-tener-una-pagina-web': [
            {
                'num': '01',
                'badge': 'PRESUPUESTO',
                'title': 'Mito: "Es muy caro"',
                'points': [
                    'La web cuesta $150.000 ARS en un pago único transparente.',
                    'Se amortiza con solo 1 o 2 ventas nuevas en el primer mes.',
                    'Sin suscripciones obligatorias en dólares ni comisiones.'
                ]
            },
            {
                'num': '02',
                'badge': 'TIEMPO RÉCORD',
                'title': 'Mito: "Lleva mucho tiempo"',
                'points': [
                    'Tu sitio web listo en 3 a 5 días hábiles funcionando.',
                    'Nos mandás audios por WhatsApp y nosotros armamos todo.',
                    'Cero complicaciones técnicas ni peleas con constructores.'
                ]
            },
            {
                'num': '03',
                'badge': 'ACTIVO PROPIO',
                'title': 'Mito: "Con Instagram alcanza"',
                'points': [
                    'El algoritmo de Instagram solo le muestra tus posts al 5%.',
                    'En Google la gente busca con dinero en mano para comprar ya.',
                    'En Instagram sos inquilino; tu web con dominio propio es tuya.'
                ]
            },
            {
                'num': '04',
                'badge': 'VISIBILIDAD 24/7',
                'title': 'Mito: "Nadie mira páginas web"',
                'points': [
                    'Enlazar una web propia a Google Maps duplica tus llamados.',
                    'Los buscadores con IA (ChatGPT, Gemini) citan páginas oficiales.',
                    'Funciona como tu mejor vendedor respondiendo dudas las 24 horas.'
                ]
            }
        ]
    }

    # Format the cards into HTML
    for slug, cards in summary_cards_by_slug.items():
        file_path = f'blog/{slug}/index.html'
        if not os.path.exists(file_path):
            continue

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        cards_html = ''
        for c in cards:
            points_li = ''.join([f'<li class="flex items-start gap-2"><span class="text-emerald-500 font-bold mt-0.5">•</span><span>{p}</span></li>' for p in c['points']])
            cards_html += f'''
            <div class="p-5 sm:p-6 rounded-2xl bg-white border border-black/[0.08] shadow-2xs hover:shadow-md hover:border-emerald-500/30 transition-all flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between mb-3">
                  <span class="text-xs font-bold text-neutral-400">{c['num']}</span>
                  <span class="text-[10px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-100">
                    {c['badge']}
                  </span>
                </div>
                <h4 class="font-display font-bold text-neutral-900 text-base sm:text-lg mb-3">
                  {c['title']}
                </h4>
                <ul class="text-xs sm:text-sm text-neutral-600 space-y-2 font-light">
                  {points_li}
                </ul>
              </div>
            </div>'''

        section_html = f'''
        <!-- RESUMEN EN TARJETAS RESPONSIVAS (100% LEGIBLE EN CELULARES) -->
        <section class="my-8 p-5 sm:p-7 rounded-3xl bg-neutral-900 text-white border border-white/[0.08] shadow-sm">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-6 pb-4 border-b border-white/[0.08]">
            <div>
              <span class="inline-block text-[11px] font-bold uppercase tracking-wider text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-2.5 py-0.5 rounded-full mb-1">
                Resumen Ejecutivo
              </span>
              <h3 class="font-display font-bold text-xl sm:text-2xl text-white">
                Los 4 Pilares Clave de esta Guía
              </h3>
            </div>
            <span class="text-xs text-neutral-400 font-light">
              Deslizá o leé en 2 minutos
            </span>
          </div>
          <div class="grid sm:grid-cols-2 gap-4 text-neutral-900">
            {cards_html}
          </div>
        </section>
        '''

        # Insert right after the featured image wrapper
        pattern = re.compile(r'(<div class="mb-10">.*?<\/div>\s*<\/div>)', re.DOTALL)
        if pattern.search(content):
            if 'Resumen Ejecutivo' not in content:
                content = pattern.sub(f'\\1\n\n{section_html}', content)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Injected responsive cards in: {file_path}")
            else:
                print(f"Already has cards: {file_path}")
        else:
            print(f"Pattern not found in: {file_path}")

def update_article_older():
    # 1. CUANTO CUESTA UNA WEB: Add interactive breakdown
    path1 = 'blog/cuanto-cuesta-una-pagina-web-argentina/index.html'
    if os.path.exists(path1):
        with open(path1, 'r', encoding='utf-8') as f:
            c1 = f.read()
        
        interactive_calc = '''
        <!-- DESGLOSE INTERACTIVO DE COSTOS EN TIEMPO REAL (100% RESPONSIVO) -->
        <div class="my-10 p-5 sm:p-8 rounded-3xl bg-neutral-900 text-white border border-white/[0.08] shadow-sm">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-4 pb-4 border-b border-white/[0.08]">
            <div>
              <span class="text-[11px] font-bold uppercase tracking-wider text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-2.5 py-0.5 rounded-full">
                Estructura Transparente 2026
              </span>
              <h3 class="font-display font-bold text-xl sm:text-2xl text-white mt-1">
                Desglose Real: ¿Cuánto vas a pagar?
              </h3>
            </div>
            <span class="text-xs text-neutral-400">Sin costos ocultos</span>
          </div>

          <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4 text-neutral-900">
            <!-- Item 1 -->
            <div class="p-5 rounded-2xl bg-white border border-black/[0.08] shadow-2xs flex flex-col justify-between">
              <div>
                <span class="text-xs font-bold text-neutral-400">01 • ANUAL</span>
                <h4 class="font-bold text-base text-neutral-900 mt-1 mb-2">Dominio Oficial</h4>
                <div class="text-xl font-extrabold text-emerald-600 mb-2">$8.500 - $25.000</div>
                <p class="text-xs text-neutral-600 font-light leading-relaxed">
                  Arancel anual oficial en nic.ar (.com.ar o .ar). La titularidad legal del nombre queda 100% a nombre tuyo o de tu empresa.
                </p>
              </div>
            </div>

            <!-- Item 2 -->
            <div class="p-5 rounded-2xl bg-white border border-black/[0.08] shadow-2xs flex flex-col justify-between">
              <div>
                <span class="text-xs font-bold text-neutral-400">02 • MENSUAL</span>
                <h4 class="font-bold text-base text-neutral-900 mt-1 mb-2">Hosting y SSL</h4>
                <div class="text-xl font-extrabold text-neutral-900 mb-2">$15.000 - $30.000</div>
                <p class="text-xs text-neutral-600 font-light leading-relaxed">
                  Servidor seguro de alta velocidad con candado verde HTTPS obligatorio. Carga tu web en celulares en menos de 1 segundo.
                </p>
              </div>
            </div>

            <!-- Item 3 -->
            <div class="p-5 rounded-2xl bg-white border-2 border-emerald-500 shadow-md flex flex-col justify-between relative overflow-hidden">
              <span class="absolute top-2 right-2 text-[9px] font-bold uppercase bg-emerald-500 text-slate-950 px-2 py-0.5 rounded-full">PLAN ERIK</span>
              <div>
                <span class="text-xs font-bold text-emerald-600">03 • PAGO ÚNICO</span>
                <h4 class="font-bold text-base text-neutral-900 mt-1 mb-2">Desarrollo Web</h4>
                <div class="text-xl font-extrabold text-emerald-600 mb-2">$150.000 ARS</div>
                <p class="text-xs text-neutral-600 font-light leading-relaxed">
                  En 2 cuotas (50% anticipo y 50% al entregar). Incluye diseño adaptado, textos comerciales por audios y optimización Maps.
                </p>
              </div>
            </div>

            <!-- Item 4 -->
            <div class="p-5 rounded-2xl bg-white border border-black/[0.08] shadow-2xs flex flex-col justify-between">
              <div>
                <span class="text-xs font-bold text-neutral-400">04 • OPTATIVO</span>
                <h4 class="font-bold text-base text-neutral-900 mt-1 mb-2">Mantenimiento</h4>
                <div class="text-xl font-extrabold text-neutral-900 mb-2">$20.000 / mes</div>
                <p class="text-xs text-neutral-600 font-light leading-relaxed">
                  1º mes 100% bonificado. Hasta 3 cambios de fotos, textos o precios por mes, copias de seguridad continuas y soporte directo.
                </p>
              </div>
            </div>
          </div>
        </div>
        '''
        if 'Estructura Transparente 2026' not in c1:
            c1 = c1.replace('<!-- INFOGRAFÍA DESGLOSE COSTOS -->', interactive_calc + '\n        <!-- INFOGRAFÍA DESGLOSE COSTOS -->')
            with open(path1, 'w', encoding='utf-8') as f:
                f.write(c1)
            print("Injected interactive breakdown in cuanto-cuesta")

    # 2. GOOGLE MAPS: Add 4-pillar checklist
    path2 = 'blog/como-conseguir-clientes-google-maps/index.html'
    if os.path.exists(path2):
        with open(path2, 'r', encoding='utf-8') as f:
            c2 = f.read()
        
        maps_checklist = '''
        <!-- RESUMEN INTERACTIVO DE LOS 4 PILARES LOCAL PACK -->
        <div class="my-10 p-5 sm:p-8 rounded-3xl bg-neutral-900 text-white border border-white/[0.08] shadow-sm">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-4 pb-4 border-b border-white/[0.08]">
            <div>
              <span class="text-[11px] font-bold uppercase tracking-wider text-sky-400 bg-sky-500/10 border border-sky-500/20 px-2.5 py-0.5 rounded-full">
                Checklist Local SEO 2026
              </span>
              <h3 class="font-display font-bold text-xl sm:text-2xl text-white mt-1">
                Los 4 Factores que te ponen #1 en Google Maps
              </h3>
            </div>
            <span class="text-xs text-neutral-400 font-light">Sin pagar publicidad</span>
          </div>

          <div class="grid sm:grid-cols-2 gap-4 text-neutral-900">
            <div class="p-5 rounded-2xl bg-white border border-black/[0.08] shadow-2xs">
              <span class="text-xs font-bold text-sky-700 bg-sky-50 px-2 py-0.5 rounded-full">01 • RELEVANCIA</span>
              <h4 class="font-bold text-base text-neutral-900 mt-2 mb-1">Categoría Primaria Exacta</h4>
              <p class="text-xs text-neutral-600 font-light leading-relaxed">
                Elegí la actividad principal sin relleno artificial. Un electricista debe poner "Electricista" y no "Electricista urgente barato San Juan 24hs".
              </p>
            </div>

            <div class="p-5 rounded-2xl bg-white border border-black/[0.08] shadow-2xs">
              <span class="text-xs font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded-full">02 • CONVERSIÓN</span>
              <h4 class="font-bold text-base text-neutral-900 mt-2 mb-1">Enlazar una Página Web</h4>
              <p class="text-xs text-neutral-600 font-light leading-relaxed">
                Google premia fichas con sitio web porque demuestran mayor entidad de negocio. Multiplica por 2 las llamadas frente a fichas con links a redes.
              </p>
            </div>

            <div class="p-5 rounded-2xl bg-white border border-black/[0.08] shadow-2xs">
              <span class="text-xs font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full">03 • COBERTURA</span>
              <h4 class="font-bold text-base text-neutral-900 mt-2 mb-1">Área de Servicio Clara</h4>
              <p class="text-xs text-neutral-600 font-light leading-relaxed">
                Si no tenés local a la calle, configurá el radio de atención en tu municipio o departamento para no perder clientes que buscan en tu zona.
              </p>
            </div>

            <div class="p-5 rounded-2xl bg-white border border-black/[0.08] shadow-2xs">
              <span class="text-xs font-bold text-purple-700 bg-purple-50 px-2 py-0.5 rounded-full">04 • REPUTACIÓN</span>
              <h4 class="font-bold text-base text-neutral-900 mt-2 mb-1">Reseñas con Respuesta</h4>
              <p class="text-xs text-neutral-600 font-light leading-relaxed">
                Conseguir 15 a 20 opiniones de clientes reales y responderlas mencionando tu servicio te posiciona por encima de negocios antiguos abandonados.
              </p>
            </div>
          </div>
        </div>
        '''
        if 'Checklist Local SEO 2026' not in c2:
            c2 = c2.replace('<!-- INFOGRAFÍA LOCAL SEO -->', maps_checklist + '\n        <!-- INFOGRAFÍA LOCAL SEO -->')
            with open(path2, 'w', encoding='utf-8') as f:
                f.write(c2)
            print("Injected maps checklist in google-maps")

    # 3. WEB VS INSTAGRAM: Add responsive comparison table
    path3 = 'blog/pagina-web-vs-instagram/index.html'
    if os.path.exists(path3):
        with open(path3, 'r', encoding='utf-8') as f:
            c3 = f.read()

        comparison_table = '''
        <!-- TABLA COMPARATIVA RESPONSIVA (WEB VS INSTAGRAM) -->
        <div class="my-10 p-5 sm:p-8 rounded-3xl bg-neutral-900 text-white border border-white/[0.08] shadow-sm overflow-hidden">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-6 pb-4 border-b border-white/[0.08]">
            <div>
              <span class="text-[11px] font-bold uppercase tracking-wider text-rose-400 bg-rose-500/10 border border-rose-500/20 px-2.5 py-0.5 rounded-full">
                Comparativa Estratégica
              </span>
              <h3 class="font-display font-bold text-xl sm:text-2xl text-white mt-1">
                Página Web vs. Instagram: ¿Dónde poner tu esfuerzo?
              </h3>
            </div>
            <span class="text-xs text-neutral-400 font-light">Efectividad para vender</span>
          </div>

          <div class="grid sm:grid-cols-2 gap-4 text-neutral-900">
            <!-- Columna Instagram -->
            <div class="p-5 rounded-2xl bg-neutral-800/80 border border-neutral-700 text-neutral-300">
              <div class="flex items-center justify-between mb-3">
                <h4 class="font-bold text-lg text-white">Instagram</h4>
                <span class="text-xs text-rose-400 font-bold bg-rose-950/60 px-2.5 py-0.5 rounded-full border border-rose-900/50">Canal de Ocio</span>
              </div>
              <ul class="text-xs space-y-2.5 font-light">
                <li class="flex items-start gap-2"><span class="text-rose-400 font-bold">✕</span><span><strong>Alcance en caída:</strong> Tus posts solo llegan al 5-10% de tus propios seguidores si no pagás anuncios.</span></li>
                <li class="flex items-start gap-2"><span class="text-rose-400 font-bold">✕</span><span><strong>Pérdida de tiempo:</strong> Responder 30 mensajes de "¿precio por privado?" para cerrar 1 sola venta.</span></li>
                <li class="flex items-start gap-2"><span class="text-rose-400 font-bold">✕</span><span><strong>Sos un inquilino:</strong> La cuenta no es tuya; si Meta la inhabilita, perdés todo tu historial.</span></li>
              </ul>
            </div>

            <!-- Columna Web -->
            <div class="p-5 rounded-2xl bg-white border-2 border-emerald-500 text-neutral-800 shadow-md">
              <div class="flex items-center justify-between mb-3">
                <h4 class="font-bold text-lg text-neutral-900">Página Web Propia</h4>
                <span class="text-xs text-emerald-800 font-bold bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-200">Canal de Compra</span>
              </div>
              <ul class="text-xs space-y-2.5 font-light text-neutral-600">
                <li class="flex items-start gap-2"><span class="text-emerald-600 font-bold">✓</span><span><strong>Intención comercial pura:</strong> Quien te busca en Google está listo para contratar o comprar ya.</span></li>
                <li class="flex items-start gap-2"><span class="text-emerald-600 font-bold">✓</span><span><strong>Filtro 24 horas:</strong> Precios claros, fotos y respuestas frecuentes antes de que te escriban.</span></li>
                <li class="flex items-start gap-2"><span class="text-emerald-600 font-bold">✓</span><span><strong>Tu activo legal:</strong> Dominio oficial en NIC Argentina que nadie puede suspenderte ni quitarte.</span></li>
              </ul>
            </div>
          </div>
        </div>
        '''
        if 'Tabla Comparativa Estratégica' not in c3:
            c3 = c3.replace('<!-- INFOGRAFÍA COMPARATIVA -->', comparison_table + '\n        <!-- INFOGRAFÍA COMPARATIVA -->')
            with open(path3, 'w', encoding='utf-8') as f:
                f.write(c3)
            print("Injected comparison table in web-vs-ig")

def main():
    update_article_7_new()
    update_article_older()

if __name__ == '__main__':
    main()
