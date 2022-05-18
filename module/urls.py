from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from module import ModuleViews , views
from django.contrib import admin

urlpatterns = [
    #*@author ABDELHADI MOUZAFIR BEGIN
    
    path('modules/filieres', ModuleViews.display_majors, name = "display_majors"),
    path('modules/<str:name_>/niveaux', ModuleViews.display_levels, name = "display_levels"),
    path('modules/add_module', ModuleViews.add_module, name = "add_module"),
    path('modules/<str:name_>/modules/add_module_level', ModuleViews.add_module_level, name = "add_module_level"),
    path('add_module_save', ModuleViews.add_module_save),
    path('modules/modules', ModuleViews.manage_modules ,name ="manage_modules"),
    path('delete_module/<str:id_>', ModuleViews.delete_module, name="delete_module"),
    path('delete_elem_module/<str:id_>', ModuleViews.delete_elem_module, name="delete_elem_module"),
    path('edit_module_save', ModuleViews.edit_module_save),
    path('edit_module/<str:name_>/<str:id_>', ModuleViews.edit_module),
    path('modules/modules/filtrebySemestre<str:name_>', ModuleViews.search_modules_semestres , name="search_modules_semestres"),
    path('modules/modules/filtrebyFiliere<str:name_>', ModuleViews.search_modules_filiere , name="search_modules_filiere"),
    path('modules/modules/filtrebyNiveau<str:name_>', ModuleViews.search_modules_niveau , name="search_modules_niveau"),
    path('modules/<str:name_>/modules/add_element_module_level', ModuleViews.add_element_module_level , name="add_element_module_level"),
    path('add_element_module_save', ModuleViews.add_element_module_save),
    path('modules/elements_module', ModuleViews.manage_elem_modules ,name ="manage_elem_modules"),
    path('modules/modules/search_module',ModuleViews.search_module ,name = "search_module"),
    path('modules/elements_module/search_elem_module',ModuleViews.search_elem_module ,name = "search_elem_module"),
    path('modules/elements_module/filtrebyFiliere<str:name_>', ModuleViews.search_elem_modules_filiere , name="search_elem_modules_filiere"),
    path('modules/elements_module/filtrebyNiveau<str:name_>', ModuleViews.search_elem_modules_niveau , name="search_elem_modules_niveau"),
    path('modules/elements_module/filtrebySemestre<str:name_>', ModuleViews.search_elem_modules_semestres , name="search_elem_modules_semestres"),
    path('modules/elements_module/filtrebyModule<str:name_>', ModuleViews.search_elem_modules_modules , name="search_elem_modules_modules"),
    path('edit_element_module_level/<str:name_>/<str:id_>', ModuleViews.edit_element_module_level, name="edit_element_module_level"),
    path('edit_element_module_save', ModuleViews.edit_element_module_save),
    # machine learning : learning par web 
    path('create_dataset_submit', views.test_module_submit),
    path('create_dataset', views.test_module),
    path('video_feed/<str:id>', views.video_feed, name='video_feed'),
    path('training', views.training , name ='training'),
    # rest framework 
    path('mobile/filieres', views.filiere_liste, name='filiere_liste'),
    path('mobile/niveau/<int:id>', views.Niveau_liste, name='niveau_liste'),
    path('mobile/niveau_Choisi', views.post_niveau, name='post_niveau'),
    
    
    #*@author ABDELHADI MOUZAFIR END
    
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



