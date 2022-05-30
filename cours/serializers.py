from rest_framework import serializers

from .models import Document, Traitement,Modele3D,File

class TraitementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traitement
        fields = '__all__'
        
class Modele3DSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modele3D
        fields = '__all__'
        
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
        
       
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'  
        