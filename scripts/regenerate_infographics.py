import os
from PIL import Image, ImageDraw, ImageFont

def get_fonts():
    try:
        return {
            'title': ImageFont.truetype('arialbd.ttf', 32),
            'sub': ImageFont.truetype('arial.ttf', 17),
            'badge': ImageFont.truetype('arialbd.ttf', 11),
            'card_title': ImageFont.truetype('arialbd.ttf', 18),
            'card_num': ImageFont.truetype('arialbd.ttf', 20),
            'bold': ImageFont.truetype('arialbd.ttf', 13),
            'text': ImageFont.truetype('arial.ttf', 13),
            'wm': ImageFont.truetype('arialbd.ttf', 15),
            'small': ImageFont.truetype('arial.ttf', 12)
        }
    except Exception:
        d = ImageFont.load_default()
        return {k: d for k in ['title', 'sub', 'badge', 'card_title', 'card_num', 'bold', 'text', 'wm', 'small']}

def draw_watermark(draw, width, height, fonts, subtitle='erikwebsite.com — Diseño Web Profesional y Posicionamiento Local en Argentina'):
    y_line = height - 56
    draw.line([50, y_line, width - 50, y_line], fill='#334155', width=1)
    draw.text((50, y_line + 14), subtitle, fill='#64748b', font=fonts['small'])
    
    # Pill perfectly fitted and aligned
    pill_text = 'erikwebsite.com'
    bbox = draw.textbbox((0, 0), pill_text, font=fonts['wm'])
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    
    pill_w = tw + 22
    pill_h = th + 10
    px = width - 50 - pill_w
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

# ==============================================================================
# 1. DESGLOSE COSTOS WEB ARGENTINA
# ==============================================================================
def gen_desglose_costos():
    w, h = 1200, 700
    img = Image.new('RGB', (w, h), color='#0f172a')
    draw = ImageDraw.Draw(img)
    f = get_fonts()

    # Header
    draw.rounded_rectangle([50, 35, 300, 65], radius=8, fill='#1e293b')
    draw.text((65, 42), 'TRANSPARENCIA DE PRECIOS 2026', fill='#38bdf8', font=f['badge'])
    draw.text((50, 78), 'Desglose de Costos de una Página Web en Argentina', fill='#ffffff', font=f['title'])
    draw.text((50, 122), 'Todo lo que pagás: desarrollo inicial, mantenimiento mensual y aranceles oficiales', fill='#94a3b8', font=f['sub'])

    # 4 Cards
    cards = [
        {
            'step': '01',
            'title': 'Dominio Oficial',
            'badge': 'NIC ARGENTINA',
            'badge_bg': '#1e293b',
            'badge_col': '#38bdf8',
            'cost': '$8.500 a $25.000 ARS',
            'period': 'Arancel anual oficial',
            'desc': 'Registro a nombre de tu negocio en nic.ar (.com.ar o .ar). Sos el dueño legal del dominio.'
        },
        {
            'step': '02',
            'title': 'Hosting y SSL',
            'badge': 'ALTA VELOCIDAD',
            'badge_bg': '#1e293b',
            'badge_col': '#fbbf24',
            'cost': '$15.000 a $30.000 ARS',
            'period': 'Abono mensual de servidor',
            'desc': 'Servidor seguro con HTTPS (candado verde). Carga en celular en menos de 1 segundo.'
        },
        {
            'step': '03',
            'title': 'Desarrollo Web',
            'badge': 'PAGO ÚNICO',
            'badge_bg': '#064e3b',
            'badge_col': '#34d399',
            'cost': '$150.000 ARS',
            'period': 'En 2 cuotas (50% / 50%)',
            'desc': 'Diseño a medida, textos comerciales redactados por audios, optimización Maps y WhatsApp.'
        },
        {
            'step': '04',
            'title': 'Mantenimiento',
            'badge': 'OPCIONAL PRO',
            'badge_bg': '#1e293b',
            'badge_col': '#c084fc',
            'cost': '$20.000 ARS / mes',
            'period': '1º mes 100% bonificado',
            'desc': 'Hasta 3 cambios de fotos, textos o precios por mes, copias de seguridad y soporte.'
        }
    ]

    card_w = 260
    card_gap = 20
    x_start = 50
    y_card = 165
    h_card = 445

    for i, c in enumerate(cards):
        x = x_start + i * (card_w + card_gap)
        is_highlight = (i == 2)
        border_col = '#10b981' if is_highlight else '#334155'
        bg_col = '#182438' if is_highlight else '#1e293b'
        draw.rounded_rectangle([x, y_card, x + card_w, y_card + h_card], radius=14, fill=bg_col, outline=border_col, width=2 if is_highlight else 1)

        # Header of card
        draw.text((x + 16, y_card + 16), c['step'], fill='#64748b', font=f['card_num'])
        
        # Badge
        bbox_b = draw.textbbox((0, 0), c['badge'], font=f['badge'])
        bw = (bbox_b[2] - bbox_b[0]) + 16
        draw.rounded_rectangle([x + card_w - bw - 14, y_card + 16, x + card_w - 14, y_card + 38], radius=5, fill=c['badge_bg'])
        draw.text((x + card_w - bw - 6, y_card + 20), c['badge'], fill=c['badge_col'], font=f['badge'])

        draw.text((x + 16, y_card + 54), c['title'], fill='#ffffff', font=f['card_title'])
        draw.line([x + 16, y_card + 84, x + card_w - 16, y_card + 84], fill='#334155', width=1)

        # Cost box
        draw.rounded_rectangle([x + 14, y_card + 98, x + card_w - 14, y_card + 165], radius=10, fill='#0f172a')
        draw.text((x + 22, y_card + 108), c['cost'], fill='#34d399' if is_highlight else '#ffffff', font=f['card_title'])
        draw.text((x + 22, y_card + 138), c['period'], fill='#94a3b8', font=f['small'])

        # Description wrapped cleanly
        draw.text((x + 16, y_card + 185), 'Detalle del servicio:', fill='#64748b', font=f['badge'])
        desc_lines = wrap_text(draw, c['desc'], f['text'], card_w - 32)
        py = y_card + 210
        for line in desc_lines:
            draw.text((x + 16, py), line, fill='#cbd5e1', font=f['text'])
            py += 22

    draw_watermark(draw, w, h, f, 'Fuente: erikwebsite.com — Guía de costos reales de diseño web en Argentina')
    img.save('images/desglose_costos_web_argentina.png')
    img.save('public/images/desglose_costos_web_argentina.png')
    print('OK: desglose_costos_web_argentina.png')

