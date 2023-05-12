void debug_QTR(){
  Serial.print(analogRead(qtr_sensors[0]));
  Serial.print(" , ");
  Serial.print(analogRead(qtr_sensors[1]));
  Serial.print(" , ");
  Serial.print(analogRead(qtr_sensors[2]));
  Serial.print(" , ");
  Serial.print(analogRead(qtr_sensors[3]));
  Serial.print(" , ");
  Serial.print(analogRead(qtr_sensors[4]));
  Serial.print(" , ");
  Serial.print(analogRead(qtr_sensors[5]));
  Serial.print(" , ");
  Serial.print(analogRead(qtr_sensors[6]));
  Serial.print(" , ");
  Serial.print(analogRead(qtr_sensors[7]));
  Serial.println(";");
}
