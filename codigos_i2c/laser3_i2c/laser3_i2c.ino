#include <Wire.h>
#include <VL53L0X.h>
VL53L0X sensor;

int laser1 = 5;
int laser2 = 9;
int laser3 = 11;
int color1 = 51;
int color2 = 53;

void setup()
{
  Serial.begin(9600);
  Wire.begin();

  pinMode(laser1, OUTPUT); // Configurar el pin XSHUT como salida
  pinMode(laser2, OUTPUT);
  pinMode(laser3, OUTPUT);
  pinMode(color2, OUTPUT);
  pinMode(color1, OUTPUT);
  digitalWrite(laser2, LOW);
  digitalWrite(laser3, LOW);
  digitalWrite(color1, LOW);
  digitalWrite(color2, LOW);

  digitalWrite(laser1, LOW); // Establecer el pin XSHUT en LOW para apagar el sensor láser
  delay(10); // Esperar 10 ms

  digitalWrite(laser1, HIGH); // Establecer el pin XSHUT en HIGH para activar el sensor láser
  delay(10); // Esperar 10 ms

  sensor.setTimeout(500);
  if (!sensor.init())
  {
    Serial.println("Failed to detect and initialize sensor!");
    while (1) {}
  }

  sensor.startContinuous();

  digitalWrite(laser1, LOW);
}

void loop()
{
  read_laser1();
  read_laser2();
  read_laser3();
}
