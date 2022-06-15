
""" EQUIPE : CodeVerse et ARopedia
    @authors :  + FIROUD REDA
                + MOUZAFIR ABDELHADI
"""

import cv2, time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from .registerPresence import registerPresenceDB
from .utils import assure_path_exists, CAMERA_PORT


def RecognizerMethod():
        print('hiii')
        # gauth = GoogleAuth()
        # drive = GoogleDrive(gauth)
        path_dir = "face_recognition/service_metier/folder/"
        assure_path_exists(path_dir) 
        i=0
        cap = cv2.VideoCapture(CAMERA_PORT, cv2.CAP_DSHOW)    
        ret, frame = cap.read()
        
        while(i <8):
                if ret:                
                        # cv2.namedWindow('Camera',cv2.WINDOW_NORMAL)
                        # cv2.imshow('Camera',frame)
                        #assure_path_exists("module/folder/") 
                        #cv2.imwrite("folder/frame"+str(i)+".jpg", frame)

                        cv2.imwrite(path_dir + "frame"+str(i)+".jpg", frame)

                        #gfile = drive.CreateFile({'parents': [{'id': '11USmWh7Dm0aUFnzwEKpCX8JjNwO6VAAe'}]})
                        # Read file and set it as the content of this instance.
                        #gfile.SetContentFile(path_dir + "frame"+str(i)+".jpg")
                        #gfile.Upload()  # Upload the file.
                else:
                        print("No image detected. Please! try again")

                time.sleep(5)
                i+=1
                if cv2.waitKey(1) & 0xFF == ord('q') :
                        break
        
        cap.release()
        cv2.destroyAllWindows()

        return registerPresenceDB(2)