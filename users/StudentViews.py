import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage  # To upload Profile Picture
from django.urls import reverse
import datetime  # To Parse input DateTime into Python Date Time Object

from semestre.models import Groupe
from users.forms import EditStudentForm, AddStudentForm
from users.models import *
from users.roleForm import GroupeListForm
from rest_framework.decorators import api_view
from django.http import JsonResponse


def student_home(request):
    return render(request, "student/student_home_template.html")


def student_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    student = Students.objects.get(admin=user)

    context = {
        "user": user,
        "student": student
    }
    return render(request, 'student/student_profile.html', context)


def student_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('student_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()

            student = Students.objects.get(admin=customuser.id)
            student.address = address
            student.save()

            messages.success(request, "Profile Updated Successfully")
            return redirect('student_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('student_profile')


# UnivIt responsable : ismail errouk
# def add_student(request, id=0):
#     users = CustomUser.objects.all()
#     if request.method == 'GET':
#         if id == 0:
#             form = AddStudentForm()  # form vide
#         else:
#             student = Students.objects.get(pk=id)
#             form = AddStudentForm(instance=student)  # form remplie par employee
#
#         # return render(request, 'users/etudiants/etudiant_form.html', {'form': form, 'users': users})
#         return render(request, 'admin/add_student_template.html', {'form': form, 'users': users})
# UnivIt responsable : ismail errouk
def add_student(request, id=0):
    admins = Admin.objects.all()
    if request.method == 'GET':
        # form remplie par employee
        # return render(request, 'users/etudiants/etudiant_form.html', {'form': form, 'users': users})
        return render(request, 'student/add_student_template.html', {'admins': admins})


# UnivIt responsable : ismail errouk
# def add_student_save(request):
#     global student
#     form = AddStudentForm(request.POST, request.FILES)
#     if form.is_valid():
#         adresse = form.cleaned_data['adresse']
#         admin = form.cleaned_data['admin']
#         user = form.cleaned_data['user']
#         # print(admin.admin.admin)
#         print(user.username)
#         cne = form.cleaned_data['cne']
#         code_apogee = form.cleaned_data['code_apogee']
#         telephone = form.cleaned_data['telephone']
#         path_photos = form.cleaned_data['path_photos']
#         form.save()
#         student = Students.objects.get(cne=cne)
#
#     return redirect(to='add_student_groups', id=student.id)
# UnivIt responsable : ismail errouk
def add_student_save(request):
    global student
    if request.method == 'POST':
        admin = Admin.objects.get(id=request.POST['select_admin'])
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        user = CustomUser()
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.username = request.POST['first_name'] + '_' + request.POST['last_name']
        user.user_type = 'STUDENT'
        if request.POST['password'] == request.POST['confirm_password']:
            user.password = request.POST['password']
        user.save()
        student = Students()
        student.user = user
        student.admin = admin
        student.cne = request.POST['cne']
        student.adresse = request.POST['adresse']
        student.profile_pic = request.POST['profile_pic']
        student.path_photos = "module/dataset1/Etudiant_"+ first_name + "_" + last_name + "/"
        student.telephone = request.POST['telephone']
        student.code_apogee = request.POST['code_apogee']
        student.save()
    return redirect(to='add_student_groups', id=student.id)


@api_view(['GET'])
def getAllStudents(request):
    all_students = Students.objects.all()
    students = []
    for student in all_students:
        groupes = student.groupes.all()
        student_groupes = []
        for groupe in groupes:
            student_groupes.append({'nom groupe': groupe.nom_group, 'niveau': groupe.niveau.nom_niveau})
        students.append({
            'first_name': student.user.first_name,
            'last_name': student.user.last_name,
            'username': student.user.username,
            'email': student.user.email,
            'cne': student.cne,
            'adresse': student.adresse,
            'telephone': student.telephone,
            'code apogee': student.code_apogee,
            'path photos': student.path_photos,
            'groupes': student_groupes
        })
    return JsonResponse(students, safe=False)
    # return JsonResponse(students)


# UnivIt responsable : ismail errouk
def add_student_groups(request, id):
    context = {}
    context['form'] = GroupeListForm()
    context['id'] = id
    return render(request, "student/add_Student_Groupe_template.html", context)


# UnivIt responsable : ismail errouk
def add_student_groups_save(request, id):
    global temp
    context = {}
    form = GroupeListForm(request.POST or None)
    context['form'] = form
    if request.POST:
        if form.is_valid():
            temp = form.cleaned_data.get("Groupes")
        groupes = []
        for t in temp:
            print("hey " + t)
            groupes.append(Groupe.objects.get(pk=int(t)))
        student = Students.objects.get(pk=id)
        for groupe in groupes:
            student.groupes.add(groupe)
        student.save()

    return redirect(to='manage_student')


# UnivIt responsable : ismail errouk
def manage_student(request):
    students = Students.objects.all()
    context = {
        "students": students
    }
    return render(request, 'student/manage_student_template.html', context)


# UnivIt responsable : ismail errouk
def edit_student(request, student_id):
    # Adding Student ID into Session Variable
    request.session['student_id'] = student_id

    student = Students.objects.get(id=student_id)
    print(student.cne)
    form = EditStudentForm()
    # Filling the form with Data from Database
    form.fields['cne'].initial = student.cne
    form.fields['adresse'].initial = student.adresse
    form.fields['path_photos'].initial = student.path_photos
    form.fields['telephone'].initial = student.telephone
    form.fields['code_apogee'].initial = student.code_apogee

    context = {
        "id": student_id,
        "username": student.user.username,
        "student": student,
        "form": form
    }
    return render(request, "student/edit_student_template.html", context)


# UnivIt responsable : ismail errouk
def edit_student_save(request, id):
    # print('------------')
    # student = Students.objects.get(id=id)
    # form = EditStudentForm(request.POST, request.FILES)
    # if form.is_valid():
    #     student.cne = form.cleaned_data['cne']
    #     student.adresse = form.cleaned_data['adresse']
    #     student.path_photos = form.cleaned_data['path_photos']
    #     student.telephone = form.cleaned_data['telephone']
    #     student.code_apogee = form.cleaned_data['code_apogee']
    #     student.save()
    global student
    if request.method == 'POST':

        student = Students.objects.get(id=id)
        user = student.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.username = request.POST['first_name'] + '_' + request.POST['last_name']
        user.user_type = 'STUDENT'
        user.password = request.POST['password']
        user.save()
        student.cne = request.POST['cne']
        student.adresse = request.POST['adresse']
        student.path_photos = request.POST['path_photos']
        student.telephone = request.POST['telephone']
        student.code_apogee = request.POST['code_apogee']
        if request.POST['profile_pic'] != None:
            student.profile_pic = request.POST['profile_pic']
        student.save()
    return redirect(to='manage_student')


# UnivIt responsable : ismail errouk
def delete_student_groupe(request, id1, id2):
    student = Students.objects.get(id=id1)
    group = Groupe.objects.get(id=id2)
    student.groupes.remove(group)
    return redirect(to='manage_student')


# UnivIt responsable : ismail errouk
def edit_groupe_add_save(request, id):
    global temp
    if request.method == "POST":
        form = GroupeListForm(request.POST or None)
        if form.is_valid():
            temp = form.cleaned_data.get("Groupes")
        groupes = []
        for t in temp:
            groupes.append(Groupe.objects.get(pk=int(t)))
        student = Students.objects.get(pk=int(id))
        for groupe in groupes:
            student.groupes.add(groupe)
        student.save()
    return redirect(to='manage_student')


# UnivIt responsable : ismail errouk
def edit_groupe_groupes(request, id):
    student = Students.objects.get(id=id)
    groupes = student.groupes.all()
    form = GroupeListForm()
    context = {
        "form": form,
        "student": student,
        "groupes": groupes,
        "id": id
    }
    return render(request, "student/edit_student_groupe_template.html", context)


# UnivIt responsable : ismail errouk
def delete_student(request, student_id):
    student = Students.objects.get(id=student_id)
    try:
        student.delete()
        messages.success(request, "Student Deleted Successfully.")
        return redirect('manage_student')
    except:
        messages.error(request, "Failed to Delete Student.")
        return redirect('manage_student')
