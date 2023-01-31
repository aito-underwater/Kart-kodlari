import sys
import pigpio
import psutil

sys.path.append('../../Kart-kodlari')
import Sensors.AITOSensors as sensors

import math

RX = 23
pigpio.exceptions = False
pi = pigpio.pi()
pi.set_mode(RX, pigpio.INPUT)
pi.bb_serial_read_open(RX, 115200)

class Vector3:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.Z = 0


class Device:
    def __init__(self):
        self.position = Vector3()

        self.rotation = Vector3()


class AITOMap:

    def __init__(self):
        self.transform = Device()
        self.mapW = 1250
        self.mapH = 2500
        self.map = [[[0] * self.mapW] * self.mapH]
        self.lidarRight = 0
        self.lidarLeft = 0
        self.lidarForward = 0

    def UpdateMap(self):  # Update map depend on Lidars gyro and digital compass
        pass

    def InitialMap(self):  # initial map on start time
        pass

    def GetSensorsData(self):  # Read Sensor Data
        #
        # # Getting Lidar Sensors Data
        # self.lidarRight = sensors.getRightLidarData()
        # self.lidarLeft = sensors.getLeftLidarData()
        # self.lidarForward = sensors.getFrontLidarData()
        #
        # # Getting rotation of device
        # Gx, Gy, Gz, Ax, Ay, Az = sensors.MPUData()
        # self.transform.rotation.X += Gx
        # self.transform.rotation.Y += Gy
        # self.transform.rotation.Z += Gz

        # Getting target coordinate on camera
        cameraX = 30
        cameraY = 30

    def GenerateRoute(self):
        pass

    def UpdateRoute(self):
        pass

    def CalculateCurrentPosition(self):

        if self.transform.rotation.Y > 0 and self.transform.rotation.Y < 90:
            # Calculate for Y axis
            self.transform.position.Y = math.cos(self.transform.rotation.Y) * self.lidarForward
            # Calculate for X axis
            if self.lidarLeft is not None and self.lidarRight is not None:

                if math.cos(self.transform.rotation.Y) * self.lidarLeft - math.cos(
                        self.transform.rotation.Y) * self.lidarRight < 0.01:
                    self.transform.position.X = math.cos(self.transform.rotation.Y) * self.lidarLeft

        elif (self.transform.rotation.Y > 90 and self.transform.rotation.Y < 180):
            pass
        elif (self.transform.rotation.Y > 180 and self.transform.rotation.Y < 270):
            pass
        elif (self.transform.rotation.Y > 270 and self.transform.rotation.Y < 360):
            self.transform.position.X = math.cos(self.transform.rotation.X) * self.lidarForward
            pass


mapper = AITOMap()


mapper.transform.rotation.X = 1



if __name__ == '__main__':
  try:
        t1 = threading.Thread(target=getTFminiData1)
        t2 = threading.Thread(target=getTFminiData2)
        t22 = threading.Thread(target=getTFminiData22)
        tWPS = threading.Thread(target=WPSData)
        tMPU = threading.Thread(target=MPUData)
        tBME = threading.Thread(target=BMEData)
        t1.start()
        t2.start()
        t22.start()
        tWPS.start()
        tMPU.start()
        tBME.start()
        t1.join()
        t2.join()
        t22.join()
        tWPS.join()
        tMPU.join()
        tBME.join()

  except KeyboardInterrupt:
    for proc in psutil.process_iter():

      if proc.name() == "pigpiod.py":
         proc.kill()
  except:
    pi.bb_serial_read_close(RX)
    pi.stop()


# while True:
#     mapper.GetSensorsData()
#  #   print(mapper.transform.rotation)
#
#     pass
# print("I am not gonna die")
