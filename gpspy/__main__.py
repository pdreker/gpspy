import pynmea2
import serial

with serial.Serial("/dev/ttyACM0") as ser:
    while True:
        line = ser.readline().decode("ascii")
        sentence = pynmea2.parse(line)
        print(sentence.fields)
