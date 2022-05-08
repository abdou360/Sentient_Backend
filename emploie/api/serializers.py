
""" EQUIPE : CODEVERSE
    @author : KANNOUFA FATIMA EZZAHRA
"""

from rest_framework import serializers
from emploie.models import Planning, Presence, Seance
from semestre.models import Groupe, Niveau

#   serialisation   #       
class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields = '__all__'
 
        
class GroupeSerializer(serializers.ModelSerializer):
    niveau = NiveauSerializer()
    class Meta:
        model = Groupe
        fields = '__all__'
            
        
class PlanningSerializer(serializers.ModelSerializer):
    groupe = GroupeSerializer()
    class Meta:
        model = Planning
        fields = '__all__'        


class SeanceSerializer(serializers.ModelSerializer):
    planning = PlanningSerializer()
    class Meta:
        model = Seance
        fields = '__all__'   
        
class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presence
        fields = '__all__'
               
    