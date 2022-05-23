
""" EQUIPE : CodeVerse et ARopedia
    @authors :  + KANNOUFA F. EZZAHRA
                + MOUZAFIR ABDELHADI
"""

import cv2, os
from .utils import getFaceDetectorXML


# @Author by FIROUD Reda
# this fucntion is gonna auto adjust the brightness and contrast of pictures
def automatic_brightness_and_contrast(image, clip_hist_percent=1):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate grayscale histogram
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    hist_size = len(hist)

    # Calculate cumulative distribution from the histogram
    accumulator = []
    accumulator.append(float(hist[0]))
    for index in range(1, hist_size):
        accumulator.append(accumulator[index - 1] + float(hist[index]))

    # Locate points to clip
    maximum = accumulator[-1]
    clip_hist_percent *= (maximum / 100.0)
    clip_hist_percent /= 2.0

    # Locate left cut
    minimum_gray = 0
    while accumulator[minimum_gray] < clip_hist_percent:
        minimum_gray += 1

    # Locate right cut
    maximum_gray = hist_size - 1
    while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
        maximum_gray -= 1

    # Calculate alpha and beta values
    alpha = 255 / (maximum_gray - minimum_gray)
    beta = -minimum_gray * alpha

    auto_result = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return (auto_result, alpha, beta)

# @authors abdelhadi mouzafir & fatima Ezzahra Kannoufa
# @recustomized by abdelhadi to fit the requirements 
def facerecognition():
    detected_persons=set()
    label = "Unknown"
    camera_port = 0

    etudiants = {
    
    6 : "mOUZAFIR",
    3 : "fATIMA",
    9 : "Aminatou",
    8 : "Sami",
    4 : "fIROUD",
}

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    recognizer.read('face_recognition/service_metier/saved_model/IRISI/IRISI_1/G1/s_model_IRISI_IRISI_1_G1.yml')

    faceCascade = getFaceDetectorXML()

    # cam = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)

    # while True:
    imagePaths = [os.path.join("face_recognition/service_metier/folder", f) for f in os.listdir("face_recognition/service_metier/folder")]
    print(imagePaths)
    i = 0
    for imagePath in imagePaths:
        i = i + 1
        print(imagePath)
        # ret, img =cam.read()
        img = cv2.imread(imagePath).copy()
        
        
        auto_result, alpha, beta = automatic_brightness_and_contrast(img)
        # cv2.imshow('face recognition'+str(i), auto_result)
       
        gray = cv2.cvtColor(auto_result, cv2.COLOR_BGR2GRAY)
        print(gray)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(30, 30))
        print(faces)
        for (x, y, w, h) in faces:
            # cv2.rectangle(img, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 2)

            Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            if ((100 - confidence) > 10):
                label = etudiants[Id] + " {0:.2f}%".format(round(100 - confidence, 2))
                detected_persons.add(etudiants[Id])
                print(label)
            else:
                # cv2.putText(img, "non reconnu", (x, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                print(label)

        # cv2.imshow('face recognition', img)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

        # while (True):
        #     # cv2.imshow('frame', auto_result);
        #     if cv2.waitKey(100) & 0xFF == ord('q'):
        #         break;

    # cam.release()

    return detected_persons


# facerecognition()
