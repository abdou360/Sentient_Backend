from email.headerregistry import Group
from operator import imod
from tokenize import group
from django.db import models
from django.core.validators import MaxValueValidator
from module.models import ElementModule
from semestre.models import Groupe
from users.models import Professeur, Students

""" Responsable : CODEVERSE
"""
JOURS =(
    ("1", "MONDAY"),
    ("2", "TUESDAY"),
    ("3", "WEDNESDAY"),
    ("4", "THURSDAY"),
    ("5", "FRIDAY"),
    ("6", "SATURDAY"),
    ("7", "SUNDAY"),
)
class TypeSalle(models.Model):
    capacite =  models.IntegerField(validators=[MaxValueValidator(100)]) 
    libelle =   models.CharField(max_length=100, null=True) 
    
    def __str__(self):
        return self.libelle
    
    
class Salle(models.Model):
    nom_salle =  models.CharField(max_length=100, null=True) 
    disponible = models.BooleanField()
    type_salle = models.ForeignKey(TypeSalle ,  null=True , on_delete= models.SET_NULL )
    
    def __str__(self):
        return self.nom_salle


class Planning(models.Model):
    jour =  models.CharField(max_length=100, null=True) 
    groupe = models.ForeignKey(Groupe , null = True , on_delete= models.SET_NULL )
    salle = models.ForeignKey(Salle , null = True , on_delete= models.SET_NULL )
    professeur = models.ForeignKey(Professeur , null = True , on_delete= models.SET_NULL )
    element_module = models.ForeignKey(ElementModule , null = True , on_delete= models.SET_NULL )
    
    def __str__(self):
        return self.liblle


class Seance(models.Model):
    heure_debut = models.TimeField(null = True )
    heure_fin = models.TimeField(null = True )
    planning = models.ForeignKey(Planning , null = True , on_delete= models.SET_NULL )



class Presence(models.Model):
    libelle = models.CharField(max_length=100, null=True) 
    seance = models.ForeignKey(Seance , null = True , on_delete= models.SET_NULL )
    etudiant = models.ForeignKey(Students , null = True , on_delete= models.SET_NULL )
    is_present = models.BooleanField(null = False  , default=False)
    
    def __str__(self):
        return self.libelle













  

