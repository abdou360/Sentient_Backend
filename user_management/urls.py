from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('users.urls')),
    path('semestre/',include('semestre.urls.index')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
