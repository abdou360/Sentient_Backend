from django.shortcuts import render
  
import numpy as np
import cv2
import os
from module.classVideo import VideoCamera 
from django.http.response import StreamingHttpResponse
from PIL import Image

 #*@author ABDELHADI MOUZAFIR END
def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


def test_module_submit(request):
    
    
    if request.method != "POST":
        return HttpResponse("<h2> Get or whatever method is not allowed here </h2>")
    
    else:
        
        face_id=request.POST.get("id_etud")
        print(face_id)
        return render(request,"modules/test_module.html",{"face_id":face_id})

def test_module(request):
    return render(request,"modules/test_module.html")

 #*@author ABDELHADI MOUZAFIR END
def gen(camera):
    while True:
        frame = camera.get_frame()	
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        elif camera.count>=20:
            print("Successfully Captured")
            break	
        else:
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
  
            
    

 #*@author ABDELHADI MOUZAFIR END
def video_feed(request,id):
    print(id)
    assure_path_exists("module/dataset1/") 
    return StreamingHttpResponse(gen(VideoCamera(id)),
                    content_type='multipart/x-mixed-replace; boundary=frame')

def training(request):
    
    if request.method != "POST":
        return HttpResponse("<h2> Get or whatever method is not allowed here </h2>")
    
    else:
        
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        faces,ids = getImagesAndLabels('module/dataset1/')


        print("Training ...\nWAIT !")
        recognizer.train(faces, np.array(ids))

    
        assure_path_exists('module/saved_model1/')
        recognizer.write('module/saved_model1/s_model.yml')
        return render(request,"modules/test_module.html")

 #*@author ABDELHADI MOUZAFIR END
def getImagesAndLabels(path):

    detector = cv2.CascadeClassifier("module/face_detection.xml")
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
    print(imagePaths)
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:
        print("traitement de : " + imagePath)
        PIL_img = Image.open(imagePath).convert('L')
        print(PIL_img)
        img_numpy = np.array(PIL_img,'uint8')
        print(img_numpy)
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        print(id)
        faces = detector.detectMultiScale(img_numpy)
        print(faces)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])

            ids.append(id)

    return faceSamples,ids




            
 