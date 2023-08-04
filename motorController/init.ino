void qtr_init(){
  pinMode(qtr_1, INPUT);
  pinMode(qtr_2, INPUT);
  pinMode(qtr_3, INPUT);
  pinMode(qtr_4, INPUT);
  pinMode(qtr_5, INPUT);
  pinMode(qtr_6, INPUT);
  pinMode(qtr_7, INPUT);
  pinMode(qtr_8, INPUT);
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

void color_init(int pinSensor){
  activateSensor(pinSensor);
  Serial.begin(9600);
  Serial.println("inicializando sensor de color ...");
  
  if ( apds.init() ) {
    Serial.println(F("APDS-9960 initialization complete"));
  } else {
    Serial.println(F("Something went wrong during APDS-9960 init!"));
  }
  
  // Start running the APDS-9960 light sensor (no interrupts)
  if ( apds.enableLightSensor(false) ) {
    Serial.println(F("Sensor de color funcionando"));
  } else {
    Serial.println(F("Something went wrong during light sensor init!"));
  }
  delay(500);
}

void init_lasers(int pinLaser){
  pinMode(laser1, OUTPUT); // Configurar el pin XSHUT como salida
  pinMode(laser2, OUTPUT);
  pinMode(laser3, OUTPUT);
  digitalWrite(laser2, LOW);
  digitalWrite(laser3, LOW);
  digitalWrite(laser1, LOW);
  delay(10);
}

void init_i2c(){
  while (!Serial);
  
  // Configurar los pines XSHUT como salidas
  pinMode(SENSOR1_XSHUT_PIN, OUTPUT);
  pinMode(SENSOR2_XSHUT_PIN, OUTPUT);
  pinMode(SENSOR3_XSHUT_PIN, OUTPUT);
  
  // Activar todos los sensores
  digitalWrite(SENSOR1_XSHUT_PIN, LOW);
  digitalWrite(SENSOR2_XSHUT_PIN, LOW);
  digitalWrite(SENSOR3_XSHUT_PIN, LOW);
}
