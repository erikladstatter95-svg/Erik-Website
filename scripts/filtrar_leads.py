import json
import csv
import re
from urllib.parse import urlparse

# Archivo origen generado por Apify
INPUT_FILE = 'dataset_crawler-google-places_2026-09-09_22-10-28-061.json'
OUTPUT_CSV = 'leads_potenciales_san_juan.csv'
OUTPUT_JSON = 'leads_potenciales_san_juan.json'

SOCIAL_DOMAINS = [
    'instagram.com', 'facebook.com', 'fb.com', 'wa.me', 
    'linktr.ee', 'bit.ly', 'pedidosya.com.ar', 'pedidosya.com',
    'mercadolibre.com.ar', 'tiktok.com', 'beacons.ai', 'bio.link'
]

def format_whatsapp_phone(raw_phone):
    if not raw_phone:
        return '', ''
    # Limpiar caracteres no numéricos
    clean = re.sub(r'\D', '', str(raw_phone))
    
    # Normalizar números de Argentina
    # Ejemplos comunes: 0264 15-4123456, +54 9 264 412-3456, 2644123456
    if clean.startswith('549'):
        final = clean
    elif clean.startswith('54') and len(clean) >= 12 and clean[2] != '9':
        final = '549' + clean[2:]
    elif clean.startswith('0'):
        # Quitar 0 inicial y sumar 549
        final = '549' + clean[1:]
    elif len(clean) == 10: # ej 2644123456
        final = '549' + clean
    else:
        final = clean

    # Quitar el '15' móvil si quedó en el medio (ej: 264 15 4123456 -> 264 4123456)
    # Patrón común sanjuanino: 549 264 15 XXXXXX -> 549 264 XXXXXX
    if final.startswith('54926415'):
        final = '549264' + final[8:]

    wa_link = f'https://wa.me/{final}' if final else ''
    return raw_phone, wa_link

def classify_website(web_url):
    if not web_url or not str(web_url).strip():
        return 'SIN_WEB', 'No tiene sitio web (Oportunidad Máxima)'
    
    parsed = urlparse(str(web_url)).netloc.lower()
    for social in SOCIAL_DOMAINS:
        if social in parsed:
            return 'SOLO_RED_SOCIAL', f'Usa {social} como web (Oportunidad Alta)'
            
    return 'TIENE_WEB_REAL', 'Tiene sitio web propio'

def main():
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error al abrir {INPUT_FILE}: {e}")
        return

    total_scraped = len(data)
    leads_potenciales = []
    con_web_propia = []

    for item in data:
        nombre = item.get('title') or ''
        categoria = item.get('categoryName') or (item.get('categories') or [''])[0]
        direccion = item.get('address') or ''
        ciudad = item.get('city') or 'San Juan'
        raw_phone = item.get('phone') or item.get('phoneUnformatted') or ''
        web = item.get('website') or ''
        rating = item.get('totalScore') or ''
        reviews = item.get('reviewsCount') or 0
        maps_url = item.get('url') or ''
        
        tipo_web, motivo = classify_website(web)
        phone_display, wa_link = format_whatsapp_phone(raw_phone)
        
        lead_dict = {
            'nombre': nombre,
            'categoria': categoria,
            'telefono': phone_display,
            'enlace_whatsapp': wa_link,
            'tipo_oportunidad': motivo,
            'clasificacion': tipo_web,
            'web_actual': web,
            'ciudad': ciudad,
            'direccion': direccion,
            'calificacion': rating,
            'total_resenas': reviews,
            'maps_url': maps_url
        }

        if tipo_web in ('SIN_WEB', 'SOLO_RED_SOCIAL'):
            # Priorizamos los que tienen teléfono de contacto
            leads_potenciales.append(lead_dict)
        else:
            con_web_propia.append(lead_dict)

    # Ordenar por: primero los que tienen teléfono y más reseñas
    leads_con_telefono = [l for l in leads_potenciales if l['telefono']]
    leads_sin_telefono = [l for l in leads_potenciales if not l['telefono']]

    leads_con_telefono.sort(key=lambda x: (x['clasificacion'] == 'SOLO_RED_SOCIAL', x['total_resenas']), reverse=True)
    leads_sin_telefono.sort(key=lambda x: x['total_resenas'], reverse=True)

    leads_finales = leads_con_telefono + leads_sin_telefono

    # Exportar a CSV (UTF-8 con BOM para abrir directo en Excel en español)
    with open(OUTPUT_CSV, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'nombre', 'categoria', 'telefono', 'enlace_whatsapp', 
            'tipo_oportunidad', 'web_actual', 'ciudad', 'direccion', 
            'calificacion', 'total_resenas', 'maps_url'
        ], extrasaction='ignore')
        writer.writeheader()
        for lead in leads_finales:
            writer.writerow(lead)

    # Exportar a JSON
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump({
            'metadata': {
                'total_scraped': total_scraped,
                'leads_potenciales_total': len(leads_finales),
                'leads_con_telefono': len(leads_con_telefono),
                'descartados_con_web_real': len(con_web_propia)
            },
            'leads': leads_finales
        }, f, ensure_ascii=False, indent=2)

    print("=" * 60)
    print("REPORTE DE FILTRADO DE LEADS - GOOGLE MAPS")
    print("=" * 60)
    print(f"Total comercios en dataset Apify: {total_scraped}")
    print(f"Descartados (ya tienen web real): {len(con_web_propia)} ({len(con_web_propia)/total_scraped*100:.1f}%)")
    print(f"LEADS POTENCIALES TOTALES: {len(leads_finales)} ({len(leads_finales)/total_scraped*100:.1f}%)")
    print(f"  -> Con teléfono / WhatsApp directo: {len(leads_con_telefono)}")
    print(f"  -> Sin teléfono público (contactar por Instagram o visita): {len(leads_sin_telefono)}")
    print("=" * 60)
    print(f"Archivos exportados exitosamente:")
    print(f"1. CSV para Excel/Sheets: {OUTPUT_CSV}")
    print(f"2. JSON estructurado: {OUTPUT_JSON}")
    print("=" * 60)

if __name__ == '__main__':
    main()
