
""" EQUIPE : CODEVERSE
    @author : KANNOUFA FATIMA EZZAHRA
"""

from rest_framework import serializers
from emploie.models import Planning, Presence, Seance
from semestre.models import Groupe, Niveau
from users.models import Students, CustomUser


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


class UserSerializer:
    class Meta:
        model =CustomUser
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Students
        fields = '__all__'

class PresenceSerializer(serializers.ModelSerializer):
    etudiant = StudentSerializer()
    class Meta:
        model = Presence
        fields = '__all__'




