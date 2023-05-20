void activateSensor(int xshutPin) {
  // Desactivar todos los sensores
  digitalWrite(SENSOR1_XSHUT_PIN, LOW);
  digitalWrite(SENSOR2_XSHUT_PIN, LOW);
  digitalWrite(SENSOR3_XSHUT_PIN, LOW);

  // Activar el sensor correspondiente al pin XSHUT proporcionado
  digitalWrite(xshutPin, LOW);
  delay(100); // Esperar a que el sensor se estabilice
}

int readSensorLaser(int pinLaser){
  activateSensor(pinLaser);
  return sensor.readRangeContinuousMillimeters();
}

int readSensorColor(int color){ //1 verde, 2 rojo, 3 azul, 4 ambiente
  if (  !apds.readAmbientLight(ambient_light) ||
        !apds.readRedLight(red_light) ||
        !apds.readGreenLight(green_light) ||
        !apds.readBlueLight(blue_light) ) {
    Serial.println("Error reading light values");
  } else {
    delay(10);
    if (color == 1) return green_light;
    else if(color == 2) return red_light;
    else if(color == 3) return green_light;
    else if(color == 4) return ambient_light;
  }
  delay(50);
}