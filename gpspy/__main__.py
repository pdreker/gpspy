import pynmea2
import serial

with serial.Serial("/dev/ttyACM0") as ser:
    while True:
        line = ser.readline()
        sentence = pynmea2.parse(line)
        print(sentence)
