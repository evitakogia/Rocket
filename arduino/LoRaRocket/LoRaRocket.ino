//Libraries for LoRa
#include <Wire.h>
#include <SPI.h>
#include <LoRa.h>

//Libraries for BMP280
#include <Adafruit_BMP280.h>

//define the pins used by the LoRa transceiver module
#define BMP_SCK  (5)
#define BMP_MISO (19)
#define BMP_MOSI (27)
#define BMP_SS   (18)
#define BMP_RST   (14)
#define BMP_DIO0  (26)

Adafruit_BMP280 bmp; // I2C

//global variables for temperature and Humidity
float Temperature = 0;
float Altitude = 0;
float Pressure = 0;

//initilize packet counter
String LoRaMessage = "";

void setup() {
  delay(1000);
  Serial.begin(9600);
  while (!Serial);
  
  Serial.println("LoRa Sender Test!");
  
  if (!LoRa.begin(915E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
  
  if (!bmp.begin(0x76)) {
    Serial.println(F("Could not find a valid BMP280 sensor, check wiring or "
                      "try a different address!"));
    while (1) delay(10);
  }

  /* Default settings from datasheet. */
  bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,     /* Operating Mode. */
                  Adafruit_BMP280::SAMPLING_X2,     /* Temp. oversampling */
                  Adafruit_BMP280::SAMPLING_X16,    /* Pressure oversampling */
                  Adafruit_BMP280::FILTER_X16,      /* Filtering. */
                  Adafruit_BMP280::STANDBY_MS_500); /* Standby time. */
}

void getReadings() {
    Temperature = bmp.readTemperature();
    Serial.print(F("Temperature = "));
    Serial.print(bmp.readTemperature());
    Serial.println(" °C");

    Pressure = bmp.readPressure();
    Serial.print(F("Pressure = "));
    Serial.print(bmp.readPressure());
    Serial.println(" Pa");

    Altitude = bmp.readAltitude(1013.25);
    Serial.print(F("Approx altitude = "));
    Serial.print(bmp.readAltitude(1013.25)); /* Adjusted to local forecast! */
    Serial.println(" m");

    Serial.println();
    delay(500);
}

void displayReadings()
{
  LoRa.print("TEMPERATURE");
  LoRa.print(":");
  LoRa.print(Temperature);
  LoRa.print("*C");
  LoRa.print("PRESSURE");
  LoRa.print(":");
  LoRa.print(Pressure);
  LoRa.print("Pa");
  LoRa.print("ALTITUBE");
  LoRa.print(":");
  LoRa.print(Altitude);
  LoRa.print("m");
  Serial.println("Sending packet: ");
}

void sendReadings() {
  LoRaMessage = String(Temperature) + "&" + String(Pressure) + "#" + String(Altitude);
  //Send LoRa packet to receiver
  LoRa.beginPacket();
  LoRa.print(LoRaMessage);
  LoRa.endPacket();

  Serial.println("Packet Sent!");
  displayReadings();

  delay(1000);
}

void loop() {
  getReadings();
  sendReadings();
}
