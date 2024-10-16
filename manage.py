#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
"""
Django-Befehlszeilen-Dienstprogramm für administrative Aufgaben.

Diese Datei dient als Einstiegspunkt für die Verwaltung des Django-Projekts.
Sie ermöglicht die Ausführung verschiedener Verwaltungsbefehle wie:
- Starten des Entwicklungsservers
- Durchführen von Datenbankmigration
- Erstellen von Superuser-Konten
- und viele andere administrative Aufgaben

Die Hauptfunktion 'main()' konfiguriert die Django-Umgebung und führt
den angegebenen Verwaltungsbefehl aus.
"""
import os
import sys


def main():
    """Führt administrative Aufgaben aus."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Forstapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django konnte nicht importiert werden. Sind Sie sicher, dass es installiert ist und "
            "in der PYTHONPATH-Umgebungsvariable verfügbar ist? Haben Sie vergessen, "
            "eine virtuelle Umgebung zu aktivieren?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
