from django.urls import path,include
from semestre.views.niveau import views

urlpatterns = [
    path('', views.niveau_form,name='niveau_insert'), # get and post req. for insert operation
    path('<int:id>/', views.niveau_form,name='niveau_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.niveau_delete,name='niveau_delete'),
    path('list/',views.niveau_list,name='niveau_list') # get req. to retrieve and display all records
]