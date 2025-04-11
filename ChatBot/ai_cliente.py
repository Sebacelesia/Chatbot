from openai import OpenAI
from dotenv import load_dotenv
import os
from tools import tools


load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
if not DEEPSEEK_API_KEY:
    raise RuntimeError("Falta la variable DEEPSEEK_API_KEY en el entorno.")

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)

def generar_respuesta_ai(texto, user_id, tool_calls=None, tool_messages=None):
    mensajes = [
        {"role": "system", "content": "Sos un asistente que puede consultar el clima y contar interacciones. Solo usá la herramienta 'get_count' si el usuario te lo pide explícitamente."},
        {"role": "user", "content": f"{texto}\n\nID de usuario: {user_id}"}
    ]

    if tool_calls:
        mensajes.append({"role": "assistant", "content": None, "tool_calls": tool_calls})
        mensajes.extend(tool_messages)

    return client.chat.completions.create(
        model="deepseek-chat",
        messages=mensajes,
        tools=tools,
        stream=False
    )
