"""
Download authentic, high-resolution representative editorial photos for each blog article.
Add a subtle erikwebsite.com watermark and category tag pill.
Zero paragraphs of text. 100% representative photography as requested.
"""
import urllib.request
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

photo_configs = [
    {
        'filename': 'guia_web_abogados_argentina.png',
        'url': 'https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=1200&q=80',
        'badge': 'SECTOR JURÍDICO & ABOGADOS',
        'caption': 'Estudios legales y ejercicio del derecho profesional'
    },
    {
        'filename': 'guia_web_psicologos_argentina.png',
        'url': 'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&fit=crop&w=1200&q=80',
        'badge': 'SALUD MENTAL & PSICOLOGÍA',
        'caption': 'Atención psicológica y consulta terapéutica'
    },
    {
        'filename': 'automatizar_turnos_consultorio_argentina.png',
        'url': 'https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=1200&q=80',
        'badge': 'GESTIÓN DE CONSULTORIOS & ODONTOLOGÍA',
        'caption': 'Atención médica y asignación ágil de turnos'
    },
    {
        'filename': 'guia_web_estetica_salones_argentina.png',
        'url': 'https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=1200&q=80',
        'badge': 'BELLEZA & CENTROS DE ESTÉTICA',
        'caption': 'Tratamientos faciales y corporales profesionales'
    },
    {
        'filename': 'guia_web_personal_trainers_argentina.png',
        'url': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?auto=format&fit=crop&w=1200&q=80',
        'badge': 'FITNESS & PERSONAL TRAINERS',
        'caption': 'Entrenamiento personalizado y asesoría deportiva'
    },
    {
        'filename': 'guia_web_oficios_hogar_argentina.png',
        'url': 'https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=1200&q=80',
        'badge': 'OFICIOS & URGENCIAS DEL HOGAR',
        'caption': 'Servicios técnicos y reparaciones especializadas'
    },
    {
        'filename': 'guia_web_estudios_contables_argentina.png',
        'url': 'https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=1200&q=80',
        'badge': 'ESTUDIOS CONTABLES & FINANZAS',
        'caption': 'Asesoría contable y planificación fiscal para empresas'
    },
    {
        'filename': 'guia_web_salones_eventos_argentina.png',
        'url': 'https://images.unsplash.com/photo-1519167758481-83f550bb49b3?auto=format&fit=crop&w=1200&q=80',
        'badge': 'EVENTOS, SALONES & CATERING',
        'caption': 'Salones de fiestas y servicios para recepciones'
    },
    {
        'filename': 'guia_posicionar_google_maps_argentina.png',
        'url': 'https://images.unsplash.com/photo-1569336415962-a4bd9f69cd83?auto=format&fit=crop&w=1200&q=80',
        'badge': 'LOCAL SEO & GOOGLE MAPS',
        'caption': 'Búsqueda de comercios y servicios locales en mapa'
    },
    {
        'filename': 'comparativa_web_vs_instagram.png',
        'url': 'https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&w=1200&q=80',
        'badge': 'ESTRATEGIA DIGITAL: WEB VS IG',
        'caption': 'Canales de captación y conversión digital'
    },
    {
        'filename': 'que_negocios_necesitan_pagina_web.png',
        'url': 'https://images.unsplash.com/photo-1556740758-90de374c12ad?auto=format&fit=crop&w=1200&q=80',
        'badge': 'COMERCIOS & PYMES EN ARGENTINA',
        'caption': 'Presencia digital para negocios y profesionales'
    },
    {
        'filename': 'desglose_costos_web_argentina.png',
        'url': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1200&q=80',
        'badge': 'PRESUPUESTOS Y COSTOS WEB',
        'caption': 'Inversión, hosting y desarrollo profesional'
    },
    {
        'filename': 'comparativa_precios_web_argentina.png',
        'url': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1200&q=80',
        'badge': 'COMPARATIVA DE MERCADO 2026',
        'caption': 'Opciones y presupuestos de desarrollo web'
    },
    {
        'filename': 'guia_por_que_tener_pagina_web_argentina.png',
        'url': 'https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=1200&q=80',
        'badge': 'DIGITALIZACIÓN & CONVERSIÓN',
        'caption': 'Crecimiento comercial y captación de clientes'
    }
]

