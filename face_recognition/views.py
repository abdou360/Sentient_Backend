
""" EQUIPE : CodeVerse et ARopedia
    @authors :  + KANNOUFA F. EZZAHRA
                + MOUZAFIR ABDELHADI
"""

from django.shortcuts import render, redirect
import numpy as np
import cv2
from datetime import date
from django.http import HttpResponse
from .service_metier.utils import *
from users.models import  Students
from emploie.models import Presence, Seance
from .service_metier.face_recognition import automatic_brightness_and_contrast


#   dashboard de l'admin pour l'entrainement du modèle
def EntrainementAdminDash(request):
    context = {}
    return render(request, 'face_recognition/pages/entrainement_modele.admin.html', context)


def test_module_submit(request):

    if request.method != "POST":
        return HttpResponse("<h2> Get or whatever method is not allowed here </h2>")
    
    else:
        face_id = request.POST.get("id_etud")
        print(face_id)
        return render(request, "modules/test_module.html", {"face_id": face_id})





path_dataset = "face_recognition/service_metier/dataset/"

def training(request, filiere, niveau, groupe):
    recognizer = cv2.face.LBPHFaceRecognizer_create() 
    faces,ids = getImagesAndLabels(filiere, niveau, groupe)

    print("Training ...\nWAIT !")
    recognizer.train(faces, np.array(ids))
    
    #   dans le dossier saved_model on enregistre le modèle dans le dossier <saved_model/nom_filiere/nom_niveau/nom_grp/>
    path_dir = 'face_recognition/service_metier/saved_model/' + filiere + '/' + niveau + '/' + groupe + '/'
    assure_path_exists(path_dir)
    
    nom_modele = path_dir + 's_model_' + filiere + '_' + niveau + '_' + groupe + '.yml'
    recognizer.write(nom_modele)
    return redirect('EntrainementAdminDash')


# tester le modèle de reconnaissance
def TesterModel(request, filiere='IRISI', niveau='IRISI_2', groupe='G1'):
    # enregistrement de la séance
    # id_planning
    seance = Seance(id=261, planning_id=28, date=date.today())
    seance.save()
    
    detected_students = facerecognition(filiere, niveau, groupe)
    print("\n\nDETECTED STUDENTS\n")
    for student in detected_students:
        print(str(student.id) + " - " + student.user.username)

    print("\n\nSTUDENTS\n")
    students =  getStudentsByGrp(filiere, niveau, groupe)
    for student in students:
        if student in detected_students:
            presence = Presence(libelle='Séance : ' + str(seance.date),
                            etudiant_id= student.id,
                            is_present=True,
                            seance_id= seance.id)
            presence.save()
            print(str(student.id) + " - " + student.user.username + " --->DETECTED")
        
        else:
            presence = Presence(libelle='Séance : ' + str(seance.date),
                            etudiant_id= student.id,
                            is_present=False,
                            seance_id= seance.id)
            presence.save()
            print(str(student.id) + " - " + student.user.username)
            
    
    return redirect('EntrainementAdminDash')


######### FACE RECOGNITION
def facerecognition(filiere, niveau, groupe):
    detected_persons=set()
    label = "Unknown"

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path_model = 'face_recognition/service_metier/saved_model/'+ filiere +'/' + niveau +'/' + groupe +'/s_model_'+ filiere + '_' + niveau +'_' + groupe+ '.yml'
    recognizer.read(path_model)

    faceCascade = getFaceDetectorXML()

    imagePaths = [os.path.join("face_recognition/service_metier/folder", f) for f in os.listdir("face_recognition/service_metier/folder")]
    print(imagePaths)
    i = 0
    for imagePath in imagePaths:
        i = i + 1
        print(imagePath)
        img = cv2.imread(imagePath).copy()
        
        auto_result, alpha, beta = automatic_brightness_and_contrast(img)
       
        gray = cv2.cvtColor(auto_result, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            
            # récupérer l'etudiant à partir de son id
            etudiant = Students.objects.get(id=Id)

            if ((100 - confidence) > 10):
                label = etudiant.user.username
                detected_persons.add(etudiant)
                print("id = " + str(label))
            else:
                print(label)

    return detected_persons


###########

