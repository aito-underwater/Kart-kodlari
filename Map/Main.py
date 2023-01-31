import AITOSensors as Sensor
import AITOMap as Map
import threading
import psutil


def Test():
    for i in range(10):
        print(i)
if __name__ == '__main__':
  try:
        # t1 = threading.Thread(target=Sensor.getTFminiData1)
        t1 = threading.Thread(target=Test)
        t2 = threading.Thread(target=Sensor.getTFminiData2())
        t22 = threading.Thread(target=Sensor.getTFminiData22)
        tWPS = threading.Thread(target=Sensor.WPSData)

        tMPU = threading.Thread(target=Sensor.MPUData)
        tBME = threading.Thread(target=Sensor.BMEData)
        t1.start()
        t2.start()
        t22.start()
        tWPS.start()
        tMPU.start()
        tBME.start()
        print("asdsadad2")
        t1.join()
        print("dasdsad")
        t2.join()
        print("1")
        t22.join()
        print("2")
        tWPS.join()
        print("3")
        tMPU.join()
        print("4")
        tBME.join()

  except KeyboardInterrupt:
    for proc in psutil.process_iter():

      if proc.name() == "pigpiod.py":
         proc.kill()
  except:
    print("-------------------------------------------------")
    print(">>>>>>>>>>>>>>>>>>>>>>>ERROR<<<<<<<<<<<<<<<<<<<<<")
    print("-------------------------------------------------")

print("2345")