from django.urls import path
from . import views


urlpatterns = [
    path('r^login', views.UserLoginView.as_view())
]