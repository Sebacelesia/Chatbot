# 🤖 Telegram Bot - Clima, Contador e IA (Deepseek)

Este proyecto es un bot de Telegram desarrollado en Python que permite:

- 🌦️ Consultar el clima en cualquier ciudad del mundo
- 🧮 Contar cuántas veces interactuó un usuario con el bot
- 💬 Chatear con una IA basada en modelos de lenguaje (usando [Deepseek](https://deepseek.com))

---

## 🚀 ¿Cómo funciona?

Cuando el usuario envía un mensaje:

1. Se registra en una base de datos SQLite (si es la primera vez)
2. El mensaje es procesado con IA usando el modelo `deepseek-chat`
3. Si el modelo solicita herramientas ("tools"), como `get_weather` o `get_count`, se ejecutan localmente
4. La respuesta se guarda en la base de datos y se envía al usuario

---

## 🛠️ Requisitos

- Python 3.10 o superior 
- Crear un bot de Telegram en [@BotFather](https://t.me/BotFather)
- Tener API Key de:
  - [Deepseek](https://platform.deepseek.com)
  - [OpenWeather](https://openweathermap.org/api)

---

## 🔐 Configuración de variables de entorno

Crear un archivo `.env` (basado en `.env.example`) con las siguientes claves:

```env
TELEGRAM_TOKEN=TU_TOKEN_DEL_BOT
DEEPSEEK_API_KEY=CLAVE_DEEPSEEK
OPENWEATHER_KEY=CLAVE_OPENWEATHER
```

---

## ▶️ Cómo ejecutar el bot

```bash
# Crear y activar entorno virtual 


# Instalar dependencias


# Ejecutar el bot


---

## 📁 Estructura del proyecto

```bash
ChatBot/
├── ai_cliente.py       # Lógica para enviar mensajes a la API de Deepseek
├── bd.py               # Funciones para registrar usuarios y conversaciones en SQLite
├── bot.py              # Punto de entrada: arranca el bot y registra los handlers
├── clima.py            # Obtiene el clima usando la API de OpenWeather
├── contador.py         # Contador de interacciones por usuario
├── handlers.py         # Define cómo responder a los mensajes de Telegram
├── tools.py            # Define herramientas (tools) para que la IA pueda invocar funciones
├── utils.py            # Funciones auxiliares para componer mensajes
├── ver_tablas.py       # Script para visualizar la base de datos manualmente
├── .env.example        # Archivo de ejemplo con variables necesarias
├── requirements.txt    # Lista de librerías usadas

```

---

## 🧠 Funcionalidad IA

El modelo IA tiene acceso a funciones que puede invocar si detecta que el usuario lo solicita. Estas funciones están definidas en `tools.py`:

- `get_weather(location: str)` → Clima en una ciudad
- `get_count(user_id: int)` → Cuántas veces el usuario interactuó

Los mensajes del usuario se estructuran con contexto para guiar al modelo.

---

## 💾 Base de datos

Se usa SQLite para guardar:

- Usuarios: ID, nombre, username
- Conversaciones: texto enviado y respuesta generada

Podés ver su contenido con:

```bash
python ChatBot/ver_tablas.py
```

---

## 📦 Requerimientos (requirements.txt)

```txt
python-telegram-bot==20.7
openai==1.14.3
requests
python-dotenv
```



