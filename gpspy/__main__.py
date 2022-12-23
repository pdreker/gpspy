import pynmea2
import serial

with serial.Serial("/dev/ttyACM0") as ser:
    while True:
        line = ser.readline().decode("ascii")
        sentence = pynmea2.parse(line)
        if sentence.sentence_type == "GSA":

            sat_list = [
                sat
                for sat in [
                    sentence.sv_id01,
                    sentence.sv_id02,
                    sentence.sv_id03,
                    sentence.sv_id04,
                    sentence.sv_id05,
                    sentence.sv_id06,
                    sentence.sv_id07,
                    sentence.sv_id08,
                    sentence.sv_id09,
                    sentence.sv_id10,
                    sentence.sv_id11,
                    sentence.sv_id12,
                ]
                if sat
            ]

            print(
                f"Satellite stats: Mode: {sentence.mode},  Fix Type: {sentence.mode_fix_type} "
                f"Satellites: {sat_list} - PDOP: {sentence.pdop}, HDOP: {sentence.hdop}, "
                f"VDOP: {sentence.vdop}"
            )
