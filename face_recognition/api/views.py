
""" EQUIPE : CodeVerse et ARopedia
    @authors :  + KANNOUFA F. EZZAHRA
                + FIROUD REDA
                + MOUZAFIR ABDELHADI
"""

from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from ..service_metier.ReglageCounter import RecognizerMethod
from .serializers import *
from semestre.models import Groupe, Niveau
from filiere.models import  Filiere


#   Récupérer les données de Filières, Niveaux et groupes
def get_json_filiere_data(request):
    data = list(Filiere.objects.values())
    return JsonResponse({'data': data})

def get_json_niveau_data(request, filiere):
    data = list(Niveau.objects.filter(filiere__nom_filiere=filiere).values())
    return JsonResponse({'data': data})

def get_json_group_data(request, niveau):
    data = list(Groupe.objects.filter(niveau__nom_niveau=niveau).values())
    return JsonResponse({'data': data})


#   API   #
@api_view(['GET'])
def getSalles(request):
    try:
        salles = Salle.objects.all()
        serializer = SalleSerializer(salles, many=True)
        return Response(serializer.data)
    except Niveau.DoesNotExist:
        return Response([])

@api_view(['GET'])
def filiere_liste(request):
    try:
        filieres = Filiere.objects.all()
        serializer = FiliereSerializer(filieres, many=True)
        return Response(serializer.data)
    except Filiere.DoesNotExist:
        return Response([])


@api_view(['GET'])
def Niveau_liste(request, nom_filiere):
    try:
        filiere = Filiere.objects.get(nom_filiere__exact=nom_filiere)
        niveaus = Niveau.objects.filter(filiere_id__exact=filiere.id).all()
        serializer = NiveauSerializer(niveaus, many=True)
        return Response(serializer.data)
    except Niveau.DoesNotExist:
        return Response([])


@api_view(['POST'])
def post_niveau(request):
    if request.data:
        label = RecognizerMethod()
        return Response(
            {
                "detected faces": label,
                "success" : "success"
            },
            status=200
        )

    return Response(
        {
            "error": True,
            "error_msg": "not valid",
        },
        status=400
    )
    
