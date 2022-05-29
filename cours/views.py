
import os
import time
import datetime
from django.db.models import Q
from cours.serializers import *
from users.models import Professeur
from semestre.models import Niveau, Semestre
from module.models import ElementModule, Module
from filiere.models import Filiere
from cours.models import Chapitre, Document, Modele3D, Traitement, File, Image
from django.db.models import Count
from django.db.models.functions import ExtractYear
from django.contrib.auth.decorators import login_required
from cours.forms import *
from pymysql import NULL
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
import json
from django.core.serializers import serialize
from distutils.command import check
import sys
from rest_framework.response import Response
from rest_framework.decorators import api_view

NoneType = type(None)


# , VisibiliteModele


# Create your views here.


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
    professeur = Professeur.objects.filter(
        admin_id=request.user.id).first()
    chapitre = Chapitre.objects.filter(id=id).first()

    Traitements_visibles = Traitement.objects.filter(visibilite=professeur)
    modeles_visibles = Modele3D.objects.filter(
        id__in=[val.id for val in Traitements_visibles])
    if request.method == "GET":
        new_traitement = TraitementForm(request=request)
        new_image = ImageForm()
        new_modele3d = Modele3DForm()
        new_file = FileForm()

    elif request.method == "POST":
        # print('<message>', file=sys.stderr)
        print('post : ', request.POST)

        new_traitement = TraitementForm(
            request.POST, request.FILES, request=request)

        # print('<titre_modele3d>'+request.POST.get("titre_modele3d"), file=sys.stderr)
        # print('<titre_traitement>' +
        #       request.POST.get("titre_traitement"), file=sys.stderr)
        # print('<label_traitement>' +
        #       request.POST.get("label_traitement"), file=sys.stderr)
        # print('<type_traitement>' +
        #       request.POST.get("type_traitement"), file=sys.stderr)

        invalid_extension = 0

        if new_traitement.is_valid():
            print('post : valid')
            # print('<traitement valid>', file=sys.stderr)
            traitement = new_traitement.save(commit=False)
            traitement.chapitre = chapitre
            print('<traitement>'+traitement.type_traitement, file=sys.stderr)

            new_modele3d = Modele3DForm(request.POST, request.FILES)
            # print('<new_modele3d["titre_modele3d"]>' +
            #       new_modele3d['titre_modele3d'].value(), file=sys.stderr)
            if request.POST.get("modele3D") != '':

                existant_modele3d = Modele3D.objects.get(
                    id=request.POST.get("modele3D"))

                # new_modele3d.titre_modele3d = request.POST.get(
                #     "titre_modele3d")

                # new_modele = new_modele3d.save(commit=False)
                # new_modele.path_modele3d = model_location(
                #     request.POST.get("titre_modele3d"))

                # makedirs(new_modele.path_modele3d)

                # new_modele.save()

                # existant_files = File.objects.filter(
                #     modele3D=existant_modele3d)
                # for f in existant_files:
                #     obj = File.objects.create(
                #         modele3D=new_modele, path_file=f.path_file)

                if traitement.type_traitement == "Texte":
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
                # traitement.modele3D = new_modele
                traitement.modele3D = existant_modele3d
                # print(new_modele)
                traitement.save()
                traitement.visibilite.add(professeur)
                messages.success(request, ('Le modele AR a été ajouté !'))
            elif new_modele3d.is_valid():
                print('post : modele 3d', request.POST.get("modele3D") != '')
                # print('post : modele 3d', new_traitement.modele3D.length)
                new_modele = new_modele3d.save(commit=False)
                new_modele.path_modele3d = model_location(
                    new_modele3d['titre_modele3d'].value())
                makedirs(new_modele.path_modele3d)

                # print('<modele3d //>'+str(new_modele.id), file=sys.stderr)

                new_modele.save()

                files = request.FILES.getlist('path_file')

                for f in files:
                    filebase, extension = f.name.split('.')
                    if EXTENSIONS.__contains__(extension):
                        ...
                    else:
                        invalid_extension += 1
                        messages.error(
                            request, 'Erreur : L\'extension n\'est pas autorisée !')

                if invalid_extension == 0:
                    for f in files:
                        obj = File.objects.create(
                            modele3D=new_modele, path_file=f)

                    if traitement.type_traitement == "Texte":
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
                    traitement.modele3D = new_modele
                    traitement.save()
                    traitement.visibilite.add(professeur)
                    # visibilite = VisibiliteModele.objects.create(
                    #     modele3D=new_modele, professeur=professeur)
                    messages.success(request, ('Le modele AR a été ajouté !'))
                # else:
                #     return redirect('add_traitement')
            else:
                messages.error(
                    request, 'Erreur : Le modèle ne peut pas être enregistré !')
        # return redirect("chapitres_list")
        else:
            messages.error(
                request, 'Erreur : Le modèle ne peut pas être enregistré !')
        return redirect('chapitre_details', id)
        # return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    return render(request, 'cours/add_traitement.html', context={'new_traitement': new_traitement, 'new_modele3d': new_modele3d, 'new_image': new_image, 'new_file': new_file, 'modeles_visibles': modeles_visibles
                                                                 #  , 'trait': trait
                                                                 })


