import serial
import json
import requests

SERIAL = 'COM7'
RATE = 9600
SERVER = "127.0.0.1:8000"


def create_json_body(data):
    list_data = list(data)
    body = {
        "Temperature": list_data[0],
        "Pressure": list_data[1],
        "Altitude": list_data[2]
    }
    return json.dumps(body)


def read_from_port(ser):
    reading = ""
    while True:
        reading += ser.readline().decode()
        if reading != "":
            data = reading.split(" ")
            if len(data) == 3:
                return map(float, data)


def main():
    print("Hello Rocket")
    serial_port = serial.Serial(SERIAL, RATE, timeout=0)

    # Read data from serial and send them in JSON to server
    while True:
        data = read_from_port(serial_port)
        body = create_json_body(data)
        requests.post(SERVER, json=body)


if __name__ == "__main__":
    main()
