import smtplib
import csv
import os
import re
import time
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ==== CONFIGURACIÓN SMTP (WEBMAIL) ====
SMTP_SERVER = ""
SMTP_PORT = 465
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""

# ==== ARCHIVOS ====
CSV_PATH = "destinatarios.csv"
HTML_TEMPLATES_DIR = "plantillas"  # Carpeta con múltiples plantillas .html

# ==== LIMPIEZA BÁSICA DEL HTML ====
def limpiar_html(html):
    html = re.sub(r"<!--.*?-->", "", html, flags=re.DOTALL)  # Elimina comentarios
    html = re.sub(r"\s+", " ", html)  # Compacta espacios
    return html.strip()

# ==== CARGAR UNA PLANTILLA HTML ALEATORIA ====
def cargar_plantilla_aleatoria():
    if not os.path.exists(HTML_TEMPLATES_DIR):
        raise FileNotFoundError(f"[!] No se encontró la carpeta {HTML_TEMPLATES_DIR}")
    
    archivos = [f for f in os.listdir(HTML_TEMPLATES_DIR) if f.endswith(".html")]
    if not archivos:
        raise ValueError("[!] No hay archivos .html en la carpeta de plantillas.")
    
    plantilla_aleatoria = random.choice(archivos)
    ruta = os.path.join(HTML_TEMPLATES_DIR, plantilla_aleatoria)

    with open(ruta, 'r', encoding='utf-8') as f:
        return f.read()

# ==== ENVIAR CORREO PERSONALIZADO ====
def enviar_correo(destinatario, nombre, link, tracker, plantilla_original):
    html_personalizado = (
        plantilla_original
        .replace("{{nombre}}", nombre)
        .replace("{{link}}", link)
        .replace("{{tracker}}", tracker)
    )
    html_limpio = limpiar_html(html_personalizado)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Descuentos exclusivos"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = destinatario
    msg.attach(MIMEText(html_limpio, "html"))

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"[+] Enviado a {destinatario}")
    except Exception as e:
        print(f"[-] Error con {destinatario}: {e}")

# ==== ENVÍO MASIVO ====
def enviar_masivo():
    with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email = row["email"]
            nombre = row["nombre"]
            link = row["link"]
            tracker = row["tracker"]
            plantilla_html = cargar_plantilla_aleatoria()
            enviar_correo(email, nombre, link, tracker, plantilla_html)
            time.sleep(10)  # Delay entre envíos

if __name__ == "__main__":
    enviar_masivo()
