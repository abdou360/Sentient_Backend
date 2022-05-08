
""" EQUIPE : CODEVERSE
    @author : KANNOUFA FATIMA EZZAHRA
"""

from django.urls import path
from .views import getSeances

urlpatterns = [
    path('api/prof/<int:idProf>/seances', getSeances),
]
