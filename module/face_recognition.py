# @enhanced by FIROUD Reda
import cv2
import numpy as np
import os

import skimage.measure as measure
from matplotlib import pyplot as plt


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

# @author abdelhadi mouzafir & fatima & Reda
def facerecognition():
    camera_port = 0

    etudiants = {
        1: "FIROUD",
        2: "NAOUFAL",
    }

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    recognizer.read('module/saved_model1/s_model.yml')

    faceCascade = cv2.CascadeClassifier("face_detection.xml")

    # cam = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)

    # while True:
    imagePaths = [os.path.join("module/folder", f) for f in os.listdir("module/folder")]
    i = 0
    for imagePath in imagePaths:
        i = i + 1
        print(imagePath)
        # ret, img =cam.read()
        img = cv2.imread(imagePath).copy()
        # //////////////////////

        auto_result, alpha, beta = automatic_brightness_and_contrast(img)

        ############################################
        gray = cv2.cvtColor(auto_result, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(auto_result, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 2)

            Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            if ((100 - confidence) > 10):
                label = etudiants[Id] + " {0:.2f}%".format(round(100 - confidence, 2))

                cv2.rectangle(auto_result, (x - 20, y - 85), (x + w + 20, y - 20), (0, 255, 0), -1)
                cv2.putText(auto_result, label, (x, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                writer.output('Presence_IRISI2_', 'IRISI 2', Id, etudiants[Id], 'yes')
            else:
                cv2.putText(auto_result, "non reconnu", (x, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # cv2.imshow('face recognition', img)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

        while (True):
            # cv2.imshow('frame', auto_result);
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break;

    # cam.release()

    cv2.destroyAllWindows()


# facerecognition()
