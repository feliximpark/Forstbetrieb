"""
Django-Einstellungen für das Forstapp-Projekt.

Generiert durch 'django-admin startproject' mit Django 5.1.2.

Für weitere Informationen zu dieser Datei siehe:
https://docs.djangoproject.com/en/5.1/topics/settings/

Für die vollständige Liste der Einstellungen und ihre Werte siehe:
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Erstellt Pfade innerhalb des Projekts wie folgt: BASE_DIR / 'subdir'.
# BASE_DIR ist das Stammverzeichnis des Projekts und wird für relative Pfadangaben verwendet.
BASE_DIR = Path(__file__).resolve().parent.parent


# Schnellstart-Entwicklungseinstellungen - ungeeignet für die Produktion
# Siehe https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SICHERHEITSWARNUNG: Halten Sie den in der Produktion verwendeten Geheimschlüssel geheim!
SECRET_KEY = 'django-insecure-tew$x#_f#bf5)^jmn(=law@*82#xlq5zskqefg-&_#rr5+8zes'

# SICHERHEITSWARNUNG: Führen Sie die Anwendung nicht mit aktiviertem Debug-Modus in der Produktion aus!
DEBUG = True

ALLOWED_HOSTS = []


# Anwendungsdefinition
# Hier werden alle installierten Django-Apps aufgelistet, einschließlich der benutzerdefinierten Apps 'core' und 'accounts'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'accounts',
]

# Definiert die Umleitungs-URLs nach dem Login und Logout
LOGIN_REDIRECT_URL = '/'  # Benutzer werden nach dem Login zur Startseite weitergeleitet
LOGOUT_REDIRECT_URL = '/'  # Benutzer werden nach dem Logout zur Startseite weitergeleitet

# Middleware-Konfiguration
# Diese Klassen verarbeiten Anfragen/Antworten global für das Projekt
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Forstapp.urls'

# Template-Konfiguration
# Definiert, wie Django Templates findet und verarbeitet
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Forstapp.wsgi.application'


# Datenbank-Konfiguration
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Passwort-Validierung
# Definiert die Regeln für die Passwortstärke
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalisierung
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'  # Legt die Standardsprache fest

TIME_ZONE = 'UTC'  # Definiert die Zeitzone für die Anwendung

USE_I18N = True  # Aktiviert Django's Übersetzungssystem

USE_TZ = True  # Aktiviert die Zeitzonen-Unterstützung


# Statische Dateien (CSS, JavaScript, Bilder)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'  # URL-Präfix für statische Dateien

# Verzeichnisse, in denen Django nach statischen Dateien sucht
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']

# Standard-Primärschlüsselfeld-Typ
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
# Definiert den Standardtyp für automatisch erstellte Primärschlüssel
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# OpenWeatherMap API-Schlüssel
# SICHERHEITSWARNUNG: Halten Sie diesen Schlüssel in Produktionsumgebungen geheim
# Dieser Schlüssel wird für den Zugriff auf die OpenWeatherMap-API verwendet
OPENWEATHERMAP_API_KEY = 'your_api_key_here'
