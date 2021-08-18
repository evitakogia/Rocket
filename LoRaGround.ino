//Libraries for LoRa WAN
#include <SPI.h>
#include <LoRa.h>

// Initialize variables to get and save LoRa data
String loRaMessage;
String Temperature;
String Altitude;
String Pressure;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("LoRa Receiver");

  if (!LoRa.begin(915E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}

void loop() {
  // try to parse packet
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    // received a packet
    Serial.println("Received packet '");

    // read packet
    while (LoRa.available()) {
      String LoRaData = LoRa.readString();
      //Serial.println(LoRaData); 
      
      // Get readingID, temperature and soil moisture
      int pos1 = LoRaData.indexOf('&');
      int pos2 = LoRaData.indexOf('#');
      Temperature = LoRaData.substring(0, pos1);
      Pressure = LoRaData.substring(pos1+1, pos2);
      Altitude = LoRaData.substring(pos2+1, LoRaData.length());  

      Serial.print("TEMPERATURE");
      Serial.print(":");
      Serial.print(Temperature);
      Serial.println("*C");
      Serial.print("PRESSURE");
      Serial.print(":");
      Serial.print(Pressure);
      Serial.println("Pa");
      Serial.print("ALTITUBE");
      Serial.print(":");
      Serial.print(Altitude);
      Serial.println("m"); 
      Serial.println();   
    }
  }
}
