void Mov (float X2 ,float X1 ){
  X2 = X2;
  X1 = -X1;
  if(X2>=255) X2=255;           // Satura los valores en maximos y minimos admitidos por pwm
  if(X2<=-255) X2=-255;
  if(X1>=255) X1=255;
  if(X1<=-255) X1=-255;

  motor_power_1 = X1;
  motor_power_2 = X2;

  if(X1 >= 0 && X2 >= 0){
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  analogWrite(P1,X1);
  
  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
  analogWrite(P2,X2);
  }
  
  else if (X1 < 0  && X2 < 0){
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  analogWrite(P1,-X1);
  
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,HIGH);
  analogWrite(P2,-X2);
  }
  else if(X1 >= 0 && X2 < 0){
    digitalWrite(IN1,HIGH);
    digitalWrite(IN2,LOW);
    analogWrite(P1,X1);
    
    digitalWrite(IN3,LOW);
    digitalWrite(IN4,HIGH);
    analogWrite(P2,-X2); 
  }
  else if(X1 < 0 && X2 >= 0){
    digitalWrite(IN1,LOW);
    digitalWrite(IN2,HIGH);
    analogWrite(P1,-X1);
    
    digitalWrite(IN3,HIGH);
    digitalWrite(IN4,LOW);
    analogWrite(P2,X2); 
  }
}

void Accelerate(float p1, float p2){
  //aumenta o disminuye la velocidad
  Mov(motor_power_1+p1,motor_power_2+p2);
}

void Brake(){
  Mov(0,0);
  delay(10);
}

void Brake_controlled(float p1, float p2){
  //ahora creamos una relacion entre p1 y p2
  float p1_new = p1;
  float p2_new = p2;
  if(p1 > p2){
    p2_new = p2 * (p1/p2);
  }
  else if(p2 > p1){
    p1_new = p1 * (p2/p1);
  }
  //ahora que ya creamos la relacion, frenamos progresivamente
  while(p1_new > 0 && p2_new > 0){
    Mov(p1_new,p2_new);
    p1_new -= 0.25;
    p2_new -= 0.25;
    delay(5);
  }
}

void turn_left(double grados_radianes){
  //esta función hace que el robot gire a la izquierda
  //primero frenamos
  Brake();
  //ahora giramos
  Mov(-100,100);
  //ahora esperamos
  delay((grados_radianes/6.283185307)*LAP_TIME_LEFT);
  //ahora frenamos
  Brake();
}

void turn_right(double grados_radianes){
  //esta función hace que el robot gire a la derecha
  //primero frenamos
  Brake();
  //ahora giramos
  Mov(100,-100);
  //ahora esperamos
  delay((grados_radianes/6.283185307)*LAP_TIME_RIGHT);
  //ahora frenamos
  Brake();
}
