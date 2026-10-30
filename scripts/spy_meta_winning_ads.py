import time
import re
import json
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_driver():
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36')
    options.add_argument('--lang=es-ES')
    return webdriver.Chrome(options=options)

def extract_ads_for_query(query, country="AR", scroll_times=4):
    driver = get_driver()
    encoded_q = query.replace(' ', '%20').replace('"', '%22')
    # We sort by relevancy_monthly_grouped or start_date
    url = f"https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country={country}&q={encoded_q}&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all"
    
    print(f"[*] Buscando en Meta Ad Library: '{query}' en país: {country}...")
    driver.get(url)
    time.sleep(6)
    
    # Scroll to load more ads
    for s in range(scroll_times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        
    full_text = driver.find_element(By.TAG_NAME, 'body').text
    driver.quit()
    
    # Save raw for inspection
    os.makedirs('scratch', exist_ok=True)
    clean_q = re.sub(r'[^a-zA-Z0-9]', '_', query)
    with open(f"scratch/raw_ads_{clean_q}.txt", "w", encoding="utf-8") as f:
        f.write(full_text)
        
    return parse_ads_from_text(full_text, query)

def parse_ads_from_text(text, query):
    # Split ad cards by "Identificador de la biblioteca:"
    cards = re.split(r'Identificador de la biblioteca:\s*', text)
    parsed_ads = []
    
    for i, card in enumerate(cards[1:], 1):
        lines = [line.strip() for line in card.split('\n') if line.strip()]
        if not lines:
            continue
            
        ad_id = lines[0]
        
        # Look for start date / circulation
        circulacion = ""
        variantes = 1
        anunciante = ""
        copy_lines = []
        cta = ""
        
        for idx, line in enumerate(lines):
            if "En circulación desde" in line:
                circulacion = line
            elif "anuncios usan este contenido" in line or "anuncio usa este contenido" in line:
                m = re.search(r'(\d+)\s+anuncio', line)
                if m:
                    variantes = int(m.group(1))
            elif line == "Publicidad" and idx > 0:
                # Advertiser is usually the line right before 'Publicidad'
                anunciante = lines[idx-1]
                # Copy starts after Publicidad
                # Capture next 15 lines until common footers
                for c_line in lines[idx+1:idx+25]:
                    if any(stop_word in c_line for stop_word in [
                        "Identificador de la biblioteca", "Activo", "Inactivo", "Número de impresiones", 
                        "Plataformas", "Ver detalles", "Abrir menú", "0:00 /", "Más información", 
                        "Enviar mensaje", "Contactar", "Comprar", "Registrarte", "WhatsApp"
                    ]):
                        if any(c in c_line for c in ["Más información", "Enviar mensaje", "Contactar", "WhatsApp"]):
                            cta = c_line
                        break
                    copy_lines.append(c_line)
                    
        copy_text = "\n".join(copy_lines).strip()
        
        # Only keep ads that have an actual copy
        if copy_text and len(copy_text) > 30:
            parsed_ads.append({
                "id": ad_id,
                "query": query,
                "anunciante": anunciante,
                "circulacion": circulacion,
                "variantes": variantes,
                "copy": copy_text,
                "cta": cta
            })
            
    return parsed_ads

def main():
    target_queries = [
        '"diseño de paginas web"',
        '"creamos tu pagina web"',
        '"hacemos tu web"',
        '"landing page para tu negocio"'
    ]
    
    all_ads = []
    for q in target_queries:
        ads = extract_ads_for_query(q, country="ALL", scroll_times=3)
        print(f"[+] Encontrados {len(ads)} anuncios parseados para: {q}")
        all_ads.extend(ads)
        time.sleep(2)
        
    # Deduplicate by ID
    unique_ads = {}
    for a in all_ads:
        unique_ads[a['id']] = a
        
    ads_list = list(unique_ads.values())
    
    # Sort by variants count and text length
    ads_list.sort(key=lambda x: (x['variantes'], len(x['copy'])), reverse=True)
    
    output_path = "scratch/winning_meta_ads.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(ads_list, f, ensure_ascii=False, indent=2)
        
    print(f"\n==========================================")
    print(f"TOTAL DE ANUNCIOS EXTRAÍDOS: {len(ads_list)}")
    print(f"Guardados en: {output_path}")
    print(f"==========================================")
    
    # Generate human readable report
    report_path = "scratch/winning_meta_ads_report.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("=== REPORTE DE ANUNCIOS GANADORES EN META (DISEÑO WEB & LANDING PAGES) ===\n\n")
        for idx, ad in enumerate(ads_list[:15], 1):
            f.write(f"--- ANUNCIO #{idx} ---\n")
            f.write(f"Anunciante: {ad['anunciante']}\n")
            f.write(f"Circulación: {ad['circulacion']}\n")
            f.write(f"Variantes Activas: {ad['variantes']}\n")
            f.write(f"CTA: {ad['cta']}\n")
            f.write(f"Copy:\n{ad['copy']}\n")
            f.write("="*60 + "\n\n")
            
    print(f"Reporte legible guardado en: {report_path}")

if __name__ == "__main__":
    main()
