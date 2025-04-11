tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Obtener el clima actual de una ciudad",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "Ciudad y país. Ej: Montevideo, Uruguay"
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_count",
            "description": "Obtener cuántas veces el usuario interactuó con el bot",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "integer",
                        "description": "ID del usuario de Telegram"
                    }
                },
                "required": ["user_id"]
            }
        }
    }
]