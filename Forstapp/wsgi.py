"""
WSGI-Konfiguration für das Forstapp-Projekt.

Es stellt die WSGI-Anwendung als Modul-Level-Variable namens `application` bereit.

Für weitere Informationen zu dieser Datei siehe:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Setzt die Standard-Django-Einstellungen für die WSGI-Anwendung
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Forstapp.settings')

# Erstellt die WSGI-Anwendung
application = get_wsgi_application()
