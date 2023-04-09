import csv
import os
import struct
import sys
import threading
import time
import warnings

import keyboard
import psutil
import serial
from prettytable import PrettyTable

sys.path.insert(0, '../../')

import AITOSensors as Sensor
import EnginePower

my_file = open("data.csv", "a")
my_file.seek(0, os.SEEK_END)
cvs_writer = csv.writer(my_file)


def main():
    count = 0
    go_down = False
    ser = serial.Serial('/dev/ttyS0', 115200, timeout=None)  # replace ttyAMA0 with the appropriate serial port

    timer = time.time()
    task = None
    target = None
    data = []
    while ser.in_waiting:
        ser.flush()
        response = ser.read(8)
        data_left = ser.inWaiting()  # Get the number of characters ready to be read
        response += ser.read(data_left)
        print(response)
        time.sleep(1)
        if len(response) > 8:
            permData = struct.unpack('ii', response[0:8])
            data.append(permData[0])
            data.append(permData[1])

        print("---------------------")
        if go_down is True:
            print("###############")
            EnginePower.send_data_to_engines(EnginePower.down_vector)

        else:
            print("+++++++++++++++++")
            if len(data) != 0:

                #  temperature, pressure, humidity = Sensor.readBME280All()
                # Gx, Gy, Gz, Ax, Ay, Az = Sensor.MPUData()

                myTable = PrettyTable(["Sensor Name:", "Value"])
                myTable.add_row(["Lidar1 cm", Sensor.getTFminiData2()])
                # myTable.add_row(["Lidar2 cm", Sensor.getTFminiData1()])
                # myTable.add_row(["Lidar3 cm", str(Sensor.getTFminiData22())])
                # myTable.add_row(["Gyro Gx", Gx])
                # myTable.add_row(["Gyro Gy", Gy])
                # myTable.add_row(["Gyro Gz", Gz])
                # myTable.add_row(["Gyro Ax", Ax])
                # myTable.add_row(["Gyro Ay", Ay])
                # myTable.add_row(["Gyro Az", Az])
                # myTable.add_row(["Bar", Sensor.WPSData()])
                # myTable.add_row(["Temperature C", temperature]
                # myTable.add_row(["Pressure hPa", pressure])
                # myTable.add_row(["Humidity %", humidity])

                # <-------------------------------------------------------->
                # !!! Yapay zeka kodu burası !!!
                power_vector = EnginePower.calculate_engines_power(data)
                print(go_down)

                if power_vector is True:
                    go_down = True

                if go_down is True:
                    EnginePower.send_data_to_engines(EnginePower.down_vector)
                else:
                    EnginePower.send_data_to_engines(
                        EnginePower.select_vector(power_vector) + EnginePower.stable_vector)
                # <-------------------------------------------------------->

                engine_data = EnginePower.select_vector(power_vector)
                myTable.add_row(["Engine 1", engine_data[0]])
                myTable.add_row(["Engine 2", engine_data[1]])
                myTable.add_row(["Engine 3", engine_data[2]])
                myTable.add_row(["Engine 4", engine_data[3]])
                myTable.add_row(["Engine 5", engine_data[4]])
                myTable.add_row(["Engine 6", engine_data[5]])

                print(myTable)

                cvs_writer.writerow([Sensor.getTFminiData2(),
                                     Sensor.getTFminiData1(),
                                     Sensor.getTFminiData22(),
                                     # Gx, Gy, Gz,
                                     # Ax, Ay, Az,
                                     engine_data[0],
                                     engine_data[1],
                                     engine_data[2],
                                     engine_data[3],
                                     engine_data[4],
                                     engine_data[5]
                                     ])

                if keyboard.is_pressed("q"):  # returns True if "q" is pressed
                    EnginePower.stop_all_functions()

            else:

                print("Lidar Verisi : " + str(Sensor.getTFminiData2()))
                if Sensor.getTFminiData2() < 100:
                    print("go_down")
                    if count < 4:
                        EnginePower.rotate_right(time.time())
                        count = count + 1
                    else:
                        EnginePower.rotate_random(time.time())
                else:
                    print("----------Forward-------------")
                    EnginePower.send_data_to_engines(EnginePower.forward_vector)


if __name__ == '__main__':
    try:
        print("--------------------------------------------")
        # t1 = threading.Thread(target=Sensor.getTFminiData1)
        # t2 = threading.Thread(target=Sensor.getTFminiData2)
        t22 = threading.Thread(target=Sensor.getTFminiData22)
        # tWPS = threading.Thread(target=Sensor.WPSData)
        # # tMPU = threading.Thread(target=Sensor.MPUData)
        # tBME = threading.Thread(target=Sensor.BMEData)
        test = threading.Thread(target=main)

        # allOfData = threading.Thread(target=Sensor.getAllSensorData)

        # t1.start()
        # t2.start()
        t22.start()
        #   tWPS.start()
        # #  tMPU.start()
        #   tBME.start()

        test.start()
        # t1.join()
        # t2.join()
        t22.join()
        # test.start()
        #    tWPS.join()
        # #   tMPU.join()
        #    tBME.join()
        test.join()

    except KeyboardInterrupt:
        for proc in psutil.process_iter():

            if proc.name() == "pigpiod.py":
                proc.kill()
                sys.exit()

    except:
        print("-------------------------------------------------")
        print(">>>>>>>>>>>>>>>>>>>>>>>ERROR<<<<<<<<<<<<<<<<<<<<<")
        print("-------------------------------------------------")