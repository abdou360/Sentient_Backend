from dataclasses import fields
from pyexpat import model
from django import forms

from cours.models import Chapitre, Document, Image, Modele3D, Traitement, File
from module.models import ElementModule
from users.models import Professeur


def get_prof_id(request):
    professeur = Professeur.objects.filter(
        admin_id=request.user.id).first()
    return professeur


class ChapitreForm(forms.ModelForm):

    # element_module = forms.ModelChoiceField(
    #     queryset=ElementModule.objects.filter(prof_id=get_prof_id(request)))

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
        widgets = {
            'libelle': forms.TextInput(attrs={'placeholder': 'Nom du chapitre',
                                              'class': 'form-control',
                                              }),
            'description': forms.Textarea(attrs={'placeholder': 'Description du chapitre',
                                                 'class': 'form-control',
                                                 'cols': 80, 'rows': 5
                                                 }),
            # 'element_module': forms.ChoiceField(choices="hi")
        }

    def __init__(self, *args, **kwargs):
        # if kwargs.__contains__("request"):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)
        self.fields['libelle'].label = ''
        self.fields['description'].label = ''
        self.fields['image'].label = ''
        self.fields['element_module'].label = ''
        self.fields['element_module'].required = False
        self.fields["element_module"].queryset = ElementModule.objects.filter(
            prof_id=get_prof_id(self.request))


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
        widgets = {
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
            'titre_modele3d',
            # 'path_modele3d'
        }
        labels = {
            'titre_modele3d': 'Nom du Modèle 3D'
        }
        widgets = {
            'titre_modele3d': forms.TextInput(attrs={'placeholder': 'Nom du Modèle 3D',
                                                     'class': 'form-control',
                                                     }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titre_modele3d'].label = ''


CHOICES = [('image', 'Image'), ('texte', 'Texte'), ('qrcode', 'QR-Code')]


class TraitementForm(forms.ModelForm):
    class Meta:
        model = Traitement
        fields = (
            'titre_traitement',
            'label_traitement',
            'type_traitement',
        )
        labels = {
            'titre_traitement': 'Titre',
            'label_traitement': 'Type du generateur du modele',
            'type_traitement': 'Label'
        }
        widgets = {
            'titre_traitement': forms.TextInput(attrs={'placeholder': 'Nom',
                                                       'class': 'form-control',
                                                       }),
            'label_traitement': forms.Textarea(attrs={'placeholder': 'Label',
                                                      'class': 'form-control',
                                                               'cols': 80, 'rows': 3
                                                      }),
            'type_traitement': forms.RadioSelect(choices=CHOICES
                                                 #   , attrs={'class': 'custom-control-input'}
                                                 )
            # 'type_traitement': forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'custom-control-input'}))
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titre_traitement'].label = ''
        self.fields['label_traitement'].label = ''


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = {
            'name_image': 'Nom de l\'Image',
            'path_image': 'Image',
            # 'is_qrcode': ''
        }
        widgets = {
            'name_image': forms.TextInput(attrs={'placeholder': 'Nom de l\'image',
                                                 'class': 'form-control',
                                                 }),
            # 'is_qrcode': forms.HiddenInput(attrs={'id': 'is-qrcode'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name_image'].label = ''
        self.fields['path_image'].label = ''


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = {
            'path_file': 'Fichier(s)'
        }
        widgets = {
            'path_file': forms.ClearableFileInput(attrs={'multiple': True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['path_file'].label = ''
        # self.fields['path'].label = ''
