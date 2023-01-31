/*
Program: Receive Strings From Raspberry Pi
File: receive_string_from_raspberrypi.ino
Description: Receive strings from a Raspberry Pi
Author: Addison Sears-Collins
Website: https://automaticaddison.com
Date: July 5, 2020
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
void ChangeEngineSpeed(Servo* engine);
int PIDAlgoritmForEngines(Servo* engine, int power);

// <------------ Communication param ------------> //

// <------------ Engine param ------------> //
Servo engines[6];
int enginesPower[6];
int count = 0;

// <------------ Loop params ------------> //
int value, engineIndex, i, index, scale;


void setup() {

  Serial.begin(9600);
  Serial.println("Don't forget to subscribe!");
  Serial.println("ELECTRONOOBS ESC calibration...");
  Serial.println(" ");
  delay(1500);
  Serial.println("Program begin...");
  delay(1000);
  Serial.println("This program will start the ESC.");

    engines[0].attach(MOTOR_PIN1);
    engines[1].attach(MOTOR_PIN2);
    engines[2].attach(MOTOR_PIN3);
    engines[3].attach(MOTOR_PIN4);
    engines[4].attach(MOTOR_PIN5);
    engines[5].attach(MOTOR_PIN6);

  Serial.print("Now writing maximum output: (");Serial.print(MAX_SIGNAL);Serial.print(" us in this case)");Serial.print("\n");
  Serial.println("Turn on power source, then wait 2 seconds and press any key.");
  
  engines[0].writeMicroseconds(MAX_SIGNAL);
  engines[1].writeMicroseconds(MAX_SIGNAL);
  engines[2].writeMicroseconds(MAX_SIGNAL);
  engines[3].writeMicroseconds(MAX_SIGNAL);
  engines[4].writeMicroseconds(MAX_SIGNAL);
  engines[5].writeMicroseconds(MAX_SIGNAL);

  // Wait for input
  // while (!Serial.available());
  // Serial.read();

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

void loop() {

  delay(500);
  count = (millis() / 1000) % 50;


  // Serial.println(count);


Serial.println(engines[0].attached());
Serial.println(engines[1].attached());
Serial.println(engines[2].attached());
Serial.println(engines[3].attached());
Serial.println(engines[4].attached());
Serial.println(engines[5].attached());

 
    if (count < 5) {  // 1
      engines[0].writeMicroseconds(1700);
      engines[1].writeMicroseconds(1300);
      engines[2].writeMicroseconds(1300);
      engines[3].writeMicroseconds(1700);
      engines[4].writeMicroseconds(1500);
      engines[5].writeMicroseconds(1500);

          Serial.println("1");
    } else if (count < 10) {  //2
      engines[0].writeMicroseconds(1300);
      engines[1].writeMicroseconds(1700);
      engines[2].writeMicroseconds(1700);
      engines[3].writeMicroseconds(1300);
      engines[4].writeMicroseconds(1500);
      engines[5].writeMicroseconds(1500);
            Serial.println("2");
    
    } else if (count < 15) {  // 3
      engines[0].writeMicroseconds(1700);
      engines[1].writeMicroseconds(1700);
      engines[2].writeMicroseconds(1700);
      engines[3].writeMicroseconds(1700);
      engines[4].writeMicroseconds(1500);
      engines[5].writeMicroseconds(1500);
            Serial.println("3");
    
    } else if (count < 20) {  // 4
      engines[0].writeMicroseconds(1300);
      engines[1].writeMicroseconds(1300);
      engines[2].writeMicroseconds(1300);
      engines[3].writeMicroseconds(1300);
      engines[4].writeMicroseconds(1500);
      engines[5].writeMicroseconds(1500);
            Serial.println("4");
    
    } else if (count < 25) {  //5
      engines[0].writeMicroseconds(1700);
      engines[1].writeMicroseconds(1500);
      engines[2].writeMicroseconds(1500);
      engines[3].writeMicroseconds(1700);
      engines[4].writeMicroseconds(1500);
      engines[5].writeMicroseconds(1500);
            Serial.println("5");
    
    } else if (count < 30) {  // 6
      engines[0].writeMicroseconds(1500);
      engines[1].writeMicroseconds(1700);
      engines[2].writeMicroseconds(1700);
      engines[3].writeMicroseconds(1500);
      engines[4].writeMicroseconds(1500);
      engines[5].writeMicroseconds(1500);
            Serial.println("6");
    
    } else if (count < 35) {  //7
      engines[0].writeMicroseconds(1300);
      engines[1].writeMicroseconds(1500);
      engines[2].writeMicroseconds(1500);
      engines[3].writeMicroseconds(1300);
      engines[4].writeMicroseconds(1500);
      engines[5].writeMicroseconds(1500);
            Serial.println("7");
    
    } else if (count < 40) {  // 8
      engines[0].writeMicroseconds(1500);
      engines[1].writeMicroseconds(1300);
      engines[2].writeMicroseconds(1300);
      engines[3].writeMicroseconds(1500);
      engines[4].writeMicroseconds(1500);
      engines[5].writeMicroseconds(1500);
            Serial.println("8");
    
    } else if (count < 45) {  // 9
      engines[0].writeMicroseconds(1500);
      engines[1].writeMicroseconds(1500);
      engines[2].writeMicroseconds(1500);
      engines[3].writeMicroseconds(1500);
      engines[4].writeMicroseconds(2000);
      engines[5].writeMicroseconds(2000);
            Serial.println("9");
    
    } else if (count < 50) {  // 10
      engines[0].writeMicroseconds(1500);
      engines[1].writeMicroseconds(1500);
      engines[2].writeMicroseconds(1500);
      engines[3].writeMicroseconds(1500);
      engines[4].writeMicroseconds(1000);
      engines[5].writeMicroseconds(1000);
           
    
    } else
      count = 0;

}