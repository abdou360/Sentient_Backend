# @author abdelhadi mouzafir
import cv2
import os
import numpy as np
import time
from .face_recognition import *
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive






def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


# # cap = cv2.VideoCapture(0)
# # i=0
# def video(i):
#     cap = cv2.VideoCapture(0)    
#     ret, frame = cap.read()

#     if ret:
#             assure_path_exists("module/folder/") 
#             cv2.namedWindow('Camera',cv2.WINDOW_NORMAL)
#             cv2.imshow('Camera',frame)
#             cv2.imwrite("folder/frame"+str(i)+".jpg", frame)
#     else:
#             print("No image detected. Please! try again")

def RecognizerMethod():
        gauth = GoogleAuth()
        drive = GoogleDrive(gauth)
        assure_path_exists("module/folder") 
        i=0
        cap = cv2.VideoCapture(0)    
        ret, frame = cap.read()
        
        while(i <4):
                   
                if ret:
                      
                        # cv2.namedWindow('Camera',cv2.WINDOW_NORMAL)
                        # cv2.imshow('Camera',frame)
                        cv2.imwrite("module/folder/frame"+str(i)+".jpg", frame)

                        gfile = drive.CreateFile({'parents': [{'id': '11USmWh7Dm0aUFnzwEKpCX8JjNwO6VAAe'}]})
                        # Read file and set it as the content of this instance.
                        gfile.SetContentFile("module/folder/frame"+str(i)+".jpg")
                        gfile.Upload()  # Upload the file.
                else:
                        print("No image detected. Please! try again")

                
                
                time.sleep(5)
                i+=1
                if cv2.waitKey(1) & 0xFF == ord('q') :
                        break
        
        cap.release()
        cv2.destroyAllWindows()

        return facerecognition()