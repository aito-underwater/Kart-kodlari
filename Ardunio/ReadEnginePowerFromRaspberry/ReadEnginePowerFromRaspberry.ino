/*
Program: Receive Strings From Raspberry Pi
File: receive_string_from_raspberrypi.ino
Description: Receive strings from a Raspberry Pi
Author: Addison Sears-Collins
Website: https://automaticaddison.com
Date: July 5, 2020
*/
#include <Servo.h>

#define MAX_SIGNAL 2000
#define MIN_SIGNAL 1000
#define MOTOR_PIN1 3
#define MOTOR_PIN2 5
#define MOTOR_PIN3 6  
#define MOTOR_PIN4 9
#define MOTOR_PIN5 10
#define MOTOR_PIN6 11

void ChangeEngineSpeed( Servo* engine);
int PIDAlgoritmForEngines( Servo* engine, int power);

int DELAY = 1000;

const int BUFFER_SIZE = 48;
char buf[BUFFER_SIZE]; 

Servo engines[6];
int enginesPower[6];


void setup(){

  engines[0].attach(MOTOR_PIN1);
  engines[1].attach(MOTOR_PIN1);
  engines[2].attach(MOTOR_PIN2);
  engines[3].attach(MOTOR_PIN3);  
  engines[4].attach(MOTOR_PIN4);
  engines[5].attach(MOTOR_PIN5);



   
}
 
void loop(){
  

  if(Serial.available() > 0) {
    int rlen = Serial.readBytes(buf, BUFFER_SIZE);
 
    int value = 0;
    int engineIndex = 0;
    int i,index;
    int scale ;
    for(index = 0; index < BUFFER_SIZE;)
    {    
      scale = 1;

      for(i = 7; i >=0 ; i--)
      {
        if(i == 7 && buf[index]  == '-')
        {
         scale = -1;
        }
        else {
          value = value+ pow(2,i) * (buf[index] - '0');
          index++;
        }
      }
      value *= scale;
      enginesPower[engineIndex] = value;
      value = 0;
      engineIndex++;
    }
    for(i = 0; i < 6; i++)
    {
      ChangeEngineSpeed(&engines[i],enginesPower[i]);
    }
   // Serial.println("1 : %d, 2 : %d, 3 : %d, 4 : %d, 5 : %d",enginesPower[0],enginesPower[1],enginesPower[2],enginesPower[3],enginesPower[4],enginesPower[5]);
    Serial.print("1 : ");
  Serial.print(enginesPower[0]);
    Serial.print("2 : ");
  Serial.print(enginesPower[1]);
    Serial.print("3 : ");
  Serial.print(enginesPower[2]);
    Serial.print("4 : ");
  Serial.print(enginesPower[3]);
    Serial.print("5 : ");
  Serial.print(enginesPower[4]);
    Serial.print("6 : ");
  Serial.print(enginesPower[5]);
Serial.println("");
  }
  

}

void ChangeEngineSpeed( Servo* engine, int power)
{
  engine->writeMicroseconds(power);

}


// lerp
int PIDAlgoritmForEngines( Servo* engine, int power)
{
  return (engine->read() + (engine->read() - power) * 0.5);
}
