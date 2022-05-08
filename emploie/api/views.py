
""" EQUIPE : CODEVERSE
    @author : KANNOUFA FATIMA EZZAHRA
"""

from emploie.models import Planning, Seance
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SeanceSerializer


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
