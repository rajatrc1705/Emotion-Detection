from imutils.video import VideoStream, FPS
import torch
import torch.nn as nn
import torch.nn.functional as F
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from torch.autograd import Variable
from torch.optim import Adam
from torchvision.transforms import transforms
from torch.utils.data import DataLoader
from PIL import Image
from login.Model import Net
from auth.settings import BASE_DIR
from sys import platform

class Emotion_detection():
    def __init__(self):
        self.vs = VideoStream(src=0).start()
        self.fps = FPS().start()

    def __del__(self):
        cv2.destroyAllWindows()

    def get_frame(self):
        model_load = Net()
        model_load.load_state_dict(torch.load(
            BASE_DIR / 'best_checkpoint.model', map_location=torch.device('cpu')))
        model_load.eval()

        if platform == "linux":    
            cascPath = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
        else:
            cascPath = os.path.dirname(cv2.__file__) + "\\data\\haarcascade_frontalface_alt2.xml"
        print("CascPath ", cascPath)
        faceCascade = cv2.CascadeClassifier(cascPath)

        frame = self.vs.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,
                                             scaleFactor=1.1,
                                             minNeighbors=5,
                                             minSize=(60, 60),
                                             flags=cv2.CASCADE_SCALE_IMAGE)

        face_detected = 0
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face_detected = 1
            # Display the resulting frame
        moods = ["angry", "disgusted", "fearful",
                 "happy", "neutral", "sad", "surprised"]
    #     cv2.imshow('Video', frame)

        if face_detected == 1:
            roi = frame[y:y+h, x:x+w]
            # cv2.imshow('Face', roi)
        else:
            roi = frame
        key = cv2.waitKey(5) & 0xFF
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (48, 48))
    #     gray.resize(48, 48)
        gray1 = gray.copy()
        gray_np = np.array([[gray]])
    #     gray = gray.resize((48, 48))
        final_image = Variable(torch.Tensor(gray_np))

        image, grayimg = final_image, gray1

        output = model_load(image)

        cv2.putText(frame, moods[int(str(torch.max(output.data, 1))[-4])],
                    (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        # cv2.imshow('Video', frame)
        # cv2.imshow('Grayscale', grayimg)
    #     print(str(torch.max(output.data, 1)))
        output = torch.max(output.data, 1)
        self.fps.update()

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
