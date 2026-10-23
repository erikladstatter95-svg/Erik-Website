"""
Update alt text and figcaptions across all blog articles to accurately reflect
the new representative editorial photography.
"""
import glob
import re

updates = {
    'paginas-web-para-abogados-argentina': (
        'Estudio jurídico y asesoramiento legal profesional en Argentina',
        'Asesoramiento letrado y ejercicio del derecho profesional. Foto de referencia erikwebsite.com.'
    ),
    'paginas-web-para-psicologos-argentina': (
        'Sesión de consulta y atención psicológica profesional en Argentina',
        'Atención psicológica y acompañamiento terapéutico. Foto de referencia erikwebsite.com.'
    ),
    'como-automatizar-turnos-consultorio': (
        'Consulta odontológica y atención de salud en clínica moderna',
        'Atención médica y asignación ágil de turnos. Foto de referencia erikwebsite.com.'
    ),
    'paginas-web-salones-belleza-estetica': (
        'Tratamiento estético profesional en cabina de belleza',
        'Tratamientos faciales y corporales de alta gama. Foto de referencia erikwebsite.com.'
    ),
    'paginas-web-personal-trainers-gimnasios': (
        'Entrenador personal asistiendo a un alumno en el gimnasio',
        'Entrenamiento personalizado y asesoría deportiva. Foto de referencia erikwebsite.com.'
    ),
    'paginas-web-oficios-servicios-hogar': (
        'Técnico especialista realizando reparaciones del hogar con herramientas',
        'Servicios técnicos y reparaciones especializadas del hogar. Foto de referencia erikwebsite.com.'
    ),
    'paginas-web-estudios-contables-argentina': (
        'Contador público analizando balances y finanzas de empresas',
        'Asesoría impositiva y planificación fiscal para PyMEs. Foto de referencia erikwebsite.com.'
    ),
    'paginas-web-salones-eventos-catering': (
        'Salón de eventos iluminado con mesas preparadas para una recepción',
        'Salones de fiestas y servicios para recepciones. Foto de referencia erikwebsite.com.'
    ),
    'como-conseguir-clientes-google-maps': (
        'Smartphone mostrando ubicación y navegación de negocios en Google Maps',
        'Búsqueda de comercios y servicios locales en mapa. Foto de referencia erikwebsite.com.'
    ),
    'pagina-web-vs-instagram': (
        'Usuario comparando redes sociales en smartphone y sitio web profesional en laptop',
        'Estrategia digital: Redes sociales para atracción y web propia para conversión. Foto de referencia erikwebsite.com.'
    ),
    'que-negocios-necesitan-una-pagina-web': (
        'Comerciante y dueño de negocio atendiendo clientes en su local',
        'Presencia digital para negocios y profesionales locales. Foto de referencia erikwebsite.com.'
    ),
    'cuanto-cuesta-una-pagina-web-argentina': (
        'Planificación de presupuesto y métricas de sitio web en computadora',
        'Inversión, hosting cloud y desarrollo web profesional. Foto de referencia erikwebsite.com.'
    ),
    'por-que-tener-una-pagina-web': (
        'Emprendedores celebrando el crecimiento digital de su negocio',
        'Crecimiento comercial y digitalización de negocios en Argentina. Foto de referencia erikwebsite.com.'
    ),
}

for slug, (new_alt, new_caption) in updates.items():
    file_path = f'blog/{slug}/index.html'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update alt attribute in main figure
        content = re.sub(
            r'(<figure class="[^"]*">.*?<img [^>]*alt=")[^"]*(")',
            rf'\g<1>{new_alt}\g<2>',
            content,
            flags=re.DOTALL
        )

        # Update figcaption content
        content = re.sub(
            r'(<figcaption[^>]*>).*?(<\/figcaption>)',
            rf'\g<1>\n            {new_caption}\n          \g<2>',
            content,
            flags=re.DOTALL
        )

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated captions in {slug}")
    except Exception as e:
        print(f"Error updating {slug}: {e}")

print("All captions and alt texts updated!")
