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
        # Getting Lidar Sensors Data
        self.lidarRight = 1
        self.lidarLeft = 1
        self.lidarForward = 1
        # Getting rotation of device
        self.transform.rotationX = 90
        self.transform.rotationY = 90
        self.transform.rotationZ = 0
        # Getting target coordinate on camera
        cameraX = 30
        cameraY = 30

    def GenerateRoute(self):
        pass

    def UpdateRoute(self):
        pass

    def CalculateCurrentPosition(self):

        # self.map[self.mapW]

        if (self.transform.rotationY > 0 and self.transform.rotationY < 90):
            # Calculate for Y axis
            self.transform.position.Y = math.cos(self.transform.rotation.Y) * self.lidarForward
            # Calculate for X axis
            if self.lidarLeft is not None and self.lidarRight is not None:

                if math.cos(self.transform.rotation.Y) * self.lidarLeft - math.cos(
                        self.transform.rotation.Y) * self.lidarRight < 0.01:
                    self.transform.position.X = math.cos(self.transform.rotation.Y) * self.lidarLeft


        elif (self.transform.rotationY > 90 and self.transform.rotationY < 180):
            pass
        elif (self.transform.rotationY > 180 and self.transform.rotationY < 270):
            pass
        elif (self.transform.rotationY > 270 and self.transform.rotationY < 360):
            self.transform.transform.position.X = math.cos(self.transform.rotation.X) * self.lidarForward

            pass


mapper1 = AITOMap()

mapper2 = AITOMap()

mapper1.transform.rotation.X = 1
mapper2.transform.rotation.X = 2

while True:
    # print(mapper1.transform.rotation.X)
    # print(mapper2.transform.rotation.X)

    pass
print("I am not gonna die")
