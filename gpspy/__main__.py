import pynmea2
import serial

with serial.Serial("/dev/ttyACM0") as ser:
    line = ser.readline()
    print(line)
