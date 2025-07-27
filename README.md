# 📬 Script de Envío Masivo de Correos con Plantillas Personalizadas

Este script en Python permite el **envío masivo de correos electrónicos personalizados** utilizando múltiples plantillas HTML. Es útil para campañas de correo donde se requiere modificar datos como el nombre del destinatario, un enlace y un parámetro adicional llamado `tracker`.

## 🛠️ Funcionalidades

- Envío de correos mediante **SMTP con SSL**.
- Lectura de destinatarios desde un archivo CSV.
- Uso de **plantillas HTML aleatorias** para personalizar cada mensaje.
- Personalización dinámica de los campos `{{nombre}}`, `{{link}}` y `{{tracker}}`.
- Limpieza del HTML eliminando comentarios y espacios innecesarios.
- Tiempo de espera entre envíos para evitar bloqueos por spam.

---

## 📁 Estructura del Proyecto

```
.
├── script.py
├── destinatarios.csv
├── plantillas/
│   ├── plantilla1.html
│   ├── plantilla2.html
│   └── ...
```

---

## 🔍 Explicación del Código

### 1. Configuración SMTP

```python
SMTP_SERVER = ""
SMTP_PORT = 465
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""
```

Define el servidor y las credenciales de correo que se usarán para el envío. Se recomienda no dejar estos valores en claro en el código fuente por razones de seguridad.

---

### 2. Limpieza del HTML

```python
def limpiar_html(html):
```

- Elimina los comentarios HTML (`<!-- ... -->`).
- Compacta los espacios en blanco.
- Devuelve el HTML listo para enviarse.

---

### 3. Selección Aleatoria de Plantilla

```python
def cargar_plantilla_aleatoria():
```

- Escoge un archivo `.html` al azar desde la carpeta `plantillas/`.
- Si no encuentra archivos válidos, lanza una excepción.

---

### 4. Envío de Correo Personalizado

```python
def enviar_correo(destinatario, nombre, link, tracker, plantilla_original):
```

- Reemplaza en la plantilla los marcadores `{{nombre}}`, `{{link}}` y `{{tracker}}`.
- Construye el mensaje con `email.mime`.
- Usa `smtplib.SMTP_SSL` para enviar el mensaje de forma segura.

---

### 5. Envío Masivo desde CSV

```python
def enviar_masivo():
```

- Lee el archivo `destinatarios.csv` con los campos: `email`, `nombre`, `link`, `tracker`.
- Por cada destinatario:
  - Carga una plantilla aleatoria.
  - Personaliza el mensaje.
  - Lo envía por correo.
  - Espera 10 segundos antes del siguiente envío.

---

## 📄 Formato del Archivo CSV

El archivo `destinatarios.csv` debe tener el siguiente formato:

```csv
email,nombre,link,tracker
correo1@ejemplo.com,Ana,https://ejemplo.com/promo1,TRK001
correo2@ejemplo.com,Luis,https://ejemplo.com/promo2,TRK002
```

---

## ⚠️ Recomendaciones de Seguridad

- Nunca subas tus credenciales (`EMAIL_ADDRESS`, `EMAIL_PASSWORD`) a un repositorio público.
- Considera usar variables de entorno o archivos `.env` para proteger datos sensibles.
- Asegúrate de contar con permiso explícito de los destinatarios antes de enviar correos.

---

## ▶️ Ejecución del Script

Desde la terminal:

```bash
python envio_de_correos.py
```

---

## ✅ Requisitos

- Python 3.x
- Librerías estándar (no requiere instalación externa):
  - `smtplib`
  - `csv`
  - `os`
  - `re`
  - `time`
  - `random`
  - `email.mime`

---

## ✍️ Autor

Este script fue diseñado con fines educativos y profesionales, para automatizar el envío controlado y personalizado de correos electrónicos.

---
