from distutils.command import check
import sys
from tkinter import Image
from types import NoneType
from django.contrib import messages
from django.shortcuts import redirect, render
from pymysql import NULL
from cours.forms import *
from django.contrib.auth.decorators import login_required
from django.db.models.functions import ExtractYear

from cours.models import Chapitre, Document, Modele3D, Traitement, File
from filiere.models import Filiere
from module.models import ElementModule, Module
from semestre.models import Niveau, Semestre
from users.models import Professeur

from django.db.models import Q

import datetime
import time

import os

# Create your views here.

from django.contrib.auth.decorators import login_required


@login_required
def chapitres_list(request):
    search_by = NoneType
    professeur = Professeur.objects.filter(admin_id=request.user.id).first()
    # professeur = Professeur.objects.filter(admin_id = 1).first()
    # filieres = Filiere.objects.all()
    # niveaux = Niveau.objects.all()
    element_modules = ElementModule.objects.filter(prof_id=professeur)
    modules = Module.objects.filter(
        id__in=element_modules.values_list('module_id'))
    semestres = Semestre.objects.filter(
        id__in=modules.values_list('semestre_id'))
    niveaux = Niveau.objects.filter(
        id__in=semestres.values_list('niveau_id'))
    filieres = Filiere.objects.filter(id__in=niveaux.values_list('filiere_id'))

    # annees = Chapitre.objects.filter(
    #     professeur=professeur.id).dates('created_at', 'year')

    annees = Chapitre.objects.annotate(year=ExtractYear('created_at'))
    search_chapitre = request.GET.get('search')
    if search_chapitre:
        # chapitres = search_chapitres(search_chapitre, professeur)
        chapitres = Chapitre.objects.filter((Q(libelle__icontains=search_chapitre) | Q(
            description__icontains=search_chapitre)) & Q(professeur=professeur.id))
        search_by = " qui contiennent \" " + search_chapitre + " \""
    else:
        chapitres = Chapitre.objects.filter(professeur=professeur.id)
    context = {
        "chapitres": chapitres,
        "professeur": professeur,
        "filieres": filieres,
        "niveaux": niveaux,
        "element_modules": element_modules,
        "annees": annees,
        "search_by": search_by
    }
    return render(request, 'cours/chapitres.html', context)


# def search_chapitres(search_chapitre, professeur):
#     chapitres = Chapitre.objects.filter((Q(libelle__icontains=search_chapitre) | Q(
#         description__icontains=search_chapitre)) & Q(professeur=professeur.id))
#     return chapitres


@login_required
def search_chapitres_by_filiere(request, val):

    professeur = Professeur.objects.filter(admin_id=request.user.id).first()

    filieres = Filiere.objects.all()
    filiere = Filiere.objects.filter(nom_filiere=val).first()
    niveaux = Niveau.objects.filter(filiere=filiere)
    semestres = Semestre.objects.filter(niveau__in=niveaux)
    modules = Module.objects.filter(semestre__in=semestres)
    element_modules = ElementModule.objects.filter(module__in=modules)
    chapitres = Chapitre.objects.filter(element_module__in=element_modules)
    annees = Chapitre.objects.annotate(year=ExtractYear('created_at'))

    search_by = "pour la filière \" "+val + " \""
    search_chapitre = request.GET.get('search')
    if search_chapitre:
        chapitres = Chapitre.objects.filter((Q(libelle__icontains=search_chapitre) | Q(
            description__icontains=search_chapitre)) & Q(professeur=professeur.id) & Q(element_module__in=element_modules))
        search_by += " qui contiennent \" " + search_chapitre + " \""

    context = {
        "chapitres": chapitres,
        "professeur": professeur,
        "filieres": filieres,
        "niveaux": niveaux,
        "element_modules": element_modules,
        "annees": annees,
        "search_by": search_by
    }

    return render(request, "cours/chapitres.html", context)


