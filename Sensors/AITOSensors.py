#!/usr/bin/env python3
## -*- coding: utf-8 -*

import threading
import time
from ctypes import c_short

import Adafruit_ADS1x15
import pigpio
import psutil
import smbus
from prettytable import PrettyTable

pigpio.exceptions = False

adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

DEVICE = 0x76  # Default device I2C address

bus = smbus.SMBus(1)

# Set up lidars Setting

rightLidarPin = 23

pi_right = pigpio.pi()
pi_right.set_mode(rightLidarPin, pigpio.INPUT)
pi_right.bb_serial_read_open(rightLidarPin, 115200)

leftLidarPin = 24

pi_left = pigpio.pi()
pi_left.set_mode(leftLidarPin, pigpio.INPUT)
pi_left.bb_serial_read_open(leftLidarPin, 115200)

forwardLidarPin = 22

pi_forward = pigpio.pi()
pi_forward.set_mode(forwardLidarPin, pigpio.INPUT)
pi_forward.bb_serial_read_open(forwardLidarPin, 115200)

PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47


# Get TFmini Data on right
def getRightLidarData():
    while True:

        time.sleep(0.1)  # change the value if needed
        (count, recv) = pi_right.bb_serial_read(rightLidarPin)

        if count > 8:
            for i in range(0, count - 9):
                if recv[i] == 89 and recv[i + 1] == 89:  # 0x59 is 89
                    checksum = 0
                    for j in range(0, 8):
                        checksum = checksum + recv[i + j]
                    checksum = checksum % 256
                    if checksum == recv[i + 8]:
                        distance = recv[i + 2] + recv[i + 3] * 256
                        strength = recv[i + 4] + recv[i + 5] * 256

                        return distance


# Get TFmini Data on left
def getLeftLidarData():
    while True:

        time.sleep(0.1)
        (count, recv) = pi_left.bb_serial_read(leftLidarPin)

        if count > 8:
            for i in range(0, count - 9):
                if recv[i] == 89 and recv[i + 1] == 89:  # 0x59 is 89
                    checksum = 0
                    for j in range(0, 8):
                        checksum = checksum + recv[i + j]
                    checksum = checksum % 256
                    if checksum == recv[i + 8]:
                        distance = recv[i + 2] + recv[i + 3] * 256
                        strength = recv[i + 4] + recv[i + 5] * 256

                        return distance


# get MegaLidar Data on front
def getFrontLidarData():
    while True:

        time.sleep(0.1)
        (count, recv) = pi_forward.bb_serial_read(forwardLidarPin)

        if count > 8:
            for i in range(0, count - 9):
                if recv[i] == 89 and recv[i + 1] == 89:
                    checksum = 0
                    for j in range(0, 8):
                        checksum = checksum + recv[i + j]
                    checksum = checksum % 256
                    if checksum == recv[i + 8]:
                        distance = recv[i + 2] + recv[i + 3] * 256
                        strength = recv[i + 4] + recv[i + 5] * 256
                        print("e32we")
                        return distance


def WPSData():
    while True:
        value = [0]
        value[0] = adc.read_adc(0, gain=1)
        volts = value[0] / 32767.0 * 6.144
        psi = 50.0 * volts - 25.0
        bar = psi * 0.0689475729
        a = bar
        return a


def MPUData():
    def MPU_Init():

        bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

        bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

        bus.write_byte_data(Device_Address, CONFIG, 0)

        bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

        bus.write_byte_data(Device_Address, INT_ENABLE, 1)

    def read_raw_data(addr):

        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr + 1)

        value = ((high << 8) | low)

        if (value > 32768):
            value = value - 65536
        return value

    bus = smbus.SMBus(1)
    Device_Address = 0x68

    MPU_Init()

    while True:
        acc_x = read_raw_data(ACCEL_XOUT_H)
        acc_y = read_raw_data(ACCEL_YOUT_H)
        acc_z = read_raw_data(ACCEL_ZOUT_H)

        gyro_x = read_raw_data(GYRO_XOUT_H)
        gyro_y = read_raw_data(GYRO_YOUT_H)
        gyro_z = read_raw_data(GYRO_ZOUT_H)

        Ax = acc_x / 16384.0
        Ay = acc_y / 16384.0
        Az = acc_z / 16384.0

        Gx = gyro_x / 131.0
        Gy = gyro_y / 131.0
        Gz = gyro_z / 131.0
        return Gx, Gy, Gz, Ax, Ay, Az,


