import serial
import json

def json_data(data):
    l = list(data)
    x = {
        "Temperature": l[0],
        "Pressure": l[1],
        "Altitude": l[2]
    }
    print(json.dumps(x))
   
def read_from_port(ser):
    reading = ""
    while True:
        reading += ser.readline().decode()
        if reading != "":
            print(reading)
            data = reading.split(" ")
            if len(data) == 3:
                json_data(map(float, data))
                reading = ""

def main():
    print("Hello Rocket")
    port = 'COM7'
    baud = 9600

    serial_port = serial.Serial(port, baud, timeout=0)

    read_from_port(serial_port)
    
if __name__ == "__main__":
    main()