os.makedirs('temp_dl', exist_ok=True)
os.makedirs('public/images', exist_ok=True)
os.makedirs('images', exist_ok=True)

try:
    font_badge = ImageFont.truetype('arialbd.ttf', 13)
    font_watermark = ImageFont.truetype('arialbd.ttf', 14)
except:
    font_badge = font_watermark = ImageFont.load_default()

TARGET_W, TARGET_H = 1200, 675

for item in photo_configs:
    filename = item['filename']
    temp_path = os.path.join('temp_dl', filename.replace('.png', '.jpg'))
    
    print(f"Downloading {filename}...")
    try:
        req = urllib.request.Request(item['url'], headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp, open(temp_path, 'wb') as out_f:
            out_f.write(resp.read())
            
        img = Image.open(temp_path).convert('RGB')
        
        # Center-crop to exact 16:9 (1200 x 675)
        w, h = img.size
        target_ratio = TARGET_W / float(TARGET_H)
        curr_ratio = w / float(h)
        
        if curr_ratio > target_ratio:
            new_w = int(h * target_ratio)
            img = img.crop(((w - new_w) // 2, 0, (w + new_w) // 2, h))
        else:
            new_h = int(w / target_ratio)
            img = img.crop((0, (h - new_h) // 2, w, (h + new_h) // 2))
            
        img = img.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
        
        # Overlay subtle dark gradient at bottom and top for elegance
        overlay = Image.new('RGBA', (TARGET_W, TARGET_H), (0, 0, 0, 0))
        odraw = ImageDraw.Draw(overlay)
        
        # Top gradient for badge legibility
        for y in range(90):
            a = int(140 * (1.0 - (y / 90.0)))
            odraw.line([(0, y), (TARGET_W, y)], fill=(0, 0, 0, a))
            
        # Bottom gradient for watermark legibility
        for y in range(TARGET_H - 80, TARGET_H):
            prog = (y - (TARGET_H - 80)) / 80.0
            a = int(160 * prog)
            odraw.line([(0, y), (TARGET_W, y)], fill=(0, 0, 0, a))
            
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
        draw = ImageDraw.Draw(img)
        
        # Draw category pill top-left
        badge_text = f"✦ {item['badge']}"
        bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
        bw = (bbox[2] - bbox[0]) + 32
        bh = 34
        draw.rounded_rectangle([32, 28, 32 + bw, 28 + bh], radius=12, fill='#0f172a', outline='#334155', width=1)
        draw.text((48, 36), badge_text, fill='#38bdf8' if 'Maps' in filename else '#34d399', font=font_badge)
        
        # Draw watermark bottom-right
        wm_text = "erikwebsite.com"
        wm_bbox = draw.textbbox((0, 0), wm_text, font=font_watermark)
        wm_w = (wm_bbox[2] - wm_bbox[0]) + 30
        wm_h = 34
        wm_x = TARGET_W - wm_w - 32
        wm_y = TARGET_H - wm_h - 24
        draw.rounded_rectangle([wm_x, wm_y, wm_x + wm_w, wm_y + wm_h], radius=12, fill='#0f172a', outline='#334155', width=1)
        draw.text((wm_x + 15, wm_y + 8), wm_text, fill='#f8fafc', font=font_watermark)
        
        # Save both to images/ and public/images/
        img.save(os.path.join('public/images', filename), quality=92)
        img.save(os.path.join('images', filename), quality=92)
        print(f"Processed and saved {filename}")
        
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("All representative photos successfully downloaded and saved!")
