import os
from PIL import Image, ImageDraw, ImageFont

def get_fonts():
    try:
        return {
            'badge': ImageFont.truetype('arialbd.ttf', 14),
            'title': ImageFont.truetype('arialbd.ttf', 44),
            'title_sub': ImageFont.truetype('arial.ttf', 20),
            'pill_title': ImageFont.truetype('arialbd.ttf', 18),
            'pill_sub': ImageFont.truetype('arial.ttf', 14),
            'stat_num': ImageFont.truetype('arialbd.ttf', 32),
            'stat_label': ImageFont.truetype('arialbd.ttf', 13),
            'wm': ImageFont.truetype('arialbd.ttf', 15),
            'small': ImageFont.truetype('arial.ttf', 12)
        }
    except Exception:
        d = ImageFont.load_default()
        return {k: d for k in ['badge', 'title', 'title_sub', 'pill_title', 'pill_sub', 'stat_num', 'stat_label', 'wm', 'small']}

def draw_watermark(draw, width, height, fonts, subtitle='erikwebsite.com — Diseño Web Profesional y Posicionamiento Local en Argentina'):
    y_line = height - 52
    draw.line([60, y_line, width - 60, y_line], fill='#334155', width=1)
    draw.text((60, y_line + 14), subtitle, fill='#64748b', font=fonts['small'])
    
    pill_text = 'erikwebsite.com'
    bbox = draw.textbbox((0, 0), pill_text, font=fonts['wm'])
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    
    pill_w = tw + 22
    pill_h = th + 10
    px = width - 60 - pill_w
    py = y_line + 8
    
    draw.rounded_rectangle([px, py, px + pill_w, py + pill_h], radius=6, fill='#022c22', outline='#10b981', width=1)
    draw.text((px + 11, py + 4), pill_text, fill='#34d399', font=fonts['wm'])

def wrap_text(draw, text, font, max_width):
    words = text.split(' ')
    lines = []
    curr = ''
    for w in words:
        test = (curr + ' ' + w).strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if (bbox[2] - bbox[0]) <= max_width:
            curr = test
        else:
            if curr:
                lines.append(curr)
            curr = w
    if curr:
        lines.append(curr)
    return lines

def render_keynote_cover(filename, badge_text, title_text, subtitle_text, highlights, theme_color='#10b981', badge_bg='#064e3b', badge_col='#34d399'):
    w, h = 1200, 630
    img = Image.new('RGB', (w, h), color='#090d16')
    draw = ImageDraw.Draw(img)
    f = get_fonts()

    # Subtle ambient gradient glow in top corner
    for r in range(300, 0, -20):
        alpha_col = '#0f2922' if theme_color == '#10b981' else '#132338'
        # Draw background accents
        draw.ellipse([w - 400 + (300-r), -100 + (300-r), w + 200 - (300-r), 500 - (300-r)], fill=alpha_col)

    # Clean Dark Content Area
    # 1. Badge Pill
    bbox_b = draw.textbbox((0, 0), badge_text, font=f['badge'])
    bw = (bbox_b[2] - bbox_b[0]) + 28
    draw.rounded_rectangle([60, 50, 60 + bw, 86], radius=18, fill=badge_bg, outline=badge_col, width=1)
    draw.text((74, 58), badge_text, fill=badge_col, font=f['badge'])

    # 2. Big Title (Wrapped with big font 44pt)
    title_lines = wrap_text(draw, title_text, f['title'], 1080)
    y_title = 110
    for line in title_lines:
        draw.text((60, y_title), line, fill='#ffffff', font=f['title'])
        y_title += 56

    # 3. Subtitle (20pt font)
    sub_lines = wrap_text(draw, subtitle_text, f['title_sub'], 1080)
    y_sub = y_title + 8
    for line in sub_lines:
        draw.text((60, y_sub), line, fill='#94a3b8', font=f['title_sub'])
        y_sub += 28

    # 4. Highlight Feature Pills (3 or 4 big, clean blocks with huge contrast)
    num_pills = len(highlights)
    gap = 20
    total_w = 1080
    pill_w = (total_w - (num_pills - 1) * gap) // num_pills
    y_pills = 390
    h_pill = 135

    for i, h_item in enumerate(highlights):
        px = 60 + i * (pill_w + gap)
        is_highlight = h_item.get('active', False)
        bg_col = '#131e32' if not is_highlight else '#0d281e'
        border_col = '#38bdf8' if not is_highlight else '#10b981'
        
        draw.rounded_rectangle([px, y_pills, px + pill_w, y_pills + h_pill], radius=16, fill=bg_col, outline=border_col, width=2 if is_highlight else 1)
        
        # Pill top tag / icon label
        draw.text((px + 20, y_pills + 18), h_item['tag'].upper(), fill=border_col, font=f['stat_label'])
        
        # Pill main stat or main bold title (32pt / 22pt)
        draw.text((px + 20, y_pills + 42), h_item['main'], fill='#ffffff', font=f['pill_title'] if len(h_item['main']) > 12 else f['stat_num'])
        
        # Pill descriptive short text
        draw.text((px + 20, y_pills + 88), h_item['desc'], fill='#cbd5e1', font=f['pill_sub'])

    # 5. Watermark
    draw_watermark(draw, w, h, f)

    os.makedirs('images', exist_ok=True)
    os.makedirs('public/images', exist_ok=True)
    img.save(f'images/{filename}')
    img.save(f'public/images/{filename}')
    print(f'OK: {filename}')

