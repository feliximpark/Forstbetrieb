"""
Dieses Modul definiert die Datenbankmodelle für die 'core' App.

Hier werden die Datenstrukturen und Beziehungen für die Kernfunktionalitäten
der Forstapp definiert. Jedes Modell repräsentiert eine Tabelle in der Datenbank
und definiert die Felder und das Verhalten dieser Tabelle.

Beispiele für mögliche Modelle könnten sein:
- Wald: Repräsentiert einen Waldbestand mit Eigenschaften wie Name, Fläche, etc.
- Baum: Repräsentiert einzelne Bäume mit Eigenschaften wie Art, Alter, Position, etc.
- Abteilung: Repräsentiert Unterabteilungen eines Waldes.

Verwenden Sie die Django Model-Klasse, um neue Modelle zu definieren.
"""

from django.db import models

# Create your models here.
# Beispiel:
# class Wald(models.Model):
#     name = models.CharField(max_length=100)
#     flaeche = models.FloatField()
#     # Weitere Felder...
