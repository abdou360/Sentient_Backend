from dataclasses import fields
from pyexpat import model
from django import forms

from cours.models import Chapitre, Document, Image, Modele3D, Traitement, File

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
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['libelle'].label = ''
        self.fields['description'].label = ''
        self.fields['image'].label = ''
        self.fields['element_module'].label = ''

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = (
            'titre',
            'type',
            'path',
        )
        labels = {
            'titre': 'Nom du Document',
            'type': 'Type du Document',
            'path': 'Fichier',
            'image': 'Image',
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
            'titre',
        }
        labels = {
            'titre': 'Nom du Modèle 3D'
        }
        widgets={
            'titre': forms.TextInput(attrs={'placeholder': 'Nom du Modèle 3D',
                                                               'class': 'form-control',
                                                               }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titre'].label = ''
        
CHOICES=[('image','Image'),('texte','Texte'),('qrcode','QR-Code')]

class TraitementForm(forms.ModelForm):
    class Meta:
        model = Traitement
        fields = {
            'titre',
            'label',
            'type',
        }
        labels = {
            'titre': 'Titre',
            'type': 'Type du generateur du modele',
            'label': 'Label'
        }
        widgets={
            'titre': forms.TextInput(attrs={'placeholder': 'Nom',
                                                               'class': 'form-control',
                                                               }),
            'label': forms.Textarea(attrs={'placeholder': 'Label',
                                                               'class': 'form-control',
                                                               'cols': 80, 'rows': 3
                                                               }),
            'type': forms.RadioSelect(choices=CHOICES
                                    #   , attrs={'class': 'custom-control-input'}
                                      )
            # 'type': forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'custom-control-input'}))
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titre'].label = ''
        self.fields['label'].label = ''

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = {
            'name': 'Nom de l\'Image',
            'path': 'Image',
            # 'is_qrcode': ''
        }
        widgets={
            'name': forms.TextInput(attrs={'placeholder': 'Nom de l\'image',
                                                               'class': 'form-control',
                                                               }),
            # 'is_qrcode': forms.HiddenInput(attrs={'id': 'is-qrcode'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ''
        self.fields['path'].label = ''

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = {
            'path': 'Fichier(s)'
        }
        # widgets = {
        #     'path': forms.ClearableFileInput(attrs={'multiple': True}),
        # }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['path'].label = ''
    #     # self.fields['path'].label = ''
        