def main():
    # 1. PSICÓLOGOS
    render_keynote_cover(
        'guia_web_psicologos_argentina.png',
        'SALUD MENTAL Y TERAPIA 2026',
        'Páginas Web para Psicólogos en Argentina',
        'Turnos online por WhatsApp, matrícula profesional visible y cobro sin comisiones de directorios.',
        [
            {'tag': 'Privacidad', 'main': 'WhatsApp Directo', 'desc': 'Sin apps que el paciente olvida.'},
            {'tag': 'Alcance', 'main': 'Terapia Online', 'desc': 'Pacientes de todo el país y exterior.', 'active': True},
            {'tag': 'Honorarios', 'main': '100% Para Vos', 'desc': 'Cobro por CBU, CVU o Mercado Pago.'}
        ]
    )

    # 2. OFICIOS
    render_keynote_cover(
        'guia_web_oficios_hogar_argentina.png',
        'OFICIOS Y URGENCIAS EN ARGENTINA',
        'Páginas Web para Electricistas, Plomeros y Gasistas',
        'Cómo posicionar en Google Maps, generar confianza barrial y filtrar presupuestos por WhatsApp.',
        [
            {'tag': 'Google Maps', 'main': 'Local Pack #1', 'desc': 'Aparecé cuando buscan una urgencia.', 'active': True},
            {'tag': 'Confianza', 'main': 'Matrícula Oficial', 'desc': 'Fotos reales de trabajos finalizados.'},
            {'tag': 'Presupuesto', 'main': 'Cotizá por Audio', 'desc': 'El cliente te manda foto del problema.'}
        ]
    )

    # 3. CONTABLES
    render_keynote_cover(
        'guia_web_estudios_contables_argentina.png',
        'CIENCIAS ECONÓMICAS Y NEGOCIOS',
        'Páginas Web para Estudios Contables en Argentina',
        'Estrategia digital para captar PyMEs, asesorar monotributistas y brindar atención 100% online.',
        [
            {'tag': 'Segmentación', 'main': 'PyMEs y Monotributo', 'desc': 'Servicios adaptados a cada cliente.'},
            {'tag': 'Atención', 'main': '100% Digital', 'desc': 'Clientes de todo el país por Meet.', 'active': True},
            {'tag': 'Autoridad', 'main': 'Matrícula CPCE', 'desc': 'Solvencia legal ante ARCA y AFIP.'}
        ]
    )

    # 4. ESTÉTICA
    render_keynote_cover(
        'guia_web_estetica_salones_argentina.png',
        'BELLEZA Y CENTROS DE ESTÉTICA',
        'Páginas Web para Salones de Belleza y Estética',
        'Catálogo de tratamientos con fotos reales, precios transparentes y reservas con seña previa.',
        [
            {'tag': 'Resultados', 'main': 'Antes y Después', 'desc': 'Galería de fotos sin filtros falsos.'},
            {'tag': 'Claridad', 'main': 'Precios Visibles', 'desc': 'Basta de responder "por privado".', 'active': True},
            {'tag': 'Agenda', 'main': 'Seña por WhatsApp', 'desc': 'Reducí el ausentismo a casi cero.'}
        ]
    )

    # 5. EVENTOS
    render_keynote_cover(
        'guia_web_salones_eventos_argentina.png',
        'SALONES DE FIESTAS Y CATERING',
        'Páginas Web para Salones de Eventos y Catering',
        'Cómo exhibir el parque y salón, cotizar según cantidad de invitados y cerrar reservas anticipadas.',
        [
            {'tag': 'Visual', 'main': 'Galería Día / Noche', 'desc': 'El parque iluminado y la pista vip.'},
            {'tag': 'Cotizador', 'main': 'Por Invitados', 'desc': 'Presupuestos automáticos al chat.', 'active': True},
            {'tag': 'Anticipación', 'main': 'Fechas con Seña', 'desc': 'Reservas cerradas con meses antes.'}
        ]
    )

    # 6. FITNESS
    render_keynote_cover(
        'guia_web_personal_trainers_argentina.png',
        'FITNESS Y ENTRENAMIENTO 2026',
        'Páginas Web para Personal Trainers y Gimnasios',
        'Cómo vender asesorías online a todo el país y cupos presenciales con suscripciones automáticas.',
        [
            {'tag': 'Modelos', 'main': 'Online y Presencial', 'desc': 'Asesorías remotas o cupos en gym.'},
            {'tag': 'Cobros', 'main': 'Abono Recurrente', 'desc': 'Suscripciones por Mercado Pago.', 'active': True},
            {'tag': 'Prueba Social', 'main': 'Casos de Éxito', 'desc': 'Testimonios reales de tus alumnos.'}
        ]
    )

    # 7. POR QUÉ TENER UNA WEB (MITOS)
    render_keynote_cover(
        'guia_por_que_tener_pagina_web_argentina.png',
        'DECISIÓN DIGITAL ESTRATÉGICA',
        '¿Por qué Debería Tener una Página Web en Argentina?',
        'Derribando los 4 mitos más comunes: "es muy caro", "lleva mucho tiempo" y "con Instagram alcanza".',
        [
            {'tag': 'Mito 1', 'main': '$150.000 ARS', 'desc': 'Pago único. Se amortiza con 1 o 2 ventas.', 'active': True},
            {'tag': 'Mito 2', 'main': '3 a 5 Días', 'desc': 'Nos mandás audios, nosotros hacemos todo.'},
            {'tag': 'Mito 3', 'main': 'Dueño de tu Activo', 'desc': 'En IG sos inquilino, la web te pertenece.'}
        ]
    )

    # 8. CUÁNTO CUESTA UNA WEB
    render_keynote_cover(
        'desglose_costos_web_argentina.png',
        'TRANSPARENCIA DE PRECIOS 2026',
        '¿Cuánto Cuesta una Página Web en Argentina?',
        'Desglose real de costos: desarrollo inicial, dominio en NIC Argentina, hosting y mantenimiento.',
        [
            {'tag': 'Desarrollo', 'main': '$150.000 ARS', 'desc': 'Pago único en 2 cuotas (50% y 50%).', 'active': True},
            {'tag': 'Dominio Oficial', 'main': '$8.500 ARS / año', 'desc': 'Arancel oficial en nic.ar a tu nombre.'},
            {'tag': 'Hosting y SSL', 'main': '$15.000 ARS / mes', 'desc': 'Servidor ultrarrápido y seguro.'}
        ]
    )

    # 9. COMPARATIVA PRECIOS
    render_keynote_cover(
        'comparativa_precios_web_argentina.png',
        'GUÍA DE MERCADO ARGENTINO',
        'Comparativa de Precios de Páginas Web 2026',
        'Landing page comercial vs. sitio institucional pyme vs. tienda online: qué conviene para tu rubro.',
        [
            {'tag': 'Landing Comercial', 'main': '$150.000 ARS', 'desc': 'Directo a WhatsApp. Alta conversión.', 'active': True},
            {'tag': 'Institucional PyME', 'main': '$400.000+ ARS', 'desc': 'Varias páginas y servicios corporativos.'},
            {'tag': 'Tienda Online', 'main': '$500.000+ ARS', 'desc': 'Catálogo con carrito y pasarela de pago.'}
        ]
    )

    # 10. GOOGLE MAPS
    render_keynote_cover(
        'guia_posicionar_google_maps_argentina.png',
        'POSICIONAMIENTO LOCAL ORGÁNICO',
        'Cómo Conseguir Clientes en Google Maps sin Pagar',
        'Los 3 factores clave para aparecer en los primeros puestos del Local Pack en tu ciudad.',
        [
            {'tag': 'Relevancia', 'main': 'Categoría Exacta', 'desc': 'Nombre real sin palabras clave spam.'},
            {'tag': 'Conversión', 'main': 'Enlazar Web Propia', 'desc': 'Duplica llamadas frente a fichas solas.', 'active': True},
            {'tag': 'Reputación', 'main': 'Reseñas Locales', 'desc': 'Opiniones verificadas de clientes.'}
        ]
    )

    # 11. WEB VS INSTAGRAM
    render_keynote_cover(
        'comparativa_web_vs_instagram.png',
        'ESTRATEGIA DE VENTAS EN ARGENTINA',
        'Página Web vs. Instagram: ¿Cuál te Hace Vender Más?',
        'Por qué depender solo de redes sociales te hace perder ventas de clientes listos para comprar.',
        [
            {'tag': 'Intención', 'main': 'Google: Compra Ya', 'desc': 'Quien busca en Google necesita el servicio.', 'active': True},
            {'tag': 'Alcance', 'main': 'Sin Algoritmo', 'desc': 'Tu web no depende del 5% de alcance de IG.'},
            {'tag': 'Propiedad', 'main': 'Tu Activo Propio', 'desc': 'Nadie te puede cerrar o suspender tu web.'}
        ]
    )

    # 12. ABOGADOS
    render_keynote_cover(
        'guia_web_abogados_argentina.png',
        'SECTOR JURÍDICO EN ARGENTINA',
        'Páginas Web para Abogados y Estudios Jurídicos',
        'Generar confianza institucional, validar matrículas y captar consultas laborales y de familia.',
        [
            {'tag': 'Matrícula', 'main': 'CPACF / Colegios', 'desc': 'Exhibición clara del fuero y jurisdicción.'},
            {'tag': 'Especialidad', 'main': 'Páginas por Fuero', 'desc': 'Laboral, despidos, familia o accidentes.', 'active': True},
            {'tag': 'Contacto', 'main': 'WhatsApp Jurídico', 'desc': 'Consultas prefiltradas con confidencialidad.'}
        ]
    )

    # 13. CONSULTORIOS Y TURNOS
    render_keynote_cover(
        'automatizar_turnos_consultorio_argentina.png',
        'SALUD Y CLÍNICAS PRIVADAS',
        'Cómo Organizar Turnos en tu Consultorio de Salud',
        'Flujo ágil con WhatsApp para consultorios médicos y odontológicos sin abonos en dólares.',
        [
            {'tag': 'Simplicidad', 'main': 'Sin Apps Pesadas', 'desc': 'El paciente no tiene que crear cuentas.'},
            {'tag': 'Filtro', 'main': 'Particular / Prepaga', 'desc': 'Aclaración de aranceles antes de agendar.', 'active': True},
            {'tag': 'Confirmación', 'main': 'Recordatorio 24hs', 'desc': 'Reduce ausencias de pacientes sin aviso.'}
        ]
    )

    # 14. QUÉ NEGOCIOS NECESITAN WEB
    render_keynote_cover(
        'que_negocios_necesitan_pagina_web.png',
        'DECISIÓN DE NEGOCIO REALISTA',
        '¿Qué Negocios Necesitan Realmente una Página Web?',
        'Análisis sincero: quién puede vivir sin página web y quién pierde miles de pesos todos los meses.',
        [
            {'tag': 'Obligatorio', 'main': 'Servicios y Salud', 'desc': 'Abogados, médicos, oficios, eventos.', 'active': True},
            {'tag': 'Opcional', 'main': 'Negocios de Paso', 'desc': 'Kioscos de barrio y verdulerías.'},
            {'tag': 'Diferencia', 'main': 'Ticket Promedio', 'desc': 'A mayor valor, más se investiga en Google.'}
        ]
    )

    print('TODAS LAS 14 PORTADAS GENERADAS CON TIPOGRAFÍA GIGANTE Y FORMATO KEYNOTE!')

if __name__ == '__main__':
    main()
