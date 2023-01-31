import sys

sys.path.append('../../Kart-kodlari')

import math


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



# while True:
#     mapper.GetSensorsData()
#  #   print(mapper.transform.rotation)


print("I am not gonna die")
