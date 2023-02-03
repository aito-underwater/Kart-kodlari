/*
#include <Servo.h>

#define MAX_SIGNAL 2000
#define MIN_SIGNAL 1000
#define MOTOR_PIN1 3
#define MOTOR_PIN2 5
#define MOTOR_PIN3 6  
#define MOTOR_PIN4 9
#define MOTOR_PIN5 10
#define MOTOR_PIN6 11

/*
Servo myservo; 
Servo myservo2;// Create a Servo object for the motor
Servo myservo3;
Servo myservos[3]; 
*//*
Servo engines[6];
const int motorPin =6;    // Pin that controls the motor
const int motorPin2 = 9;
void setup() {
  engines[0].attach(MOTOR_PIN1);
  engines[1].attach(MOTOR_PIN2);
  engines[2].attach(MOTOR_PIN3);
  engines[3].attach(MOTOR_PIN4);
  engines[4].attach(MOTOR_PIN5);
  engines[5].attach(MOTOR_PIN6);
//  myservo.attach(MOTOR_PIN1);   // Attach the Servo object to the motor pin

}

void loop() {
  for (int i = 1000; i <= 2000; i++) {    // Increase the PWM value from 1000 to 2000 microseconds
  /* myservo.writeMicroseconds(i);
   myservo2.writeMicroseconds(i);
   myservo3.writeMicroseconds(i);
   myservos[0].writeMicroseconds(i);
  *//*
  // Write the PWM value to the motor pin
    delay(1);   // Wait for 1 millisecond
  }
  for (int i = 2000; i >= 1000; i--) {    // Decrease the PWM value from 2000 to 1000 microseconds
   // for (int k = 0;k < 6; k++)
      //   engines[k].writeMicroseconds(i);   // Write the PWM value to the motor pin
    delay(1);   // Wait for 1 millisecond
  }
}

*/

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
  engines[1].attach(MOTOR_PIN2);
  engines[2].attach(MOTOR_PIN3);
  engines[3].attach(MOTOR_PIN4);
  engines[4].attach(MOTOR_PIN5);
  engines[5].attach(MOTOR_PIN6);



  // Wait for input
  while (!Serial.available());
  Serial.read();



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


void ChangeEngineSpeed( Servo* engine, int power)
{
  // engine->writeMicroseconds(power parameters);
  engine->writeMicroseconds(power);
    Serial.println(" sadasdsad");
}


// lerp
int PIDAlgoritmForEngines( Servo* engine, int power)
{
  return (engine->read() + (engine->read() - power) * 0.5);
}