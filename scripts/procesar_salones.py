import json
import csv
import re
import urllib.parse

SRC_FILE = r"C:/Users/erikl/.gemini/antigravity/brain/5c49ab30-bf3e-4aa0-9768-56edc2e80fa7/.system_generated/steps/454/output.txt"
CSV_OUT = "leads_salones_san_juan_limpio.csv"
HTML_OUT = "leads_salones_viewer.html"

SOCIAL_DOMAINS = [
    "instagram.com", "facebook.com", "fb.me", "linktr.ee",
    "wa.me", "api.whatsapp.com", "bit.ly", "pedidosya.com", "tiktok.com"
]

def format_whatsapp(phone, business_name):
    if not phone:
        return "", "", ""
    digits = re.sub(r"\D", "", phone)
    if digits.startswith("549"):
        clean = digits
    elif digits.startswith("54"):
        clean = "549" + digits[2:]
    elif digits.startswith("0"):
        d = digits.lstrip("0")
        clean = "549" + (d if d.startswith("264") else "264" + d)
    elif digits.startswith("264"):
        clean = "549" + digits
    elif len(digits) in [7, 8]:
        clean = "549264" + digits
    else:
        clean = "549" + digits

    # Pre-drafted WhatsApp message
    msg = f"Hola gente de {business_name}! Les escribo de Erik Web Studio en San Juan. Vi que tienen excelentes referencias pero no cuentan con web oficial para mostrar las instalaciones y fotos del salón. ¿Les puedo compartir una demo rápida que armamos para eventos?"
    encoded_msg = urllib.parse.quote(msg)
    
    direct_link = f"https://wa.me/{clean}?text={encoded_msg}"
    excel_formula = f'=HIPERVINCULO("{direct_link}"; "Enviar WhatsApp")'
    return phone, direct_link, excel_formula

with open(SRC_FILE, "r", encoding="utf-8") as f:
    line = f.readline()
    data = json.loads(line)

items = data.get("items", [])
leads = []

for item in items:
    name = item.get("title", "").strip()
    website = (item.get("website") or "").strip()
    phone_raw = item.get("phone", "").strip()
    city = item.get("city") or "San Juan"
    
    if not website:
        status = "Sin página web"
    elif any(d in website.lower() for d in SOCIAL_DOMAINS):
        status = "Solo Instagram / Red"
    else:
        continue # Discard businesses that already have a real website
        
    phone_display, direct_link, excel_formula = format_whatsapp(phone_raw, name)
    
    # We only include businesses that have a reachable phone or social media
    if not direct_link and not website:
        continue

    leads.append({
        "name": name,
        "status": status,
        "city": city,
        "phone_display": phone_display,
        "website": website,
        "direct_link": direct_link,
        "excel_formula": excel_formula if direct_link else "Sin teléfono"
    })

# 1. GENERATE EXCEL-OPTIMIZED CSV (Delimiter: SEMICOLON, Excel Hyperlink Formula)
with open(CSV_OUT, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["Negocio", "Zona", "Situación Web", "Instagram / Enlace", "Contacto WhatsApp", "Mi Seguimiento"])
    for l in leads:
        writer.writerow([
            l["name"],
            l["city"],
            l["status"],
            l["website"] if l["website"] else "No tiene",
            l["excel_formula"],
            "Pendiente"
        ])

