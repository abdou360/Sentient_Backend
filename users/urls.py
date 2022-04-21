from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from users import views
from users.views import home
from django.contrib.auth.views import LoginView, LogoutView
from . import AdminViews, TeacherViews, StudentViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='users-home'),
    
    # Users Login :
    path('login', views.loginPage, name="login"),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('admin_home/', AdminViews.admin_home, name="admin_home"),
    
    
    path('add_teacher/', AdminViews.add_teacher, name="add_teacher"),
    path('add_teacher_save/', AdminViews.add_teacher_save, name="add_teacher_save"),
    path('manage_teacher/', AdminViews.manage_teacher, name="manage_teacher"),
    path('edit_teacher/<teacher_id>/', AdminViews.edit_teacher, name="edit_teacher"),
    path('edit_teacher_save/', AdminViews.edit_teacher_save, name="edit_teacher_save"),
    path('delete_teacher/<teacher_id>/', AdminViews.delete_teacher, name="delete_teacher"),

    path('manage_session/', AdminViews.manage_session, name="manage_session"),
    path('add_session/', AdminViews.add_session, name="add_session"),
    path('add_session_save/', AdminViews.add_session_save, name="add_session_save"),
    path('edit_session/<session_id>', AdminViews.edit_session, name="edit_session"),
    path('edit_session_save/', AdminViews.edit_session_save, name="edit_session_save"),
    path('delete_session/<session_id>/', AdminViews.delete_session, name="delete_session"),
    
    path('add_student/', AdminViews.add_student, name="add_student"),
    path('add_student_save/', AdminViews.add_student_save, name="add_student_save"),
    path('edit_student/<student_id>', AdminViews.edit_student, name="edit_student"),
    path('edit_student_save/', AdminViews.edit_student_save, name="edit_student_save"),
    path('manage_student/', AdminViews.manage_student, name="manage_student"),
    path('delete_student/<student_id>/', AdminViews.delete_student, name="delete_student"),
    
    path('admin_profile/', AdminViews.admin_profile, name="admin_profile"),
    path('admin_profile_update/', AdminViews.admin_profile_update, name="admin_profile_update"),
    


    # URLS for teacher
    path('teacher_home/', TeacherViews.teacher_home, name="teacher_home"),
    # path('get_students/', TeacherViews.get_students, name="get_students"),
    path('teacher_profile/', TeacherViews.teacher_profile, name="teacher_profile"),
    path('teacher_profile_update/', TeacherViews.teacher_profile_update, name="teacher_profile_update"),

    # URSL for Student
    path('student_home/', StudentViews.student_home, name="student_home"),
    path('student_profile/', StudentViews.student_profile, name="student_profile"),
    path('student_profile_update/', StudentViews.student_profile_update, name="student_profile_update"),

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
from .views import home, profile, RegisterView
from django.urls import path, include, re_path


urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
     path('admin/', admin.site.urls),

    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

     re_path(r'^oauth/', include('social_django.urls', namespace='social')),
]
>>>>>>> ecaf05613685bad4c664a487587c9d81ef7f8e59
