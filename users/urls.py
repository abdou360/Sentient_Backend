from django.contrib import admin
from django.urls import path
from users import views, PermissionsView, rolesView
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
    path('edit_student_save/<int:id>', AdminViews.edit_student_save, name="edit_student_save"),
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

    # Permissions
    path('add_permission/', PermissionsView.addPermission, name="add_permission"),
    path('add_permission_save/', PermissionsView.addPermissionSave, name="add_permission_save"),
    path('edit_permission/<int:id>', PermissionsView.editPermission, name="edit_permission"),
    path('edit_permission_save/<int:id>', PermissionsView.editPermissionSave, name="edit_permission_save"),
    path('delete_permission/<int:id>', PermissionsView.deletePermission, name="delete_permission"),
    path('manage_permissions', PermissionsView.managePermission, name="manage_permissions"),


    # Roles
    path('manage_roles', rolesView.manageRoles, name="manage_roles"),
    path('add_role', rolesView.addRole, name="add_role"),
    path('add_role_save', rolesView.addRoleSave, name="add_role_save"),
    path('edit_role/<int:id>', rolesView.editRole, name="edit_role"),
    path('edit_role_save/<int:id>', rolesView.editRoleSave, name="edit_role_save"),
    path('delete_role/<int:id>', rolesView.deleteRole, name="delete_role"),
    path('delete_role_permission/<int:id1>/<int:id2>', rolesView.deleteRolePermission, name="delete_role_permission"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
