import serial
import time


# Replace with your actual serial port (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux/Mac)
SERIAL_PORT = '/dev/cu.usbmodem11401'
BAUD_RATE = 9600

class ArduinoReader:
    def __init__(self, port=SERIAL_PORT, baud=BAUD_RATE):
        self.ser = serial.Serial(port, baud, timeout=1)
        time.sleep(2)  # wait for Arduino reset

    def read_line(self):
        return self.ser.readline().decode('utf-8').strip()

    def close(self):
        self.ser.close()