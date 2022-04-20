
from django import views
from django.urls import path
# from .views import chapitres_list
from django.conf.urls import url
from django.urls import path, include
from cours.views import chapitres_list, add_chapitre, delete_chapitre, update_chapitre,chapitre_details

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', chapitres_list, name='chapitres_list'),
    path('add_chapitre', add_chapitre, name='add_chapitre'),
    path('update_chapitre/<int:id>', update_chapitre, name='update_chapitre'),
     path('chapitre/<int:id>', chapitre_details, name='chapitre_details'),
    path('delete_chapitre/<int:id>', delete_chapitre, name='delete_chapitre'),
    
    # path('', home, name='users-home'),
    
#     path('register/', RegisterView.as_view(), name='users-register'),
#     path('profile/', profile, name='users-profile'),
#      path('admin/', admin.site.urls),

#     path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
#                                            authentication_form=LoginForm), name='login'),

#     path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

#     path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

#     path('password-reset-confirm/<uidb64>/<token>/',
#          auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
#          name='password_reset_confirm'),

#     path('password-reset-complete/',
#          auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
#          name='password_reset_complete'),

#     path('password-change/', ChangePasswordView.as_view(), name='password_change'),

#     url(r'^oauth/', include('social_django.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
