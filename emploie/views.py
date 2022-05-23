import http

from django.shortcuts import render
from emploie.forms import PlanningForm
from module.models import ElementModule
from users.models import Professeur, CustomUser
from semestre.models import Semestre, Groupe, Niveau
from filiere.models import Filiere, Etablissement
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from slugify import slugify
from emploie.models import Planning, Presence, Salle, Seance

""" RESPONSABLE : CODEVERSE
        + Espace admin : FIROUD Reda & OUSSAHI Salma
        + Espace professeur : @authors : KANNOUFA Fatima Ezzahra
"""

#   permet a l'admin de créer les emploies des profs    #
selectefilliere: Filiere
selecteniveau: Niveau
selectegroupe: Groupe


def EmploieAdmin(request):
    fillieres = Filiere.objects.all()
    semestres = Semestre.objects.all()
    return render(request, 'emploie/espace_admin/pages/emploie_calendar.admin.html', {"filliers": fillieres})

def AddPlanning (request):
    if request.method == "POST":  
        form = PlanningForm(request.POST) 
        if form.is_valid():  
            try:  
                plan=form.save()  
                return redirect('')  
            except:  
                pass  


    else:   
        form = PlanningForm()
    return render(request,'emploie/espace_admin/pages/emploie_calendar.addSchedule.html',{"form":form})

    

def all(request):  
    plannings = Planning.objects.all()
    return render(request, 'emploie/espace_admin/pages/emploie_calendar.all.html', {"plannings": plannings})

def edit(request, id):  
    plannings = Planning.objects.get(id=id) 
    return render(request, 'emploie/espace_admin/pages/emploie_calendar.edit.html', {'plannings': plannings}) 

def update(request, id):  
    plannings = Planning.objects.get(id=id)  
    form = PlanningForm(request.POST, instance = plannings)
    if form.is_valid():  
        form.save()  
        return redirect("emploie/all")  
    return render(request, 'emploie/espace_admin/pages/emploie_calendar.edit.html', {'plannings': plannings})  


def destroy(request, id):  
    planning = Planning.objects.get(id=id)  
    planning.delete()  
    return redirect("/emploie/all")

def GetNiveaux(request):
    if request.method == 'POST':
        global selectefilliere
        selectefilliere = Filiere.objects.filter(nom_filiere__exact=request.POST['filiereselection']).first()
        niveaux = Niveau.objects.filter(filiere_id__exact=selectefilliere.id).all()
        return render(request, 'emploie/espace_admin/pages/emploie_calendar.admin.html',
                      {"fillier": selectefilliere, "niveaux": niveaux})


def GetGroupes(request):
    if request.method == 'POST':
        global selecteniveau
        selecteniveau = Niveau.objects.filter(id=request.POST['niveauselection']).first()
        groupes = Groupe.objects.filter(niveau_id=selecteniveau.id).all()
        return render(request, 'emploie/espace_admin/pages/emploie_calendar.admin.html',
                      {"fillier": selectefilliere, "niveau": selecteniveau, "groupes": groupes})


def SendGroupes(request):
    if request.method == 'POST':
        global selectegroupe
        selectegroupe = Groupe.objects.filter(id=request.POST['groupeselection']).first()
        plannings = Planning.objects.filter(groupe=selectegroupe)

        return render(request, 'emploie/espace_admin/pages/emploie_calendar.admin.html',
                      {"fillier": selectefilliere, "niveau": selecteniveau, "groupe": selectegroupe,"plannings":plannings})
        





#   permet d'afficher l'emploi du professeur connécté dans un calendrier    #
@login_required
def EmploieProf(request):
    return render(request, "emploie/espace_prof/pages/emploie_calendar.prof.html")


#   permet de lister la liste des étudiants avec leur présence pour une séance donnée   #
@login_required
def ListePresence(request, slug, idSeance):
    
    seance = Seance.objects.get(pk = idSeance)
    presences = Presence.objects.filter(seance_id = idSeance)
    
    context = {
        "seance" : seance,
        "presences" : presences,
    }
    return render(request, "emploie/espace_prof/pages/liste_presence.prof.html", context)


#   modifier la présence d'un étudiant   #
@login_required
def ModifierPresence(request, idSeance, idEtudiant):
    seance = Seance.objects.get(pk = idSeance)
    slug = slugify(seance.planning.liblle + '-' + str(seance.date_debut))
    
    presence = Presence.objects.get(etudiant_id = idEtudiant, seance_id = idSeance)
    presence.is_present = not presence.is_present
    presence.save()
    
    return redirect('ListePresence', slug=slug, idSeance=idSeance)

