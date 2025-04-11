import os
import requests

def obtener_clima_por_ciudad(ciudad):
    API_KEY = os.getenv("OPENWEATHER_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    res = requests.get(url)
    data = res.json()

    if res.ok:
        nombre = data.get("name", ciudad)
        temp = data["main"]["temp"]
        clima = data["weather"][0]["description"]
        humedad = data["main"]["humidity"]
        return f"El clima en {nombre} es {clima}, con {temp}°C y humedad del {humedad}%."
    else:
        return f"No pude obtener el clima para {ciudad}."
