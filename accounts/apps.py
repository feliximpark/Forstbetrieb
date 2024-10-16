"""
Dieses Modul definiert die Konfiguration für die 'accounts' App.
Es enthält die AccountsConfig-Klasse, die von Django verwendet wird,
um app-spezifische Konfigurationen zu verwalten.
"""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Konfigurationsklasse für die 'accounts' App.
    Diese Klasse wird von Django verwendet, um app-spezifische Einstellungen zu definieren.
    """
    # Legt das Standard-Datenbankfeld für automatisch generierte IDs fest
    default_auto_field = 'django.db.models.BigAutoField'
    # Definiert den Namen der App, wie er von Django verwendet wird
    name = 'accounts'