@login_required
def traitement_details(request):
    # if request.is_ajax and request.method == "GET":
    traitement_id = request.GET.get("traitement_id", None)
    professeur = Professeur.objects.filter(
        admin_id=request.user.id).first()

    traitement = Traitement.objects.filter(id=traitement_id).first()
    modele3d = Modele3D.objects.filter(id=traitement.modele3D_id).first()
    files = File.objects.filter(modele3D=modele3d).all()
    # fileCount = {"count": files}
    if(traitement.type_traitement != "Texte"):
        image = Image.objects.filter(id=traitement.image_id).first()
        context = {
            "traitement": json.loads(serialize('json', [traitement]))[0],
            "professeur": json.loads(serialize('json', [professeur]))[0],
            "modele3d": json.loads(serialize('json', [modele3d]))[0],
            "files": serialize('json', files),
            "image": json.loads(serialize('json', [image]))[0]
        }
    else:
        context = {
            "traitement": json.loads(serialize('json', [traitement]))[0],
            "professeur": json.loads(serialize('json', [professeur]))[0],
            "modele3d": json.loads(serialize('json', [modele3d]))[0],
            # "files": files
            "files": serialize('json', files),
            # "professeur": json.dumps(professeur),
            # "modele3d": json.dumps(modele3d),
            # "image": image,
            # "traitement": serialize('json', [traitement, ]),
            # "professeur": serialize('json', [professeur, ]),
            # "modele3d": serialize('json', [modele3d]),
        }
    return JsonResponse(context, status=200)
    # return JsonResponse({}, status=400)
    # return HttpResponse(context)
    # return render(request, 'cours/chapitre_details.html', context)


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


@login_required
def update_traitement(request, id):
    professeur = Professeur.objects.filter(
        admin_id=request.user.id).first()
    traitement = Traitement.objects.filter(id=id).first()
    q = Traitement.objects.filter(id=id).annotate(Count('id'))
    type_traitement = q[0].type_traitement
    chapitre_id = q[0].chapitre_id
    modele3d = Modele3D.objects.filter(id=traitement.modele3D_id).first()
    files = File.objects.filter(modele3D=modele3d).all()
    if type_traitement != 'Texte':
        image = Image.objects.filter(id=traitement.image_id).first()
    updated_image = None
    # print('ggtemp')
    if request.method == "GET":
        updated_traitement = TraitementForm(
            instance=traitement, request=request)
        updated_modele3d = Modele3DForm(instance=modele3d, request=request)
        if type_traitement != 'Texte':
            updated_image = ImageForm(instance=image, request=request)

    elif request.method == "POST":
        updated_traitement = TraitementForm(
            request.POST, request.FILES, instance=traitement, request=request)
        updated_modele3d = Modele3DForm(
            request.POST, request.FILES, instance=modele3d, request=request)
        if type_traitement != 'Texte':
            updated_image = ImageForm(
                request.POST, request.FILES, instance=image, request=request)

        if updated_traitement.is_valid():
            visibilite_profs = updated_traitement.cleaned_data.get(
                "visibilite")
            # print('visibilite')
            # print(visibilite_profs.count())
            # print(visibilite_profs[0].pk)
            traitement = updated_traitement.save(commit=False)
            traitement.type_traitement = type_traitement
            if updated_modele3d.is_valid():
                updated_modele3d = updated_modele3d.save()

                if traitement.type_traitement != "Texte":
                    if updated_image.is_valid():
                        updated_image = updated_image.save()
                        traitement.image = updated_image
                    else:
                        messages.error(
                            request, 'Erreur : L\'image que vous avez entré ne peut pas être acceptée !')
                traitement.modele3D = updated_modele3d
                traitement.save()
                # print('traitement.visibilite[0].id')
                # print(traitement.visibilite.all()[0].pk)
                # [val for val in Traitement.attribute_answers.all(
                # ) if val in WishList.attribute_answers.all()]
                for prof in Professeur.objects.all():
                    # .exclude(id=professeur.id):
                    traitement.visibilite.remove(prof)
                traitement.visibilite.add(professeur)
                for prof in visibilite_profs:
                    prof_exist = 0
                    for visible in traitement.visibilite.all():
                        if(prof.pk == visible.pk):
                            prof_exist += 1
                            print('equal')
                        if(prof_exist == 0):
                            print('inexist')
                            traitement.visibilite.add(prof)
                messages.success(request, ('Le modele AR a été modifié !'))
            else:
                messages.error(
                    request, 'Erreur : Le modèle ne peut pas être enregistré !')
        else:
            messages.error(
                request, 'Erreur : Le modèle ne peut pas être enregistré !' + traitement.type_traitement)
        return redirect('chapitre_details', chapitre_id)

    return render(request, 'cours/update_traitement.html', context={'updated_traitement': updated_traitement, 'updated_modele3d': updated_modele3d, 'updated_image': updated_image                                                                    # , 'new_file': new_file
                                                                    , 'updated_files': files
                                                                    #  , 'trait': trait
                                                                    })


