
import cv2,os,urllib.request
import numpy as np
from django.conf import settings




face_detection_videocam = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
#*@author ABDELHADI MOUZAFIR END
class VideoCamera():
	def __init__(self,id):
		self.id=id
		self.video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
		self.count = 0
  
  
	def __del__(self):
		self.video.release()
	def get_frame(self):
     
		
		success, image = self.video.read()
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces_detected = face_detection_videocam.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5,minSize= (30,30))
  
  
		for (x, y, w, h) in faces_detected:
			cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
			self.count += 1
   
			cv2.imwrite("module/dataset1/User." + str(self.id) + '.' + str(self.count) + ".jpg", gray[y:y+h,x:x+w])
   
		
   
   
		frame_flip = cv2.flip(image,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()

