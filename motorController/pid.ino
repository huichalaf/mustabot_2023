void PID(){
  /*if(1023 - analogRead(qtr_1) >= BLACK_UMBRAL) semiinterseccion_counter_left += 1; intersection_counter += 1;
  if(1023- analogRead(qtr_2) >= BLACK_UMBRAL) semiinterseccion_counter_left += 1; intersection_counter += 1;
  if(1023-analogRead(qtr_3) >= BLACK_UMBRAL) semiinterseccion_counter_left += 1; intersection_counter += 1;
  if(1023-analogRead(qtr_4) >= BLACK_UMBRAL) semiinterseccion_counter_left += 1; intersection_counter += 1;
  if(1023-analogRead(qtr_5) >= BLACK_UMBRAL) semiinterseccion_counter_right += 1; intersection_counter += 1;
  if(1023-analogRead(qtr_6) >= BLACK_UMBRAL) semiinterseccion_counter_right += 1; intersection_counter += 1;
  if(1023-analogRead(qtr_7) >= BLACK_UMBRAL) semiinterseccion_counter_right += 1; intersection_counter += 1;
  if(1023-analogRead(qtr_8) >= BLACK_UMBRAL) semiinterseccion_counter_right += 1; intersection_counter += 1;
*/
  /*if(intersection_counter >= 6){
    Serial.println("en una interseccion completa");
    semiinterseccion_counter_right = 0;
    semiinterseccion_counter_left = 0;
    intersection_counter = 0;
  }
  else if(semiinterseccion_counter_right >= 3){
    Serial.println("en una semiinterseccion derecha");
    semiinterseccion_counter_right = 0;
  }
  else if(semiinterseccion_counter_left >= 3){
    Serial.println("en una semiinterseccion izquierda");
    semiinterseccion_counter_left = 0;
  }*/

  long error = multiplier3*(1023-analogRead(qtr_1)) + multiplier2*(1023-analogRead(qtr_2)) + 
  multiplier1*(1023-analogRead(qtr_3)) + multiplier0*(1023-analogRead(qtr_4)) + -multiplier0*(1023-analogRead(qtr_5))
  + -multiplier1*(1023-analogRead(qtr_6)) + -multiplier2*(1023-analogRead(qtr_7)) + -multiplier3*(1023-analogRead(qtr_8));
  error *= kp;
  Serial.print(error);
  Serial.print(" , ");
  error = error + (error-error_previo)*kd;
  //if (error < 20) error = 0;
  Serial.println(error);
  int potencia1 = PBASE+error;
  int potencia2 = PBASE-error;
  //if (potencia2 < 0) potencia2 = 0;
  //if (potencia1 < 0) potencia1 = 0;
  Mov(potencia1, potencia2);
  error_previo = error;
}
