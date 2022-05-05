from django.shortcuts import render

""" RESPONSABLE : CODEVERSE
        + Espace professeur : @author : KANNOUFA Fatima Ezzahra
"""

#   permet d'afficher l'emploi du professeur connécté dans un calendrier    #

def EmploieProf(request):
    return render(request, "emploie/espace_prof/pages/emploie_calendar.prof.html")


#   permet de lister la liste des étudiants avec leur présence pour une séance donnée   #
def ListePresence(request, filiere, idSeance):
    context = {
        "data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
    return render(request, "emploie/espace_prof/pages/liste_presence.prof.html", context)