# API

@api_view(['GET'])
def chapitres_list_api(request):
    chapitres = Chapitre.objects.all()
    chapitre_serializer = ChapitreSerializer(
        chapitres, many=True)
    # chapitres = chapitre_serializer.data

    return Response(chapitre_serializer.data.c)


@api_view(['GET'])
def chapitre_details_api(request, id_chapitre):
    chapitre = Chapitre.objects.get(id=id_chapitre)
    chapitre_serializer = ChapitreSerializer(chapitre, many=False)
    return Response(chapitre_serializer.data)


@api_view(['GET'])
def traitements_list_api(request, id_chapitre):
    # chapitre = Chapitre.objects.get(id=id_chapitre)
    # chapitre_serializer = ChapitreSerializer(chapitre, many=False)
    traitements = Traitement.objects.filter(chapitre_id=id_chapitre)
    traitement_serializer = TraitementSerializerImage(traitements, many=True)
    # print("query : ", traitements)
    modele3d = Modele3D.objects.filter(
        id__in=[t.modele3D_id for t in traitements])
    modele3d_serializer = Modele3DSerializerImage(modele3d, many=True)
    image_serializer = []
    # if(traitements.image != None):
    # image = Image.objects.filter(id__in=[t.image_id for t in traitements])
    # image_serializer = ImageSerializerImage(image, many=True)

    files_set = []

    files = File.objects.filter(modele3D=modele3d)
    file_serializer = FileSerializerImage(files, many=True)

    # for val in file_serializer.data:
    #     files_set.append(val['path_file'])

    res = []

    # for i, j, k in traitement_serializer.data, modele3d_serializer.data, image_serializer.data:
    for i in range(0, len(traitement_serializer.data)):
        # image_serializer = None
        # print(i)
        print(traitements[i].modele3D_id)
        # print(traitement_serializer.data[i]['id'])
        # print(len(traitement_serializer.data))
        # print(len(image_serializer.data))
        # print(len(modele3d_serializer.data))
        # image_serializer.data[i] = image_serializer.data[i] if image_serializer.data[i] != None else None
        modele3d = Modele3D.objects.get(
            id=traitements[i].modele3D_id)
        modele3d_serializer = Modele3DSerializerImage(modele3d, many=False)
        # if(traitements.image != None):
        image = None
        try:
            image = Image.objects.get(id=traitements[i].image_id)
            image_serializer = ImageSerializerImage(image, many=False)
        except Image.DoesNotExist:
            image = None
            image_serializer = None
        print(image)
        if image != None:
            path_image = image_serializer.data['path_image']
        else:
            path_image = None
        res.append(
            {'traitement': traitement_serializer.data[i],
             'path_modele3d': modele3d_serializer.data['path_modele3d'],
             'path_image': path_image
             #  'image': image_serializer.data[i]
             })
        #  'image': image_serializer.data[i] if image_serializer.data[i] else None})
        # res.append(
        #     {'image': image_serializer.data[1] if image_serializer.data[1] else None})
        # res.append({'modele3d': modele3d_serializer.data[1]})
        # res.append({'files': files_set[i]})

    # response = {
    #     'traitements': traitement_serializer.data,
    #     'modeles': modele3d_serializer.data,
    #     'images': image_serializer.data
    # }

    # response = [
    #     res
    # ]

    return Response(res)


@api_view(['GET'])
def traitement_api(request, id):
    traitement = Traitement.objects.filter(id=id).first()

    traitement_serializer = TraitementSerializerImage(traitement, many=False)

    modele3d = Modele3D.objects.filter(
        id=traitement.modele3D_id).first()
    # modele3d_serializer = Modele3DSerializerImage(modele3d, many=False)

    files_set = []

    files = File.objects.filter(modele3D=modele3d)
    file_serializer = FileSerializerImage(files, many=True)

    for val in file_serializer.data:
        files_set.append(val['path_file'])

    image_serializer = None
    # if(traitements.image != None):
    image = Image.objects.filter(id=traitement.image_id).first()
    image_serializer = ImageSerializerImage(image, many=False)
    response = {
        'traitement': traitement_serializer.data['titre_traitement'],
        # 'modele': modele3d_serializer.data,
        # 'files': file_serializer.data,
        'files': files_set,
        'image': image_serializer.data['path_image']
    }
    return Response(response)