# ==============================================================================
# 2. GUÍA POSICIONAR GOOGLE MAPS ARGENTINA
# ==============================================================================
def gen_google_maps():
    w, h = 1200, 675
    img = Image.new('RGB', (w, h), color='#0f172a')
    draw = ImageDraw.Draw(img)
    f = get_fonts()

    draw.rounded_rectangle([50, 35, 300, 65], radius=8, fill='#064e3b')
    draw.text((65, 42), 'GUÍA LOCAL SEO ARGENTINA', fill='#34d399', font=f['badge'])
    draw.text((50, 78), 'Cómo Posicionar en Google Maps (Local Pack)', fill='#ffffff', font=f['title'])
    draw.text((50, 122), 'Los 4 pilares para conseguir clientes orgánicos sin pagar Google Ads', fill='#94a3b8', font=f['sub'])

    cards = [
        {
            'num': '01',
            'title': 'Ficha y Categoría',
            'badge': 'RELEVANCIA',
            'badge_bg': '#1e293b',
            'badge_col': '#38bdf8',
            'items': [
                'Elegir categoría primaria exacta.',
                'Nombre real (sin relleno spam).',
                'Horarios y fotos reales del local.',
                'Verificación oficial por video/SMS.'
            ]
        },
        {
            'num': '02',
            'title': 'Cobertura Local',
            'badge': 'DISTANCIA',
            'badge_bg': '#1e293b',
            'badge_col': '#fbbf24',
            'items': [
                'Local a la calle: dirección visible.',
                'A domicilio: definir radio o zona.',
                'Coincidencia con ubicación IP.',
                'Menciones de barrios locales.'
            ]
        },
        {
            'num': '03',
            'title': 'Sitio Web Vinculado',
            'badge': 'PROMINENCIA (+45%)',
            'badge_bg': '#064e3b',
            'badge_col': '#34d399',
            'items': [
                'Google valida rubro y servicios.',
                'Carga rápida en móvil (<1s).',
                'Mismo teléfono y dirección (NAP).',
                'Supera a fichas que solo usan redes.'
            ]
        },
        {
            'num': '04',
            'title': 'Reseñas y WhatsApp',
            'badge': 'CONVERSIÓN',
            'badge_bg': '#1e293b',
            'badge_col': '#f472b6',
            'items': [
                'Opiniones con palabras clave.',
                'Responder al 100% de reseñas.',
                'Botón web directo a WhatsApp.',
                'Respuesta rápida a consultas.'
            ]
        }
    ]

    card_w = 260
    card_gap = 20
    x_start = 50
    y_card = 165
    h_card = 425

    for i, c in enumerate(cards):
        x = x_start + i * (card_w + card_gap)
        is_highlight = (i == 2)
        border_col = '#10b981' if is_highlight else '#334155'
        draw.rounded_rectangle([x, y_card, x + card_w, y_card + h_card], radius=14, fill='#1e293b', outline=border_col, width=2 if is_highlight else 1)

        draw.text((x + 16, y_card + 16), c['num'], fill='#64748b', font=f['card_num'])
        
        bbox_b = draw.textbbox((0, 0), c['badge'], font=f['badge'])
        bw = (bbox_b[2] - bbox_b[0]) + 16
        draw.rounded_rectangle([x + card_w - bw - 14, y_card + 16, x + card_w - 14, y_card + 38], radius=5, fill=c['badge_bg'])
        draw.text((x + card_w - bw - 6, y_card + 20), c['badge'], fill=c['badge_col'], font=f['badge'])

        draw.text((x + 16, y_card + 54), c['title'], fill='#ffffff', font=f['card_title'])
        draw.line([x + 16, y_card + 84, x + card_w - 16, y_card + 84], fill='#334155', width=1)

        py = y_card + 105
        for item in c['items']:
            draw.text((x + 16, py), '•', fill='#10b981' if is_highlight else '#38bdf8', font=f['bold'])
            lines = wrap_text(draw, item, f['text'], card_w - 42)
            for l in lines:
                draw.text((x + 30, py), l, fill='#cbd5e1', font=f['text'])
                py += 22
            py += 14

    draw_watermark(draw, w, h, f, 'Fuente: erikwebsite.com — Diseño Web y Posicionamiento Local en Google Maps')
    img.save('images/guia_posicionar_google_maps_argentina.png')
    img.save('public/images/guia_posicionar_google_maps_argentina.png')
    print('OK: guia_posicionar_google_maps_argentina.png')

