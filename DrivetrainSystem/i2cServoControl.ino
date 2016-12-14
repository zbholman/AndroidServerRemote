#include <Wire.h>
#include <Servo.h> 
#define SLAVE_ADDRESS 0x07

Servo steering;
Servo gas;
int selector = 0;
boolean secondByte = false;

void setup() {
  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);
  // define callbacks for i2c communication
  Wire.onReceive(setServo);
  Serial.begin(9600); // start serial for output
  steering.attach(5);
  gas.attach(6);
}

void loop() {
}

// callback for received data
void setServo(int byteCount) {
  while (Wire.available()) {

    int number = (int)Wire.read();
    if(number>180){
      secondByte = true;
      selector = number;
    }
    else if(secondByte){
      if(selector == 200){ //Gas
        Serial.print("set gas servo to: ");
        Serial.println(number);
        gas.write(number);
        selector = 0;
      }
      else if(selector == 201){
        Serial.print("set steering servo to: ");
        Serial.println(number);
        steering.write(number);
        selector = 0;
      }
      
      secondByte = false;
    }
    
  }
}

