from django import forms

from emploie.models import Planning

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
        fields = ['jour','groupe','salle','professeur','element_module','heure_debut','heure_fin']
        widgets = {
                "jour" : forms.Select(choices = JOURS) 
            } 

