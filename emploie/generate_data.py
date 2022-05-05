from faker import Faker
from datetime import date
from emploie.models import TypeSalle, Salle
from filiere.models import Etablissement, Filiere
from semestre.models import Groupe, Niveau, Semestre
from module.models import Module
from users.models import CustomUser, Students, Professeur


""" EQUIPE : CodeVerse
    @author : KANNOUFA FATIMA EZZAHRA
"""


Faker.seed(3)
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

################################################################################################
################################################################################################
################################################################################################
########### users_customuser (820 users : 20 profs + 800 students)
users_prof = []
users_students = []
# users_students
for i in range(800):
    first_name = fake.first_name()
    last_name = fake.last_name()
    user = CustomUser(i+4 , "pbkdf2_sha256$260000$tgju8L06fP2IOwmmF9D7X7$89SE3SCUcjNN8PFKmOsvDOP7xt+o4dfwWeF5CPgMnMs=",
                      date.today(), 0, first_name + " " + last_name, first_name, last_name, fake.email(), 
                      0, 1, date.today(), 3)
    user.save()
    
# users_prof
for i in range(20):
    first_name = fake.first_name()
    last_name = fake.last_name()
    # mdp = irisifstg@22
    user = CustomUser(i+3 , "pbkdf2_sha256$260000$tgju8L06fP2IOwmmF9D7X7$89SE3SCUcjNN8PFKmOsvDOP7xt+o4dfwWeF5CPgMnMs=",
                      date.today(), 0, first_name + " " + last_name, first_name, last_name, fake.email(), 
                      0, 1, date.today(), 2)
    user.save()
print("insertion de 820 users")

# student : id	cne	adresse	path_photos	telephone	code_apogee	admin_id	user_id	
########### STUDENTS (800 students)
for i in range(800):
    student = Students(i+1, fake.numerify('EE######'), fake.address(), "/path_photos/",	fake.numerify('+212 6########'), fake.numerify('18#####'),	1,	1)
    student.save()
print("insertion de 800 students")

# prof : id	matricule	address	specialite	phone	profile_pic	created_at	updated_at	admin_id	
########### STUDENTS (800 students)
for i in range(20):
    prof = Professeur(matricule=fake.numerify('########'), address=fake.address(), specialite="Professeur", phone=fake.numerify('+212 6########'), profile_pic="profile", created_at=fake.date(), updated_at=date.today(), admin_id=1)
    prof.save()
print("insertion de 20 profs")

















desc = ''
for paragraph in fake.paragraphs(10):
    desc += '\n' + paragraph
    
i+1, fake.name(),fake.sentence(2), fake.sentence(10), fake.date()