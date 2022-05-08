
""" EQUIPE : CodeVerse
    @author : KANNOUFA FATIMA EZZAHRA
"""

from faker import Faker
from datetime import date
from emploie.models import Planning, Presence, Seance, TypeSalle, Salle
from filiere.models import Etablissement, Filiere
from semestre.models import Groupe, Niveau, Semestre
from module.models import ElementModule, Module
from users.models import Admin, CustomUser, Students, Professeur

  
  
#   Générer des données alétoire à l'aide de faker
#   Tables remplies : Salle, TypeSalle, Etablissement, Filiere, Niveau, Groupe, Semestre, Module, ElementModule, 
#                     CustomUser, Student, Professeur, Admin, Seance, Presence, Planning.


Faker.seed(321)
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


########### NIVEAU (2 niveaux / filière)	
irisi_N1 = Niveau(1, "IRISI_1", "ingénierie", 1)
irisi_N1.save()

irisi_N2 = Niveau(2, "IRISI_2", "ingénierie", 1)
irisi_N2.save()

sdad_N1 = Niveau(3, "SDAD_1", "master", 2)
sdad_N1.save()

sdad_N2 = Niveau(4, "SDAD_2", "master", 2)
sdad_N2.save()

sir_N1 = Niveau(5, "SIR", "licence", 3)
sir_N1.save()
print("insertion de 5 niveaux")


########### GROUPE 	(1~2 groupes / niveau)
irisi1 = Groupe(1, "G1", 1)
irisi1.save()

irisi2 = Groupe(2, "G1", 2)
irisi2.save()

sdad1 = Groupe(3, "G1", 3)
sdad1.save()

sdad2 = Groupe(4, "G1", 4)
sdad2.save()

sir_G1 = Groupe(5, "G1", 5)
sir_G1.save()

sir_G2 = Groupe(6, "G2", 5)
sir_G2.save()
print("insertion de 6 groupes")


########### SEMESTRE (1 semstre / niveau)
tab_semestres = []
s1_irisi = Semestre(1, "S1", 1)
s1_irisi.save()

s4_irisi = Semestre(2, "S4", 2)
s4_irisi.save()

s1_sdad = Semestre(3, "S1", 3)
s1_sdad.save()

s3_sdad = Semestre(4, "S3", 4)
s3_sdad.save()

s5_sir = Semestre(5, "S5", 5)
s5_sir.save()

print("insertion de 5 semestres")


########### MODULE 	(13 modules)
tab_module = [
    "Intelligence artificielle",
    "base de données répartie",
    "Analyse de données",
    "Programmation concurrentielle",
    "Communication",
    "Système d'exploitation",
    "JEE",
    "Conception UML",
    "Méthode agile",
    "administration de base de données",
]
for i in range(13):
    module = Module(libelle_module=tab_module[fake.random.randint(0,9)], semestre=Semestre.objects.get(pk = fake.random.randint(1,5)) , created_at=fake.date(), updated_at=date.today())
    module.save()
print("insertion de 13 modules")

########### users_customuser (820 users : 20 profs + 800 students)
# users_students
users_students = []
for i in range(800):
    first_name = fake.first_name()
    last_name = fake.last_name()
    user = CustomUser(username=first_name + " " + last_name + "_" + str(i), password="pbkdf2_sha256$260000$tgju8L06fP2IOwmmF9D7X7$89SE3SCUcjNN8PFKmOsvDOP7xt+o4dfwWeF5CPgMnMs=", email=last_name + "." + first_name + "@edu.uca.ma",  first_name=first_name, last_name=last_name, last_login = date.today(), user_type=3)
    user.save()
    users_students += [user]
    
# users_prof
users_prof = []
for i in range(20):   
    first_name = fake.first_name()
    last_name = fake.last_name()
    user = CustomUser(username=first_name + " " + last_name + "_" + str(i), password="pbkdf2_sha256$260000$tgju8L06fP2IOwmmF9D7X7$89SE3SCUcjNN8PFKmOsvDOP7xt+o4dfwWeF5CPgMnMs=", email=last_name + "." + first_name + "@edu.uca.ma", first_name=first_name, last_name=last_name, last_login = date.today(), user_type=2)
    user.save()
    users_prof += [user]
print("insertion de 820 users")


########### ADMIN 	
admin = Admin(created_at=fake.date(), updated_at=date.today(), admin_id=1)
admin.save()

########### STUDENTS (800 students)
for i in range(800):
    student = Students(cne=fake.numerify('EE######'), adresse=fake.address(), path_photos="/path_photos/",	telephone=fake.numerify('06########'), code_apogee=fake.numerify('18#####'), admin_id=1,	user_id=users_students[i].id)
    student.save()
print("insertion de 800 students")


############ PROFESSEUR (20 profs)
for i in range(20):
    prof = Professeur(matricule=fake.numerify('########'), specialite="Informatique", telephone=fake.numerify('06########'), created_at=fake.date(), updated_at=date.today(), admin_id=users_prof[i].id)
    prof.save()
print("insertion de 20 profs")


############ Element de module (1 element / module)
modules = Module.objects.all()
profs = Professeur.objects.all()
for i in range(13):
    elt_module = ElementModule(i+1, modules[i].libelle_module, volumeHoraire=fake.random.randint(20,30), objectif=fake.text(), created_at=fake.date(), updated_at=date.today(), module_id=modules[i].id, responsable_id=profs[i].id)
    elt_module.save()


############ Planning
elts_mod = ElementModule.objects.all()	
for i in range(20):
    elt_mod = elts_mod[fake.random.randint(0,12)]
    planning = Planning(liblle=elt_mod.libelle_element_module,
                        groupe_id=fake.random.randint(1,6),
                        professeur_id=profs[i].id,
                        salle_id=fake.random.randint(1,4),
                        element_module_id=elt_mod.id
                        )
    planning.save()


############ Seance (8~15 séances / planning)
plannings = Planning.objects.all()	
for planning in plannings:
    for i in range(fake.random.randint(8,15)):
        day = fake.date_this_month()
        seance = Seance(date_debut=day,
                        date_fin=day,
                        planning_id=planning.id
                        )
        seance.save()

############ Presence (enregistrer des présences pour chaque séance)

seances = Seance.objects.all()
etudiants = Students.objects.all()

for seance in seances:
        for i in range(fake.random.randint(20,100)):
            presence = Presence(libelle="Séance : " + str(seance.date_debut), etudiant_id=etudiants[fake.random.randint(1,800)].id, is_present=fake.boolean(), seance_id=seance.id)
            presence.save()
