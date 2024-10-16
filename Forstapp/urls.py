"""
URL-Konfiguration für das Forstapp-Projekt.

Die `urlpatterns`-Liste leitet URLs zu Views weiter. Weitere Informationen finden Sie unter:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Beispiele:
Funktionsbasierte Views
    1. Import hinzufügen:  from my_app import views
    2. URL zu urlpatterns hinzufügen:  path('', views.home, name='home')
Klassenbasierte Views
    1. Import hinzufügen:  from other_app.views import Home
    2. URL zu urlpatterns hinzufügen:  path('', Home.as_view(), name='home')
Einbinden einer anderen URLconf
    1. Importieren Sie die include()-Funktion: from django.urls import include, path
    2. URL zu urlpatterns hinzufügen:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from core import views

urlpatterns = [
    # URL für die Django-Admin-Oberfläche
    path('admin/', admin.site.urls),

    # Startseite, nur für eingeloggte Benutzer zugänglich
    path('', login_required(views.home), name='home'),

    # URL zum Aktualisieren der Karte, nur für eingeloggte Benutzer
    path('update_map/', login_required(views.update_map), name='update_map'),

    # URL für die Login-Seite
    path('accounts/login/', LoginView.as_view(), name='login'),

    # URL für die Logout-Funktion
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
