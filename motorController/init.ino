void qtr_init(){
  pinMode(qtr_sensors[1], INPUT);
  pinMode(qtr_sensors[2], INPUT);
  pinMode(qtr_sensors[3], INPUT);
  pinMode(qtr_sensors[4], INPUT);
  pinMode(qtr_sensors[5], INPUT);
  pinMode(qtr_sensors[6], INPUT);
  pinMode(qtr_sensors[7], INPUT);
  pinMode(qtr_sensors[8], INPUT);
  Serial.println("QTR inicializado");
}

void motor_init(){
  pinMode(P1,OUTPUT);
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(P2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  Serial.println("Motores inicializados");
}
