from cours.models import *
from rest_framework import serializers


# class


class ChapitreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapitre
        fields = '__all__'


class TraitementSerializerImage(serializers.ModelSerializer):
    class Meta:
        model = Traitement
        # fields = '__all__'
        fields = ['id', 'titre_traitement']


class Modele3DSerializerImage(serializers.ModelSerializer):
    class Meta:
        model = Modele3D
        fields = ['path_modele3d']


class FileSerializerImage(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['path_file']


class ImageSerializerImage(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['path_image']
