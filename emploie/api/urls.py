
""" EQUIPE : CODEVERSE
    @author : KANNOUFA FATIMA EZZAHRA
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('api/prof/<int:idProf>/seances', getSeances),
    path('api/classes-json/', get_json_classe_data, name="jsonClasses"),
    path('api/modules-json/<str:car>/', get_json_module_data, name="jsonModules"),
]
