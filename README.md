Telegram Bot - Clima, Contador e IA (Deepseek)
Este proyecto es un bot de Telegram desarrollado en Python que permite:

📍 Consultar el clima actual en una ciudad
🔢 Llevar un contador de interacciones por usuario
🤖 Hablar con una inteligencia artificial basada en Deepseek
🧠 Registrar los usuarios y sus conversaciones en una base de datos SQLite

¿Cómo funciona?
Al iniciar el bot con /start, el usuario puede interactuar libremente con la IA.
Si el usuario menciona el clima o quiere saber cuántas veces ha hablado con el bot, se activan herramientas especiales mediante function calling de Deepseek.
Cada mensaje enviado queda registrado en una base de datos junto con el usuario correspondiente.

Estructura del proyecto.
ChatBot/
├── ai_cliente.py       # Lógica desacoplada para comunicarte con la API de Deepseek
├── bd.py               # Configura la base de datos SQLite y funciones para insertar usuarios y conversaciones
├── bot.py              # Punto de entrada: crea la aplicación de Telegram y conecta los handlers
├── clima.py            # Lógica para consultar el clima por ciudad o coordenadas usando OpenWeather
├── contador.py         # Mantiene un contador en memoria para cada usuario (interacciones)
├── handlers.py         # Recibe y gestiona los mensajes de Telegram (comando /start, conversación)
├── tools.py            # Define las herramientas (tools) que puede usar el modelo IA: clima y contador
├── utils.py            # Funciones auxiliares, como generar la estructura de mensajes para el modelo
├── ver_tablas.py       # Script utilitario para visualizar el contenido actual de la base de datos

.env                  # Variables reales (IGNORADO en el repositorio)
.env.example          # Ejemplo de .env para que otros puedan configurarlo
requirements.txt      # Dependencias del proyecto
README.md             # Documentación general del bot



Requisitos
Python 3.11 o superior
API Keys de:
OpenWeather
Deepseek
Telegram Bot

Configuración del archivo .env
Este proyecto utiliza variables de entorno para manejar credenciales de forma segura.

Creá un archivo .env basado en .env.example con este contenido:
TELEGRAM_TOKEN=tu_token_generado
OPENWEATHER_KEY=tu_api_key_openweather
DEEPSEEK_API_KEY=tu_api_key_deepseek

 Base de datos
El bot crea automáticamente un archivo bot.db con dos tablas:

usuarios → Guarda ID, nombre y username de cada usuario
conversaciones → Registra cada mensaje y respuesta

Cómo ejecutar el bot
Cloná el repositorio
Activá tu entorno virtual
Instalá las dependencias
Ejecutá el bot