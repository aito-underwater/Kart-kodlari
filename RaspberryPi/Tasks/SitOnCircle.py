
import csv
import os
import struct
import sys
import threading
import time

# import keyboard
import numpy as np
import psutil
import serial
from prettytable import PrettyTable

import EnginePower

sys.path.insert(0, '../../')

my_file = open("data.csv", "a")
my_file.seek(0, os.SEEK_END)
cvs_writer = csv.writer(my_file)

timer = time.time() + 6
while time.time() < timer:
    EnginePower.send_data_to_engines([20, 20, 20, 20, 20, 20])

timer = time.time() + 6
while time.time() < timer:
    EnginePower.send_data_to_engines([0, 0, 0, 0, 0, 0])


def main():
    count = 0
    go_down = False
    ser = serial.Serial('/dev/ttyS0', 115200, timeout=0)  # replace ttyAMA0 with the appropriate serial port


    EnginePower.set_task('Models/sitCircle/SitOnCircle_mustafa_10_5.dat')
    timer = time.time()
    data = []
    flag = True
    while True:

        response = ser.read(8)
        ser.flushInput()
        time.sleep(1)
        if len(response) >= 8:
            perm_data = struct.unpack('!ii', response[0:8])
            data.append(perm_data[0])
            data.append(perm_data[1])
        print(go_down)
        if go_down is True:

            # while timer > time.time():
            #     EnginePower.send_data_to_engines(EnginePower.forward_vector)
            #
            # timer = time.time() + 5
            # while timer > time.time() :
            #     EnginePower.send_data_to_engines(np.multiply(EnginePower.down_vector, EnginePower.right_vector))
            # timer = time.time() + 10
            # while timer > time.time() :
            EnginePower.send_data_to_engines(EnginePower.down_vector)
        else:

            if len(data) != 0:
                #  temperature, pressure, humidity = Sensor.readBME280All()
                # Gx, Gy, Gz, Ax, Ay, Az = Sensor.MPUData()

                myTable = PrettyTable(["Sensor Name:", "Value"])
                # myTable.add_row(["Lidar1 cm", Sensor.getTFminiData2()])
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

                next_move = EnginePower.select_vector_for_sit(power_vector)
                if next_move is True:
                    go_down = True
                    timer = time.time() + 7

                else:
                    EnginePower.send_data_to_engines(next_move)
                # <-------------------------------------------------------->

                # engine_data = EnginePower.select_vector(next_move)
                # if engine_data is not None:
                #     myTable.add_row(["Engine 1", engine_data[0]])
                #     myTable.add_row(["Engine 2", engine_data[1]])
                #     myTable.add_row(["Engine 3", engine_data[2]])
                #     myTable.add_row(["Engine 4", engine_data[3]])
                #     myTable.add_row(["Engine 5", engine_data[4]])
                #     myTable.add_row(["Engine 6", engine_data[5]])
                #
                #     print(myTable)
                #
                #     cvs_writer.writerow([
                #                          # Sensor.getTFminiData2(),
                #                          # Sensor.getTFminiData1(),
                #                          # Sensor.getTFminiData22(),
                #                          # Gx, Gy, Gz,
                #                          # Ax, Ay, Az,
                #                          engine_data[0],
                #                          engine_data[1],
                #                          engine_data[2],
                #                          engine_data[3],
                #                          engine_data[4],
                #                          engine_data[5]
                #                          ])
                print(myTable)
                # if keyboard.is_pressed("q"):  # returns True if "q" is pressed
                #     EnginePower.stop_all_functions()

            else:

                # print("Lidar Verisi : " + str(Sensor.getTFminiData2()))

                # if Sensor.getTFminiData2() < 100:
                if False:
                    if count < 4:
                        EnginePower.rotate_right(time.time())
                        count = count + 1
                    else:
                        EnginePower.rotate_random(time.time())
                else:
                    print("----------Forward-------------")
                    EnginePower.send_data_to_engines(EnginePower.forward_vector)
        data = []

if __name__ == '__main__':
    try:
        print("--------------------------------------------")
        # t1 = threading.Thread(target=Sensor.getTFminiData1)
        # t2 = threading.Thread(target=Sensor.getTFminiData2)
        # t22 = threading.Thread(target=Sensor.getTFminiData22)
        # tWPS = threading.Thread(target=Sensor.WPSData)
        # # tMPU = threading.Thread(target=Sensor.MPUData)
        # tBME = threading.Thread(target=Sensor.BMEData)
        test = threading.Thread(target=main)

        # allOfData = threading.Thread(target=Sensor.getAllSensorData)

        # t1.start()
        # t2.start()
        # t22.start()
        #   tWPS.start()
        # #  tMPU.start()
        #   tBME.start()

        test.start()
        # t1.join()
        # t2.join()
        # t22.join()
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
