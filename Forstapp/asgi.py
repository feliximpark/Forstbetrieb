"""
ASGI-Konfiguration für das Forstapp-Projekt.

Es stellt die ASGI-Anwendung als Modul-Level-Variable namens `application` bereit.

Für weitere Informationen zu dieser Datei siehe:
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Setzt die Standard-Django-Einstellungen für die ASGI-Anwendung
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Forstapp.settings')

# Erstellt die ASGI-Anwendung
application = get_asgi_application()
