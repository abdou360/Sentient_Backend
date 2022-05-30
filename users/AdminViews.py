from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage  # To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from semestre.models import Groupe
from users.models import CustomUser, Professeur, Students



def admin_home(request):
    all_student_count = Students.objects.all().count()
    # course_count = Courses.objects.all().count()
    all_teacher_count = Professeur.objects.all().count()

    # Total Subjects and students in Each Module

    # For Teachers : Statistics

    # For Students : Statistics

    context = {
        "all_student_count": all_student_count,
        "all_teacher_count": all_teacher_count
    }
    return render(request, "admin/home_content.html", context)


def add_teacher(request):
    return render(request, "admin/add_teacher_template.html")


def add_teacher_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_teacher')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        specialite = request.POST.get('specialite')
        matricule = request.POST.get('matricule')
        telephone = request.POST.get('telephone')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            user.teacher.specialite = specialite
            user.teacher.matricule = matricule
            user.teacher.telephone = telephone
            user.save()
            messages.success(request, "teacher Added Successfully!")
            return redirect('add_teacher')
        except:
            messages.error(request, "Failed to Add teacher!")
            return redirect('add_teacher')



def manage_teacher(request):
    teachers = Professeur.objects.all()
    context = {
        "teachers": teachers
    }
    return render(request, "admin/manage_teacher_template.html", context)


def edit_teacher(request, teacher_id):
    teacher = Professeur.objects.get(admin=teacher_id)

    context = {
        "teacher": teacher,
        "id": teacher_id
    }
    return render(request, "admin/edit_teacher_template.html", context)


def edit_teacher_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        teacher_id = request.POST.get('teacher_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        specialite = request.POST.get('specialite')
        matricule = request.POST.get('matricule')
        telephone = request.POST.get('telephone')

        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=teacher_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            # INSERTING into Professeur Model
            teacher_model = Professeur.objects.get(admin=teacher_id)
            teacher_model.specialite = specialite
            teacher_model.matricule = matricule
            teacher_model.telephone = telephone
            teacher_model.save()

            messages.success(request, "Teacher Updated Successfully !")
            return redirect('/edit_teacher/'+teacher_id)

        except:
            messages.error(request, "Failed to Update teacher !")
            return redirect('/edit_teacher/'+teacher_id)



def delete_teacher(request, teacher_id):
    teacher = Professeur.objects.get(admin=teacher_id)
    try:
        teacher.delete()
        messages.success(request, "teacher Deleted Successfully.")
        return redirect('manage_teacher')
    except:
        messages.error(request, "Failed to Delete teacher.")
        return redirect('manage_teacher')


def add_user(request):
    return render(request, "admin/add_user_template.html")


def add_user_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_teacher')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')


        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
            user.save()
            messages.success(request, "User Added Successfully !")
            return redirect('add_user')
        except:
            messages.error(request, "Failed to Add User !")
            return redirect('add_user')



def manage_user(request):
    users = CustomUser.objects.all()
    context = {
        "users": users
    }
    return render(request, "admin/manage_user_template.html", context)


def edit_user(request, user_id):
    user = CustomUser.objects.get(admin=user_id)

    context = {
        "user": user,
        "id": user_id
    }
    return render(request, "admin/edit_user_template.html", context)


