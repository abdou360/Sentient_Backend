
from http.client import PAYMENT_REQUIRED
import os

from ...semestre.models import AnneUniversitaire, Groupe

def test():
    path="dataset/"
    
    list_dir = os.listdir(path)
    print(list_dir)


    for i in range(len(list_dir)):  
        path_imgs = path + list_dir[i]
        print(path_imgs) # dossier
        list_images = os.listdir(path_imgs)
        
        for i in range(len(list_images)):
            imagePath = path_imgs + '/' + list_images[i]
            print(imagePath)
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            print("------>id " + str(id))

# modifier le nom des images pour chaque étudiant
def modifierUnDir(path, id):
    list_images = os.listdir(path)
        
    for i in range(len(list_images)):
        path_img = path + list_images[i]
        print(path_img)
        
        # on modifie le nom de chaque image
        new_name = path + 'Etudiant.' + str(id) + '.' + str(i+1) + '.jpg'
        os.rename(path_img, new_name) 



# modifierUnDir("../service_metier/dataset/Etudiant_Oussahi_Salma/", 804)      


# recupérer le chemin de dossier des images pour les étudiants d'un groupe donnée
def getPathDir(filiere, niveau, groupe):
    paths = []
    # récuperer l'id du groupe
    groupe = Groupe.objects.get(nom_group=groupe, niveau__nom_niveau=niveau, niveau__filiere__nom_filiere=filiere)
    groupe_id = groupe.id
    print('groupe_id' + str(groupe_id))
    # on cherche les étudiants associés à cet groupe dans la table AnneeUniversitaire
    students_grp = AnneUniversitaire.objects.filter(group_id=groupe_id)
    for student_grp in students_grp:
        path = student_grp.etudiant.path_photos
        paths += [path]
        
    return paths
    
    
    
paths = getPathDir("IRISI", "IRISI_2", "G1")

for path in paths:
    print(path)
    
        
        
        
        
