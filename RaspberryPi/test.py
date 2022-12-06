#!/usr/bin/env python3
import time  # Module needed to add delays in the code

import serial  # Module needed for serial communication

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1.0)


ser.flush()

# Infinite loop
import random

import numpy as np

a = 0
count = 0
send_binary = ''
while (1):

    send_float = np.array(
        [random.randint(-100, 100),
         random.randint(-100, 100),
         random.randint(-100, 100),
         random.randint(-100, 100),
         random.randint(-100, 100),
         random.randint(-100, 100)])

    for data in send_float:
        data = str("{:08b}".format(data, 'b'))

        if data[0] == '-':
            data = '1' + data[1:]
            print(data[0])
        else:
            pass


        send_binary += str(data)

    # Send the string. Make sure you encode it before you send it to the Arduino.
    ser.write(send_binary.encode('utf-8'))

    send_binary = ''
    # Do nothing for 500 milliseconds (0.5 seconds)
    time.sleep(0.2)

    # Receive data from the Arduino
    receive_string = ser.readline().decode('utf-8').rstrip()

    # Print the data received from Arduino to the terminal
    print("------------")
    print(send_float)
    count = count + 1
    print(receive_string)
    print("----" + str(count) + "----")
