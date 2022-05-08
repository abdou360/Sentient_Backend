from django.contrib import admin

from django.urls import path, include,re_path
# from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', include('users.urls')),
    path('filiere_etab/', include('filiere.urls')),
    path('emploie/',include('emploie.urls')),
    path('cours/', include('cours.urls')),
    path('', include('module.urls')),
    path('semestre/',include('semestre.urls.index')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
