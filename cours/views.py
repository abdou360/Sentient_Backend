from distutils.command import check
import sys
from tkinter import Image
from django.contrib import messages
from django.shortcuts import redirect, render
from pymysql import NULL
from cours.forms import *

from cours.models import Chapitre, Document, Modele3D, Traitement
from filiere.models import Filiere
from module.models import ElementModule, Enseignant_Responsable, Module
from semestre.models import Niveau, Semestre
from users.models import Professeur

from django.db.models import Q

import datetime
import time

import os

# Create your views here.

from django.contrib.auth.decorators import login_required


def chapitres_list(request): 
    professeur = Professeur.objects.filter(user = request.user.id).first()
    
    search_chapitre = request.GET.get('search')
    if search_chapitre:
        chapitres = Chapitre.objects.filter((Q(libelle__icontains=search_chapitre) | Q(description__icontains=search_chapitre)) & Q(professeur = professeur.id))
    else:
        chapitres = Chapitre.objects.filter(professeur = professeur.id)
    context = {
        "chapitres": chapitres,
        "professeur": professeur
    }
    return render(request, 'cours/chapitres.html', context) 
def chapitre_details(request,id): 
    professeur = Professeur.objects.filter(user = request.user.id).first()
    chapitre = Chapitre.objects.filter(id = id).first()
    traitements = Traitement.objects.filter(chapitre_id = id).all()
    documents=Document.objects.filter(chapitre_id = id).all()
    context = {
        "chapitre": chapitre,
        "professeur": professeur,
        "traitements":traitements,
        "documents":documents,
    }
    # context = {'chapitre_details': Traitem.objects.all()}
    return render(request, 'cours/chapitre_details.html',context) 

def add_chapitre(request): 
    professeur = Professeur.objects.filter(user = request.user.id).first()
    if request.method == "GET":
        new_chapitre = ChapitreForm()
    elif request.method == "POST":
        new_chapitre = ChapitreForm(request.POST, request.FILES)
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
        


def delete_chapitre(request, id):
    chapitre = Chapitre.objects.get(id=id)
    if chapitre.delete():
        messages.success(request, ('Le chapitre a été supprimé !'))
    else:
        messages.error(request, 'Erreur : Le chapitre n\'a pas été supprimé')
    return redirect('chapitres_list')

def update_chapitre(request, id):
    chapitre = Chapitre.objects.get(id=id)
    if request.method == "GET":
        updated_chapitre = ChapitreForm(instance=chapitre)
    elif request.method == "POST":
        updated_chapitre = ChapitreForm(request.POST, request.FILES, instance=chapitre)
        if updated_chapitre.is_valid():
            updated_chapitre.save()
            messages.success(request, ('Le chapitre a été modifié avec succès'))
            return redirect('chapitres_list')
        else:
            messages.error(request, 'Erreur : Le chapitre n\'a pas été modifié')
            return redirect('update_chapitre')
    return render(request, 'cours/update_chapitre.html', context={'updated_chapitre': updated_chapitre})
    
    

def delete_document(request, id):
    document = Document.objects.get(id=id)
    if document.delete():
        messages.success(request, ('Le document a été supprimé !'))
    else:
        messages.error(request, 'Erreur : Le document n\'a pas été supprimé')
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

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

def delete_image(request, id):
    traitement = Traitement.objects.get(id=id)
    image = Image.objects.get(id=traitement.image.id)
    if image.delete():
        messages.success(request, ('L\'image a été supprimé !'))
    else:
        messages.error(request, 'Erreur : L\'image n\'a pas été supprimé')
    return redirect('#')

