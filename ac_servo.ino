
#include <AccelStepper.h>
AccelStepper stepper(AccelStepper::DRIVER, 12, 11);

const int MAX_SPEED = 10000;
const long interval = 30;  // formula = 6000/rpm ms
unsigned long previousMillis = 0;
const word MAX_POSITION = 60000;


void setup()
{
  stepper.setMaxSpeed(MAX_SPEED);
  Serial.begin(115200);
  delay(2000);
  Serial.setTimeout(50);
}
void loop()
{
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval && Serial.available() > 0) {
    String incoming = Serial.readStringUntil('\n');
    float position = incoming.toFloat();
    if (abs(position) <= MAX_POSITION) {
      stepper.moveTo(position);  
      stepper.setSpeed(MAX_SPEED);
    }
    previousMillis = currentMillis;
  }
  stepper.runSpeedToPosition();
}
