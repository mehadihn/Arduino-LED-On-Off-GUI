import serial
import time


class arduino_LED:
    def __init__(self):
        self.port = ""
        print("Arduino Object")

    def arduino_value(self, data, COM):
        print("Inside LED, ", data)
        print(data)
        arduino = serial.Serial(port=COM, baudrate=115200, timeout=.5)

        time.sleep(2)
        print("data " , data)
        try:
            arduino.write(data.encode())
            time.sleep(2)
            print(arduino.readline().decode('ascii'))
            print(arduino.readline().decode('utf-8').rstrip('\r\n'))
            print("Close")
            arduino.close()
        except Exception as e:
            print(e)
