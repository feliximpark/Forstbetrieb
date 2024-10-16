from django.shortcuts import render
from django.http import JsonResponse
from .weather import get_weather
import folium
import json
import os
from django.conf import settings

# Create your views here.

def home(request):
    # Create a Folium map centered on Germany
    m = folium.Map(location=[51.1657, 10.4515], zoom_start=6)

    # Get the selected region from the request, default to 'kolkwitz'
    selected_region = request.GET.get('region', 'kolkwitz')

    # Define the path to the geojson files
    geojson_dir = os.path.join(settings.BASE_DIR, 'static', 'geojson')
    geojson_file = os.path.join(geojson_dir, f'{selected_region}_komplett.geojson')

    # Load the appropriate geojson file
    try:
        with open(geojson_file, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)

        # Add the geojson data to the map
        folium.GeoJson(geojson_data).add_to(m)
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"GeoJSON file not found: {geojson_file}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {geojson_file}")

    # Generate the map HTML
    map_html = m.get_root().render()

    # Pass the map HTML to the template context
    context = {
        'map_html': map_html,
    }

    return render(request, 'base.html', context)

def weather(request):
    city = request.GET.get('city', 'Berlin')
    weather_data = get_weather(city)
    if weather_data:
        return JsonResponse(weather_data)
    else:
        return JsonResponse({'error': 'Unable to fetch weather data'}, status=400)

def update_map(request):
    selected_region = request.GET.get('region', 'kolkwitz')
    geojson_dir = os.path.join(settings.BASE_DIR, 'static', 'geojson')
    geojson_file = os.path.join(geojson_dir, f'{selected_region}_komplett.geojson')

    try:
        with open(geojson_file, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)

        # Calculate the center of the GeoJSON data
        bounds = folium.GeoJson(geojson_data).get_bounds()
        center = [(bounds[0][0] + bounds[1][0]) / 2, (bounds[0][1] + bounds[1][1]) / 2]

        return JsonResponse({
            'geojson': geojson_data,
            'center': {'lat': center[0], 'lng': center[1]},
            'zoom': 10  # You can adjust this zoom level as needed
        })
    except FileNotFoundError:
        return JsonResponse({'error': 'GeoJSON file not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Error decoding JSON file'}, status=500)
