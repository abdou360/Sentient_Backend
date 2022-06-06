from django.contrib import admin

from django.urls import path, include,re_path
# from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #path('admin', admin.site.urls),

    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('filiere_etab/', include('filiere.urls')),
    path('emploie/',include('emploie.urls')),
    path('cours/', include('cours.urls')),
    path('', include('module.urls')),
    path('semestre/',include('semestre.urls.index')),
    path('face-recognition/',include('face_recognition.urls')),
    path('api/user/', include('users.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
