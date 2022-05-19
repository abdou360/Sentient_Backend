
""" EQUIPE : CODEVERSE
    @author : KANNOUFA FATIMA EZZAHRA
"""

from emploie.models import Planning, Seance
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SeanceSerializer
from django.http import HttpResponse, JsonResponse


from module.models import ElementModule
from users.models import Professeur


#   récupérer toutes les séances d'un professeur    #
@api_view(['GET'])
def getSeances(request, idProf):
    #   chercher les planning
    plannings = Planning.objects.filter(professeur_id = idProf)
    
    seances_prof = []    
    #   chercher pour chaque planning les séances qui lui correspond
    for planning in plannings:
        seances = Seance.objects.filter(planning_id = planning.id)
        seances_prof += seances

    serializer = SeanceSerializer(seances_prof, many=True)
    
    return Response(serializer.data) 


# filtrage d'1 séance
def get_json_module_data(request):
    professeur = Professeur.objects.get(admin_id=request.user.id)
    qs_val = list(Planning.objects.filter(professeur_id=professeur.id).values())
    return JsonResponse({'data': qs_val})


def get_json_classe_data(request, planning_id):
    qs_val = list(Seance.objects.values())
    return JsonResponse({'data': qs_val})



def get_json_seance_data(request, car):
    qs_val = list(Seance.objects.filter(car__name=car).values())
    return JsonResponse({'data': qs_val})