@login_required
def search_chapitres_by_niveau(request, val):

    professeur = Professeur.objects.filter(admin_id=request.user.id).first()

    filieres = Filiere.objects.all()
    niveaux = Niveau.objects.all()
    niveau = Niveau.objects.get(nom_niveau=val)
    semestres = Semestre.objects.filter(niveau=niveau)
    modules = Module.objects.filter(semestre__in=semestres)
    element_modules = ElementModule.objects.filter(module__in=modules)
    chapitres = Chapitre.objects.filter(element_module__in=element_modules)
    annees = Chapitre.objects.annotate(year=ExtractYear('created_at'))

    search_by = "pour le niveau \" "+val + " \""

    search_chapitre = request.GET.get('search')
    if search_chapitre:
        chapitres = Chapitre.objects.filter((Q(libelle__icontains=search_chapitre) | Q(
            description__icontains=search_chapitre)) & Q(professeur=professeur.id) & Q(element_module__in=element_modules))
        search_by += " qui contiennent \" " + search_chapitre + " \""

    context = {
        "chapitres": chapitres,
        "professeur": professeur,
        "filieres": filieres,
        "niveaux": niveaux,
        "element_modules": element_modules,
        "annees": annees,
        "search_by": search_by
    }

    return render(request, "cours/chapitres.html", context)


@login_required
def search_chapitres_by_element_module(request, val):

    professeur = Professeur.objects.filter(admin_id=request.user.id).first()

    filieres = Filiere.objects.all()
    niveaux = Niveau.objects.all()
    # semestres = Semestre.objects.all()
    # modules = Module.objects.all()
    element_modules = ElementModule.objects.all()
    element_module = ElementModule.objects.filter(
        libelle_element_module=val).first()
    chapitres = Chapitre.objects.filter(element_module=element_module)
    annees = Chapitre.objects.annotate(year=ExtractYear('created_at'))

    search_by = "pour le module \" "+val + " \""

    search_chapitre = request.GET.get('search')
    if search_chapitre:
        chapitres = Chapitre.objects.filter((Q(libelle__icontains=search_chapitre) | Q(
            description__icontains=search_chapitre)) & Q(professeur=professeur.id) & Q(element_module=element_module))
        search_by += " qui contiennent \" " + search_chapitre + " \""

    context = {
        "chapitres": chapitres,
        "professeur": professeur,
        "filieres": filieres,
        "niveaux": niveaux,
        "element_modules": element_modules,
        "annees": annees,
        "search_by": search_by
    }

    return render(request, "cours/chapitres.html", context)


@login_required
def search_chapitres_by_annee(request, val):

    professeur = Professeur.objects.filter(admin_id=request.user.id).first()
    # professeur = Professeur.objects.filter(admin_id = 1).first()
    filieres = Filiere.objects.all()
    niveaux = Niveau.objects.all()
    element_modules = ElementModule.objects.all()
    annees = Chapitre.objects.annotate(year=ExtractYear('created_at'))

    # print('annes', annees)

    chapitres = Chapitre.objects.filter(created_at__contains=val)

    search_by = "crées pendant l'année \" "+val + " \""

    search_chapitre = request.GET.get('search')
    if search_chapitre:
        chapitres = Chapitre.objects.filter((Q(libelle__icontains=search_chapitre) | Q(
            description__icontains=search_chapitre)) & Q(professeur=professeur.id) & Q(created_at__contains=val))
        search_by += " qui contiennent \" " + search_chapitre + " \""

    context = {
        "chapitres": chapitres,
        "professeur": professeur,
        "filieres": filieres,
        "niveaux": niveaux,
        "element_modules": element_modules,
        "annees": annees,
        "search_by": search_by
    }

    return render(request, "cours/chapitres.html", context)


@login_required
def chapitre_details(request, id):
    professeur = Professeur.objects.filter(admin_id=request.user.id).first()
    # professeur = Professeur.objects.filter(admin_id=1).first()
    chapitre = Chapitre.objects.filter(id=id).first()
    traitements = Traitement.objects.filter(chapitre_id=id).all()
    documents = Document.objects.filter(chapitre_id=id).all()
    context = {
        "chapitre": chapitre,
        "professeur": professeur,
        "traitements": traitements,
        "documents": documents,
    }
    # context = {'chapitre_details': Traitem.objects.all()}
    return render(request, 'cours/chapitre_details.html', context)


