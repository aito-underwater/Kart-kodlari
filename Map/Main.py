import sys
import threading

import psutil
from prettytable import PrettyTable

import AITOSensors as Sensor


def main():
    while True:
        temperature, pressure, humidity = Sensor.readBME280All()
        Gx, Gy, Gz, Ax, Ay, Az = Sensor.MPUData()

        myTable = PrettyTable(["Sensor Name:", "Value"])
        myTable.add_row(["Lidar1 cm", Sensor.getTFminiData2()])
        myTable.add_row(["Lidar2 cm", Sensor.getTFminiData1()])
        myTable.add_row(["Lidar3 cm", Sensor.getTFminiData22()])
        myTable.add_row(["Gyro Gx", Gx])
        myTable.add_row(["Gyro Gy", Gy])
        myTable.add_row(["Gyro Gz", Gz])
        myTable.add_row(["Gyro Ax", Ax])
        myTable.add_row(["Gyro Ay", Ay])
        myTable.add_row(["Gyro Az", Az])
        myTable.add_row(["Bar", Sensor.WPSData()])
        myTable.add_row(["Temperature C", temperature])
        myTable.add_row(["Pressure hPa", pressure])
        myTable.add_row(["Humidity %", humidity])
        print(myTable)


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