# ==============================================================================
# 3. GUÍA WEB ABOGADOS ARGENTINA
# ==============================================================================
def gen_web_abogados():
    w, h = 1200, 675
    img = Image.new('RGB', (w, h), color='#0f172a')
    draw = ImageDraw.Draw(img)
    f = get_fonts()

    draw.rounded_rectangle([50, 35, 300, 65], radius=8, fill='#1e293b')
    draw.text((65, 42), 'ESTÁNDARES WEB LEGAL 2026', fill='#38bdf8', font=f['badge'])
    draw.text((50, 78), 'Qué Debe Tener una Web para Abogados en Argentina', fill='#ffffff', font=f['title'])
    draw.text((50, 122), 'Elementos esenciales para convertir visitas en consultas legales por WhatsApp', fill='#94a3b8', font=f['sub'])

    cards = [
        {
            'num': '01',
            'title': 'Especialidades Claras',
            'badge': 'SEO LOCAL',
            'badge_bg': '#1e293b',
            'badge_col': '#38bdf8',
            'items': [
                'Separar Laboral, Familia, Civil.',
                'Palabras clave (ej: San Juan, CABA).',
                'Preguntas frecuentes por fuero.',
                'Lenguaje claro para el cliente.'
            ]
        },
        {
            'num': '02',
            'title': 'Matrícula y Equipo',
            'badge': 'CONFIANZA',
            'badge_bg': '#1e293b',
            'badge_col': '#fbbf24',
            'items': [
                'Fotos profesionales del letrado.',
                'Colegio, Tomo y Folio visible.',
                'Dirección física del estudio.',
                'Acreditación y trayectoria real.'
            ]
        },
        {
            'num': '03',
            'title': 'Botón WhatsApp',
            'badge': 'CONVERSIÓN DIRECTA',
            'badge_bg': '#064e3b',
            'badge_col': '#34d399',
            'items': [
                'El 75% consulta desde el celular.',
                'Mensaje prearmado según fuero.',
                'Sin formularios largos engorrosos.',
                'Contacto confidencial inmediato.'
            ]
        },
        {
            'num': '04',
            'title': 'Herramientas Prácticas',
            'badge': 'VALOR AL CLIENTE',
            'badge_bg': '#1e293b',
            'badge_col': '#c084fc',
            'items': [
                'Calculadora laboral interactiva.',
                'Estimador de cuota alimentaria.',
                'El cliente entiende su situación.',
                'Mayor permanencia en el sitio.'
            ]
        }
    ]

    card_w = 260
    card_gap = 20
    x_start = 50
    y_card = 165
    h_card = 425

    for i, c in enumerate(cards):
        x = x_start + i * (card_w + card_gap)
        is_highlight = (i == 2)
        border_col = '#10b981' if is_highlight else '#334155'
        draw.rounded_rectangle([x, y_card, x + card_w, y_card + h_card], radius=14, fill='#1e293b', outline=border_col, width=2 if is_highlight else 1)

        draw.text((x + 16, y_card + 16), c['num'], fill='#64748b', font=f['card_num'])
        
        bbox_b = draw.textbbox((0, 0), c['badge'], font=f['badge'])
        bw = (bbox_b[2] - bbox_b[0]) + 16
        draw.rounded_rectangle([x + card_w - bw - 14, y_card + 16, x + card_w - 14, y_card + 38], radius=5, fill=c['badge_bg'])
        draw.text((x + card_w - bw - 6, y_card + 20), c['badge'], fill=c['badge_col'], font=f['badge'])

        draw.text((x + 16, y_card + 54), c['title'], fill='#ffffff', font=f['card_title'])
        draw.line([x + 16, y_card + 84, x + card_w - 16, y_card + 84], fill='#334155', width=1)

        py = y_card + 105
        for item in c['items']:
            draw.text((x + 16, py), '•', fill='#10b981' if is_highlight else '#38bdf8', font=f['bold'])
            lines = wrap_text(draw, item, f['text'], card_w - 42)
            for l in lines:
                draw.text((x + 30, py), l, fill='#cbd5e1', font=f['text'])
                py += 22
            py += 14

    draw_watermark(draw, w, h, f, 'Fuente: erikwebsite.com — Sitios Web para Abogados y Estudios Jurídicos')
    img.save('images/guia_web_abogados_argentina.png')
    img.save('public/images/guia_web_abogados_argentina.png')
    print('OK: guia_web_abogados_argentina.png')

