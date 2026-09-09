# Sistema de Landing Pages de Alta Conversión (WebErik)

Plataforma modular de páginas de aterrizaje ultrarrápidas y optimizadas para conversión directa a WhatsApp para negocios locales y profesionales en Argentina. Diseñado para despliegue estático continuo en **Cloudflare Pages**.

---

## 🚀 Inicio Rápido

### 1. Levantar servidor local de desarrollo
```bash
npm run dev
```
Abrirá automáticamente el servidor local en `http://localhost:5173`.
- **Portfolio Principal**: `http://localhost:5173/`
- **Cluster 1 (Estética Médica & Spa)**: `http://localhost:5173/demos/estetica/`

### 2. Generar build de producción
```bash
npm run build
```
Genera la carpeta `/dist` 100% estática (HTML, CSS y JS minificados, gzip < 30 KB).

### 3. Previsualizar build de producción
```bash
npm run preview
```

---

## ☁️ Despliegue en Cloudflare Pages

1. Conectá tu repositorio de GitHub / GitLab en **Cloudflare Pages**.
2. En la sección **Build settings**:
   - **Framework preset**: `Vite` (o None)
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`
3. Hacé clic en **Save and Deploy**. En menos de 60 segundos tu sitio y todas sus demos estarán online en la red global de Cloudflare con certificado SSL automático y carga ultrarrápida.

---

## 🛠️ Personalización y Configuración

### Cambiar el número de WhatsApp por defecto
En `src/js/whatsapp.js`:
```javascript
const DEFAULT_PORTFOLIO_PHONE = '54911XXXXXXXX'; // Tu número de WhatsApp real
```
*Formato:* Código de país (`549`) + código de área sin 0 (ej. `11` para Buenos Aires, `351` para Córdoba) + número de celular sin el 15.

### Mensajes dinámicos de WhatsApp
Cualquier botón o elemento HTML puede activar WhatsApp usando los atributos de datos:
```html
<button 
  data-wa-phone="54911XXXXXXXX"
  data-wa-service="Nombre del Servicio"
  data-wa-msg="Hola! Quisiera reservar un turno para {servicio}.">
  Reservar
</button>
```

---

## 📂 Arquitectura del Proyecto

```text
WebErik/
├── dist/                      # Salida estática compilada para Cloudflare Pages
├── public/                    # Archivos estáticos públicos
├── src/
│   ├── js/
│   │   ├── whatsapp.js        # Helper dinámico de WhatsApp y tracking
│   │   ├── accordion.js       # Acordeón accesible para FAQs
│   │   └── main.js            # Lógica interactiva del Portfolio
│   └── styles/
│       └── main.css           # Tailwind base, componentes y animación WhatsApp
├── demos/
│   └── estetica/              # CLUSTER 1: Estética Médica, Spa y Salud
│       ├── index.html         # Landing de demostración completa
│       └── app.js             # Lógica de filtros y turnos
├── index.html                 # PORTFOLIO PRINCIPAL de Servicios Web
├── tailwind.config.js         # Paletas de color, tipografía y sombras
├── vite.config.js             # Configuración multi-página (MPA)
└── package.json
```
