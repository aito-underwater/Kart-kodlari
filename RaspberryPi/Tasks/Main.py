import csv
import os
import sys
import threading
import time  # Module needed to add delays in the code
import warnings
from time import time

import keyboard
import numpy as np
import psutil

from prettytable import PrettyTable

import AITOSensors as Sensor
import EnginPower

my_file = open("data.csv", "a")
my_file.seek(0, os.SEEK_END)
cvs_writer = csv.writer(my_file)


def send_power_to_engines():
    pass


def main():
    # # Set USB Port for serial communication
    # ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    # ser.flush()
    # Infinite loop
    count = 0
    send_binary = ''

    timer = time.time()
    task = None
    target = None
    while True:
        if task is not None:
            if target is not None:
                #  temperature, pressure, humidity = Sensor.readBME280All()
                Gx, Gy, Gz, Ax, Ay, Az = Sensor.MPUData()

                myTable = PrettyTable(["Sensor Name:", "Value"])
                myTable.add_row(["Lidar1 cm", Sensor.getTFminiData2()])
                # myTable.add_row(["Lidar2 cm", Sensor.getTFminiData1()])
                # myTable.add_row(["Lidar3 cm", Sensor.getTFminiData22()])
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




                # !!!  send_float parametresi kesinlikle değişecek !!!
                # Burası Yapay zeakanın çalışacağı yer aman dikkat edelim
                send_float = np.array(EnginPower.geEnginePower())

                # !!! Yapay zeka kodu burası !!!
                # EnginPower.calculate_engines_power()


                myTable.add_row(["Engine 1", send_float[0]])
                myTable.add_row(["Engine 2", send_float[1]])
                myTable.add_row(["Engine 3", send_float[2]])
                myTable.add_row(["Engine 4", send_float[3]])
                myTable.add_row(["Engine 5", send_float[4]])
                myTable.add_row(["Engine 6", send_float[5]])

                print(myTable)

                EnginPower.send_data_to_engines(send_float)



                cvs_writer.writerow([Sensor.getTFminiData2(),
                                     Sensor.getTFminiData1(),
                                     Sensor.getTFminiData22(),
                                     Gx, Gy, Gz,
                                     Ax, Ay, Az,
                                     send_float[0],
                                     send_float[1],
                                     send_float[2],
                                     send_float[3],
                                     send_float[4],
                                     send_float[5]
                                     ])

                if keyboard.is_pressed("q"):  # returns True if "q" is pressed
                    EnginPower.stop_all_functions()

                    warnings.warn(
                        '!!!WARNINGGG!!! You are changing current task. !!!WARNINGGG!!!',
                        stacklevel=2)
                    task = None
            else:

                if Sensor.getTFminiData2() < 100:
                    if count < 4:
                        EnginPower.rotate_right(time())
                        count = count + 1
                    else:
                        EnginPower.rotate_random(time())
                else:
                    EnginPower.go_forward()
        else:

            print("Please select task")
            print("1. Pass Through Circle.")
            print("2. Sit On Circle.")
            print("3. Hit Pinger.")
            arg = int(input())
            EnginPower.change_task(arg)


if __name__ == '__main__':
    try:
        t1 = threading.Thread(target=Sensor.getTFminiData1)
        t2 = threading.Thread(target=Sensor.getTFminiData2)
        t22 = threading.Thread(target=Sensor.getTFminiData22)
        tWPS = threading.Thread(target=Sensor.WPSData)
        tMPU = threading.Thread(target=Sensor.MPUData)
        tBME = threading.Thread(target=Sensor.BMEData)
        test = threading.Thread(target=main)

        # allOfData = threading.Thread(target=Sensor.getAllSensorData)

        t1.start()
        t2.start()
        t22.start()
        tWPS.start()
        tMPU.start()
        tBME.start()
        test.start()
        t1.join()
        t2.join()
        t22.join()
        test.start()
        tWPS.join()
        tMPU.join()
        tBME.join()
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
