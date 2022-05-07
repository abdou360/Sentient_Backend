import http

from django.shortcuts import render
from users.models import Professeur, CustomUser
from semestre.models import Semestre, Groupe, Niveau
from filiere.models import Filiere, Etablissement
from django.http import HttpResponseRedirect

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
        return render(request, 'emploie/espace_admin/pages/emploie_calendar.admin.html',
                      {"fillier": selectefilliere, "niveau": selecteniveau, "groupe": selectegroupe})


#   permet d'afficher l'emploi du professeur connécté dans un calendrier    #

def EmploieProf(request):
    return render(request, "emploie/espace_prof/pages/emploie_calendar.prof.html")


#   permet de lister la liste des étudiants avec leur présence pour une séance donnée   #
def ListePresence(request, filiere, idSeance):
    context = {
        "data": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
    return render(request, "emploie/espace_prof/pages/liste_presence.prof.html", context)