# 2. GENERATE INTERACTIVE HTML CRM DASHBOARD
html_rows = ""
for i, l in enumerate(leads):
    wa_btn = f'''<a href="{l['direct_link']}" target="_blank" class="btn-wa">
        <svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.771-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.007c.106.005.249-.04.39.299.144.347.491 1.2.534 1.288.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.087-.179.182-.077.357.101.174.449.741.964 1.2.662.591 1.221.774 1.394.861.173.087.275.072.376-.043.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.043.073.043.419-.101.824z"/></svg>
        Escribir a WhatsApp
    </a>''' if l['direct_link'] else '<span class="no-phone">Sin teléfono</span>'

    ig_btn = f'''<a href="{l['website']}" target="_blank" class="btn-ig">Ver Perfil</a>''' if l['website'] else '<span class="text-muted">Ninguno</span>'

    badge_class = "badge-ig" if "Instagram" in l['status'] else "badge-noweb"

    html_rows += f'''
    <tr id="row-{i}">
        <td><strong>{l['name']}</strong></td>
        <td><span class="badge-city">{l['city']}</span></td>
        <td><span class="{badge_class}">{l['status']}</span></td>
        <td>{ig_btn}</td>
        <td>{wa_btn}</td>
        <td>
            <select onchange="updateStatus(this, 'row-{i}')" class="status-select">
                <option value="pending">Pendiente</option>
                <option value="contacted">Contactado</option>
                <option value="demo_sent">Demo Enviada</option>
                <option value="interested">Interesado</option>
                <option value="closed">Cerrado / Cliente</option>
                <option value="rejected">No le interesa</option>
            </select>
        </td>
    </tr>
    '''

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Leads Salones de Eventos - Erik Web Studio</title>
    <style>
        :root {{
            --bg: #090d16;
            --card: #111827;
            --border: #1f2937;
            --text: #f3f4f6;
            --muted: #9ca3af;
            --accent: #3b82f6;
            --green: #10b981;
            --ig: #ec4899;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: system-ui, -apple-system, sans-serif; }}
        body {{ background-color: var(--bg); color: var(--text); padding: 2rem 1rem; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; flex-wrap: wrap; gap: 1rem; }}
        h1 {{ font-size: 1.6rem; color: #fff; }}
        p.subtitle {{ color: var(--muted); font-size: 0.95rem; margin-top: 0.25rem; }}
        .stats {{ display: flex; gap: 1rem; }}
        .stat-badge {{ background: #1f2937; padding: 0.5rem 1rem; border-radius: 9999px; font-size: 0.85rem; border: 1px solid #374151; }}
        .stat-badge strong {{ color: var(--green); }}
        
        .table-wrap {{ background: var(--card); border: 1px solid var(--border); border-radius: 12px; overflow-x: auto; }}
        table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem; }}
        th {{ background: #1a2234; padding: 1rem; font-weight: 600; color: #d1d5db; border-bottom: 1px solid var(--border); }}
        td {{ padding: 1rem; border-bottom: 1px solid #1e293b; vertical-align: middle; }}
        tr:hover {{ background: rgba(255,255,255,0.02); }}
        
        .badge-noweb {{ background: rgba(239, 68, 68, 0.15); color: #f87171; padding: 0.25rem 0.6rem; border-radius: 6px; font-size: 0.8rem; font-weight: 600; }}
        .badge-ig {{ background: rgba(236, 72, 153, 0.15); color: #f472b6; padding: 0.25rem 0.6rem; border-radius: 6px; font-size: 0.8rem; font-weight: 600; }}
        .badge-city {{ background: rgba(59, 130, 246, 0.15); color: #60a5fa; padding: 0.2rem 0.5rem; border-radius: 6px; font-size: 0.8rem; }}
        
        .btn-wa {{ display: inline-flex; align-items: center; gap: 0.4rem; background: #059669; color: white; text-decoration: none; padding: 0.45rem 0.85rem; border-radius: 8px; font-size: 0.85rem; font-weight: 600; transition: background 0.2s; }}
        .btn-wa:hover {{ background: #10b981; }}
        .btn-wa .icon {{ width: 16px; height: 16px; }}
        
        .btn-ig {{ display: inline-block; color: #f472b6; border: 1px solid #db2777; text-decoration: none; padding: 0.35rem 0.7rem; border-radius: 6px; font-size: 0.8rem; font-weight: 500; transition: all 0.2s; }}
        .btn-ig:hover {{ background: rgba(219, 39, 119, 0.15); }}
        
        .text-muted {{ color: #6b7280; font-size: 0.85rem; }}
        .no-phone {{ color: #9ca3af; font-size: 0.85rem; }}
        
        .status-select {{ background: #1f2937; color: #fff; border: 1px solid #374151; padding: 0.4rem 0.6rem; border-radius: 6px; font-size: 0.85rem; outline: none; cursor: pointer; }}
        .status-select:focus {{ border-color: var(--accent); }}
        .row-contacted {{ opacity: 0.6; background: rgba(16, 185, 129, 0.05); }}
    </style>
    <script>
        function updateStatus(select, rowId) {{
            const row = document.getElementById(rowId);
            if (select.value === 'contacted' || select.value === 'demo_sent' || select.value === 'closed') {{
                row.classList.add('row-contacted');
            }} else {{
                row.classList.remove('row-contacted');
            }}
        }}
    </script>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>
                <h1>Leads Calificados: Salones de Eventos (San Juan)</h1>
                <p class="subtitle">Prospectos listos para contactar con mensaje pre-redactado de WhatsApp y demo del Cluster 2.</p>
            </div>
            <div class="stats">
                <div class="stat-badge">Total leads: <strong>{len(leads)}</strong></div>
                <div class="stat-badge">Con WhatsApp: <strong>{sum(1 for l in leads if l['direct_link'])}</strong></div>
            </div>
        </div>

        <div class="table-wrap">
            <table>
                <thead>
                    <tr>
                        <th>Negocio</th>
                        <th>Zona</th>
                        <th>Situación Web</th>
                        <th>Red Social</th>
                        <th>Acción Directa</th>
                        <th>Mi Seguimiento</th>
                    </tr>
                </thead>
                <tbody>
                    {html_rows}
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
'''

with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Archivos simplificados generados con éxito: {CSV_OUT} y {HTML_OUT}")
