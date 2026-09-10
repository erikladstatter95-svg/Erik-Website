import json
import csv
import re

SRC_FILE = r"C:/Users/erikl/.gemini/antigravity/brain/5c49ab30-bf3e-4aa0-9768-56edc2e80fa7/.system_generated/steps/454/output.txt"
CSV_OUT = "leads_salones_san_juan.csv"
JSON_OUT = "leads_salones_san_juan.json"

SOCIAL_DOMAINS = [
    "instagram.com", "facebook.com", "fb.me", "linktr.ee",
    "wa.me", "api.whatsapp.com", "bit.ly", "pedidosya.com", "tiktok.com"
]

def format_whatsapp(phone):
    if not phone:
        return "", ""
    digits = re.sub(r"\D", "", phone)
    # Argentine phone formatting
    if digits.startswith("549"):
        clean = digits
    elif digits.startswith("54"):
        rest = digits[2:]
        clean = "549" + rest
    elif digits.startswith("0"):
        digits_no_zero = digits.lstrip("0")
        if digits_no_zero.startswith("264"):
            clean = "549" + digits_no_zero
        else:
            clean = "549264" + digits_no_zero
    elif digits.startswith("264"):
        clean = "549" + digits
    elif len(digits) in [7, 8]:
        clean = "549264" + digits
    else:
        clean = "549" + digits
    
    wa_link = f"https://wa.me/{clean}"
    return phone, wa_link

with open(SRC_FILE, "r", encoding="utf-8") as f:
    line = f.readline()
    data = json.loads(line)

items = data.get("items", [])
print(f"Total venues scraped: {len(items)}")

leads = []
discarded = []

for item in items:
    name = item.get("title", "").strip()
    website = (item.get("website") or "").strip()
    phone_raw = item.get("phone", "").strip()
    rating = item.get("totalScore")
    reviews = item.get("reviewsCount", 0)
    address = item.get("address", "")
    category = item.get("categoryName", "")
    maps_url = item.get("url", "")
    
    # Check web status
    if not website:
        status = "SIN_WEB"
    elif any(d in website.lower() for d in SOCIAL_DOMAINS):
        status = "SOLO_RED_SOCIAL"
    else:
        status = "TIENE_WEB_REAL"
        
    formatted_phone, wa_link = format_whatsapp(phone_raw)
    
    record = {
        "Nombre": name,
        "Estado Web": status,
        "Web o Red Actual": website if website else "Ninguna",
        "Teléfono": formatted_phone if formatted_phone else "No disponible",
        "Link WhatsApp": wa_link if wa_link else "",
        "Categoría": category,
        "Rating": rating if rating is not None else "S/D",
        "Total Reseñas": reviews,
        "Dirección": address,
        "Google Maps URL": maps_url
    }
    
    if status in ["SIN_WEB", "SOLO_RED_SOCIAL"]:
        leads.append(record)
    else:
        discarded.append(record)

print(f"Leads potenciales (Sin web o solo IG/FB): {len(leads)}")
print(f"Descartados (Ya tienen web real): {len(discarded)}")

# Save CSV
fieldnames = [
    "Nombre", "Estado Web", "Web o Red Actual", "Teléfono", "Link WhatsApp",
    "Categoría", "Rating", "Total Reseñas", "Dirección", "Google Maps URL"
]

with open(CSV_OUT, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(leads)

# Save JSON
with open(JSON_OUT, "w", encoding="utf-8") as f:
    json.dump({
        "metadata": {
            "busqueda": "Salones de eventos en San Juan",
            "total_extraidos": len(items),
            "leads_calificados": len(leads),
            "descartados_con_web": len(discarded),
            "fecha": "2026-09-10"
        },
        "leads": leads
    }, f, indent=2, ensure_ascii=False)

print(f"Archivos generados con éxito: {CSV_OUT} y {JSON_OUT}")
