import os, cv2

from ...semestre.models import AnneUniversitaire, Groupe
from ...users.models import Students
from ..service_metier.face_recognition import automatic_brightness_and_contrast
from ..service_metier.utils import getFaceDetectorXML

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
    
    
# TEST DU MODELE

def TesterModel(request):
    camera_port = 0

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    recognizer.read('face_recognition\service_metier\saved_model\IRISI\IRISI_2\G1\s_model_IRISI_IRISI_2_G1.yml')

    faceCascade = cv2.CascadeClassifier("face_recognition/service_metier/models/face_detection.xml")

    cam = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)

    while True:
        ret, img =cam.read()

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, 1.2,5)

        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 2)

            Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            
            # récupérer l'etudiant à partir de son id
            etudiant = Students.objects.get(pk=Id)

            if((100 - confidence)>10):
                label = etudiant.user.first_name + ' ' + etudiant.user.last_name + " {0:.2f}%".format(round(100 - confidence, 2))
                
                cv2.rectangle(img, (x-20,y-85), (x+w+20, y-20), (0,255,0), -1)
                cv2.putText(img, label, (x,y-40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
            else :
                cv2.putText(img,"non reconnu" , (x,y-40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
                
        cv2.imshow('face recognition', img) 

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cam.release()

    cv2.destroyAllWindows()
    

def TesterModelUpgraded(request):
    label = "Unknown"
    camera_port = 0

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    recognizer.read('face_recognition/service_metier/saved_model/IRISI/IRISI_2/G1/s_model_IRISI_IRISI_2_G1.yml')

    faceCascade = getFaceDetectorXML()

    cam = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)

    while True:
        ret, img =cam.read()
        
        auto_result, alpha, beta = automatic_brightness_and_contrast(img)
       
        gray = cv2.cvtColor(auto_result, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            
            cv2.rectangle(img, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 2)
            Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            
            # récupérer l'etudiant à partir de son id
            etudiant = Students.objects.get(pk=Id)

            if((100 - confidence)>10):
                label = etudiant.user.first_name + ' ' + etudiant.user.last_name + " {0:.2f}%".format(round(100 - confidence, 2))
                
                cv2.rectangle(img, (x-20,y-85), (x+w+20, y-20), (0,255,0), -1)
                cv2.putText(img, label, (x,y-40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
            else :
                cv2.putText(img,"non reconnu" , (x,y-40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

        cv2.imshow('face recognition', img) 
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cam.release()

    cv2.destroyAllWindows()
    
    
        
        
        
        
