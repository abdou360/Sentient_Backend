
""" EQUIPE : CodeVerse et ARopedia
    @authors :  + KANNOUFA F. EZZAHRA
                + MOUZAFIR ABDELHADI
"""

import cv2
from .utils import *
from users.models import Students


face_detection_videocam = cv2.CascadeClassifier(cv2.data.haarcascades +'face_recognition/service_metier/models/haarcascade_frontalface_default.xml')
path_dataset = "face_recognition/service_metier/dataset/"

class VideoCamera():
	def __init__(self,id):
		self.id=id
		self.video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
		self.count = 0 
  
	def __del__(self):
		self.video.release()
  
	def get_frame(self):
		success, image = self.video.read()
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5,minSize= (30,30))

		# données de l'étudiant
		etudiant = Students.objects.get(pk=self.id)
  
		for (x, y, w, h) in faces_detected:
			cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
			self.count += 1
			# e.g folder name = dataset/Etudiant_oussahi_salma/
			folder_name = path_dataset + "Etudiant_"+etudiant.user.last_name + "_" + etudiant.user.first_name  +'/'
			assure_path_exists(folder_name)
			cv2.imwrite(folder_name + "Etudiant." + str(self.id) + '.' + str(self.count) +".jpg", gray[y:y+h,x:x+w])
   
		frame_flip = cv2.flip(image,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()

