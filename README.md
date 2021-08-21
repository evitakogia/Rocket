# Avionics of a Model Rocket  (Arduino based telemetry board)
## Concept
This project is avionics of a model rocket. It consists of 2 Arduinos MKR wan 1300. One is on the rocket and the other on the ground. The first one is connected with a sensor (temperature, pressure, altitude). These two Arduinos communicate each other with LoRaWan. LoRaWAN is a cloud-based medium access control (MAC) layer protocol. Then, the data which the second Arduino receives, is sent to a remote server.

## Features
* 2 Arduino - MKR WAN 1300
* 2 Antennas - GSM Antenna uFL 2dBi Slim
* BMP280 Sensor - Temperature, Pressure, Altitude