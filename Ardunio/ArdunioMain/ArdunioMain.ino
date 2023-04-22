// <---------- Engine Libraries ------------> //
#include <Servo.h>

// <------------Camera Libraries -----------> //
#include <SoftwareSerial.h>
SoftwareSerial Serial2(7,8); //(18Rx,Tx)

#include "SerialTransfer.h"
SerialTransfer myTransfer;


// <------------- Structs ------------------> //

struct __attribute__((packed)) STRUCT {
  int degree;
  int speed;
  int reset;
  int dim;
}testStruct ;

// <----------- Global Params --------------> //

// <------------Camera Params ---------------> //

int incomingData;

// <------------ Engines params ------------> //
#define MAX_SIGNAL 2000
#define MIN_SIGNAL 1000

// Sağ arka motor port : 5
// Sol arka motor port : 6
// Sağ orta motor port : 3
// Sol orta motor port : 9
// Sağ ön   motor port : 10
// Sol ön   motor port : 11


// Sağ arka motor
#define MOTOR_PIN1 5
// Sol arka motor
#define MOTOR_PIN2 6

// Sağ orta motor
#define MOTOR_PIN3 3
// Sol orta motor
#define MOTOR_PIN4 9

// Sağ ön   motor
#define MOTOR_PIN5 10
// Sol ön   motor
#define MOTOR_PIN6 11

struct ServoEngine {   // Structure declaration
  Servo engine;           // Member (int variable)
  int power;       // Member (char variable)
}; // End the structure with a semicolon


// <------------ Functions ------------> //
void ChangeEngineSpeed( ServoEngine* engine);
int PIDAlgorithmForEngines( ServoEngine* engine, int power);

// <------------ Communication param ------------> //
const int BUFFER_SIZE = 48;
char buf[BUFFER_SIZE];

// <------------ Engine param ------------> //

ServoEngine engines[6];
// Servo engines[6];
int enginesPower[6];

// <------------ Loop params ------------> //
int value, engineIndex, i, index, scale;


void setup(){
  Serial2.begin(9600);
  Serial.begin(9600);
  myTransfer.begin(Serial2);


  engines[0].engine.attach(MOTOR_PIN1);
  engines[1].engine.attach(MOTOR_PIN2);
  engines[2].engine.attach(MOTOR_PIN3);
  engines[3].engine.attach(MOTOR_PIN4);
  engines[4].engine.attach(MOTOR_PIN5);
  engines[5].engine.attach(MOTOR_PIN6);

  for (int i = 0; i < 6 ; i++){
    engines[i].power = 1500;
  }
  // Wait for input
  while (!Serial.available());
  Serial.read();
  testStruct.degree = 180;





}


void loop(){

  if(Serial.available() > 0) {
    int rlen = Serial.readBytes(buf, BUFFER_SIZE);

    value = 0;
    engineIndex = 0;
    for(index = 0; index < BUFFER_SIZE;)
    {
      scale = 1;

      for(i = 7; i >=0 ; i--)
      {
        if(i == 7 && buf[index]  == '1')
        {
          scale = -1;
        }
        else
        {
          value = value+ pow(2,i) * (buf[index] - '0');
        }
        index++;
      }
      value *= scale;
      enginesPower[engineIndex] = value * 5  + 1500;
      value = 0;
      engineIndex++;
    }
    for(i = 0; i < 6; i++)
    {
      ChangeEngineSpeed(&engines[i],enginesPower[i]);
    }



   Serial.print("Hi Raspberry Pi! You sent me: ");
    Serial.print(" 1 : ");
  Serial.print(enginesPower[0]);
    Serial.print(" 2 : ");
  Serial.print(enginesPower[1]);
    Serial.print(" 3 : ");
  Serial.print(enginesPower[2]);
    Serial.print(" 4 : ");
  Serial.print(enginesPower[3]);
    Serial.print(" 5 : ");
  Serial.print(enginesPower[4]);
    Serial.print(" 6 : ");
  Serial.print(enginesPower[5]);
  Serial.println(" ");

    }



}


void ChangeEngineSpeed( ServoEngine* engine, int power)
{
  // engine->writeMicroseconds(power parameters);
  engine->engine.writeMicroseconds(PIDAlgorithmForEngines(engine,power));

}


// lerp
int PIDAlgorithmForEngines( ServoEngine* engine, int power)
{
  int newPower =  engine->power + (engine->power - power) * 0.5;
  return (power);
}