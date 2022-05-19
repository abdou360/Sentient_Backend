from django.shortcuts import render
from module.ReglageCounter import RecognizerMethod

from semestre.models import Niveau
from filiere.models import  Filiere
from users.models import  Students

from .serializers import *
import numpy as np
import cv2
import os
from module.classVideo import VideoCamera
from django.http.response import StreamingHttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from PIL import Image

# *@author ABDELHADI MOUZAFIR END


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


def test_module_submit(request):

    if request.method != "POST":
        return HttpResponse("<h2> Get or whatever method is not allowed here </h2>")

    else:

        face_id = request.POST.get("id_etud")
        print(face_id)
        return render(request, "modules/test_module.html", {"face_id": face_id})


def test_module(request):
    return render(request, "modules/test_module.html")

 # *@author ABDELHADI MOUZAFIR END


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

 # *@author ABDELHADI MOUZAFIR END


def video_feed(request, id):
    print(id)
    assure_path_exists("module/dataset/") 
    return StreamingHttpResponse(gen(VideoCamera(id)),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


def training(request):

    if request.method != "POST":
        return HttpResponse("<h2> Get or whatever method is not allowed here </h2>")
    
    else: 
        recognizer = cv2.face.LBPHFaceRecognizer_create() 
        faces,ids = getImagesAndLabels('module/dataset/')

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        faces, ids = getImagesAndLabels('module/dataset/')

        print("Training ...\nWAIT !")
        recognizer.train(faces, np.array(ids))

        assure_path_exists('module/saved_model1/')
        recognizer.write('module/saved_model1/s_model.yml')
        return render(request,"student/manage_student_template.html")

def getImagesAndLabels(path):

    detector = cv2.CascadeClassifier("module/face_detection.xml")
    
    faceSamples=[]
    ids = []
  
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
            
            print("traitement de : " + imagePath + "------>id " + str(id))
            PIL_img = Image.open(imagePath).convert('L')
            print(PIL_img)
            img_numpy = np.array(PIL_img,'uint8')
            print(img_numpy)
            print(id)
            faces = detector.detectMultiScale(img_numpy)
            print(faces)
            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])

                ids.append(id)

    return faceSamples,ids

def TesterModel(request):
    camera_port = 0

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    recognizer.read('module/saved_model1/s_model.yml')

    faceCascade = cv2.CascadeClassifier("module/face_detection.xml")

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
    
    return render(request,"student/manage_student_template.html")

 # *@author ABDELHADI MOUZAFIR START


@api_view(['GET'])
def filiere_liste(request):
    try:
        filieres = Filiere.objects.all()
        serializer = FiliereSerializer(filieres, many=True)
        return Response(serializer.data)
    except Filiere.DoesNotExist:
        return Response([])


@api_view(['GET'])
def Niveau_liste(request, nom_filiere):
    try:
        filiere = Filiere.objects.get(nom_filiere__exact=nom_filiere)
        niveaus = Niveau.objects.filter(filiere_id__exact=filiere.id).all()
        serializer = NiveauSerializer(niveaus, many=True)
        return Response(serializer.data)
    except Niveau.DoesNotExist:
        return Response([])


@api_view(['POST'])
def post_niveau(request):
    if request.data:
        label = RecognizerMethod()
        return Response(
            {
                "detected faces": label,
             "success" : "success"
             
             },

            status=200
        )

    return Response(
        {
            "error": True,
            "error_msg": "not valid",
        },
        status=400
    )
 # *@author ABDELHADI MOUZAFIR END
