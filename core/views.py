"""
Dieses Modul enthält die Hauptansichten (Views) für die Forstapp.

Es definiert die Funktionen für die Startseite, Wetterabfrage und Kartenaktualisierung.
Die Views verarbeiten Benutzeranfragen, interagieren mit den Modellen und
rendern die entsprechenden Templates.
"""

from django.shortcuts import render
from django.http import JsonResponse
from .weather import get_weather
import folium
import json
import os
from django.conf import settings

# Erstellen Sie hier Ihre Ansichten.

def home(request):
    """
    Rendert die Startseite mit einer Karte von Deutschland.

    Args:
        request: Die HTTP-Anfrage.

    Returns:
        Eine gerenderte HTML-Seite mit einer eingebetteten Karte.
    """
    # Erstellen einer Folium-Karte, zentriert auf Deutschland
    m = folium.Map(location=[51.1657, 10.4515], zoom_start=6)

    # Ausgewählte Region aus der Anfrage erhalten, Standard ist 'kolkwitz'
    selected_region = request.GET.get('region', 'kolkwitz')

    # Pfad zu den GeoJSON-Dateien definieren
    geojson_dir = os.path.join(settings.BASE_DIR, 'static', 'geojson')
    geojson_file = os.path.join(geojson_dir, f'{selected_region}_komplett.geojson')

    # Laden der entsprechenden GeoJSON-Datei
    try:
        with open(geojson_file, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)

        # GeoJSON-Daten zur Karte hinzufügen
        folium.GeoJson(geojson_data).add_to(m)
    except FileNotFoundError:
        # Behandlung des Falls, wenn die Datei nicht gefunden wird
        print(f"GeoJSON-Datei nicht gefunden: {geojson_file}")
    except json.JSONDecodeError:
        print(f"Fehler beim Dekodieren der JSON-Datei: {geojson_file}")

    # Generieren des Karten-HTML
    map_html = m.get_root().render()

    # Übergeben des Karten-HTML an den Template-Kontext
    context = {
        'map_html': map_html,
    }

    return render(request, 'base.html', context)

def weather(request):
    """
    Liefert Wetterdaten für eine angegebene Stadt.

    Args:
        request: Die HTTP-Anfrage mit einem optionalen 'city' Parameter.

    Returns:
        Ein JsonResponse-Objekt mit Wetterdaten oder einer Fehlermeldung.
    """
    city = request.GET.get('city', 'Berlin')
    weather_data = get_weather(city)
    if weather_data:
        return JsonResponse(weather_data)
    else:
        return JsonResponse({'error': 'Wetterdaten konnten nicht abgerufen werden'}, status=400)

def update_map(request):
    """
    Aktualisiert die Karte basierend auf der ausgewählten Region.

    Args:
        request: Die HTTP-Anfrage mit einem 'region' Parameter.

    Returns:
        Ein JsonResponse-Objekt mit GeoJSON-Daten, Kartenzentrum und Zoomstufe.
    """
    selected_region = request.GET.get('region', 'kolkwitz')
    geojson_dir = os.path.join(settings.BASE_DIR, 'static', 'geojson')
    geojson_file = os.path.join(geojson_dir, f'{selected_region}_komplett.geojson')

    try:
        with open(geojson_file, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)

        # Berechnung des Zentrums der GeoJSON-Daten
        bounds = folium.GeoJson(geojson_data).get_bounds()
        center = [(bounds[0][0] + bounds[1][0]) / 2, (bounds[0][1] + bounds[1][1]) / 2]

        return JsonResponse({
            'geojson': geojson_data,
            'center': {'lat': center[0], 'lng': center[1]},
            'zoom': 10  # Sie können diese Zoomstufe nach Bedarf anpassen
        })
    except FileNotFoundError:
        return JsonResponse({'error': 'GeoJSON-Datei nicht gefunden'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Fehler beim Dekodieren der JSON-Datei'}, status=500)
