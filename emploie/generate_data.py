import os
from random import random
from faker import Faker
from emploie.models import TypeSalle, Salle
from filiere.models import Etablissement, Filiere
from semestre.models import Niveau

""" EQUIPE : CodeVerse
    @author : KANNOUFA FATIMA EZZAHRA
"""


fake = Faker('FR_fr')

########### typesalle (amphi et salle)
type_salle_amphi = TypeSalle(1, 500, "Amphi")
type_salle_amphi.save()

type_salle_salle = TypeSalle(2, 50, "Salle")
type_salle_salle.save()
print("insertion de 2 type_salle")


########### Salle (2 salles et 2 amphi)
salle_1 = Salle(1, "I7", True, 1)
salle_1.save()

salle_1 = Salle(2, "I8", False, 1)
salle_1.save()

salle_1 = Salle(3, "Amphi 1", True, 2)
salle_1.save()

salle_1 = Salle(4, "Amphi 4", False, 2)
salle_1.save()
print("insertion de 4 salles")


	
########### Etablissement (FSTG)
etab = Etablissement(1, "Faculté des Sciences et Techniques Marrakech", "B.P 549, Av.Abdelkarim Elkhattabi, Guéliz Marrakech", "(+212) 524 43 34 04", "Enseignement supérieur", "http://www.fstg-marrakech.ac.ma/FST/", "contact@fstg-marrakech.com", "https://via.placeholder.com/640x480.png/004466?text=fstg+logo")
etab.save()
print("insertion de 1 etablissement")


########### FILIERE (IRISI, SDAD, SIR)	

irisi = Filiere(1, "IRISI", "https://via.placeholder.com/640x480.png/004466?text=irisi+logo", 1)
irisi.save()

sdad = Filiere(2, "SDAD", "https://via.placeholder.com/640x480.png/004466?text=sdad+logo", 1)
sdad.save()

sir = Filiere(3, "SIR", "https://via.placeholder.com/640x480.png/004466?text=sir+logo", 1)
sir.save()
print("insertion de 3 filieres")

#id	nom_niveau	type_niveau	filiere_id	
########### NIVEAU (2 niveaux pour chaque filière)	

irisi_N1 = Niveau(1, "IRISI", "https://via.placeholder.com/640x480.png/004466?text=irisi+logo", 1)
irisi_N1.save()

irisi_N2 = Filiere(2, "SDAD", "https://via.placeholder.com/640x480.png/004466?text=sdad+logo", 1)
irisi_N2.save()

sir = Filiere(3, "SIR", "https://via.placeholder.com/640x480.png/004466?text=sir+logo", 1)
sir.save()
print("insertion de 3 filieres")

for i in range(30):
    author_name = fake.name()
    titre = fake.sentence(6)
    desc = ''
    for paragraph in fake.paragraphs(10):
        desc += '\n' + paragraph
    
    date = fake.date()
   
    news = News(i+1,author_name,titre,desc)
    news.save()
    print("insertion d un nouveau element : " + titre)
    
# Quotes    
for i in range(30):
    quote = Quote(i+1, fake.name(),fake.sentence(2), fake.sentence(10), fake.date())
    quote.save()
    print("insertion d un nouveau element : ")