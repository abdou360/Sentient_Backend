from django import forms

from emploie.models import Planning,Seance

JOURS =(
    ( " "," "),
    ( "monday","monday"),
    ( "tuesday","tuesday"),
    ( "wednesday","wednesday"),
    ( "thursday","thursday"),
    ( "friday","friday"),
    ( "saturday","saturday"),
    ("sunday","sunday"),
)

class PlanningForm(forms.ModelForm):  
    class Meta:     
        model = Planning   
        fields = ['jour','groupe','salle','professeur','element_module']
        widgets = {
                "jour" : forms.Select(choices = JOURS) 
            } 

class SeanceForm(forms.ModelForm):  
    class Meta:     
        model = Seance   
        fields = ['heure_debut','heure_fin','planning']
        

