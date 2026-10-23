"""
Download and process 3 authentic editorial photos for Cuyo Geo-Pages:
1. San Juan
2. Mendoza
3. San Luis
"""
import urllib.request
import os
from PIL import Image, ImageDraw, ImageFont

photo_configs = [
    {
        'filename': 'guia_diseno_web_san_juan.png',
        'url': 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80',
        'badge': 'SAN JUAN & CUYO',
        'color': '#34d399'
    },
    {
        'filename': 'guia_diseno_web_mendoza.png',
        'url': 'https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?auto=format&fit=crop&w=1200&q=80',
        'badge': 'MENDOZA & GRAN MENDOZA',
        'color': '#38bdf8'
    },
    {
        'filename': 'guia_diseno_web_san_luis.png',
        'url': 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1200&q=80',
        'badge': 'SAN LUIS & VILLA MERCEDES',
        'color': '#a78bfa'
    }
]

os.makedirs('temp_dl', exist_ok=True)
os.makedirs('public/images', exist_ok=True)
os.makedirs('images', exist_ok=True)

try:
    font_badge = ImageFont.truetype('arialbd.ttf', 13)
    font_watermark = ImageFont.truetype('arialbd.ttf', 14)
except Exception:
    font_badge = font_watermark = ImageFont.load_default()

TARGET_W, TARGET_H = 1200, 675

for item in photo_configs:
    filename = item['filename']
    temp_path = os.path.join('temp_dl', filename.replace('.png', '.jpg'))
    print(f"Downloading {filename}...")
    req = urllib.request.Request(item['url'], headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp, open(temp_path, 'wb') as out_f:
        out_f.write(resp.read())
        
    img = Image.open(temp_path).convert('RGB')
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
    
    overlay = Image.new('RGBA', (TARGET_W, TARGET_H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    
    for y in range(90):
        a = int(140 * (1.0 - (y / 90.0)))
        odraw.line([(0, y), (TARGET_W, y)], fill=(0, 0, 0, a))
        
    for y in range(TARGET_H - 80, TARGET_H):
        prog = (y - (TARGET_H - 80)) / 80.0
        a = int(160 * prog)
        odraw.line([(0, y), (TARGET_W, y)], fill=(0, 0, 0, a))
        
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(img)
    
    badge_label = item['badge']
    badge_text = f"* {badge_label}"
    bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw = (bbox[2] - bbox[0]) + 32
    bh = 34
    draw.rounded_rectangle([32, 28, 32 + bw, 28 + bh], radius=12, fill='#0f172a', outline='#334155', width=1)
    draw.text((48, 36), badge_text, fill=item['color'], font=font_badge)
    
    wm_text = 'erikwebsite.com'
    wm_bbox = draw.textbbox((0, 0), wm_text, font=font_watermark)
    wm_w = (wm_bbox[2] - wm_bbox[0]) + 30
    wm_h = 34
    wm_x = TARGET_W - wm_w - 32
    wm_y = TARGET_H - wm_h - 24
    draw.rounded_rectangle([wm_x, wm_y, wm_x + wm_w, wm_y + wm_h], radius=12, fill='#0f172a', outline='#334155', width=1)
    draw.text((wm_x + 15, wm_y + 8), wm_text, fill='#f8fafc', font=font_watermark)
    
    img.save(os.path.join('public/images', filename), quality=92)
    img.save(os.path.join('images', filename), quality=92)
    print(f"Processed and saved {filename}")

print("Done downloading Cuyo photos!")
