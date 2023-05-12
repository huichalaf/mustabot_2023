//acá definimos las variables para el control de los motores, las tipo P son las que envían la señal PWM
#define P1 44
#define P2 46
#define IN1 42
#define IN2 32
#define IN3 47
#define IN4 34

//ahora definimos los pines del qtr
int qtr_sensors[8] = {6,7,8,9,11,10,13,12};
int qtr_sensors_values[8];

#define BLACK_UMBRAL 500 //umbral sobre lo cual se considera negro

//ahora los valores de lectura
int qtr_sensor_values[8];

double motor_power_1 = 0;
double motor_power_2 = 0;

//contadores para detectar inteseccion y semiinterseccion
int semiinterseccion_counter_right = 0;
int semiinterseccion_counter_left = 0;
int intersection_counter = 0;
//multiplicadores para los valores de los sensores del qtr
double multiplier0 = 1;
double multiplier1 = 2;
double multiplier2 = 3;
double multiplier3 = 4;

long error_previo = 0;

#define kp 0.03
#define kd 0
#define ki 0.0
#define PBASE 100
//-----------arriba solo parametros del PID---------------//
//valores actuales de potencia del motor, se modifican solo desde la función Mov
double power_motor_1 = 0;
double power_motor_2 = 0;

void setup(){
  Serial.begin(9600); //iniciamos la comunicacion serial

  //ahora inicializamos todos los sensores y actuadores del robot
  motor_init();
  qtr_init();
}

void loop(){
  //PID();
  Mov(100, 100);
}