@login_required
def add_chapitre(request):
    professeur = Professeur.objects.filter(admin_id=request.user.id).first()
    # professeur = Professeur.objects.filter(admin_id=1).first()
    if request.method == "GET":
        new_chapitre = ChapitreForm(request=request)
    elif request.method == "POST":
        new_chapitre = ChapitreForm(
            request.POST, request.FILES, request=request)
        if new_chapitre.is_valid():
            chapitre = new_chapitre.save(commit=False)
            chapitre.professeur = professeur
            chapitre.save()
            messages.success(request, ('Le chapitre a été ajouté avec succès'))
            return redirect('chapitres_list')
        else:
            messages.error(request, 'Erreur : Le chapitre n\'a pas été ajouté')
            return redirect('add_chapitre')
    return render(request, 'cours/add_chapitre.html', context={'new_chapitre': new_chapitre})


@login_required
def delete_chapitre(request, id):
    chapitre = Chapitre.objects.get(id=id)
    if chapitre.delete():
        messages.success(request, ('Le chapitre a été supprimé !'))
    else:
        messages.error(request, 'Erreur : Le chapitre n\'a pas été supprimé')
    return redirect('chapitres_list')


@login_required
def update_chapitre(request, id):
    chapitre = Chapitre.objects.get(id=id)
    if request.method == "GET":
        updated_chapitre = ChapitreForm(instance=chapitre, request=request)
    elif request.method == "POST":
        updated_chapitre = ChapitreForm(
            request.POST, request.FILES, instance=chapitre, request=request)
        if updated_chapitre.is_valid():
            updated_chapitre.save()
            messages.success(
                request, ('Le chapitre a été modifié avec succès'))
            return redirect('chapitres_list')
        else:
            messages.error(
                request, 'Erreur : Le chapitre n\'a pas été modifié')
            return redirect('update_chapitre')
    return render(request, 'cours/update_chapitre.html', context={'updated_chapitre': updated_chapitre})


@login_required
def delete_document(request, id):
    document = Document.objects.get(id=id)
    if document.delete():
        messages.success(request, ('Le document a été supprimé !'))
    else:
        messages.error(request, 'Erreur : Le document n\'a pas été supprimé')
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


@login_required
def delete_modele(request, id):
    traitement = Traitement.objects.get(id=id)
    modele = Modele3D.objects.get(id=traitement.modele3D.id)
    if traitement.image is not NULL:
        image = Image.objects.get(id=traitement.image.id)
        image.delete()
    if traitement.delete() & modele.delete():
        messages.success(request, ('Le Modèle 3D a été supprimé !'))
    else:
        messages.error(request, 'Erreur : Le Modèle 3D n\'a pas été supprimé')
    return redirect('#')


@login_required
def delete_image(request, id):
    traitement = Traitement.objects.get(id=id)
    image = Image.objects.get(id=traitement.image.id)
    if image.delete():
        messages.success(request, ('L\'image a été supprimé !'))
    else:
        messages.error(request, 'Erreur : L\'image n\'a pas été supprimé')
    return redirect('#')


@login_required
def delete_Traitement(request, id):
    traitement = Traitement.objects.get(id=id)

    if traitement.delete():
        messages.success(request, ('Le modele AR a été supprimé !'))
    else:
        messages.error(request, 'Erreur : Le modele  n\'a pas été supprimé')
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


EXTENSIONS = ['jpg', 'png', 'bin', 'gltf']