def delete_Traitement(request, id):
    traitement = Traitement.objects.get(id=id)
    # image = Image.objects.get(id=traitement.image.id)
    if traitement.delete():
        messages.success(request, ('Le modele AR a été supprimé !'))
    else:
        messages.error(request, 'Erreur : Le modele  n\'a pas été supprimé')
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def add_traitement(request,id): 
    
    # if else for images type
    
    chapitre = Chapitre.objects.filter(id = id).first()
    if request.method == "GET":
        new_traitement = TraitementForm()
        new_image = ImageForm()
        new_modele3d = Modele3DForm()
        new_file = FileForm()
        # trait = TraitementForm()
        # print('<message>', file=sys.stderr)
    elif request.method == "POST":
        print('<message>', file=sys.stderr)
        # new_image = ImageForm(request.POST, request.FILES)
        # new_file = (request.POST, request.FILES)
        new_traitement = TraitementForm(request.POST, request.FILES)
        
        print('<titre_modele3d>'+request.POST.get("titre_modele3d"), file=sys.stderr)
        print('<titre_traitement>'+request.POST.get("titre_traitement"), file=sys.stderr)
        print('<label_traitement>'+request.POST.get("label_traitement"), file=sys.stderr)
        print('<type_traitement>'+request.POST.get("type_traitement"), file=sys.stderr)
        
        if new_traitement.is_valid():
            print('<traitement valid>', file=sys.stderr)
            traitement = new_traitement.save(commit=False)
            traitement.chapitre = chapitre
            print('<traitement>'+traitement.type_traitement, file=sys.stderr)
            if traitement.type_traitement == "Image":
                new_image = ImageForm(request.POST, request.FILES)
                if new_image.is_valid():
                    image = new_image.save(commit=False)
                    image.is_qrcode = False
                    image.save()
                    traitement.image = image
            # elif traitement.type == "texte":
            #     traitement.label 
            elif traitement.type_traitement == "QR-Code":
                new_qrcode = ImageForm(request.POST, request.FILES)
                if new_qrcode.is_valid():
                    qrcode = new_qrcode.save(commit=False)
                    qrcode.is_qrcode = True
                    qrcode.save()
                    traitement.image = qrcode
            new_modele3d = Modele3DForm(request.POST, request.FILES)
            # print(new_modele3d.cleaned_data)
            print('<new_modele3d["titre_modele3d"]>'+new_modele3d['titre_modele3d'].value(), file=sys.stderr)
            if new_modele3d.is_valid():
                new_modele = new_modele3d.save(commit=False)
                new_modele.path_modele3d = model_location(new_modele3d['titre_modele3d'].value())
                makedirs(new_modele.path_modele3d)
                new_modele.save()
                # modele3d = Modele3D.objects.filter(titre_modele3d = new_modele3d['titre_modele3d'].value()).first()
                
                print('<modele3d //>'+str(new_modele.id), file=sys.stderr)
                # print('<new_modele3d>'+str(new_modele3d.id), file=sys.stderr)
                
                files = request.FILES.getlist('path_file')
                # files = request.FILES['path_file']
                # files = FileForm(request.POST, request.FILES.getlist('path_file'))
                # files = FileForm(request.POST, request.FILES)
                # files = FileForm(request.POST, request.FILES['path_file'])
                # if files.is_valid():
                #     handle_file_upload(request.FILES['path_file'])
                for f in files:
                    
                    print('<file name>'+f.name, file=sys.stderr)
                    
                    obj = File.objects.create(modele3D = new_modele, path_file=f)
                    
                    # new_file = FileForm(request.POST, request.FILES)
                    
                    # file = new_file.save(commit=False)
                    # file.modele3D = new_modele
                    # file.save()
                    
                    # obj = new_file.save(commit=False)
                    # if request.FILES:
                    #     for f in request.FILES.getlist('path_file'):
                    #         obj = File.model.objects.create(path_file=f)
                    
                # for x in files:
                #     print('<file name>'+x.name, file=sys.stderr)
                #     process(x, new_modele)
                    
                    # handle_file_upload(f, new_modele)
                    # new_file = FileForm(request.POST, f)
                    # if new_file.is_valid():
                    #     file = new_file.save(commit=False)
                    #     file.modele3D = new_modele3d
                    #     file.save()
                        
                        
                traitement.modele3D = new_modele
                # print(traitement.titre_traitement+"**************/")
                # print(traitement.label_traitement+"/")
                # print(traitement.type_traitement+"/")
                # print(str(traitement.chapitre.id)+"/")
                # print(str(traitement.image.id)+"/")
                # print(str(traitement.modele3D.id)+"/")
                # print(str(traitement.id))
                # print(traitement.titre_traitement+"**************/"+traitement.label_traitement+"/"+traitement.type_traitement+"/"+str(traitement.chapitre.id)+"/"+str(traitement.image.id)+"/"+str(traitement.modele3D.id)+"/"+str(traitement.id))
                traitement.save()
        
        return redirect('chapitres_list')
        # new_traitement = TraitementForm(request.POST, request.FILES)
        # if new_traitement.is_valid():
        #     Traitement = new_traitement.save(commit=False)
        #     Traitement.chapitre = chapitre
        #     Traitement.save()
        #     messages.success(request, ('Le modele AR a été ajouté avec succès'))
        #     return redirect('chapitre_details',id)
        # else:
        #     messages.error(request, 'Erreur : Le chapitre n\'a pas été ajouté')
        #     return redirect('add_traitement')
    return render(request, 'cours/add_traitement.html', context={'new_traitement': new_traitement, 'new_modele3d': new_modele3d, 'new_image': new_image, 'new_file': new_file
                                                                #  , 'trait': trait
                                                                 })


def file_upload_location(modele3d, filename):
        # now = time.time()
        # stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S')
        path_modele3d = modele3d.path_modele3d
        return '%s/%s' % (path_modele3d, filename)
    
def model_location(modelName):
        now = time.time()
        stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S')
        return 'img/cours/modeles_3d/%s-%s' % (modelName, str(stamp))  

def handle_file_upload(f, new_modele):
    with open(file_upload_location(new_modele,f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def makedirs(path):
    # os.mkdir(os.path.join('/media/', path))
    try:
        os.makedirs(os.path.join('/media/', path))
    except OSError as e:
        if e.errno == 17:
            pass


# def process(f, new_modele):
#     with open(new_modele.path_modele3d + str(f), 'wb+') as destination:
#         # print('<destination>'+str(destination), file=sys.stderr)
#         for chunk in f.chunks():
#             print('<chunk>'+str(chunk), file=sys.stderr)
#             destination.write(chunk)

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             context = {'msg' : '<span style="color: green;">File successfully uploaded</span>'}
#             return render(request, "single.html", context)
#     else:
#         form = UploadFileForm()
#     return render(request, 'single.html', {'form': form})

# def handle_uploaded_file(f):
#     with open(f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)