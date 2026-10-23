"""
Generate all visual mockups for Erik Website blog articles.
Replaces text-dense infographics with sleek, Apple-style browser hardware mockups
showing the live demo / interface for each sector.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def make_mockup(bg_img_path, title_badge, url_path, output_filename, subtitle='Demo en Vivo • 100% Mobile Ready'):
    W, H = 1200, 750
    canvas = Image.new('RGB', (W, H), '#0b0f17')
    draw = ImageDraw.Draw(canvas)
    
    # Ambient soft emerald / cyan glow in background
    for r in range(260, 0, -8):
        alpha = int(28 * (r / 260.0))
        draw.ellipse([W//2 - r*2, 220 - r, W//2 + r*2, 220 + r], fill=(16, 185, 129, alpha) if alpha > 0 else None)
    
    # Browser window dimensions
    bw_w = 1060
    bw_h = 570
    bw_x = (W - bw_w) // 2
    bw_y = 85
    
    # Draw soft drop shadow behind window
    shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shadow)
    sdraw.rounded_rectangle([bw_x - 8, bw_y + 8, bw_x + bw_w + 8, bw_y + bw_h + 24], radius=24, fill=(0, 0, 0, 180))
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))
    canvas.paste(shadow, (0, 0), shadow)
    
    # Draw browser frame header
    hbar_h = 44
    draw.rounded_rectangle([bw_x, bw_y, bw_x + bw_w, bw_y + bw_h], radius=18, fill='#1b222d', outline='#2d3748', width=1)
    
    # Window traffic light dots (macOS style)
    draw.ellipse([bw_x + 20, bw_y + 16, bw_x + 32, bw_y + 28], fill='#ff5f56')
    draw.ellipse([bw_x + 40, bw_y + 16, bw_x + 52, bw_y + 28], fill='#ffbd2e')
    draw.ellipse([bw_x + 60, bw_y + 16, bw_x + 72, bw_y + 28], fill='#27c93f')
    
    # URL bar in center
    url_w = 480
    url_x = bw_x + (bw_w - url_w) // 2
    draw.rounded_rectangle([url_x, bw_y + 9, url_x + url_w, bw_y + 35], radius=13, fill='#10151d', outline='#242e3d', width=1)
    
    try:
        font_url = ImageFont.truetype('arial.ttf', 13)
        font_badge = ImageFont.truetype('arialbd.ttf', 13)
        font_sub = ImageFont.truetype('arial.ttf', 12)
        font_brand = ImageFont.truetype('arialbd.ttf', 13)
    except:
        font_url = font_badge = font_sub = font_brand = ImageFont.load_default()
        
    draw.text((url_x + 18, bw_y + 14), f'🔒  {url_path}', fill='#7c8ba1', font=font_url)
    
    # Window content area
    content_y = bw_y + hbar_h
    content_h = bw_h - hbar_h
    
    if os.path.exists(bg_img_path):
        preview = Image.open(bg_img_path).convert('RGB')
        pw, ph = preview.size
        target_ratio = bw_w / float(content_h)
        current_ratio = pw / float(ph)
        
        if current_ratio > target_ratio:
            new_w = int(ph * target_ratio)
            preview = preview.crop(((pw - new_w)//2, 0, (pw + new_w)//2, ph))
        else:
            new_h = int(pw / target_ratio)
            preview = preview.crop((0, 0, pw, new_h))
            
        preview = preview.resize((bw_w, content_h), Image.Resampling.LANCZOS)
        canvas.paste(preview, (bw_x, content_y))
    else:
        # Fallback dark surface with clean grid
        draw.rectangle([bw_x, content_y, bw_x + bw_w, content_y + content_h], fill='#131922')
    
    # Re-draw outline around window
    draw.rounded_rectangle([bw_x, bw_y, bw_x + bw_w, bw_y + bw_h], radius=18, outline='#3b4759', width=1)
    
    # Top sector pill badge
    draw.rounded_rectangle([bw_x, 26, bw_x + 360, 62], radius=18, fill='#111827', outline='#10b981', width=1)
    draw.text((bw_x + 20, 36), f'✨ {title_badge}', fill='#34d399', font=font_badge)
    
    # Watermark brand pill top right
    wm_w = 230
    wm_x = bw_x + bw_w - wm_w
    draw.rounded_rectangle([wm_x, 26, wm_x + wm_w, 62], radius=18, fill='#111827', outline='#2d3748', width=1)
    draw.text((wm_x + 18, 36), 'erikwebsite.com', fill='#e2e8f0', font=font_brand)
    
    # Bottom floating pill
    fp_w = 420
    fp_h = 44
    fp_x = bw_x + bw_w - fp_w
    fp_y = bw_y + bw_h + 16
    draw.rounded_rectangle([fp_x, fp_y, fp_x + fp_w, fp_y + fp_h], radius=22, fill='#151c27', outline='#2b3545', width=1)
    draw.text((fp_x + 22, fp_y + 14), f'⚡ {subtitle}', fill='#94a3b8', font=font_sub)
    
    os.makedirs('public/images', exist_ok=True)
    os.makedirs('images', exist_ok=True)
    canvas.save(f'public/images/{output_filename}', quality=95)
    canvas.save(f'images/{output_filename}', quality=95)
    print(f'OK Generated: {output_filename}')

mockups = [
    ('public/images/og_abogados.jpg', 'SECTOR JURÍDICO & ABOGADOS', 'erikwebsite.com/demos/abogados/', 'guia_web_abogados_argentina.png', 'Demo en Vivo • Calculadora de Despido + WhatsApp'),
    ('public/images/og_psicologia.jpg', 'SALUD MENTAL & PSICOLOGÍA', 'erikwebsite.com/demos/psicologia/', 'guia_web_psicologos_argentina.png', 'Demo en Vivo • Turnos Online y Pacientes Particulares'),
    ('public/images/og_odontologia.jpg', 'CONSULTORIOS & ODONTOLOGÍA', 'erikwebsite.com/demos/odontologia/', 'automatizar_turnos_consultorio_argentina.png', 'Demo en Vivo • Automatización de Turnos sin Cuotas en USD'),
    ('public/images/og_estetica.jpg', 'BELLEZA & CENTROS DE ESTÉTICA', 'erikwebsite.com/demos/estetica/', 'guia_web_estetica_salones_argentina.png', 'Demo en Vivo • Galería Antes/Después y Reservas'),
    ('public/images/og_fitness.jpg', 'FITNESS & PERSONAL TRAINERS', 'erikwebsite.com/demos/fitness/', 'guia_web_personal_trainers_argentina.png', 'Demo en Vivo • Venta de Asesorías y Rutinas Online'),
    ('public/images/og_urgencias.jpg', 'OFICIOS & URGENCIAS DEL HOGAR', 'erikwebsite.com/demos/urgencias-hogar/', 'guia_web_oficios_hogar_argentina.png', 'Demo en Vivo • Botón de Urgencia 24hs y Google Maps'),
    ('public/images/og_contable.jpg', 'ESTUDIOS CONTABLES & FINANZAS', 'erikwebsite.com/demos/contable/', 'guia_web_estudios_contables_argentina.png', 'Demo en Vivo • Diagnóstico Fiscal y Captación PyME'),
    ('public/images/og_salones.jpg', 'SALONES DE EVENTOS & FIESTAS', 'erikwebsite.com/demos/salones/', 'guia_web_salones_eventos_argentina.png', 'Demo en Vivo • Recorrido Virtual y Cotizador Rápido'),
    ('public/images/og_main.jpg', 'NEGOCIOS & PYMES EN ARGENTINA', 'erikwebsite.com/#demos', 'que_negocios_necesitan_pagina_web.png', 'Demo en Vivo • Adaptada a Celulares y Carga en 0.8s'),
    ('public/images/og_main.jpg', 'DIGITALIZACIÓN & CONVERSIÓN', 'erikwebsite.com', 'guia_por_que_tener_pagina_web_argentina.png', 'Ecosistema Completo • Web Propia + WhatsApp'),
    ('public/images/og_urgencias.jpg', 'GOOGLE MAPS & LOCAL 3-PACK', 'maps.google.com/?q=servicios+profesionales', 'guia_posicionar_google_maps_argentina.png', 'Local SEO 2026 • Primeros Puestos Sin Pagar Publicidad'),
    ('public/images/og_main.jpg', 'PRECIOS CLAROS Y TRANSPARENTES', 'erikwebsite.com/#precios', 'desglose_costos_web_argentina.png', 'Tarifa Plana $150.000 ARS • Sin Letra Chica'),
    ('public/images/og_main.jpg', 'COMPARATIVA DE PRESUPUESTOS', 'erikwebsite.com/#precios', 'comparativa_precios_web_argentina.png', 'Tarifas 2026 • Calidad Agencia a Costo Freelance'),
    ('public/images/og_main.jpg', 'CANALES DIGITALES: WEB VS IG', 'erikwebsite.com', 'comparativa_web_vs_instagram.png', 'Estrategia Digital • De Seguidores a Clientes Reales')
]

for bg, badge, url, out, sub in mockups:
    make_mockup(bg, badge, url, out, sub)
