from django import forms


class FiliereForm(forms.Form):
    nom_filiere = forms.CharField(max_length=30)
    etablissement = forms.CharField(max_length=5)
    logo = forms.ImageField(required=False)

class EtablissementForm(forms.Form):
    nom = forms.CharField(max_length=30)
    adresse = forms.CharField(max_length=30)
    telephone = forms.CharField(max_length=13)
    logo = forms.ImageField(required=False)