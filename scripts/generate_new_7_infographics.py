import os
from PIL import Image, ImageDraw, ImageFont

def get_fonts():
    try:
        return {
            'title': ImageFont.truetype('arialbd.ttf', 30),
            'sub': ImageFont.truetype('arial.ttf', 16),
            'badge': ImageFont.truetype('arialbd.ttf', 11),
            'card_title': ImageFont.truetype('arialbd.ttf', 17),
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

def save_image(img, filename):
    os.makedirs('images', exist_ok=True)
    os.makedirs('public/images', exist_ok=True)
    img.save(f'images/{filename}')
    img.save(f'public/images/{filename}')
    print(f'OK: {filename}')

def render_4_card_infographic(filename, badge_text, title_text, sub_text, cards, badge_bg='#064e3b', badge_col='#34d399'):
    w, h = 1200, 675
    img = Image.new('RGB', (w, h), color='#0f172a')
    draw = ImageDraw.Draw(img)
    f = get_fonts()

    # Header
    draw.rounded_rectangle([50, 32, 340, 62], radius=8, fill=badge_bg)
    draw.text((65, 39), badge_text, fill=badge_col, font=f['badge'])
    draw.text((50, 72), title_text, fill='#ffffff', font=f['title'])
    draw.text((50, 114), sub_text, fill='#94a3b8', font=f['sub'])

    card_w = 260
    card_gap = 20
    x_start = 50
    y_card = 155
    h_card = 445

    for i, c in enumerate(cards):
        x = x_start + i * (card_w + card_gap)
        is_highlight = c.get('highlight', False)
        border_col = '#10b981' if is_highlight else '#334155'
        bg_col = '#182438' if is_highlight else '#1e293b'
        draw.rounded_rectangle([x, y_card, x + card_w, y_card + h_card], radius=14, fill=bg_col, outline=border_col, width=2 if is_highlight else 1)

        draw.text((x + 16, y_card + 16), c['num'], fill='#64748b', font=f['card_num'])
        
        # Badge
        bbox_b = draw.textbbox((0, 0), c['badge'], font=f['badge'])
        bw = (bbox_b[2] - bbox_b[0]) + 16
        draw.rounded_rectangle([x + card_w - bw - 14, y_card + 16, x + card_w - 14, y_card + 38], radius=5, fill=c.get('badge_bg', '#1e293b'))
        draw.text((x + card_w - bw - 6, y_card + 20), c['badge'], fill=c.get('badge_col', '#38bdf8'), font=f['badge'])

        draw.text((x + 16, y_card + 54), c['title'], fill='#ffffff', font=f['card_title'])
        draw.line([x + 16, y_card + 82, x + card_w - 16, y_card + 82], fill='#334155', width=1)

        draw.text((x + 16, y_card + 96), c.get('header_small', 'Puntos clave:'), fill='#64748b', font=f['badge'])

        py = y_card + 120
        for item in c['items']:
            draw.text((x + 16, py), '•', fill='#10b981' if is_highlight else '#38bdf8', font=f['bold'])
            item_lines = wrap_text(draw, item, f['text'], card_w - 44)
            for line in item_lines:
                draw.text((x + 30, py), line, fill='#cbd5e1', font=f['text'])
                py += 20
            py += 6

    draw_watermark(draw, w, h, f)
    save_image(img, filename)

# 1. PSICÓLOGOS
def gen_psicologos():
    cards = [
        {
            'num': '01',
            'title': 'Confianza y Matrícula',
            'badge': 'LEGALIDAD',
            'badge_bg': '#1e293b',
            'badge_col': '#38bdf8',
            'items': [
                'Número de matrícula visible.',
                'Enfoque clínico (TCC, psicoanálisis, sistémica).',
                'Colegio profesional correspondiente.',
                'Foto profesional y bio cercana.'
            ]
        },
        {
            'num': '02',
            'title': 'Terapia Online y Presencial',
            'badge': 'ALCANCE',
            'badge_bg': '#1e293b',
            'badge_col': '#fbbf24',
            'items': [
                'Pacientes de todo el país o el exterior.',
                'Consultorio físico con mapa exacto.',
                'Plataformas claras (Meet / Zoom).',
                'Manejo de zonas horarias.'
            ]
        },
        {
            'num': '03',
            'title': 'Turnos y Privacidad',
            'badge': 'CONVERSIÓN',
            'badge_bg': '#064e3b',
            'badge_col': '#34d399',
            'highlight': True,
            'items': [
                'Filtro previo particular vs prepagas.',
                'Botón directo a WhatsApp privado.',
                'Sin apps invasivas para el paciente.',
                'Preguntas clave antes de la primera sesión.'
            ]
        },
        {
            'num': '04',
            'title': 'Honorarios y Cobro',
            'badge': 'CLARIDAD',
            'badge_bg': '#1e293b',
            'badge_col': '#c084fc',
            'items': [
                'Transferencias y Mercado Pago.',
                'Cobros internacionales si aplica.',
                'Política de cancelación de turnos.',
                'Ahorro en comisiones de directorios.'
            ]
        }
    ]
    render_4_card_infographic(
        'guia_web_psicologos_argentina.png',
        'SALUD MENTAL Y TERAPIA 2026',
        'Páginas Web para Psicólogos y Terapeutas en Argentina',
        'Los 4 pilares para captar pacientes calificados y organizar tu agenda sin intermediarios',
        cards
    )

# 2. OFICIOS Y SERVICIOS DEL HOGAR
def gen_oficios():
    cards = [
        {
            'num': '01',
            'title': 'Ficha Google Maps',
            'badge': 'URGENCIA LOCAL',
            'badge_bg': '#1e293b',
            'badge_col': '#38bdf8',
            'items': [
                'Aparecer cuando buscan "electricista ya".',
                'Radio de cobertura barrial o municipal.',
                'Reseñas de vecinos satisfechos.',
                'Llamada directa en un solo toque.'
            ]
        },
        {
            'num': '02',
            'title': 'Matrícula y Seguridad',
            'badge': 'CONFIANZA',
            'badge_bg': '#1e293b',
            'badge_col': '#fbbf24',
            'items': [
                'Aclarar si sos gasista o electricista matriculado.',
                'Seguro de accidentes o ART de apoyo.',
                'Fotos reales de trabajos finalizados.',
                'Garantía escrita en presupuestos.'
            ]
        },
        {
            'num': '03',
            'title': 'Cotización por Audio',
            'badge': 'WHATSAPP PRO',
            'badge_bg': '#064e3b',
            'badge_col': '#34d399',
            'highlight': True,
            'items': [
                'El cliente envía foto del problema.',
                'Mensaje preconfigurado con zona y servicio.',
                'Filtro de curiosos sin perder tiempo.',
                'Respuesta rápida desde tu celular.'
            ]
        },
        {
            'num': '04',
            'title': 'Presupuesto Mínimo',
            'badge': 'RENTABILIDAD',
            'badge_bg': '#1e293b',
            'badge_col': '#c084fc',
            'items': [
                'Aclarar valor de visita técnica.',
                'Cobro con transferencia o tarjeta en obra.',
                'Menos llamadas que no pagan el viaje.',
                'Posicionamiento orgánico sin pagar avisos.'
            ]
        }
    ]
    render_4_card_infographic(
        'guia_web_oficios_hogar_argentina.png',
        'OFICIOS Y URGENCIAS EN ARGENTINA',
        'Páginas Web para Electricistas, Plomeros y Gasistas',
        'Cómo conseguir llamados urgentes en Google Maps y filtrar presupuestos por WhatsApp',
        cards
    )

# 3. ESTUDIOS CONTABLES
def gen_contables():
    cards = [
        {
            'num': '01',
            'title': 'Público Objetivo',
            'badge': 'SEGMENTACIÓN',
            'badge_bg': '#1e293b',
            'badge_col': '#38bdf8',
            'items': [
                'Monotributistas y emprendedores.',
                'PyMEs comerciales y de servicios.',
                'Liquidación de sueldos y jornales.',
                'Auditoría y balances anuales.'
            ]
        },
        {
            'num': '02',
            'title': 'Alcance Nacional',
            'badge': '100% ONLINE',
            'badge_bg': '#1e293b',
            'badge_col': '#fbbf24',
            'items': [
                'Atención virtual a clientes de todo el país.',
                'Asesoramiento fiscal ante ARCA/AFIP.',
                'Gestión de comprobantes digitales.',
                'Reuniones ágiles por videollamada.'
            ]
        },
        {
            'num': '03',
            'title': 'Autoridad y Confianza',
            'badge': 'PRESTIGIO',
            'badge_bg': '#064e3b',
            'badge_col': '#34d399',
            'highlight': True,
            'items': [
                'Matrícula CPCE visible de socios.',
                'Propuesta de valor clara frente a la competencia.',
                'Casos de éxito y sectores atendidos.',
                'Plantillas e información impositiva útil.'
            ]
        },
        {
            'num': '04',
            'title': 'Contacto Comercial',
            'badge': 'LEADS PYME',
            'badge_bg': '#1e293b',
            'badge_col': '#c084fc',
            'items': [
                'Formulario ágil de diagnóstico fiscal.',
                'WhatsApp directo al contador a cargo.',
                'Presupuestos mensuales transparentes.',
                'Independencia de recomendaciones boca a boca.'
            ]
        }
    ]
    render_4_card_infographic(
        'guia_web_estudios_contables_argentina.png',
        'CONTADORES Y CIENCIAS ECONÓMICAS',
        'Páginas Web para Estudios Contables en Argentina',
        'Estrategia digital para captar PyMEs y monotributistas de todo el país',
        cards
    )

# 4. SALONES DE BELLEZA Y ESTÉTICA
def gen_estetica():
    cards = [
        {
            'num': '01',
            'title': 'Catálogo Visual',
            'badge': 'IMPACTO',
            'badge_bg': '#1e293b',
            'badge_col': '#38bdf8',
            'items': [
                'Fotos reales de antes y después.',
                'Tratamientos faciales, corporales y capilares.',
                'Marcas de productos utilizados.',
                'Aparatología certificada y segura.'
            ]
        },
        {
            'num': '02',
            'title': 'Lista de Precios Clara',
            'badge': 'SIN RODEOS',
            'badge_bg': '#1e293b',
            'badge_col': '#fbbf24',
            'items': [
                'Basta de "precio por privado".',
                'Combos y promociones por sesiones.',
                'Medios de pago (cuotas sin interés).',
                'Filtro de clientes que valoran calidad.'
            ]
        },
        {
            'num': '03',
            'title': 'Turnos por WhatsApp',
            'badge': 'AGENDA LLENA',
            'badge_bg': '#064e3b',
            'badge_col': '#34d399',
            'highlight': True,
            'items': [
                'Botón preconfigurado por tratamiento.',
                'Pedido de seña previa para reservar.',
                'Reducción drástica del ausentismo.',
                'Atención organizada para el equipo.'
            ]
        },
        {
            'num': '04',
            'title': 'Google Maps Local',
            'badge': 'ZONA Y BARRIO',
            'badge_bg': '#1e293b',
            'badge_col': '#c084fc',
            'items': [
                'Aparecer a clientas cerca de tu salón.',
                'Ficha con fotos luminosas del espacio.',
                'Reseñas de clientas frecuentes.',
                'Ubicación y estacionamiento cercano.'
            ]
        }
    ]
    render_4_card_infographic(
        'guia_web_estetica_salones_argentina.png',
        'BELLEZA Y CENTROS DE ESTÉTICA',
        'Páginas Web para Salones de Belleza y Estética',
        'Cómo mostrar tratamientos, publicar precios claros y automatizar la agenda por WhatsApp',
        cards
    )

# 5. SALONES DE EVENTOS Y CATERING
def gen_eventos():
    cards = [
        {
            'num': '01',
            'title': 'Galería Inmersiva',
            'badge': 'VISUAL',
            'badge_bg': '#1e293b',
            'badge_col': '#38bdf8',
            'items': [
                'Fotos diurnas y nocturnas del parque.',
                'Ambientaciones reales de bodas y 15s.',
                'Pista de baile, piscina y livings.',
                'Demostración de capacidad en mesas.'
            ]
        },
        {
            'num': '02',
            'title': 'Menús y Servicios',
            'badge': 'DETALLE',
            'badge_bg': '#1e293b',
            'badge_col': '#fbbf24',
            'items': [
                'Opciones de catering (finger food, asado, gourmet).',
                'Alquiler de vajilla, mantelería y cristalería.',
                'DJ, sonido e iluminación robótica.',
                'Seguridad privada y grupo electrógeno.'
            ]
        },
        {
            'num': '03',
            'title': 'Calculadora de Evento',
            'badge': 'COTIZADOR',
            'badge_bg': '#064e3b',
            'badge_col': '#34d399',
            'highlight': True,
            'items': [
                'El cliente indica cantidad de personas.',
                'Fecha tentativa y tipo de fiesta.',
                'Llega a tu WhatsApp ya prefiltrado.',
                'Ahorro de horas en llamados vacíos.'
            ]
        },
        {
            'num': '04',
            'title': 'Respaldo de Fechas',
            'badge': 'VENTAS ANTICIPADAS',
            'badge_bg': '#1e293b',
            'badge_col': '#c084fc',
            'items': [
                'Bloqueo de fechas con seña bancaria.',
                'Condiciones de congelamiento de precio.',
                'Preguntas frecuentes sobre horarios.',
                'Cierre de fechas con meses de anticipación.'
            ]
        }
    ]
    render_4_card_infographic(
        'guia_web_salones_eventos_argentina.png',
        'SALONES DE FIESTAS Y CATERING',
        'Páginas Web para Salones de Eventos y Fiestas',
        'Cómo exhibir el espacio, cotizar por cantidad de invitados y cerrar reservas anticipadas',
        cards
    )

# 6. PERSONAL TRAINERS Y GIMNASIOS
def gen_fitness():
    cards = [
        {
            'num': '01',
            'title': 'Presencial vs Online',
            'badge': 'MODELOS',
            'badge_bg': '#1e293b',
            'badge_col': '#38bdf8',
            'items': [
                'Clases personalizadas en gimnasio o parque.',
                'Planes de asesoría online a todo el país.',
                'Rutinas en PDF o apps dedicadas.',
                'Seguimiento semanal por videollamada.'
            ]
        },
        {
            'num': '02',
            'title': 'Casos de Éxito',
            'badge': 'PRUEBA SOCIAL',
            'badge_bg': '#1e293b',
            'badge_col': '#fbbf24',
            'items': [
                'Transformaciones físicas reales.',
                'Testimonios de alumnos con nombre y foto.',
                'Especialidad (fuerza, descenso, salud).',
                'Matrícula o certificación de profe.'
            ]
        },
        {
            'num': '03',
            'title': 'Planes y Cobros',
            'badge': 'RECURRENTES',
            'badge_bg': '#064e3b',
            'badge_col': '#34d399',
            'highlight': True,
            'items': [
                'Abono mensual claro sin vueltas.',
                'Cobro con débito automático o MP.',
                'Paquetes trimestrales con descuento.',
                'Menos dependencia del algoritmo de IG.'
            ]
        },
        {
            'num': '04',
            'title': 'Evaluación Inicial',
            'badge': 'ONBOARDING',
            'badge_bg': '#1e293b',
            'badge_col': '#c084fc',
            'items': [
                'Cuestionario previo de salud y objetivos.',
                'El alumno llega listo para entrenar.',
                'Botón directo a WhatsApp comercial.',
                'Profesionalismo que justifica tus tarifas.'
            ]
        }
    ]
    render_4_card_infographic(
        'guia_web_personal_trainers_argentina.png',
        'FITNESS Y ENTRENAMIENTO 2026',
        'Páginas Web para Personal Trainers y Gimnasios',
        'Cómo vender asesorías online y cupos presenciales con cobros claros y prueba social',
        cards
    )

# 7. POR QUÉ TENER UNA PÁGINA WEB (MITOS)
def gen_por_que_web():
    cards = [
        {
            'num': '01',
            'title': 'Mito: "Es muy caro"',
            'badge': 'PRESUPUESTO',
            'badge_bg': '#1e293b',
            'badge_col': '#38bdf8',
            'items': [
                'Cuesta $150.000 ARS en pago único.',
                'Se paga con 1 o 2 ventas nuevas.',
                'No requiere suscripciones en dólares.',
                'Mantenimiento mensual optativo.'
            ]
        },
        {
            'num': '02',
            'title': 'Mito: "Lleva meses"',
            'badge': 'LLAVE EN MANO',
            'badge_bg': '#1e293b',
            'badge_col': '#fbbf24',
            'items': [
                'Tu web lista en 3 a 5 días hábiles.',
                'Nos mandás audios por WhatsApp.',
                'Nosotros redactamos y programamos todo.',
                'Cero dolores de cabeza técnicos.'
            ]
        },
        {
            'num': '03',
            'title': 'Mito: "Basta con IG"',
            'badge': 'DUEÑO DEL ACTIVO',
            'badge_bg': '#064e3b',
            'badge_col': '#34d399',
            'highlight': True,
            'items': [
                'El algoritmo de IG muestra tu post al 5%.',
                'En Google la gente busca para comprar ya.',
                'Tu dominio propio nadie te lo puede cerrar.',
                'Catálogo ordenado sin responder "al privado".'
            ]
        },
        {
            'num': '04',
            'title': 'Mito: "Nadie la ve"',
            'badge': 'GOOGLE MAPS',
            'badge_bg': '#1e293b',
            'badge_col': '#c084fc',
            'items': [
                'Enlazar web a Maps duplica llamadas.',
                'Aparecés en las búsquedas con IA (AEO).',
                'Genera autoridad ante clientes exigentes.',
                'Funciona como tu vendedor 24/7.'
            ]
        }
    ]
    render_4_card_infographic(
        'guia_por_que_tener_pagina_web_argentina.png',
        'DECISIÓN DIGITAL ESTRATÉGICA',
        '¿Por qué Debería Tener una Página Web en Argentina?',
        'Derribando los 4 mitos más comunes que frenan el crecimiento de negocios y profesionales',
        cards
    )

if __name__ == '__main__':
    gen_psicologos()
    gen_oficios()
    gen_contables()
    gen_estetica()
    gen_eventos()
    gen_fitness()
    gen_por_que_web()
    print('TODAS LAS INFOGRAFÍAS GENERADAS EXITOSAMENTE.')
