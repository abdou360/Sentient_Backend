
""" EQUIPE : CodeVerse et ARopedia
    @authors :  + KANNOUFA F. EZZAHRA
                + FIROUD REDA
                + MOUZAFIR ABDELHADI
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .api.views import *

urlpatterns = [
    # machine learning : learning par web 
    path('create_dataset_submit/', test_module_submit),
    path('training/<str:filiere>/<str:niveau>/<str:groupe>/', training , name ='training'),
    path('testerModel/', TesterModel , name ='testerModel'),
    
    # gest_presence : admin dashbord
    path('gestion-presence-modele/', EntrainementAdminDash , name ='EntrainementAdminDash'),
    path('filieres-json/', get_json_filiere_data, name="jsonFilieres"),
    path('niveaux-json/<str:filiere>/', get_json_niveau_data, name="jsonNiveaux"),
    path('groupes-json/<str:niveau>/', get_json_group_data, name="jsonGroupes"),
    
    # rest framework 
    path('mobile/filieres', filiere_liste, name='filiere_liste'),
    path('mobile/niveau/<str:nom_filiere>', Niveau_liste, name='niveau_liste'),
    path('mobile/niveau_Choisi', post_niveau, name='post_niveau'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



