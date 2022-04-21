from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    path('', include('users.urls')),
        
    path('niveau/',include('semestre.urls.niveau.urls')),
    
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
