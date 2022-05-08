from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from slugify import slugify
from emploie.models import Presence, Seance

""" RESPONSABLE : CODEVERSE
        + Espace professeur : @author : KANNOUFA Fatima Ezzahra
"""

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

