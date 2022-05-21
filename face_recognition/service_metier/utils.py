
""" EQUIPE : CodeVerse et ARopedia
    @authors :  + KANNOUFA F. EZZAHRA
                + MOUZAFIR ABDELHADI
"""

import os, cv2
from django.http.response import StreamingHttpResponse
from .classVideo import VideoCamera
from PIL import Image
import numpy as np

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
        
def getFaceDetectorXML():
    return cv2.CascadeClassifier("face_recognition/service_metier/models/face_detection.xml")

def getHaarcascadeXML():
    return cv2.CascadeClassifier(cv2.data.haarcascades +'face_recognition/service_metier/models/haarcascade_frontalface_default.xml')
  

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
    
    
def getImagesAndLabels(path, filiere, niveau, groupe):
    
    # KANNOUFA
    # Reste à faire : 
    # Au lieu de parcourir tous les dossiers, je dois tenir compte que ceux qui concerne un grp donné

    detector = getFaceDetectorXML()
    
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