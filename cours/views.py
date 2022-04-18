from distutils.command import check
from tkinter import Image
from django.contrib import messages
from django.shortcuts import redirect, render
from pymysql import NULL
from cours.forms import ChapitreForm

from cours.models import Chapitre, Document, Modele3D, Traitement
from filiere.models import Filiere
from module.models import ElementModule, Enseignant_Responsable, Module
from semestre.models import Niveau, Semestre
from users.models import Professeur

from django.db.models import Q

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
    return redirect('#')

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

