void read_laser1(){
  init_laser(laser1);
  //delay(10);
  sensor.setTimeout(500);
  if (!sensor.init())
  {
    Serial.println("Failed to detect and initialize sensor!");
    while (1) {}
  }

  sensor.startContinuous();
  Serial.print(laser1);
  Serial.print(": ");
  Serial.print(sensor.readRangeContinuousMillimeters());
  if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }

  Serial.print(" ; ");
  shut_down_laser(laser1);
}
void read_laser2(){
  init_laser(laser2);
  //delay(10);
  sensor.setTimeout(500);
  if (!sensor.init())
  {
    Serial.println("Failed to detect and initialize sensor!");
    while (1) {}
  }

  sensor.startContinuous();
  Serial.print(laser2);
  Serial.print(": ");
  Serial.print(sensor.readRangeContinuousMillimeters());
  if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }

  Serial.print(" ; ");
  shut_down_laser(laser2);
}
void read_laser3(){
  init_laser(laser3);
  //delay(10);
  sensor.setTimeout(500);
  if (!sensor.init())
  {
    Serial.println("Failed to detect and initialize sensor!");
    while (1) {}
  }

  sensor.startContinuous();
  Serial.print(laser3);
  Serial.print(": ");
  Serial.print(sensor.readRangeContinuousMillimeters());
  if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }

  Serial.println();
  shut_down_laser(laser3);
}
void init_laser(int pin){
  digitalWrite(pin, HIGH);
}
void shut_down_laser(int pin){
  digitalWrite(pin, LOW);
  //delay(10);
}