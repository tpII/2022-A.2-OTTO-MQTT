#include <Servo.h>

//pie derecho - D4
//pie izquierdo - D3
//pierna derecha - D2
//pierna izq - D1

//Sensor trigger - D5
//Sensor echo - D6

Servo foot_right;
Servo foot_left;
Servo leg_right;
Servo leg_left;

void setup() {
  foot_right.attach(D4,500,2400);
  foot_left.attach(D3,500,2400);
  leg_right.attach(D2,500,2400);
  leg_left.attach(D1,500,2400);
}

void loop(){
  leg_right.write(0);
  delay(500);
  leg_right.write(90);
  delay(500);
  leg_right.write(180);
  delay(500);
  leg_right.write(90);
  
  delay(1000);

  leg_left.write(0);
  delay(500);
  leg_left.write(90);
  delay(500);
  leg_left.write(180);
  delay(500);
  leg_left.write(90);
  
  delay(1000);

  foot_right.write(0);
  delay(500);
  foot_right.write(90);
  delay(500);
  foot_right.write(180);
  delay(500);
  foot_right.write(90);

  delay(1000);

  foot_left.write(0);
  delay(500);
  foot_left.write(90);  
  delay(500);
  foot_left.write(180);
  delay(500);
  foot_left.write(90);  
  
  delay(1000);
}


