from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .api.views import *


urlpatterns = [
    # prof
    path('emploi-prof/', EmploieProf, name='emploiProfesseur'),
    path('liste-presence/<slug:slug>/<int:idSeance>/', ListePresence, name='ListePresence'),
    
    # admin
    path('modifier-presence/<int:idSeance>/<int:idEtudiant>/', ModifierPresence, name='ModifierPresence'),
    path('emploie-admin/', EmploieAdmin, name='emploiAdmin'),
    path('GetGroupes/', GetGroupes, name='GetGroupes'),
    path('GetNiveaux/', GetNiveaux, name='GetNiveaux'),
    path('SendGroupes/', SendGroupes, name='SendGroupes'),
    
    ### API
    path('api/prof/<int:idProf>/seances', getSeances),
    path('api/classes-json/<str:planning_id>', get_json_classe_data, name="jsonClasses"),
    path('api/modules-json/', get_json_module_data, name="jsonModules"),
    path('api/seances-json/<str:car>/', get_json_seance_data, name="jsonSeances"),
    
                 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
