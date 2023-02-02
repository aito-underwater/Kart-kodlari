
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
int enginesPower[6] = {0,0,0,0,0,0};

// <------------ Loop params ------------> //
int value, engineIndex, i, index, scale;
    

void setup(){

  Serial.begin(9600);
  

  Serial.println("Don't forget to subscribe!");
  Serial.println("ELECTRONOOBS ESC calibration...");
  Serial.println(" ");
  delay(1500);
  Serial.println("Program begin...");
  delay(1000);
  Serial.println("This program will start the ESC.");

  engines[0].attach(MOTOR_PIN1);
  engines[1].attach(MOTOR_PIN1);
  engines[2].attach(MOTOR_PIN2);
  engines[3].attach(MOTOR_PIN3);
  engines[4].attach(MOTOR_PIN4);
  engines[5].attach(MOTOR_PIN5);


  Serial.print("Now writing maximum output: (");Serial.print(MAX_SIGNAL);Serial.print(" us in this case)");Serial.print("\n");
  Serial.println("Turn on power source, then wait 2 seconds and press any key.");

  engines[0].writeMicroseconds(MAX_SIGNAL);
  engines[1].writeMicroseconds(MAX_SIGNAL);
  engines[2].writeMicroseconds(MAX_SIGNAL);
  engines[3].writeMicroseconds(MAX_SIGNAL);
  engines[4].writeMicroseconds(MAX_SIGNAL);
  engines[5].writeMicroseconds(MAX_SIGNAL);

  // Wait for input
  while (!Serial.available());
  Serial.read();

  // Send min output
  Serial.println("\n");
  Serial.println("\n");
  Serial.print("Sending minimum output: (");Serial.print(MIN_SIGNAL);Serial.print(" us in this case)");Serial.print("\n");
  engines[0].writeMicroseconds(MIN_SIGNAL);
  engines[1].writeMicroseconds(MIN_SIGNAL);
  engines[2].writeMicroseconds(MIN_SIGNAL);
  engines[3].writeMicroseconds(MIN_SIGNAL);
  engines[4].writeMicroseconds(MIN_SIGNAL);
  engines[5].writeMicroseconds(MIN_SIGNAL);
  Serial.println("The ESC is calibrated");
  Serial.println("----");
  Serial.println("Now, type a values between 1000 and 2000 and press enter");
  Serial.println("and the motor will start rotating.");
  Serial.println("Send 1000 to stop the motor and 2000 for full throttle");


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
  // engine->writeMicroseconds(power /* *parameters*/);
  engine->writeMicroseconds(power);
}


// lerp
int PIDAlgoritmForEngines( Servo* engine, int power)
{
  return (engine->read() + (engine->read() - power) * 0.5);
}




