
from django.shortcuts import render
from .models import *
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
import os
import face_recognition
import time
import urllib.request as ur
import numpy as np
import urllib
from django.http import JsonResponse

def index(request):
    ms = "M2S=1"
    while (ms[-1] == '1'):
        n = urllib.request.urlopen("http://192.168.29.216/").read()
        str1 = n.decode('UTF-8')
        str1 = str1.split()
        r1 ,r2 ,r3 ,r4 ,ms = str1[0] , str1[1], str1[2] , str1[3], str1[5]
    return render(request, 'index.html',{'r1' :r1[-1],'r2' :r2[-1],'r3' :r3[-1],'r4' :r4[-1]})

def r1on(request):
    ms= "M2S=1"
    while (ms[-1] == '1'):
        n = urllib.request.urlopen("http://192.168.29.216/OPEN_relay0").read()
        str1 = n.decode('UTF-8')
        str1 = str1.split()
        r1 ,r2 ,r3 ,r4 ,ms = str1[0] , str1[1], str1[2] , str1[3], str1[5]

    return render(request, 'index.html', {'r1': r1[-1], 'r2': r2[-1], 'r3': r3[-1], 'r4': r4[-1]})
def r1off(request):
    ms = "M2S=1"
    while (ms[-1] == '1'):
        n = urllib.request.urlopen("http://192.168.29.216/CLOSE_relay0").read()
        str1 = n.decode('UTF-8')
        str1 = str1.split()
        r1 ,r2 ,r3 ,r4 ,ms = str1[0] , str1[1], str1[2] , str1[3], str1[5]
    return render(request, 'index.html', {'r1': r1[-1], 'r2': r2[-1], 'r3': r3[-1], 'r4': r4[-1]})
def r2on(request):
    ms = "M2S=1"
    while (ms[-1] == '1'):
        n = urllib.request.urlopen("http://192.168.29.216/OPEN_relay1").read()
        str1 = n.decode('UTF-8')
        str1 = str1.split()
        r1, r2, r3, r4, ms = str1[0], str1[1], str1[2], str1[3], str1[5]
    return render(request, 'index.html', {'r1': r1[-1], 'r2': r2[-1], 'r3': r3[-1], 'r4': r4[-1]})
def r2off(request):
    ms = "M2S=1"
    while (ms[-1] == '1'):
        n = urllib.request.urlopen("http://192.168.29.216/CLOSE_relay1").read()
        str1 = n.decode('UTF-8')
        str1 = str1.split()
        r1 ,r2 ,r3 ,r4 ,ms = str1[0] , str1[1], str1[2] , str1[3], str1[5]
    return render(request, 'index.html', {'r1': r1[-1], 'r2': r2[-1], 'r3': r3[-1], 'r4': r4[-1]})
def r3on(request):
    ms = "M2S=1"
    while (ms[-1] == '1'):
        n = urllib.request.urlopen("http://192.168.29.216/OPEN_relay2").read()
        str1 = n.decode('UTF-8')
        str1 = str1.split()
        r1 ,r2 ,r3 ,r4 ,ms = str1[0] , str1[1], str1[2] , str1[3], str1[5]
    return render(request, 'index.html', {'r1': r1[-1], 'r2': r2[-1], 'r3': r3[-1], 'r4': r4[-1]})
def r3off(request):
    ms = "M2S=1"
    while (ms[-1] == '1'):
        n = urllib.request.urlopen("http://192.168.29.216/CLOSE_relay2").read()
        str1 = n.decode('UTF-8')
        str1 = str1.split()
        r1 ,r2 ,r3 ,r4 ,ms = str1[0] , str1[1], str1[2] , str1[3], str1[5]
    return render(request, 'index.html', {'r1': r1[-1], 'r2': r2[-1], 'r3': r3[-1], 'r4': r4[-1]})
def r4on(request):
    ms = "M2S=1"
    while (ms[-1] == '1'):
        n = urllib.request.urlopen("http://192.168.29.216/OPEN_relay3").read()
        str1 = n.decode('UTF-8')
        str1 = str1.split()
        r1 ,r2 ,r3 ,r4 ,ms = str1[0] , str1[1], str1[2] , str1[3], str1[5]
    return render(request, 'index.html', {'r1': r1[-1], 'r2': r2[-1], 'r3': r3[-1], 'r4': r4[-1]})
def r4off(request):
    ms = "M2S=1"
    while (ms[-1] == '1'):
        n = urllib.request.urlopen("http://192.168.29.216/CLOSE_relay3").read()
        str1 = n.decode('UTF-8')
        str1 = str1.split()
        r1 ,r2 ,r3 ,r4 ,ms = str1[0] , str1[1], str1[2] , str1[3], str1[5]
    return render(request, 'index.html', {'r1': r1[-1], 'r2': r2[-1], 'r3': r3[-1], 'r4': r4[-1]})