def edit_user_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user_id = request.POST.get('teacher_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=user_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            messages.success(request, "user Updated Successfully !")
            return redirect('/edit_user/'+user_id)

        except:
            messages.error(request, "Failed to Update user !")
            return redirect('/edit_user/'+user_id)



def delete_user(request, user_id):
    user = CustomUser.objects.get(admin=user_id)
    try:
        user.delete()
        messages.success(request, "user Deleted Successfully.")
        return redirect('manage_user')
    except:
        messages.error(request, "Failed to Delete user.")
        return redirect('manage_user')
    
# def add_course(request):

# def add_course_save(request):

# def manage_course(request):

# def edit_course(request, course_id):

# def edit_course_save(request):

# def delete_course(request, course_id):

# def manage_session(request):
#     session_years = SessionYearModel.objects.all()
#     context = {
#         "session_years": session_years
#     }
#     return render(request, "admin/manage_session_template.html", context)


# def add_session(request):
#     return render(request, "admin/add_session_template.html")


# def add_session_save(request):
#     if request.method != "POST":
#         messages.error(request, "Invalid Method")
#         # return redirect('add_course')
#     else:
#         session_start_year = request.POST.get('session_start_year')
#         session_end_year = request.POST.get('session_end_year')
#         try:
#             sessionyear = SessionYearModel(session_start_year=session_start_year, session_end_year=session_end_year)
#             sessionyear.save()
#             messages.success(request, "Session Year added Successfully!")
#             return redirect("add_session")
#         except:
#             messages.error(request, "Failed to Add Session Year")
#             return redirect("add_session")


# def edit_session(request, session_id):
#     session_year = SessionYearModel.objects.get(id=session_id)
#     context = {
#         "session_year": session_year
#     }
#     return render(request, "admin/edit_session_template.html", context)


# def edit_session_save(request):
#     if request.method != "POST":
#         messages.error(request, "Invalid Method!")
#         return redirect('manage_session')
#     else:
#         session_id = request.POST.get('session_id')
#         session_start_year = request.POST.get('session_start_year')
#         session_end_year = request.POST.get('session_end_year')

#         try:
#             session_year = SessionYearModel.objects.get(id=session_id)
#             session_year.session_start_year = session_start_year
#             session_year.session_end_year = session_end_year
#             session_year.save()

#             messages.success(request, "Session Year Updated Successfully.")
#             return redirect('/edit_session/' + session_id)
#         except:
#             messages.error(request, "Failed to Update Session Year.")
#             return redirect('/edit_session/' + session_id)


# def delete_session(request, session_id):
#     session = SessionYearModel.objects.get(id=session_id)
#     try:
#         session.delete()
#         messages.success(request, "Session Deleted Successfully.")
#         return redirect('manage_session')
#     except:
#         messages.error(request, "Failed to Delete Session.")
#         return redirect('manage_session')



# if request.method != "POST":
#     return HttpResponse("Invalid Method!")
# else:
#     student_id = request.session.get('student_id')
#     if student_id == None:
#         return redirect('/manage_student')
#
#     form = EditStudentForm(request.POST, request.FILES)
#     if form.is_valid():
#         email = form.cleaned_data['email']
#         username = form.cleaned_data['username']
#         first_name = form.cleaned_data['first_name']
#         last_name = form.cleaned_data['last_name']
#         specialite = form.cleaned_data['address']
#
#         cne = form.cleaned_data['cne']
#         gender = form.cleaned_data['gender']
#         session_year_id = form.cleaned_data['session_year_id']
#
#         # Getting Profile Pic first
#         # First Check whether the file is selected or not
#         # Upload only if file is selected
#         if len(request.FILES) != 0:
#             profile_pic = request.FILES['profile_pic']
#             fs = FileSystemStorage()
#             filename = fs.save(profile_pic.name, profile_pic)
#             profile_pic_url = fs.url(filename)
#         else:
#             profile_pic_url = None
#
#         try:
#             # First Update into Custom User Model
#             user = CustomUser.objects.get(id=student_id)
#             user.first_name = first_name
#             user.last_name = last_name
#             user.email = email
#             user.username = username
#             user.save()
#
#             # Then Update Students Table
#             student_model = Students.objects.get(admin=student_id)
#             student_model.address = address
#             student_model.cne = cne
#
#             session_year_obj = SessionYearModel.objects.get(id=session_year_id)
#             student_model.session_year_id = session_year_obj
#
#             student_model.gender = gender
#             if profile_pic_url != None:
#                 student_model.profile_pic = profile_pic_url
#             student_model.save()
#             # Delete student_id SESSION after the data is updated
#             del request.session['student_id']
#
#             messages.success(request, "Student Updated Successfully!")
#             return redirect('/edit_student/' + student_id)
#         except:
#             messages.success(request, "Failed to Uupdate Student.")
#             return redirect('/edit_student/' + student_id)
#     else:
#         return redirect('/edit_student/' + student_id)

def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context = {
        "user": user
    }
    return render(request, 'admin/admin_profile.html', context)


def admin_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('admin/admin_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('admin/admin_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('admin/admin_profile')


def teacher_profile(request):
    pass


def student_profile(requtest):
    pass