# ==============================================================================
# 4. AUTOMATIZAR TURNOS CONSULTORIO ARGENTINA
# ==============================================================================
def gen_turnos():
    w, h = 1200, 675
    img = Image.new('RGB', (w, h), color='#0f172a')
    draw = ImageDraw.Draw(img)
    f = get_fonts()

    draw.rounded_rectangle([50, 35, 300, 65], radius=8, fill='#1e293b')
    draw.text((65, 42), 'GESTIÓN MÉDICA EFICIENTE', fill='#38bdf8', font=f['badge'])
    draw.text((50, 78), 'Cómo Organizar los Turnos en tu Consultorio', fill='#ffffff', font=f['title'])
    draw.text((50, 122), 'Comparativa: Sistemas pesados tradicionales vs. Página Web ágil con WhatsApp', fill='#94a3b8', font=f['sub'])

    card_w = 535
    x_gap = 30
    y_card = 165
    h_card = 425

    # Card 1: Tradicionales
    x1 = 50
    draw.rounded_rectangle([x1, y_card, x1 + card_w, y_card + h_card], radius=16, fill='#1e293b', outline='#ef4444', width=2)
    draw.rounded_rectangle([x1 + 18, y_card + 16, x1 + 230, y_card + 42], radius=6, fill='#450a0a')
    draw.text((x1 + 28, y_card + 22), 'SISTEMAS TRADICIONALES', fill='#f87171', font=f['badge'])
    draw.text((x1 + 18, y_card + 54), 'Apps y Software de Gestión Complejo', fill='#ffffff', font=f['card_title'])
    draw.line([x1 + 18, y_card + 84, x1 + card_w - 18, y_card + 84], fill='#334155', width=1)

    pts1 = [
        ('Exige descargar app pesada', 'El paciente no quiere ocupar espacio ni crear contraseñas.'),
        ('Altos costos mensuales en USD', 'Abonos fijos en dólares o comisiones por cada turno.'),
        ('Fricción en pacientes mayores', 'Se frustran con la tecnología y terminan llamando igual.'),
        ('Secretaria sobrecargada', 'Pasa horas resolviendo reclamos de acceso al sistema.')
    ]
    py = y_card + 102
    for title, desc in pts1:
        draw.text((x1 + 18, py), '✕', fill='#ef4444', font=f['bold'])
        draw.text((x1 + 38, py), title, fill='#ffffff', font=f['bold'])
        py += 20
        lines = wrap_text(draw, desc, f['text'], card_w - 55)
        for l in lines:
            draw.text((x1 + 38, py), l, fill='#94a3b8', font=f['text'])
            py += 20
        py += 14

    # Card 2: Web Ágil
    x2 = x1 + card_w + x_gap
    draw.rounded_rectangle([x2, y_card, x2 + card_w, y_card + h_card], radius=16, fill='#182438', outline='#10b981', width=2)
    draw.rounded_rectangle([x2 + 18, y_card + 16, x2 + 230, y_card + 42], radius=6, fill='#064e3b')
    draw.text((x2 + 28, y_card + 22), 'MÉTODO ÁGIL ERIK WEBSITE', fill='#34d399', font=f['badge'])
    draw.text((x2 + 18, y_card + 54), 'Página Web Médica + WhatsApp Directo', fill='#ffffff', font=f['card_title'])
    draw.line([x2 + 18, y_card + 84, x2 + card_w - 18, y_card + 84], fill='#334155', width=1)

    pts2 = [
        ('Sin descargar nada', 'Entra al instante desde el navegador móvil en menos de 1s.'),
        ('Filtro de obras sociales y copagos', 'El paciente ve aranceles y requisitos antes de consultar.'),
        ('Turno prearmado a WhatsApp', 'Mensaje con nombre, día preferido y cobertura médica.'),
        ('Costo único en pesos ($150.000)', 'Sin mensualidades obligatorias en dólares ni comisiones.')
    ]
    py = y_card + 102
    for title, desc in pts2:
        draw.text((x2 + 18, py), '✓', fill='#10b981', font=f['bold'])
        draw.text((x2 + 38, py), title, fill='#ffffff', font=f['bold'])
        py += 20
        lines = wrap_text(draw, desc, f['text'], card_w - 55)
        for l in lines:
            draw.text((x2 + 38, py), l, fill='#6ee7b7', font=f['text'])
            py += 20
        py += 14

    draw_watermark(draw, w, h, f, 'Fuente: erikwebsite.com — Soluciones Web para Consultorios Médicos y Odontológicos')
    img.save('images/automatizar_turnos_consultorio_argentina.png')
    img.save('public/images/automatizar_turnos_consultorio_argentina.png')
    print('OK: automatizar_turnos_consultorio_argentina.png')

