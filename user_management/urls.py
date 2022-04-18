from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('users.urls')),
    path('cours/', include('cours.urls')),
    path('niveau/',include('semestre.urls.niveau.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