@login_required
def add_traitement(request, id):

    chapitre = Chapitre.objects.filter(id=id).first()
    if request.method == "GET":
        new_traitement = TraitementForm()
        new_image = ImageForm()
        new_modele3d = Modele3DForm()
        new_file = FileForm()

    elif request.method == "POST":
        # print('<message>', file=sys.stderr)

        new_traitement = TraitementForm(request.POST, request.FILES)

        # print('<titre_modele3d>'+request.POST.get("titre_modele3d"), file=sys.stderr)
        # print('<titre_traitement>' +
        #       request.POST.get("titre_traitement"), file=sys.stderr)
        # print('<label_traitement>' +
        #       request.POST.get("label_traitement"), file=sys.stderr)
        # print('<type_traitement>' +
        #       request.POST.get("type_traitement"), file=sys.stderr)

        invalid_extension = 0

        if new_traitement.is_valid():
            # print('<traitement valid>', file=sys.stderr)
            traitement = new_traitement.save(commit=False)
            traitement.chapitre = chapitre
            print('<traitement>'+traitement.type_traitement, file=sys.stderr)

            new_modele3d = Modele3DForm(request.POST, request.FILES)
            # print('<new_modele3d["titre_modele3d"]>' +
            #       new_modele3d['titre_modele3d'].value(), file=sys.stderr)
            if new_modele3d.is_valid():
                new_modele = new_modele3d.save(commit=False)
                new_modele.path_modele3d = model_location(
                    new_modele3d['titre_modele3d'].value())
                makedirs(new_modele.path_modele3d)

                # print('<modele3d //>'+str(new_modele.id), file=sys.stderr)

                new_modele.save()

                files = request.FILES.getlist('path_file')

                for f in files:
                    filebase, extension = f.name.split('.')
                    # print('<file extension>'+extension, file=sys.stderr)
                    if EXTENSIONS.__contains__(extension):
                        # print('<extension //>'+str(extension), file=sys.stderr)
                        # print('<invalid_extension //>' +
                        #       str(invalid_extension), file=sys.stderr)
                        ...
                    else:
                        # print('<extension //>'+str(extension), file=sys.stderr)
                        # print('<invalid_extension //>' +
                        #       str(invalid_extension), file=sys.stderr)
                        invalid_extension += 1
                        messages.error(
                            request, 'Erreur : L\'extension n\'est pas autorisée !')

                if invalid_extension == 0:
                    for f in files:
                        # print('<file name>'+f.name, file=sys.stderr)
                        # print('<file extension>'+f.name, file=sys.stderr)
                        obj = File.objects.create(
                            modele3D=new_modele, path_file=f)

                    if traitement.type_traitement == "Texte":
                        # print('<Texte>', file=sys.stderr)
                        traitement.image = None
                    else:
                        new_image = ImageForm(request.POST, request.FILES)
                        if new_image.is_valid():
                            image = new_image.save(commit=False)
                            if traitement.type_traitement == "Image":
                                image.is_qrcode = False
                            elif traitement.type_traitement == "QR-Code":
                                image.is_qrcode = True

                            image.save()
                            traitement.image = image
                        else:
                            messages.error(
                                request, 'Erreur : L\'image que vous avez entrer ne peut pas être acceptée !')
                    # print('<Texte ??>', traitement.type_traitement, file=sys.stderr)
                    traitement.modele3D = new_modele
                    traitement.save()
                    messages.success(request, ('Le modele AR a été ajouté !'))
                # else:
                #     return redirect('add_traitement')
            else:
                messages.error(
                    request, 'Erreur : Le modèle ne peut pas être enregistré !')
        return redirect("chapitres_list")

    return render(request, 'cours/add_traitement.html', context={'new_traitement': new_traitement, 'new_modele3d': new_modele3d, 'new_image': new_image, 'new_file': new_file
                                                                 #  , 'trait': trait
                                                                 })


def file_upload_location(modele3d, filename):

    path_modele3d = modele3d.path_modele3d
    return '%s/%s' % (path_modele3d, filename)


def model_location(modelName):
    now = time.time()
    stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S')
    return 'img/cours/modeles_3d/%s-%s' % (modelName, str(stamp))


def handle_file_upload(f, new_modele):
    with open(file_upload_location(new_modele, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def makedirs(path):
    # os.mkdir(os.path.join('/media/', path))
    try:
        os.makedirs(os.path.join('/media/', path))
    except OSError as e:
        if e.errno == 17:
            pass
