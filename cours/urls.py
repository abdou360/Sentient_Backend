
from django import views
from django.urls import path
# from .views import chapitres_list
from django.urls import path
from cours.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', chapitres_list, name='chapitres_list'),
    path('filiere=<str:val>',
         search_chapitres_by_filiere, name="search_chapitres_by_filiere"),
    path('niveau=<str:val>',
         search_chapitres_by_niveau, name="search_chapitres_by_niveau"),
    path('module=<str:val>',
         search_chapitres_by_element_module, name="search_chapitres_by_element_module"),
    path('annee=<str:val>',
         search_chapitres_by_annee, name="search_chapitres_by_annee"),

    path('add_chapitre', add_chapitre, name='add_chapitre'),
    path('update_chapitre/<int:id>', update_chapitre, name='update_chapitre'),
    path('chapitre/<int:id>', chapitre_details, name='chapitre_details'),
    path('delete_chapitre/<int:id>', delete_chapitre, name='delete_chapitre'),

    path('delete_traitement/<int:id>',
         delete_Traitement, name='delete_traitement'),
    path('add_traitement/<int:id>', add_traitement, name='add_traitement'),
    path('update_traitement/<int:id>',
         update_traitement, name='update_traitement'),


    path('traitement_details',
         traitement_details, name='traitement_details'),

    path('delete_document/<int:id>', delete_document, name='delete_document'),


    path('api/chapitres', chapitres_list_api, name='chapitres_list_api'),
    path('api/chapitre/<int:id_chapitre>',
         chapitre_details_api, name='chapitre_details_api'),
    path('api/traitements/<int:id_chapitre>',
         traitements_list_api, name='traitements_list_api'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
