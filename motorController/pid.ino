void PID(){
  if(analogRead(qtr_1) >= BLACK_UMBRAL) {semiinterseccion_counter_left += 1; intersection_counter += 1;}
  if(analogRead(qtr_2) >= BLACK_UMBRAL) {semiinterseccion_counter_left += 1; intersection_counter += 1;}
  if(analogRead(qtr_3) >= BLACK_UMBRAL) {semiinterseccion_counter_left += 1; intersection_counter += 1;}
  if(analogRead(qtr_4) >= BLACK_UMBRAL) {semiinterseccion_counter_left += 1; intersection_counter += 1;}
  if(analogRead(qtr_5) >= BLACK_UMBRAL) {semiinterseccion_counter_right += 1; intersection_counter += 1;}
  if(analogRead(qtr_6) >= BLACK_UMBRAL) {semiinterseccion_counter_right += 1; intersection_counter += 1;}
  if(analogRead(qtr_7) >= BLACK_UMBRAL) {semiinterseccion_counter_right += 1; intersection_counter += 1;}
  if(analogRead(qtr_8) >= BLACK_UMBRAL) {semiinterseccion_counter_right += 1; intersection_counter += 1;}

  if(intersection_counter >= 6){
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
  }

  long error = multiplier3*(analogRead(qtr_1)) + multiplier2*(analogRead(qtr_2)) + 
  multiplier1*(analogRead(qtr_3)) + multiplier0*(analogRead(qtr_4)) + -multiplier0*(analogRead(qtr_5))
  + -multiplier1*(analogRead(qtr_6)) + -multiplier2*(analogRead(qtr_7)) + -multiplier3*(analogRead(qtr_8));
  error *= kp;
  error = error + (error-error_previo)*kd;
  int potencia1 = PBASE+error;
  int potencia2 = PBASE-error;
  Mov(potencia1, potencia2);
  error_previo = error;
}
