
from django.contrib import admin
from django.urls import path,include
from django.urls import path
from face_detector import views , facedetect

urlpatterns = [
    path('cam/', facedetect.Home , ),
    path('detect/', facedetect.Home2 , ),
    path('', views.index , ),
    path('r11/', views.r1on , ),
    path('r21/', views.r2on  , ),
    path('r31/', views.r3on  , ),
    path('r41/', views.r4on  , ),
    path('r10/', views.r1off , ),
    path('r20/', views.r2off , ),
    path('r30/', views.r3off , ),
    path('r40/', views.r4off, ),
]
