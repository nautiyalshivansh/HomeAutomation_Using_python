import face_recognition
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
import os
import time
import numpy as np
import urllib
import datetime
from django.http import JsonResponse

@gzip.gzip_page
def Home(request):
    try:

        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'index.html')

def Home2(request):
    ms = "M2S=1"
    while (ms[-1] == '1'):
        n = urllib.request.urlopen("http://192.168.29.216/").read()
        str1 = n.decode('UTF-8')
        str1 = str1.split()
        r1, r2, r3, r4, ms = str1[0], str1[1], str1[2], str1[3], str1[5]
    try:
        recog(cam)
    except:
        pass
    n = urllib.request.urlopen("http://192.168.29.216/").read()
    str1 = n.decode('UTF-8')
    str1 = str1.split()
    r1, r2, r3, r4 = str1[0], str1[1], str1[2], str1[3]
    return render(request, 'index.html', {'r1': r1[-1], 'r2': r2[-1], 'r3': r3[-1], 'r4': r4[-1]})

#to capture video class
class VideoCamera(object):
    def __init__(self):
        self.cascPath = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(self.cascPath)
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        frames = self.frame
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return frames

    def ret_frame(self):
        return self.frame
    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
cam = VideoCamera()
def gen(camera):
    while True:
        frames = camera.get_frame()
        _, jpeg = cv2.imencode('.jpg', frames)
        frame =  jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def recog(camera):
    frames = camera.ret_frame()
    Detectd = False
    i=0
    current_time = datetime.datetime.now()
    second = current_time.second
    while (not Detectd):
        current_time1 = datetime.datetime.now()
        second1 = current_time1.second
        if (second1 - second == 30):
            break;
        try:
             imgEncode = face_recognition.face_encodings(frames)[0]
             img2 = cv2.imread("images/shivansh.jpg")
             imgEncode2 = face_recognition.face_encodings(img2)[0]
             result = face_recognition.compare_faces([imgEncode], imgEncode2)
             print(result[0])
             Detectd = result[0]
             if (Detectd):
                 urllib.request.urlopen("http://192.168.29.216/OPEN_motor1")
                 time.sleep(5)
                 urllib.request.urlopen("http://192.168.29.216/CLOSE_motor1")
                 time.sleep(5)
                 urllib.request.urlopen("http://192.168.29.216/OPEN_motor2")
                 time.sleep(5)
                 urllib.request.urlopen("http://192.168.29.216/CLOSE_motor2")

        except:
            print("noface detected")

