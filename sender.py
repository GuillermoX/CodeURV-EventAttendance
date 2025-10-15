import pandas as pd
import yagmail
import os
import sys

#Script para automatizar el envio de emails con certificados de asistencia
#para los eventos de la asociación CodeURV.


# Configuración
csv_file = 'asistentes.csv'      # Tu CSV con nombres y emails
certificates_folder = 'certificates/'     # Carpeta donde están los PDFs
gmail_user = sys.argv[1]  # Tu correo Gmail
gmail_app_password = sys.argv[2]  # Contraseña de app de Gmail
subject = "Certificat d'assistència xerrada IA 2 d'octubre 2025"
body_template = """Hola {nombre},

T'enviem el certificat de participació de la última xerrada que vam fer el dia 2 d'octubre de 2025.

Gràcies per participar :)

- CodeURV"""

# Leer CSV
df = pd.read_csv(csv_file)

# Inicializar yagmail
yag = yagmail.SMTP(user=gmail_user, password=gmail_app_password)

i = 1
# Recorrer cada fila del CSV y enviar correo
for index, row in df.iterrows():
    nombre = row['Nombre']
    email = row['Email']
    pdf_path = os.path.join(certificates_folder, f"{i}.png")
    
    if os.path.isfile(pdf_path):
        body = body_template.format(nombre=nombre)
        try:
            yag.send(to=email, subject=subject, contents=body, attachments=pdf_path)
            print(f"Correo enviado a {nombre} ({email})")
        except Exception as e:
            print(f"Error enviando a {nombre}: {e}")
    else:
        print(f"No se encontró el certificado para {nombre}")

    i += 1

print("Proceso finalizado.")