def BMEData():
    while True:
        def getShort(data, index):

            return c_short((data[index + 1] << 8) + data[index]).value

        def getUShort(data, index):

            return (data[index + 1] << 8) + data[index]

        def getChar(data, index):

            result = data[index]
            if result > 127:
                result -= 256
            return result

        def getUChar(data, index):

            result = data[index] & 0xFF
            return result

        def readBME280ID(addr=DEVICE):

            REG_ID = 0xD0
            (chip_id, chip_version) = bus.read_i2c_block_data(addr, REG_ID, 2)
            return (chip_id, chip_version)

        def readBME280All(addr=DEVICE):

            REG_DATA = 0xF7
            REG_CONTROL = 0xF4
            REG_CONFIG = 0xF5

            REG_CONTROL_HUM = 0xF2
            REG_HUM_MSB = 0xFD
            REG_HUM_LSB = 0xFE

            OVERSAMPLE_TEMP = 2
            OVERSAMPLE_PRES = 2
            MODE = 1

            OVERSAMPLE_HUM = 2
            bus.write_byte_data(addr, REG_CONTROL_HUM, OVERSAMPLE_HUM)

            control = OVERSAMPLE_TEMP << 5 | OVERSAMPLE_PRES << 2 | MODE
            bus.write_byte_data(addr, REG_CONTROL, control)

            cal1 = bus.read_i2c_block_data(addr, 0x88, 24)
            cal2 = bus.read_i2c_block_data(addr, 0xA1, 1)
            cal3 = bus.read_i2c_block_data(addr, 0xE1, 7)

            dig_T1 = getUShort(cal1, 0)
            dig_T2 = getShort(cal1, 2)
            dig_T3 = getShort(cal1, 4)

            dig_P1 = getUShort(cal1, 6)
            dig_P2 = getShort(cal1, 8)
            dig_P3 = getShort(cal1, 10)
            dig_P4 = getShort(cal1, 12)
            dig_P5 = getShort(cal1, 14)
            dig_P6 = getShort(cal1, 16)
            dig_P7 = getShort(cal1, 18)
            dig_P8 = getShort(cal1, 20)
            dig_P9 = getShort(cal1, 22)

            dig_H1 = getUChar(cal2, 0)
            dig_H2 = getShort(cal3, 0)
            dig_H3 = getUChar(cal3, 2)

            dig_H4 = getChar(cal3, 3)
            dig_H4 = (dig_H4 << 24) >> 20
            dig_H4 = dig_H4 | (getChar(cal3, 4) & 0x0F)

            dig_H5 = getChar(cal3, 5)
            dig_H5 = (dig_H5 << 24) >> 20
            dig_H5 = dig_H5 | (getUChar(cal3, 4) >> 4 & 0x0F)

            dig_H6 = getChar(cal3, 6)

            wait_time = 1.25 + (2.3 * OVERSAMPLE_TEMP) + ((2.3 * OVERSAMPLE_PRES) + 0.575) + (
                    (2.3 * OVERSAMPLE_HUM) + 0.575)
            time.sleep(wait_time / 1000)

            data = bus.read_i2c_block_data(addr, REG_DATA, 8)
            pres_raw = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
            temp_raw = (data[3] << 12) | (data[4] << 4) | (data[5] >> 4)
            hum_raw = (data[6] << 8) | data[7]

            var1 = ((((temp_raw >> 3) - (dig_T1 << 1))) * (dig_T2)) >> 11
            var2 = (((((temp_raw >> 4) - (dig_T1)) * ((temp_raw >> 4) - (dig_T1))) >> 12) * (dig_T3)) >> 14
            t_fine = var1 + var2
            temperature = float(((t_fine * 5) + 128) >> 8);

            var1 = t_fine / 2.0 - 64000.0
            var2 = var1 * var1 * dig_P6 / 32768.0
            var2 = var2 + var1 * dig_P5 * 2.0
            var2 = var2 / 4.0 + dig_P4 * 65536.0
            var1 = (dig_P3 * var1 * var1 / 524288.0 + dig_P2 * var1) / 524288.0
            var1 = (1.0 + var1 / 32768.0) * dig_P1
            if var1 == 0:
                pressure = 0
            else:
                pressure = 1048576.0 - pres_raw
                pressure = ((pressure - var2 / 4096.0) * 6250.0) / var1
                var1 = dig_P9 * pressure * pressure / 2147483648.0
                var2 = pressure * dig_P8 / 32768.0
                pressure = pressure + (var1 + var2 + dig_P7) / 16.0

            humidity = t_fine - 76800.0
            humidity = (hum_raw - (dig_H4 * 64.0 + dig_H5 / 16384.0 * humidity)) * (dig_H2 / 65536.0 * (
                    1.0 + dig_H6 / 67108864.0 * humidity * (1.0 + dig_H3 / 67108864.0 * humidity)))
            humidity = humidity * (1.0 - dig_H1 * humidity / 524288.0)
            if humidity > 100:
                humidity = 100
            elif humidity < 0:
                humidity = 0

            return temperature / 100.0, pressure / 100.0, humidity

        def main():

            (chip_id, chip_version) = readBME280ID()

            temperature, pressure, humidity = readBME280All()
            Gx, Gy, Gz, Ax, Ay, Az = MPUData()
            MOVE_CURSOR_UP = "\033[1A"
            ERASE = "\x1b[2K"

            myTable = PrettyTable(["Sensor Name:", "Value"])
            myTable.add_row(["Lidar1 cm", getLeftLidarData()])
            myTable.add_row(["Lidar2 cm", getRightLidarData()])
            myTable.add_row(["Lidar3 cm", getFrontLidarData()])
            myTable.add_row(["Gyro Gx", Gx])
            myTable.add_row(["Gyro Gy", Gy])
            myTable.add_row(["Gyro Gz", Gz])
            myTable.add_row(["Gyro Ax", Ax])
            myTable.add_row(["Gyro Ay", Ay])
            myTable.add_row(["Gyro Az", Az])
            myTable.add_row(["Bar", WPSData()])
            myTable.add_row(["Temperature C", temperature])
            myTable.add_row(["Pressure hPa", pressure])
            myTable.add_row(["Humidity %", humidity])
            print(myTable)
        if __name__ == '__main__':
            main()




if __name__ == '__main__':
    try:
        t1 = threading.Thread(target=getRightLidarData)
        print("1")
        t2 = threading.Thread(target=getLeftLidarData)
        print("2")
        t22 = threading.Thread(target=getFrontLidarData)
        print("3")
        tWPS = threading.Thread(target=WPSData)
        print("4")
        tMPU = threading.Thread(target=MPUData)
        print("5")
        tBME = threading.Thread(target=BMEData)
        print("6")
        t1.start()
        print("7")
        t2.start()
        print("8")
        t22.start()
        print("9")
        tWPS.start()

        print("10")
        tMPU.start()
        print("11")
        tBME.start()
        print("12")
        t1.join()
        print("13")
        t2.join()
        print("14")
        t22.join4()
        print("15")
        tWPS.join()
        print("16")
        tMPU.join()
        print("17")
        tBME.join()
        print("18")


    except KeyboardInterrupt:
        for proc in psutil.process_iter():

            if proc.name() == "pigpiod.py":
                proc.kill()

    except:
        pi_right.bb_serial_read_close(rightLidarPin)
        pi_right.stop()

