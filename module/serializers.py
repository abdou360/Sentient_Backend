# @author abdelhadi mouzafir
from rest_framework import serializers

from filiere.models import  Filiere
from semestre.models import Niveau

class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model=Filiere
        fields='__all__'

class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields='__all__'