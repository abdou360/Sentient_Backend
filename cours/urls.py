
from django import views
from django.urls import path
# from .views import chapitres_list
from django.urls import path
from cours.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', chapitres_list, name='chapitres_list'),
    path('add_chapitre', add_chapitre, name='add_chapitre'),
    path('update_chapitre/<int:id>', update_chapitre, name='update_chapitre'),
     path('chapitre/<int:id>', chapitre_details, name='chapitre_details'),
    path('delete_chapitre/<int:id>', delete_chapitre, name='delete_chapitre'),
    
    path('delete_traitement/<int:id>', delete_Traitement, name='delete_traitement'),
    path('add_traitement/<int:id>', add_traitement, name='add_traitement'),

    path('delete_document/<int:id>', delete_document, name='delete_document'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
