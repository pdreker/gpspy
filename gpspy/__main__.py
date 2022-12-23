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

            if sentence.mode == "A":
                MODE = "Auto"
            elif sentence.mode == "M":
                MODE = "Manual"
            else:
                MODE = "Unknown"

            if sentence.mode_fix_type == "1":
                FIX_TYPE = "None"
            elif sentence.mode_fix_type == "2":
                FIX_TYPE = "2D"
            elif sentence.mode_fix_type == "3":
                FIX_TYPE = "3D"
            else:
                FIX_TYPE = "Unknown"

            print(
                f"Satellite stats: Mode: {MODE},  Fix Type: {FIX_TYPE} "
                f"Satellites: {sat_list} - PDOP: {sentence.pdop}, HDOP: {sentence.hdop}, "
                f"VDOP: {sentence.vdop}"
            )