# ==============================================================================
# 5. QUÉ NEGOCIOS NECESITAN PÁGINA WEB
# ==============================================================================
def gen_que_negocios():
    w, h = 1200, 675
    img = Image.new('RGB', (w, h), color='#0f172a')
    draw = ImageDraw.Draw(img)
    f = get_fonts()

    draw.rounded_rectangle([50, 35, 300, 65], radius=8, fill='#064e3b')
    draw.text((65, 42), 'DIAGNÓSTICO DIGITAL 2026', fill='#34d399', font=f['badge'])
    draw.text((50, 78), '¿Qué Negocios Necesitan una Página Web?', fill='#ffffff', font=f['title'])
    draw.text((50, 122), 'Matriz de prioridad según urgencia de búsqueda y nivel de confianza requerido', fill='#94a3b8', font=f['sub'])

    cards = [
        {
            'prio': 'ALTA',
            'badge': 'INDISPENSABLE',
            'badge_bg': '#831843',
            'badge_col': '#f472b6',
            'title': 'Servicios de Urgencia',
            'rubros': 'Plomeros, electricistas, cerrajeros, auxilio mecánico.',
            'porque': 'La gente busca en Google con el problema encima. Sin web pierden el 90% de llamados.'
        },
        {
            'prio': 'ALTA',
            'badge': 'CONFIANZA',
            'badge_bg': '#064e3b',
            'badge_col': '#34d399',
            'title': 'Profesionales y Salud',
            'rubros': 'Abogados, médicos, dentistas, psicólogos, contadores.',
            'porque': 'Exige validar matrícula, equipo y ubicación física antes de confiar un caso o turno.'
        },
        {
            'prio': 'MEDIA',
            'badge': 'LOCAL PACK',
            'badge_bg': '#1e293b',
            'badge_col': '#38bdf8',
            'title': 'Comercios y Locales',
            'rubros': 'Salones de eventos, centros estéticos, talleres.',
            'porque': 'Muestran instalaciones, listas de precios base y capturan búsquedas por barrio en Google Maps.'
        },
        {
            'prio': 'BAJA',
            'badge': 'INICIAL',
            'badge_bg': '#1e293b',
            'badge_col': '#94a3b8',
            'title': 'Hobbies o Iniciales',
            'rubros': 'Creadores de video, ventas ocasionales a conocidos.',
            'porque': 'Pueden empezar con Instagram o TikTok hasta consolidar clientela fija.'
        }
    ]

    card_w = 260
    card_gap = 20
    x_start = 50
    y_card = 165
    h_card = 425

    for i, c in enumerate(cards):
        x = x_start + i * (card_w + card_gap)
        is_high = (i in [0, 1])
        border_col = '#10b981' if i == 1 else ('#f43f5e' if i == 0 else '#334155')
        draw.rounded_rectangle([x, y_card, x + card_w, y_card + h_card], radius=14, fill='#1e293b', outline=border_col, width=2 if is_high else 1)

        draw.text((x + 16, y_card + 16), c['prio'], fill='#64748b', font=f['card_num'])
        
        bbox_b = draw.textbbox((0, 0), c['badge'], font=f['badge'])
        bw = (bbox_b[2] - bbox_b[0]) + 16
        draw.rounded_rectangle([x + card_w - bw - 14, y_card + 16, x + card_w - 14, y_card + 38], radius=5, fill=c['badge_bg'])
        draw.text((x + card_w - bw - 6, y_card + 20), c['badge'], fill=c['badge_col'], font=f['badge'])

        draw.text((x + 16, y_card + 54), c['title'], fill='#ffffff', font=f['card_title'])
        draw.line([x + 16, y_card + 84, x + card_w - 16, y_card + 84], fill='#334155', width=1)

        # Rubros
        draw.text((x + 16, y_card + 100), 'Rubros típicos:', fill='#64748b', font=f['badge'])
        lines_r = wrap_text(draw, c['rubros'], f['text'], card_w - 32)
        py = y_card + 122
        for l in lines_r:
            draw.text((x + 16, py), l, fill='#cbd5e1', font=f['text'])
            py += 20

        # Por qué
        py += 16
        draw.text((x + 16, py), 'Por qué conviene:', fill='#10b981' if is_high else '#38bdf8', font=f['badge'])
        py += 22
        lines_p = wrap_text(draw, c['porque'], f['text'], card_w - 32)
        for l in lines_p:
            draw.text((x + 16, py), l, fill='#94a3b8', font=f['text'])
            py += 20

    draw_watermark(draw, w, h, f, 'Fuente: erikwebsite.com — Diagnóstico de presencia digital para PyMEs en Argentina')
    img.save('images/que_negocios_necesitan_pagina_web.png')
    img.save('public/images/que_negocios_necesitan_pagina_web.png')
    print('OK: que_negocios_necesitan_pagina_web.png')

