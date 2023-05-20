#include <Wire.h>
#include <SparkFun_APDS9960.h>
#include <VL53L0X.h>

VL53L0X sensor;

//variables globales sensor de color:
SparkFun_APDS9960 apds = SparkFun_APDS9960();
uint16_t ambient_light = 0;
uint16_t red_light = 0;
uint16_t green_light = 0;
uint16_t blue_light = 0;

#define SENSOR1_XSHUT_PIN 2
#define SENSOR2_XSHUT_PIN 3
#define SENSOR3_XSHUT_PIN 4

//acá definimos las variables para el control de los motores, las tipo P son las que envían la señal PWM
#define P1 44
#define P2 46
#define IN1 42
#define IN2 32
#define IN3 47
#define IN4 34

//ahora definimos los pines del qtr
int qtr_1 = 6;
int qtr_2 = 7;
int qtr_3 = 8;
int qtr_4 = 9;
int qtr_5 = 11;
int qtr_6 = 10;
int qtr_7 = 13;
int qtr_8 = 12;

#define LAP_TIME_RIGHT 3000 //tiempo que se demora en dar una vuelta completa a una potencia de 100, 100
#define LAP_TIME_LEFT 3000
#define BLACK_UMBRAL 500 //umbral sobre lo cual se considera negro

double motor_power_1 = 0;
double motor_power_2 = 0;

//contadores para detectar inteseccion y semiinterseccion
int semiinterseccion_counter_right = 0;
int semiinterseccion_counter_left = 0;
int intersection_counter = 0;
//multiplicadores para los valores de los sensores del qtr
double multiplier0 = 1.25;
double multiplier1 = 3;
double multiplier2 = 3.7;
double multiplier3 = 4.5;

int pines_laseres[3] = {1,2,3};
int pines_color[2] = {4,5};
long error_previo = 0;

#define kp 0.95
#define kd -0.017
#define ki 0.0
#define PBASE 100
//-----------arriba solo parametros del PID---------------//
//valores actuales de potencia del motor, se modifican solo desde la función Mov
double power_motor_1 = 0;
double power_motor_2 = 0;

void setup(){
  Wire.begin();
  Serial.begin(9600); //iniciamos la comunicacion serial

  //ahora inicializamos todos los sensores y actuadores del robot
  motor_init();
  qtr_init();
  for(int i=0; i<3; i++){
    init_laser(&pines_laseres[i]);
  }
  for(int i=0; i<2; i++){
    color_init(&pines_color[i]);
  }
  //delay(5000);
}

void loop(){
  
  //debug_QTR();
  //debug_color();
  PID();
  //Mov(100, 100);
}
