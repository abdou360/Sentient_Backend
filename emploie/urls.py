from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import EmploieProf, ListePresence

""" RESPONSABLE : CODEVERSE
"""

urlpatterns = [
    path('emploi-prof/', EmploieProf, name='emploiProfesseur'),
    path('liste-presence/<str:filiere>/<int:idSeance>/', ListePresence, name='ListePresence'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
