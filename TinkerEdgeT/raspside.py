import serial
import time
import struct

ser = serial.Serial('/dev/ttyS0', 115200, timeout=None)  # replace ttyAMA0 with the appropriate serial port

while True:
    #ser.flush()
    response = ser.read(8)
    # data_left = ser.inWaiting()  # Get the number of characters ready to be read
    # response += ser.read(data_left)
    # print(response)
    # time.sleep(1)
    data = []

    if len(response) >= 8:

        perm_data = struct.unpack('!ii', response[0:8])
        data.append(perm_data[0])
        data.append(perm_data[1])
        print("aaa")
        print(data)
        ser.reset_input_buffer()
        ser.reset_output_buffer()


