"""
Dieses Modul definiert die Konfiguration für die 'core' App.

Es enthält die CoreConfig-Klasse, die von Django verwendet wird,
um app-spezifische Konfigurationen zu verwalten.
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Konfigurationsklasse für die 'core' App.

    Attribute:
        default_auto_field (str): Legt das Standard-Datenbankfeld für automatisch generierte IDs fest.
        name (str): Definiert den Namen der App, wie er von Django verwendet wird.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
