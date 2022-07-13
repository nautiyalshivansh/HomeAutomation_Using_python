
#include "ESP_MICRO.h"

const int relay0 = D0;     //GPIO4
const int relay1 = D1;     //GPIO14
const int relay2 = D2;     //GPIO12
const int relay3 = D3;
const int motor1 = D5;     //GPIO12
const int motor2 = D6;
char R1S='0',R2S='0',R3S='0',R0S='0',M1S='0',M2S='0';
String str="";
void setup(){
  Serial.begin(9600);
  Connect("JioFiber-n6Sac","Dsingh@77"); // Wifi details connect to
   pinMode(relay0, OUTPUT);
   pinMode(relay1, OUTPUT);
   pinMode(relay2, OUTPUT);
   pinMode(relay3, OUTPUT);
   pinMode(motor1, OUTPUT);
   pinMode(motor2, OUTPUT);
   
  digitalWrite(relay0, LOW);
  digitalWrite(relay1, LOW);
  digitalWrite(relay2, LOW);
  digitalWrite(relay3, LOW);
  digitalWrite(motor1, LOW);
  digitalWrite(motor2, LOW);
}

void loop(){
  waitUntilNewReq();  //Waits until a new request from python come

  if (getPath()=="/OPEN_relay0"){
    digitalWrite(relay0,HIGH);
    R0S='1';
  }
  else if (getPath()=="/CLOSE_relay0"){
    digitalWrite(relay0,LOW);
    R0S='0';
  }
  else if (getPath()=="/OPEN_relay1"){
    digitalWrite(relay1,HIGH);
    R1S='1';
  }
  else if (getPath()=="/CLOSE_relay1"){
    digitalWrite(relay1,LOW);
    R1S='0';
  }
  else if (getPath()=="/OPEN_relay2"){
    digitalWrite(relay2,HIGH);
    R2S='1';
  }
  else if (getPath()=="/CLOSE_relay2"){
    digitalWrite(relay2,LOW);
    R2S='0';
  }
  else if (getPath()=="/OPEN_relay3"){
    digitalWrite(relay3,HIGH);
    R3S='1';
  }
  else if (getPath()=="/CLOSE_relay3"){
    digitalWrite(relay3,LOW);
    R3S='0';
  }
  else if (getPath()=="/OPEN_motor1"){
     digitalWrite(motor2,LOW);
    digitalWrite(motor1,HIGH);
    M1S='1';  
    M2S='0';  
  }
  else if (getPath()=="/CLOSE_motor1"){
    digitalWrite(motor1,LOW);
    digitalWrite(motor2,LOW);
     M1S='0';
  }
  else if (getPath()=="/OPEN_motor2"){
    digitalWrite(motor1,LOW);
    digitalWrite(motor2,HIGH);
    M1S='0';
    M2S='1';
  }
  else if (getPath()=="/CLOSE_motor2"){
    digitalWrite(motor1,LOW);
    digitalWrite(motor2,LOW);
    M1S='0';
    M2S='0';
  }
	str=" R0S=";
	str+=R0S;
  str+=" R1S=";
	str+=R1S;
	str+=" R2S=";
	str+=R2S;
	str+=" R3S=";
	str+=R3S;
	str+=" M1S=";
	str+=M1S;
	str+=" M2S=";
	str+=M2S;
  returnThisStr(str);
}
