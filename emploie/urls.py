
""" EQUIPE : CODEVERSE
    @author :   + FIROUDA REDA et OUSSAHI SALMA 
                + KANNOUFA FATIMA EZZAHRA
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .api.views import *


urlpatterns = [
    
    # espace admin
    path('emploie-admin/', EmploieAdmin, name='emploiAdmin'),
    path('AddPlanning/', AddPlanning, name='AddPlanning'),
    path('GetGroupes/', GetGroupes, name='GetGroupes'),
    path('GetNiveaux/', GetNiveaux, name='GetNiveaux'),
    path('SendGroupes/', SendGroupes, name='SendGroupes'),
    path('all/', all,name='all'),  
    path('edit/<int:id>', edit),  
    path('update/<int:id>', update),  
    path('delete/<int:id>',destroy, name='destroy'),  
    
    
    # ecpace prof :
    path('emploi-prof/', EmploieProf, name='emploiProfesseur'),
    path('liste-presence/<slug:slug>/<int:idSeance>/', ListePresence, name='ListePresence'),
    path('modifier-presence/<int:idSeance>/<int:idEtudiant>/', ModifierPresence, name='ModifierPresence'),
 
    
    # API
    path('api/prof/<int:idProf>/seances', getSeances),
    path('api/classes-json/<str:planning_id>', get_json_classe_data, name="jsonClasses"),
    path('api/modules-json/', get_json_module_data, name="jsonModules"),
    path('api/seances-json/<str:car>/', get_json_seance_data, name="jsonSeances"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
