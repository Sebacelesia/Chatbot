def construir_mensajes(texto, user_id, tool_calls=None, tool_messages=None):
    mensajes = [
        {"role": "system", "content": "Sos un asistente que puede consultar el clima y contar interacciones."},
        {"role": "user", "content": f"{texto}\n\nID de usuario: {user_id}"}
    ]

    if tool_calls:
        mensajes.append({"role": "assistant", "content": None, "tool_calls": tool_calls})
    if tool_messages:
        mensajes.extend(tool_messages)

    return mensajes
