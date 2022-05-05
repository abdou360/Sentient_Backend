from django.contrib import admin
from .models import Salle, TypeSalle

# Register your models here.
admin.site.register(Salle)
admin.site.register(TypeSalle)