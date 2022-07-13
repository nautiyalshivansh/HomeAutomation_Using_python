# HomeAutomation_Using_python

CHAPTER 1 INTRODUCTION
1.1	PROBLEM STATEMENT
Automation of the Home Appliance to be control through any device with any web server. Through the web server the user should be able to control the home appliance


1.2	ABSTRACT / MOTIVATION

In today’s world everyone wants their home to be fully functional with a one click using their phone or by just scheduling the lights to be turned off or on but the problem with this already available technology is the price at which it is available. 

The motivation of building this project was to build a cheaper solution along with the added functionality of embedding the online server already available to us at home with the appliance so that they can be interconnected with each other using the microprocessor with Wi-Fi module prebuilt in it. Through this project we aim to develop an web based application accessible to all the user available to that server with any device to be able to control their applications

The System will have the ability to open the door using any of the methods like face recognition or using fingerprint recognition or using password sharing modules.


1.3	Tool Used:-
Arduino Ide
PyCharm

1.4	Requirement: -
1.4.1		Integrated Development Environment (IDE): 
•	PyCharm
•	Arduino


1.4.2		Programming Language: 
•	C (Arduino programming)
•	Python (face check)
•	HTML , CS , Js (Frontend)

1.4.3	Software Development Kit (SDK):
•	 Django
1.4.4	Model Used:  
•	Face Recognition (python) https://github.com/ageitgey/face_recognition
•	ESP8266 Wi-Fi Module
•	ESP8266 mDNS Module
•	WIFIClient 
1.4.5	Other Packages:
•	 Cv2
•	Urllib request

1.4.6	Hardware Requirements: 
•	Node Mcu Esp 8266 chip
•	Esp Compatible Wifi Module
•	Relay switch module
•	Motor (door control)
•	System:
•	Camera					
•	Web server
•	Same Wifi Access for web server + esp8266 server	


1.4.7	Minimum hardware Requirement:-
•	Multi Core CPU(octa core 1.7Ghz)
•	4 Gb ram
•	Graphic card (intel x graphic 2 gb ) or Eq.



CHAPTER 2 
Approaches

2.1	Arduino Esp8266: -
		
	All the functionality to be used in an application should be first implemented so that these functionality do not need to search again and again to do that Ardunio Module is linked with the header file to generalize the request that is being fetched from the client and is required to be processed in the server side i.e. esp8266 module.
			
In ardunio module the Code is only compile once in the Arduino ide or any other suitable id the code executed is then transferred to the Arduino board in our case that is esp8266.
Esp8266  is a microprocessor based along with the wifi module which is pocket friendly board containg in total 30 pins in it comprising of 17 analog and digital pins and 4 ground pin and      3 VCC along with rst , CH_pd , RXand tx. Esp8266 only support voltage upto 3.3 volt only.
        
	Features :- 
•	32 bit based processor
•	32 kb Cache
•	32 kb Ram
•	80 kb user data ram
•	16 kb system data ram
•	Lua Based Framework
		
	



2.2 	Connecting Esp8266 server with Python

We need to convert python – Django based server to the esp8266 server for the flexibility in the frontend so that new updates can be pushed over the air without executing the Arduino code again again  which can lead to memory degradation of the chip.
So a djngo based webframe is connected with the the microprocessor server using the python module urllib.request. using functionality of request.openurl method inside urllib module .
In this we ping the esp8266 server using openurl and the status of the pin is returned when a server is ping which is read using .read() method .
Documentation of Urllib:-
	https://docs.python.org/3/library/urllib.html




2.4	Detecting face to control door

Face detection and recognition module is used along with the cv2 “https://docs.opencv.org/4.x/”  method to detect and open the camera and if face is detected then the face recognition technique using module face-recognition “https://github.com/ageitgey/face_recognition”.
Face recognition uses built in c library Dlib which has an accuracy of about 99% to compare 2 frame and if face detected frame matches then it returned an array of flag variable i.e. True or False. The face recognition technique extract all the face from a frame and give an output in the form of an grid .
Once the face is detected and the output array is found to be true the ESp8266 server is pinged for the motor pin to be opened is is kept open till the door is not opened for demo instance the time is set to 5 can also be done with input from an pin of ardunio. After few seconds the door is again set to off mode till it is completely closed.

