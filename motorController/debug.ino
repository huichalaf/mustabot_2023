void debug_QTR(){
  Serial.print(analogRead(qtr_1));
  Serial.print(" , ");
  Serial.print(analogRead(qtr_2));
  Serial.print(" , ");
  Serial.print(analogRead(qtr_3));
  Serial.print(" , ");
  Serial.print(analogRead(qtr_4));
  Serial.print(" , ");
  Serial.print(analogRead(qtr_5));
  Serial.print(" , ");
  Serial.print(analogRead(qtr_6));
  Serial.print(" , ");
  Serial.print(analogRead(qtr_7));
  Serial.print(" , ");
  Serial.print(analogRead(qtr_8));
  Serial.println(";");
}

void debug_color(){
  if (  !apds.readAmbientLight(ambient_light) ||
        !apds.readRedLight(red_light) ||
        !apds.readGreenLight(green_light) ||
        !apds.readBlueLight(blue_light) ) {
    Serial.println("Error reading light values");
  } else {
    Serial.print("Ambient: ");
    Serial.print(ambient_light);
    Serial.print(" Red: ");
    Serial.print(red_light);
    Serial.print(" Green: ");
    Serial.print(green_light);
    Serial.print(" Blue: ");
    Serial.println(blue_light);
  }
  delay(50);
}
