"""
Dieses Modul definiert die Datenbankmodelle für die 'accounts' App.

Hier werden die Datenstrukturen und Beziehungen für die Benutzerverwaltung
der Forstapp definiert. Jedes Modell repräsentiert eine Tabelle in der Datenbank
und definiert die Felder und das Verhalten dieser Tabelle.

Beispiele für mögliche Modelle könnten sein:
- BenutzerProfil: Erweitert das Standard-User-Modell von Django mit zusätzlichen Feldern
- Berechtigung: Definiert spezifische Berechtigungen für verschiedene Benutzerrollen

Verwenden Sie die Django Model-Klasse, um neue Modelle zu definieren.
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Beispiel:
# class BenutzerProfil(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     position = models.CharField(max_length=100)
#     abteilung = models.CharField(max_length=100)
#     # Weitere Felder...
