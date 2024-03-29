
#include <Servo.h>

// <------------ Engines params ------------> //
#define MAX_SIGNAL 2000
#define MIN_SIGNAL 1000
#define MOTOR_PIN1 3
#define MOTOR_PIN2 5
#define MOTOR_PIN3 6  
#define MOTOR_PIN4 9
#define MOTOR_PIN5 10
#define MOTOR_PIN6 11

// <------------ Functions ------------> //
void ChangeEngineSpeed( Servo* engine);
int PIDAlgoritmForEngines( Servo* engine, int power);

// <------------ Communication param ------------> //
const int BUFFER_SIZE = 48;
char buf[BUFFER_SIZE]; 

// <------------ Engine param ------------> //
Servo engines[6];
int enginesPower[6];

// <------------ Loop params ------------> //
int value, engineIndex, i, index, scale;
    

void setup(){

  Serial.begin(9600);
  
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
      enginesPower[engineIndex] = value;
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

void ChangeEngineSpeed( Servo* engine, int power)
{
  // engine->writeMicroseconds(power /* *parameters*/);
  engine->writeMicroseconds(power);
}


// lerp
int PIDAlgoritmForEngines( Servo* engine, int power)
{
  return (engine->read() + (engine->read() - power) * 0.5);
}
