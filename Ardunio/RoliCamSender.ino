#include <SoftwareSerial.h>
SoftwareSerial Serial2(7,8); //(18Rx,Tx)

#include "SerialTransfer.h"
SerialTransfer myTransfer;


struct __attribute__((packed)) STRUCT {
  int degree;
  int speed;
  int reset;
  int dim;
} testStruct;

int i = 0;
int incomingData;
void setup() {
  //Roli_Port.begin(9600);
  Serial2.begin(9600);
  Serial.begin(9600);
  myTransfer.begin(Serial2);
  testStruct.degree = 0;
  

}

void loop() {

//   if(Serial.available()>0){
//     incomingData = 0
//     Serial.print(incomingData);
//     if(incomingData>0){
    testStruct.degree = 0;}

  }

  testStruct.speed = 0;
  testStruct.reset = 0;
  testStruct.dim = 10; 
 
  uint16_t sendSize = 0;
  

  sendSize = myTransfer.txObj(testStruct, sendSize);
  myTransfer.sendData(sendSize);
  delay(100);
  
}
