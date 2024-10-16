"""
Dieses Modul enthält Funktionen zum Abrufen von Wetterdaten von einer externen API.

Es verwendet die OpenWeatherMap API, um aktuelle Wetterdaten für eine bestimmte Stadt abzurufen.
Die API-Schlüssel und andere Konfigurationen werden aus den Django-Einstellungen geladen.
"""

import requests
from django.conf import settings

def get_weather(city):
    """
    Ruft Wetterdaten für eine angegebene Stadt ab.

    Args:
        city (str): Der Name der Stadt, für die Wetterdaten abgerufen werden sollen.

    Returns:
        dict: Ein Dictionary mit Wetterdaten, einschließlich Stadt, Temperatur, Beschreibung und Icon.
              Gibt None zurück, wenn ein Fehler auftritt.
    """
    api_key = settings.OPENWEATHERMAP_API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Für Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Löst einen HTTPError für schlechte Antworten aus
        data = response.json()

        weather_info = {
            'city': data['name'],
            'temperature': round(data['main']['temp']),
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather_info
    except requests.RequestException as e:
        print(f"Fehler beim Abrufen der Wetterdaten: {e}")
        return None
