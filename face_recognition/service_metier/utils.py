
""" EQUIPE : CodeVerse et ARopedia
    @authors :  + KANNOUFA F. EZZAHRA
                + MOUZAFIR ABDELHADI
"""

import os, cv2
from django.http.response import StreamingHttpResponse
from .classVideo import VideoCamera
from PIL import Image
import numpy as np
from semestre.models import Groupe, AnneUniversitaire
from emploie.models import Planning
import calendar
from datetime import date, datetime

from semestre.models import AnneUniversitaire, Groupe


CAMERA_PORT = 0

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
        
def getFaceDetectorXML():
    return cv2.CascadeClassifier("face_recognition/service_metier/models/face_detection.xml")

def getHaarcascadeXML():
    return cv2.CascadeClassifier("face_recognition/service_metier/models/haarcascade_frontalface_default.xml")

def getModel(filiere, niveau, groupe):
    return 'face_recognition/service_metier/saved_model/'+ filiere +'/' + niveau +'/' + groupe +'/s_model_'+ filiere + '_' + niveau +'_' + groupe+ '.yml'



path_dataset = "face_recognition/service_metier/dataset/"
      
def gen(camera):
    while True:
        frame = camera.get_frame()
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        elif camera.count >= 20:
            print("Successfully Captured")
            break
        else:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request, id):
    print(id)
    assure_path_exists(path_dataset) 
    return StreamingHttpResponse(gen(VideoCamera(id)),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
    

# récuperer les étudiants à partir de leur groupe/niveau/filiere
def getStudentsByGrp(filiere, niveau, groupe):
    # récuperer l'id du groupe
    groupe = Groupe.objects.get(nom_group=groupe, niveau__nom_niveau=niveau, niveau__filiere__nom_filiere=filiere)
    
    students = []
    # on cherche les étudiants associés à cet groupe dans la table AnneeUniversitaire
    students_grp = AnneUniversitaire.objects.filter(group_id=groupe.id)
    for student_grp in students_grp:
        students += [student_grp.etudiant]
        
    return students


# recupérer le chemin de dossier des images pour les étudiants d'un groupe donné
def getPaths(filiere, niveau, groupe):
    paths = []
    students = getStudentsByGrp(filiere, niveau, groupe)
    
    for student in students:
        path = student.path_photos
        assure_path_exists(path)
        paths += [path]
        
    return paths
    
    
# récupérer les plannings à partir du salle 
def getDataFromPlanning(idSalle):
    # récuperer le nom du jour actuel
    day = calendar.day_name[date.today().weekday()]
    
    # plannings qui ont la salle <idSalle> et programmé dans le jour/heure acutel
    plannings = Planning.objects.filter(salle_id=idSalle, jour=day.upper())
    
    mes_plannings = []
    for planning in plannings:
        heure_deb = planning.heure_debut
        heure_fin = planning.heure_fin
        current_time = datetime.now().time() 
        
        if (heure_deb < current_time and heure_fin > current_time):
            mes_plannings += [planning]
            
    return mes_plannings


# faire la correspondance entre un visage et l'id de l'étudiant correspondant  
def getImagesAndLabels(filiere, niveau, groupe):
    detector = getFaceDetectorXML()
    faceSamples=[]
    ids = []
  
    list_dir = getPaths(filiere, niveau, groupe)

    for i in range(len(list_dir)):  
        path_imgs = list_dir[i]
        list_images = os.listdir(path_imgs)
        
        for i in range(len(list_images)):
            imagePath = path_imgs + '/' + list_images[i]
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            
            print("traitement de : " + imagePath + "------>id " + str(id))
            
            PIL_img = Image.open(imagePath).convert('L')
            img_numpy = np.array(PIL_img,'uint8')
            faces = detector.detectMultiScale(img_numpy)
            
            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)

    return faceSamples,ids