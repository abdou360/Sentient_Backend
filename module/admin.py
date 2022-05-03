from django.contrib import admin
from filiere.models import Etablissement, Filiere
from semestre.models import Niveau, Semestre


# Register your models here.

admin.site.register(Niveau)
admin.site.register(Semestre)
admin.site.register(Filiere)
admin.site.register(Etablissement)