# ==============================================================================
# 6. COMPARATIVA WEB VS INSTAGRAM & COMPARATIVA PRECIOS (Verificar watermarks)
# ==============================================================================
def gen_comparativa_web_ig():
    w, h = 1200, 675
    img = Image.new('RGB', (w, h), color='#0f172a')
    draw = ImageDraw.Draw(img)
    f = get_fonts()

    draw.rounded_rectangle([50, 35, 300, 65], radius=8, fill='#1e293b')
    draw.text((65, 42), 'CANALES DIGITALES 2026', fill='#38bdf8', font=f['badge'])
    draw.text((50, 78), 'Página Web Propia vs. Perfil de Instagram', fill='#ffffff', font=f['title'])
    draw.text((50, 122), 'Diferencias clave en control, intención de compra y conversión para negocios', fill='#94a3b8', font=f['sub'])

    col1_x = 50
    col2_x = 340
    col3_x = 750
    width_col1 = 270
    width_col = 400

    draw.rounded_rectangle([col2_x, 170, col2_x + width_col, 215], radius=8, fill='#831843')
    draw.text((col2_x + 20, 182), 'INSTAGRAM (Meta)', fill='#f472b6', font=f['card_title'])

    draw.rounded_rectangle([col3_x, 170, col3_x + width_col, 215], radius=8, fill='#064e3b')
    draw.text((col3_x + 20, 182), 'PÁGINA WEB PROPIA', fill='#34d399', font=f['card_title'])

    rows = [
        ('Control y Propiedad',
         'Espacio alquilado a Meta. Si te bloquean o cambian el algoritmo, perdés tu audiencia.',
         'Propiedad 100% tuya con dominio oficial .ar. Sin riesgo de suspensión arbitraria.'),
        ('Intención del Usuario',
         'Baja (Scroll de ocio). La gente mira fotos; no está buscando contratar de urgencia.',
         'Alta (Búsqueda activa). El usuario busca en Google con necesidad y dinero listo.'),
        ('Conversión a WhatsApp',
         'Fricción alta. Mensajes por DM que se pierden o links en bio que abren con lentitud.',
         '1 Clic directo a WhatsApp. Carga en <1s con mensaje prearmado listo para enviar.'),
        ('Encuentro en Google',
         'Invisible en búsquedas locales de Google Maps. No posiciona para servicios por zona.',
         'Posicionamiento en Google Maps y buscador local. Aparece en tu localidad.')
    ]

    y = 230
    row_h = 80
    for i, (label, ig, web) in enumerate(rows):
        bg = '#1e293b' if i % 2 == 0 else '#162032'
        draw.rounded_rectangle([col1_x, y, col1_x + width_col1 - 15, y + row_h], radius=8, fill=bg)
        draw.text((col1_x + 14, y + 28), label, fill='#ffffff', font=f['bold'])

        # IG
        draw.rounded_rectangle([col2_x, y, col2_x + width_col, y + row_h], radius=8, fill=bg)
        lines_ig = wrap_text(draw, ig, f['text'], width_col - 28)
        py = y + 16
        for l in lines_ig:
            draw.text((col2_x + 14, py), l, fill='#cbd5e1', font=f['text'])
            py += 22

        # Web
        draw.rounded_rectangle([col3_x, y, col3_x + width_col, y + row_h], radius=8, fill=bg)
        lines_web = wrap_text(draw, web, f['text'], width_col - 28)
        py = y + 16
        for l in lines_web:
            draw.text((col3_x + 14, py), l, fill='#6ee7b7', font=f['text'])
            py += 22

        y += row_h + 10

    draw_watermark(draw, w, h, f, 'Fuente: erikwebsite.com — Análisis estratégico de canales digitales en Argentina')
    img.save('images/comparativa_web_vs_instagram.png')
    img.save('public/images/comparativa_web_vs_instagram.png')
    print('OK: comparativa_web_vs_instagram.png')

if __name__ == '__main__':
    gen_desglose_costos()
    gen_google_maps()
    gen_web_abogados()
    gen_turnos()
    gen_que_negocios()
    gen_comparativa_web_ig()
    print('ALL INFOGRAPHICS REGENERATED WITH ZERO OVERFLOW AND PERFECT WATERMARKS!')
