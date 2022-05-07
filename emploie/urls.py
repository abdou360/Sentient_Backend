from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

""" RESPONSABLE : CODEVERSE
"""

urlpatterns = [
                  path('emploi-prof/', EmploieProf, name='emploiProfesseur'),
                  path('liste-presence/<str:filiere>/<int:idSeance>/', ListePresence, name='ListePresence'),
                  path('emploie-admin/', EmploieAdmin, name='emploiAdmin'),
                  path('GetGroupes/', GetGroupes, name='GetGroupes'),
                  path('GetNiveaux/', GetNiveaux, name='GetNiveaux'),
                  path('SendGroupes/', SendGroupes, name='SendGroupes'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
