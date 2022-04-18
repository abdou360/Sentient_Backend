from dataclasses import fields
from pyexpat import model
from django import forms

from cours.models import Chapitre, Document, Image, Modele3D, Traitement


class ChapitreForm(forms.ModelForm):
    class Meta:
        model = Chapitre
        fields = (
            'libelle',
            'description',
            'image',
            'element_module',
        )
        labels = {
            'libelle': 'Nom du chapitre',
            'description': 'Description du chapitre',
            'image': 'Image',
            'element_module': 'Element de module'
        }
        widgets={
            'libelle': forms.TextInput(attrs={'placeholder': 'Nom du chapitre',
                                                               'class': 'form-control',
                                                               }),
            'description': forms.Textarea(attrs={'placeholder': 'Description du chapitre',
                                                               'class': 'form-control',
                                                               'cols': 80, 'rows': 5
                                                               }),
            # 'image': forms.ImageField(attrs={'class': 'form-control'})
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = (
            'titre',
            'type',
            'path',
            # 'chapitre'
        )
        labels = {
            'titre': 'Nom du Document',
            'type': 'Type du Document',
            'path': 'Fichier',
            'image': 'Image',
            # 'chapitre': 'Chapitre'
        }
        widgets={
            'titre': forms.TextInput(attrs={'placeholder': 'Nom du Document',
                                                               'class': 'form-control',
                                                               }),
            'path': forms.TextInput(attrs={'placeholder': 'Fichier',
                                                               'class': 'form-control',
                                                               }),
        }

class Modele3DForm(forms.ModelForm):
    class Meta:
        model = Modele3D
        fields = {
            'path'
        }
        labels = {
            'path': 'Modèle 3D'
        }
        widgets={
            'path': forms.TextInput(attrs={'placeholder': 'Modèle 3D',
                                                               'class': 'form-control',
                                                               }),
        }
        
class TraitementForm(forms.ModelForm):
    class Meta:
        model = Traitement
        fields = {
            'titre',
            'label'
        }
        labels = {
            'titre': 'Nom du modèle',
            'label': 'Label',
        }
        widgets={
            'path': forms.TextInput(attrs={'placeholder': 'Nom du modèle',
                                                               'class': 'form-control',
                                                               }),
            'path': forms.TextInput(attrs={'placeholder': 'Label',
                                                               'class': 'form-control',
                                                               }),
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = {
            'type': 'Type de l\'Image',
            'path': 'Image'
        }