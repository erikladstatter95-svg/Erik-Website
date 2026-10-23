"""
Generate 14 high-quality, topic-specific infographic diagrams for Erik Website blog.
Each graphic visually represents the educational concept of the article (diagrams,
comparison matrix, workflows, cost breakdowns) with generous margins, clean typography,
and zero text overflow.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def get_fonts():
    try:
        f_badge = ImageFont.truetype('arialbd.ttf', 13)
        f_title = ImageFont.truetype('arialbd.ttf', 32)
        f_sub = ImageFont.truetype('arial.ttf', 16)
        f_card_num = ImageFont.truetype('arialbd.ttf', 15)
        f_card_title = ImageFont.truetype('arialbd.ttf', 17)
        f_card_desc = ImageFont.truetype('arial.ttf', 13)
        f_footer = ImageFont.truetype('arialbd.ttf', 12)
    except:
        f_badge = f_title = f_sub = f_card_num = f_card_title = f_card_desc = f_footer = ImageFont.load_default()
    return f_badge, f_title, f_sub, f_card_num, f_card_title, f_card_desc, f_footer

def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    return lines

def create_base_canvas(badge_text, title_text, subtitle_text):
    W, H = 1200, 675
    canvas = Image.new('RGB', (W, H), '#0a0e17')
    draw = ImageDraw.Draw(canvas)
    
    # Ambient radial glow
    for r in range(250, 0, -10):
        alpha = int(24 * (r / 250.0))
        draw.ellipse([W//2 - r*2, 160 - r, W//2 + r*2, 160 + r], fill=(16, 185, 129, alpha) if alpha > 0 else None)
    
    f_badge, f_title, f_sub, f_card_num, f_card_title, f_card_desc, f_footer = get_fonts()
    
    # Badge
    draw.rounded_rectangle([60, 40, 60 + 320, 68], radius=14, fill='#111827', outline='#10b981', width=1)
    draw.text((75, 47), f"✦ {badge_text}", fill='#34d399', font=f_badge)
    
    # Brand Top Right
    draw.rounded_rectangle([W - 240, 40, W - 60, 68], radius=14, fill='#111827', outline='#2d3748', width=1)
    draw.text((W - 220, 47), "erikwebsite.com", fill='#94a3b8', font=f_badge)
    
    # Title & Subtitle
    draw.text((60, 85), title_text, fill='#ffffff', font=f_title)
    draw.text((60, 130), subtitle_text, fill='#94a3b8', font=f_sub)
    
    # Footer brand strip
    draw.line([(60, H - 42), (W - 60, H - 42)], fill='#1f293d', width=1)
    draw.text((60, H - 32), "GUÍA OFICIAL • DESARROLLO WEB Y ESTRATEGIA DIGITAL", fill='#64748b', font=f_footer)
    draw.text((W - 320, H - 32), "DISEÑADO POR ERIK LADSTATTER", fill='#64748b', font=f_footer)
    
    return canvas, draw

def render_grid_cards(filename, badge, title, subtitle, cards, accent_color='#10b981'):
    canvas, draw = create_base_canvas(badge, title, subtitle)
    f_badge, f_title, f_sub, f_card_num, f_card_title, f_card_desc, f_footer = get_fonts()
    
    W, H = 1200, 675
    # 2x2 Grid dimensions
    start_y = 175
    card_w = 525
    card_h = 205
    col_gap = 30
    row_gap = 25
    left_x = 60
    
    positions = [
        (left_x, start_y),
        (left_x + card_w + col_gap, start_y),
        (left_x, start_y + card_h + row_gap),
        (left_x + card_w + col_gap, start_y + card_h + row_gap)
    ]
    
    for idx, (x, y) in enumerate(positions[:len(cards)]):
        c = cards[idx]
        
        # Draw card container
        draw.rounded_rectangle([x, y, x + card_w, y + card_h], radius=18, fill='#131b29', outline='#243044', width=1)
        
        # Pill for number / tag
        draw.rounded_rectangle([x + 22, y + 20, x + 22 + 100, y + 46], radius=13, fill='#0d131f', outline=accent_color, width=1)
        draw.text((x + 32, y + 25), c['tag'], fill='#38bdf8' if 'Maps' in title else '#34d399', font=f_card_num)
        
        # Card Title
        draw.text((x + 22, y + 58), c['title'], fill='#f8fafc', font=f_card_title)
        
        # Card Description wrapped
        desc_lines = wrap_text(c['desc'], f_card_desc, card_w - 44, draw)
        cur_y = y + 88
        for l in desc_lines[:4]:
            draw.text((x + 22, cur_y), l, fill='#94a3b8', font=f_card_desc)
            cur_y += 20
            
    os.makedirs('public/images', exist_ok=True)
    os.makedirs('images', exist_ok=True)
    canvas.save(f'public/images/{filename}', quality=95)
    canvas.save(f'images/{filename}', quality=95)
    print(f"Generated {filename}")

def render_comparison_columns(filename, badge, title, subtitle, col_left, col_right):
    canvas, draw = create_base_canvas(badge, title, subtitle)
    f_badge, f_title, f_sub, f_card_num, f_card_title, f_card_desc, f_footer = get_fonts()
    
    start_y = 175
    col_w = 525
    col_h = 430
    left_x = 60
    right_x = left_x + col_w + 30
    
    # Left Column (Negative / Traditional)
    draw.rounded_rectangle([left_x, start_y, left_x + col_w, start_y + col_h], radius=20, fill='#14171f', outline='#3b1d24', width=1)
    draw.rounded_rectangle([left_x + 24, start_y + 22, left_x + 180, start_y + 52], radius=14, fill='#2a1218', outline='#f43f5e', width=1)
    draw.text((left_x + 36, start_y + 28), col_left['tag'], fill='#fb7185', font=f_card_num)
    draw.text((left_x + 24, start_y + 66), col_left['title'], fill='#ffffff', font=f_card_title)
    
    ly = start_y + 110
    for pt in col_left['points']:
        draw.text((left_x + 24, ly), "✕", fill='#f43f5e', font=f_card_title)
        lines = wrap_text(pt, f_card_desc, col_w - 70, draw)
        for l in lines:
            draw.text((left_x + 48, ly), l, fill='#cbd5e1', font=f_card_desc)
            ly += 20
        ly += 16
        
    # Right Column (Positive / Modern Web)
    draw.rounded_rectangle([right_x, start_y, right_x + col_w, start_y + col_h], radius=20, fill='#111c26', outline='#065f46', width=2)
    draw.rounded_rectangle([right_x + 24, start_y + 22, right_x + 210, start_y + 52], radius=14, fill='#064e3b', outline='#10b981', width=1)
    draw.text((right_x + 36, start_y + 28), col_right['tag'], fill='#34d399', font=f_card_num)
    draw.text((right_x + 24, start_y + 66), col_right['title'], fill='#ffffff', font=f_card_title)
    
    ry = start_y + 110
    for pt in col_right['points']:
        draw.text((right_x + 24, ry), "✓", fill='#10b981', font=f_card_title)
        lines = wrap_text(pt, f_card_desc, col_w - 70, draw)
        for l in lines:
            draw.text((right_x + 48, ry), l, fill='#e2e8f0', font=f_card_desc)
            ry += 20
        ry += 16

    os.makedirs('public/images', exist_ok=True)
    os.makedirs('images', exist_ok=True)
    canvas.save(f'public/images/{filename}', quality=95)
    canvas.save(f'images/{filename}', quality=95)
    print(f"Generated {filename}")

# ==============================================================================
# 1. ABOGADOS: Diagrama de Confianza y Captación Legal
# ==============================================================================
render_grid_cards(
    filename='guia_web_abogados_argentina.png',
    badge='SECTOR JURÍDICO & ESTUDIOS LEGALES',
    title='ESTUDIO JURÍDICO DIGITAL: 4 CLAVES DE CONFIANZA',
    subtitle='Estándares esenciales para captar clientes legales reales en Argentina',
    cards=[
        {'tag': '01 • MATRÍCULA', 'title': 'Autoridad y Colegiación Visible', 'desc': 'Exhibir Colegio de Abogados, Tomo y Folio de los profesionales. En litigios y despidos, la matrícula visible despeja desconfianza de inmediato.'},
        {'tag': '02 • ÁREAS', 'title': 'Especialidades Separadas', 'desc': 'Bloques dedicados a Laboral (Despidos/ART), Familia y Sucesiones. Permite posicionar búsquedas locales puntuales en Google.'},
        {'tag': '03 • HERRAMIENTAS', 'title': 'Calculadora de Indemnización', 'desc': 'Filtro interactivo para que el usuario calcule una estimación previa antes de contactar, atrayendo casos calificados.'},
        {'tag': '04 • ATENCIÓN', 'title': 'WhatsApp Directo y Confidencial', 'desc': 'Enlace directo con mensaje prearmado para que el cliente consulte en privado en menos de 10 segundos desde su celular.'}
    ]
)

# ==============================================================================
# 2. PSICÓLOGOS: Ecosistema de Atención y Pacientes
# ==============================================================================
render_grid_cards(
    filename='guia_web_psicologos_argentina.png',
    badge='SALUD MENTAL & PSICOLOGÍA',
    title='CONSULTORIO PSICOLÓGICO: ECOSISTEMA DIGITAL',
    subtitle='Estructura probada para captar pacientes particulares online y presencial',
    cards=[
        {'tag': '01 • ENFOQUE', 'title': 'Corriente Terapéutica Clara', 'desc': 'Explicar de forma sencilla tu enfoque (TCC, Psicoanálisis, Sistémica) y tu formación profesional matriculada.'},
        {'tag': '02 • MODALIDAD', 'title': 'Atención Dual (Online y Presencial)', 'desc': 'Separar con claridad sesiones por videollamada para todo el país y turnos presenciales en consultorio con mapa.'},
        {'tag': '03 • ARANCELES', 'title': 'Honorarios Transparentes', 'desc': 'Informar el valor de la sesión particular y reintegros de prepagas para filtrar pacientes decididos a comprometerse.'},
        {'tag': '04 • AGILIDAD', 'title': 'Canal Seguro de WhatsApp', 'desc': 'El paciente consulta de forma discreta sin formularios pesados que generen abandono en el primer contacto.'}
    ]
)

# ==============================================================================
# 3. TURNOS CONSULTORIO: Comparativa Operativa
# ==============================================================================
render_comparison_columns(
    filename='automatizar_turnos_consultorio_argentina.png',
    badge='GESTIÓN MÉDICA & ODONTOLÓGICA',
    title='GESTIÓN DE TURNOS: TRADICIONAL VS. WEB ÁGIL',
    subtitle='Comparativa operativa para consultorios médicos y clínicas en Argentina',
    col_left={
        'tag': 'SISTEMA TRADICIONAL',
        'title': 'Recepción Saturada y Pérdida de Pacientes',
        'points': [
            'Teléfono sonando sin parar: la secretaria repite "¿qué obra social?", "¿horarios?" y "¿cuánto sale?".',
            'Softwares pesados con cuotas en dólares y apps que exigen registro que el paciente mayor no usa.',
            'Alto ausentismo: turnos dados a mano sin recordatorios ágiles dejan sillones vacíos en el consultorio.',
            'Cero presencia en Google: pacientes que buscan especialistas en la zona terminan llamando a la competencia.'
        ]
    },
    col_right={
        'tag': 'WEB ÁGIL + WHATSAPP',
        'title': 'Agenda Ordenada y Consultas Filtradas',
        'points': [
            'Web médica ultrarrápida donde el paciente revisa especialidades, aranceles e indicaciones en 1 minuto.',
            'Botón de WhatsApp con mensaje prearmado que incluye nombre, cobertura y motivo de consulta.',
            'Cero abonos abusivos en dólares: un único setup accesible sin comisiones por turno gestionado.',
            'Posicionamiento en Google Maps para captar pacientes de tu barrio cuando buscan dentista o médico.'
        ]
    }
)

# ==============================================================================
# 4. GOOGLE MAPS: Ranking Factors Local 3-Pack
# ==============================================================================
render_grid_cards(
    filename='guia_posicionar_google_maps_argentina.png',
    badge='LOCAL SEO & GOOGLE MAPS 2026',
    title='LOS 4 PILARES PARA DOMINAR EL LOCAL 3-PACK',
    subtitle='Cómo aparecer en el mapa de Google en tu ciudad sin pagar publicidad',
    cards=[
        {'tag': '35% RELEVANCIA', 'title': 'Categoría Primaria Exacta', 'desc': 'Elegir la categoría específica de negocio en Google Business (ej. Fontanero, Dentista, Abogado laboralista) sin relleno de palabras clave.'},
        {'tag': '25% AUTORIDAD', 'title': 'Página Web Oficial Vinculada', 'desc': 'Las fichas que enlazan a un sitio web propio reciben 2.5 veces más clics y Google las prioriza frente a perfiles sin web.'},
        {'tag': '20% PROXIMIDAD', 'title': 'Área de Cobertura Precisa', 'desc': 'Configurar con exactitud el municipio, departamento o barrios de atención si prestás servicios a domicilio sin local abierto.'},
        {'tag': '20% REPUTACIÓN', 'title': 'Reseñas Reales con Respuesta', 'desc': 'Acumular entre 15 y 30 reseñas con texto y responder cada una mencionando la ciudad y el servicio brindado.'}
    ],
    accent_color='#38bdf8'
)

# ==============================================================================
# 5. WEB VS INSTAGRAM: Matriz Estratégica
# ==============================================================================
render_comparison_columns(
    filename='comparativa_web_vs_instagram.png',
    badge='ESTRATEGIA DIGITAL 2026',
    title='PÁGINA WEB VS. INSTAGRAM: ¿DÓNDE INVERTIR?',
    subtitle='Comparativa de rendimiento comercial para negocios y profesionales',
    col_left={
        'tag': 'INSTAGRAM (CANAL DE OCIO)',
        'title': 'Esfuerzo Diario con Alcance en Caída',
        'points': [
            'El usuario entra a distraerse, no a contratar un servicio con dinero en mano.',
            'Alcance orgánico inferior al 5%: si no pagás anuncios diarios, tus publicaciones no se ven.',
            'Pérdida de horas respondiendo 40 mensajes de "¿precio por privado?" para cerrar 1 sola venta.',
            'Terreno alquilado: si Meta sanciona o deshabilita tu cuenta, perdés todo tu historial de clientes.'
        ]
    },
    col_right={
        'tag': 'PÁGINA WEB (CANAL DE COMPRA)',
        'title': 'Tráfico con Intención Activa 24/7',
        'points': [
            'El usuario que busca en Google Maps tiene una necesidad real y busca contratar ya mismo.',
            'Información ordenada: tarifas, ubicación, portfolio y coberturas visibles sin tener que preguntar.',
            'Contacto calificado directo a WhatsApp: ahorrás tiempo y atendés consultas listas para cerrar.',
            'Activo 100% propio: tu dominio oficial y tu web son tuyos y nadie te los puede apagar.'
        ]
    }
)

# ==============================================================================
# 6. DESGLOSE DE COSTOS: Precios Web Argentina
# ==============================================================================
render_grid_cards(
    filename='desglose_costos_web_argentina.png',
    badge='FINANZAS & PRESUPUESTOS 2026',
    title='ESTRUCTURA REAL DE COSTOS DE UNA WEB',
    subtitle='Desglose transparente de lo que cuesta crear y mantener tu sitio en Argentina',
    cards=[
        {'tag': '01 • DOMINIO', 'title': 'Dominio Oficial .com.ar / .com', 'desc': 'Registro anual a nombre de tu negocio en NIC Argentina ($10.000 a $25.000 ARS/año). Da identidad profesional y protege tu marca.'},
        {'tag': '02 • HOSTING', 'title': 'Hosting Cloud de Alta Velocidad', 'desc': 'Servidor ultrarrápido con certificado de seguridad SSL. Abre en celulares en menos de 1 segundo sin caídas ni lentitud.'},
        {'tag': '03 • SETUP', 'title': 'Diseño y Programación Inicial', 'desc': 'Tarifa fija en Erik Website ($150.000 ARS). Incluye diseño a medida, redacción comercial y optimización de Google Maps.'},
        {'tag': '04 • SOPORTE', 'title': 'Mantenimiento y Actualizaciones', 'desc': '$20.000 ARS/mes con primer mes 100% gratis. Incluye hosting, renovación y hasta 3 cambios mensuales de precios y fotos.'}
    ]
)

# ==============================================================================
# 7. COMPARATIVA DE PRECIOS: Opciones del Mercado
# ==============================================================================
render_grid_cards(
    filename='comparativa_precios_web_argentina.png',
    badge='COMPARATIVA DE MERCADO 2026',
    title='OPCIONES DE DESARROLLO WEB EN ARGENTINA',
    subtitle='Diferencias de costos, tiempos de entrega y calidad de servicio',
    cards=[
        {'tag': '$50K - $90K', 'title': 'Freelance Novato / Estudiante', 'desc': 'Precios bajos pero altos riesgos: demoras de meses, plantillas lentas de WordPress y abandono sin soporte cuando surgen errores.'},
        {'tag': '$150.000 ARS', 'title': 'Erik Website (Plan Pro Todo Resuelto)', 'desc': 'Calidad de agencia a costo freelance: entrega en 3 a 5 días, redacción de textos incluida, soporte mensual y sin costos ocultos.'},
        {'tag': '$400K - $1.2M', 'title': 'Agencia Tradicional de Publicidad', 'desc': 'Costos corporativos con meses de reuniones y presupuestos en dólares inaccesibles para comercios y profesionales independientes.'},
        {'tag': 'CREADORES DIY', 'title': 'Plataformas Tipo Wix o Tiendanube', 'desc': 'Cobros mensuales continuos en dólares, plantillas pesadas difíciles de personalizar y sin redacción profesional de contenidos.'}
    ]
)

# ==============================================================================
# 8. QUE NEGOCIOS NECESITAN WEB: Matriz de Prioridad
# ==============================================================================
render_grid_cards(
    filename='que_negocios_necesitan_pagina_web.png',
    badge='DIAGNÓSTICO COMERCIAL',
    title='MATRIZ DE PRIORIDAD: ¿QUIÉN NECESITA UNA WEB?',
    subtitle='Nivel de urgencia e impacto en facturación según tu actividad en Argentina',
    cards=[
        {'tag': 'URGENCIA CRÍTICA', 'title': 'Oficios y Reparaciones Rápidas', 'desc': 'Plomeros, electricistas, cerrajeros y auxilio mecánico. Nadie busca en redes cuando se inunda el baño: buscan en Google y llaman al 1º.'},
        {'tag': 'ALTA CONFIANZA', 'title': 'Servicios Profesionales y Salud', 'desc': 'Abogados, médicos, dentistas, psicólogos y contadores. Exigen validación de matrícula, trayectoria y tarifas claras antes de contratar.'},
        {'tag': 'PRESENCIA LOCAL', 'title': 'Comercios con Atención al Público', 'desc': 'Centros de estética, salones de fiestas, catering y gimnasios. Dependen de Google Maps para atraer vecinos de su zona.'},
        {'tag': 'NO PRIORITARIO', 'title': 'Ventas Informales o Entretenimiento', 'desc': 'Creadores de contenido de ocio o venta casual a familiares donde alcanza con redes sociales y no se justifica inversión.'}
    ]
)

# ==============================================================================
# 9. OFICIOS Y SERVICIOS DEL HOGAR: Funnel de Urgencia
# ==============================================================================
render_grid_cards(
    filename='guia_web_oficios_hogar_argentina.png',
    badge='OFICIOS & URGENCIAS DEL HOGAR',
    title='OFICIOS Y REPARACIONES: RUTA DE CONVERSIÓN',
    subtitle='Cómo plomeros, cerrajeros y técnicos captan emergencias domésticas',
    cards=[
        {'tag': '01 • GOOGLE MAPS', 'title': 'Posicionamiento por Cercanía', 'desc': 'Aparecer en las búsquedas urgentes como "plomero 24 horas cerca de mí" en tu municipio o departamento.'},
        {'tag': '02 • BOTÓN RÁPIDO', 'title': 'Llamada y WhatsApp en 1 Clic', 'desc': 'El cliente que tiene una fuga de gas o cerradura trabada necesita llamar de inmediato sin leer textos largos.'},
        {'tag': '03 • COBERTURA', 'title': 'Zona de Atención y Tiempos', 'desc': 'Indicar claramente los barrios que cubrís y el tiempo estimado de llegada para generar tranquilidad y cerrar el servicio.'},
        {'tag': '04 • MATRÍCULA', 'title': 'Matrícula y Presupuesto Base', 'desc': 'Aclarar si sos matriculado y el costo de visita o guardia para evitar malentendidos y filtrar clientes curiosos.'}
    ]
)

# ==============================================================================
# 10. ESTUDIOS CONTABLES: Captación de PyMEs
# ==============================================================================
render_grid_cards(
    filename='guia_web_estudios_contables_argentina.png',
    badge='CONTABILIDAD & ASESORÍA FISCAL',
    title='ESTUDIOS CONTABLES: CAPTACIÓN DE EMPRESAS',
    subtitle='Estructura digital para sumar abonos mensuales recurrentes de PyMEs',
    cards=[
        {'tag': '01 • MATRÍCULA', 'title': 'Matrícula CPCE y Respaldo Legal', 'desc': 'Mostrar la firma de contadores públicos matriculados para transmitir solvencia técnica frente a requerimientos de AFIP.'},
        {'tag': '02 • SERVICIOS', 'title': 'Planes Claros según Tamaño', 'desc': 'Separar servicios para Monotributistas, Responsables Inscriptos y PyMEs comerciales con liquidación de sueldos e IVA.'},
        {'tag': '03 • DIAGNÓSTICO', 'title': 'Formulario Breve de Contacto', 'desc': 'El cliente detalla rubro y volumen de facturación para recibir un presupuesto mensual personalizado en 24 horas.'},
        {'tag': '04 • LENGUAJE', 'title': 'Comunicación Sin Jerga Compleja', 'desc': 'Explicar los beneficios impositivos de forma simple para que el comerciante entienda el ahorro real que le generás.'}
    ]
)

# ==============================================================================
# 11. ESTÉTICA Y SALONES: Ciclo de Reserva
# ==============================================================================
render_grid_cards(
    filename='guia_web_estetica_salones_argentina.png',
    badge='BELLEZA & CENTROS DE ESTÉTICA',
    title='CENTROS DE ESTÉTICA: CICLO DE RESERVA DIGITAL',
    subtitle='Cómo multiplicar turnos de tratamientos sin pagar comisiones de apps',
    cards=[
        {'tag': '01 • RESULTADOS', 'title': 'Galería Antes y Después Real', 'desc': 'Fotografías de alta definición de tratamientos faciales, depilación láser y lifting de pestañas realizados en tu salón.'},
        {'tag': '02 • CATÁLOGO', 'title': 'Lista de Precios y Sesiones', 'desc': 'Detalle de servicios con número de sesiones sugeridas para que la clienta consulte convencida del presupuesto.'},
        {'tag': '03 • RESERVAS', 'title': 'Turnos Directos sin Fricción', 'desc': 'El botón de WhatsApp conecta directo con la recepcionista con el tratamiento ya seleccionado por la clienta.'},
        {'tag': '04 • UBICACIÓN', 'title': 'Ubicación y Ficha Google Maps', 'desc': 'Mapa interactivo para que encuentren tu local con facilidad y lean testimonios de clientas satisfechas.'}
    ]
)

# ==============================================================================
# 12. SALONES DE FIESTAS: Conversión de Eventos
# ==============================================================================
render_grid_cards(
    filename='guia_web_salones_eventos_argentina.png',
    badge='EVENTOS, QUINTAS & CATERING',
    title='SALONES Y CATERING: CONVERSIÓN DE EVENTOS',
    subtitle='Cómo cerrar visitas y contrataciones con un sitio web vendedor',
    cards=[
        {'tag': '01 • ESPACIO', 'title': 'Galería de Fotos del Predio', 'desc': 'Fotos de pista, parque, iluminación y ambientación nocturna. El cliente contrata cuando puede imaginarse su fiesta.'},
        {'tag': '02 • COTIZADOR', 'title': 'Calculadora de Invitados', 'desc': 'Herramienta ágil para que los novios o cumpleañeros calculen un presupuesto estimado según la cantidad de personas.'},
        {'tag': '03 • MENÚS', 'title': 'Propuesta de Catering y Barras', 'desc': 'Opciones gastronómicas (finger food, cena formal, barra libre) detalladas para despejar preguntas repetitivas.'},
        {'tag': '04 • VISITAS', 'title': 'Coordinación de Visita al Salón', 'desc': 'Llamado a la acción claro para coordinar una cita presencial y señar la fecha de alquiler del evento.'}
    ]
)

# ==============================================================================
# 13. PERSONAL TRAINERS: Monetización Fitness
# ==============================================================================
render_grid_cards(
    filename='guia_web_personal_trainers_argentina.png',
    badge='FITNESS & PERSONAL TRAINERS',
    title='PERSONAL TRAINERS: MONETIZACIÓN ONLINE',
    subtitle='Cómo vender rutinas y asesorías personalizadas en toda Argentina',
    cards=[
        {'tag': '01 • ASESORÍAS', 'title': 'Planes 1 a 1 Personalizados', 'desc': 'Venta de cupos limitados para seguimiento individual con videollamada, control semanal y ajustes de rutina.'},
        {'tag': '02 • ESCALABILIDAD', 'title': 'Infoproductos y Rutinas en PDF', 'desc': 'Venta masiva de guías de hipertrofia o descenso de peso descargables para generar ingresos automáticos.'},
        {'tag': '03 • AUTORIDAD', 'title': 'Prueba Social y Cambios Físicos', 'desc': 'Fotos de transformaciones reales de alumnos que validan tu método de entrenamiento y derriban dudas.'},
        {'tag': '04 • COBROS', 'title': 'Cobros Simples con Mercado Pago', 'desc': 'Enlaces de suscripción mensual directa para no perder tiempo persiguiendo transferencias a fin de mes.'}
    ]
)

# ==============================================================================
# 14. POR QUÉ TENER WEB: Derribando 4 Mitos
# ==============================================================================
render_grid_cards(
    filename='guia_por_que_tener_pagina_web_argentina.png',
    badge='DIGITALIZACIÓN COMERCIAL 2026',
    title='¿POR QUÉ TENER PÁGINA WEB? 4 MITOS DERRIBADOS',
    subtitle='La verdad del mercado digital para comercios y profesionales en Argentina',
    cards=[
        {'tag': 'MITO 1: "ES CARO"', 'title': 'Inversión Accesible y Retorno Rápido', 'desc': 'Por $150.000 ARS tenés tu web lista. Con solo conseguir 2 o 3 clientes nuevos recuperás el 100% de la inversión.'},
        {'tag': 'MITO 2: "INSTAGRAM ALCANZA"', 'title': 'En Redes se Mira, en Google se Compra', 'desc': 'Las redes sirven para llamar la atención; la web es donde la persona confirma precios, dirección y cierra la contratación.'},
        {'tag': 'MITO 3: "NO TENGO TIEMPO"', 'title': 'Cero Redacción de tu Parte', 'desc': 'Nosotros armamos todo a partir de un par de audios de WhatsApp contándonos qué hacés. No tenés que escribir nada.'},
        {'tag': 'MITO 4: "ES MUY COMPLEJO"', 'title': 'Todo Resuelto de Punta a Punta', 'desc': 'Dominio, servidores cloud, diseño para celulares y conexión a WhatsApp resueltos en 3 a 5 días hábiles.'}
    ]
)

print("All 14 topic-specific infographics successfully generated!")
