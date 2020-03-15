/*
  f = 1 / T
  400us = 6.25Khz square wave
  Servo drive frequency - Fn9

  References
  https://reprage.com/post/non-blocking-control-of-stepper-motors-on-arduino
  https://www.makerguides.com/a4988-stepper-motor-driver-arduino-tutorial/
*/

const int STEP_PIN = 12;
const int DIR_PIN = 11;
const int STEP_DELAY = 50;
const int stepsPerRevolution = 10000;


void setup() {
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);
}


void step() {
  digitalWrite(STEP_PIN, LOW);
  delayMicroseconds(STEP_DELAY);
  digitalWrite(STEP_PIN, HIGH);
  delayMicroseconds(STEP_DELAY);
}


void loop() {
  moveCW();
  delay(1000);
  moveCCW();
  delay(1000);
}


void moveCW() {
  digitalWrite(DIR_PIN, HIGH);
  for (int i = 0; i < stepsPerRevolution; i++) {
    step();
  }
}


void moveCCW() {
  digitalWrite(DIR_PIN, LOW);
  for (int i = 0; i < stepsPerRevolution; i++) {
    step();
  }
}
