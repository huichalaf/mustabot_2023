#include <Wire.h>

void setup() {
  Wire.begin();
  Serial.begin(9600);
  while (!Serial); // Espera a que el monitor serie se abra en Arduino IDE
  Serial.println("\nEscaneo de direcciones I2C...");
}

void loop() {
  byte error, address;
  int deviceCount = 0;

  Serial.println("Buscando dispositivos...");

  for (address = 1; address < 127; address++) {
    Wire.beginTransmission(address);
    error = Wire.endTransmission();

    if (error == 0) {
      Serial.print("Dispositivo encontrado en la dirección 0x");
      if (address < 16) {
        Serial.print("0");
      }
      Serial.print(address, HEX);
      Serial.println();
      deviceCount++;
    }
  }

  if (deviceCount == 0) {
    Serial.println("No se encontraron dispositivos I2C.");
  }

  delay(5000); // Espera 5 segundos antes de volver a escanear
}
