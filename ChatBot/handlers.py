# handlers.py
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from clima import obtener_clima_por_ciudad
from contador import actualizar_contador
from bd import registrar_usuario, registrar_conversacion
from tools import tools  
from ai_cliente import generar_respuesta_ai
import json
import os
import openai
import logging

contadores = {}
logger = logging.getLogger(__name__)

def get_weather(location: str) -> str:
    return obtener_clima_por_ciudad(location)

def get_count(user_id: int) -> str:
    cantidad = contadores.get(user_id, 0)
    return f"Te hablé {cantidad} veces."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Soy un bot con inteligencia artificial. Hablame y trataré de ayudarte.",
        reply_markup=ReplyKeyboardRemove()
    )

def procesar_llamadas_de_herramientas(tool_calls):
    tool_messages = []

    funciones_disponibles = {
        "get_weather": lambda args: get_weather(**args),
        "get_count": lambda args: get_count(args["user_id"])
    }

    for tool_call in tool_calls:
        try:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            funcion = funciones_disponibles.get(function_name)
            result = funcion(arguments) if funcion else f"La función {function_name} no está implementada."
        except json.JSONDecodeError:
            result = "Error al interpretar los argumentos de la herramienta."
        except Exception as e:
            result = f"Error inesperado al ejecutar la herramienta: {e}"

        tool_messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result
        })

    return tool_messages

async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    nombre = update.effective_user.first_name
    username = update.effective_user.username

    registrar_usuario(user_id, nombre, username)
    actualizar_contador(user_id, contadores)

    texto = update.message.text.strip()

    try:
        response = generar_respuesta_ai(texto, user_id)
        message = response.choices[0].message

        if message.tool_calls:
            tool_messages = procesar_llamadas_de_herramientas(message.tool_calls)

            second_response = generar_respuesta_ai(
                texto, user_id, tool_calls=message.tool_calls, tool_messages=tool_messages
            )
            reply = second_response.choices[0].message.content
            await update.message.reply_text(reply)
            registrar_conversacion(user_id, texto, reply)
        else:
            reply = message.content
            await update.message.reply_text(reply)
            registrar_conversacion(user_id, texto, reply)

    except openai.OpenAIError as e:
        logger.error("❌ Error con la API de Deepseek:", exc_info=True)
        await update.message.reply_text("Ocurrió un error con la inteligencia artificial.")
    except Exception as e:
        logger.error("❌ Error inesperado:", exc_info=True)
        await update.message.reply_text("Ocurrió un error inesperado.")
