void update_qtr(){
  for(int i=0; i<8; i++){
    qtr_sensor_values[i] = analogRead(qtr_sensors[i]);
  }
  Serial.println("valores actualizados");
}
void PID(){
  update_qtr();
  if(qtr_sensors_values[0] >= BLACK_UMBRAL) semiinterseccion_counter_left += 1; intersection_counter += 1;
  if(qtr_sensors_values[1] >= BLACK_UMBRAL) semiinterseccion_counter_left += 1; intersection_counter += 1;
  if(qtr_sensors_values[2] >= BLACK_UMBRAL) semiinterseccion_counter_left += 1; intersection_counter += 1;
  if(qtr_sensors_values[3] >= BLACK_UMBRAL) semiinterseccion_counter_left += 1; intersection_counter += 1;
  if(qtr_sensors_values[4] >= BLACK_UMBRAL) semiinterseccion_counter_right += 1; intersection_counter += 1;
  if(qtr_sensors_values[5] >= BLACK_UMBRAL) semiinterseccion_counter_right += 1; intersection_counter += 1;
  if(qtr_sensors_values[6] >= BLACK_UMBRAL) semiinterseccion_counter_right += 1; intersection_counter += 1;
  if(qtr_sensors_values[7] >= BLACK_UMBRAL) semiinterseccion_counter_right += 1; intersection_counter += 1;

  if(intersection_counter >= 6){
    Serial.println("en una interseccion completa");
  }
  else if(semiinterseccion_counter_right >= 3){
    Serial.println("en una semiinterseccion derecha");
  }
  else if(semiinterseccion_counter_left >= 3){
    Serial.println("en una semiinterseccion izquierda");
  }

  long error = multiplier3*qtr_sensors_values[0] + multiplier2*qtr_sensors_values[1] + multiplier1*qtr_sensors_values[2] + multiplier0*qtr_sensors_values[3] + -multiplier0*qtr_sensors_values[4] + -multiplier1*qtr_sensors_values[5] + -multiplier2*qtr_sensors_values[6] + -multiplier3*qtr_sensors_values[7];
  error *= kp;
  error = error + (error-error_previo)*kd;
  Serial.println(error);
  Mov(PBASE+error, PBASE-error);
  error_previo = error;
}
