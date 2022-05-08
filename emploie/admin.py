from django.contrib import admin

from semestre.models import AnneUniversitaire
from .models import Salle, TypeSalle


""" EQUIPE : CODEVERSE
    @author : KANNOUFA FATIMA EZZAHRA
"""

admin.site.register(Salle)
admin.site.register(TypeSalle)
admin.site.register(AnneUniversitaire)