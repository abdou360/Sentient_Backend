
""" EQUIPE : CODEVERSE
    @author : KANNOUFA FATIMA EZZAHRA
"""

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import EmploieProf, ListePresence, ModifierPresence
from .api.views import getSeances


urlpatterns = [
    path('emploi-prof/', EmploieProf, name='emploiProfesseur'),
    path('liste-presence/<slug:slug>/<int:idSeance>/', ListePresence, name='ListePresence'),
    path('modifier-presence/<int:idSeance>/<int:idEtudiant>/', ModifierPresence, name='ModifierPresence'),
    
    
    ### API
    path('api/prof/<int:idProf>/seances', getSeances),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
