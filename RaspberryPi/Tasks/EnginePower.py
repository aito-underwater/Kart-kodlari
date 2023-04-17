import random
import time

import numpy as np
import serial  # Module needed for serial communication

from Algorithms import NeuralNetwork as nn

input_layer_size = 2
secret_layer_size = 4
secret_layer_count = 2
generation_count = 20


model = nn.AITONeuralNetwork(input_layer_size, secret_layer_size, secret_layer_count,
                             generation_count)

#  [sağ arka motor, sol arka motor, sağ orta motor, sol orta motor, sağ ön motor, sol ön motor]
# Main movement vectors
forward_vector = [0, 0, 0, 0, -50, -57]
right_vector = [-19, -19, 0, 0, 25, -25]
turn_right_vector = [-19, 19, 0, 0, 25, -25]
down_vector = [0, 0, 20, -20, 0, 0]
up_vector = [0, 0, -30, -30, 0, 0]
stable_vector = [0, 0, 14, -14, 0, 0]
stop_vector = [0, 0, 0, 0, 0, 0]

# ////////////////////////////////////////////
all_vector = [100, 100, 100, 100, 100, 100]
all_vector2 = [10, 10, 10, 10, 10, 10]

stable_vector2 = [0, 0, 100, -100, 0, 0]
gsb_vector = [0, 0, 28, -28, -50, -60]

vector_1 = [100, 0, 0, 0, 0, 0]
vector_2 = [0, 100, 0, 0, 0, 0]
vector_3 = [0, 0, 100, 0, 0, 0]
vector_4 = [0, 0, 0, 100, 0, 0]
vector_5 = [0, 0, 0, 0, 100, 0]
vector_6 = [0, 0, 0, 0, 0, 100]
# /////////////////////////////////////////////

# Needed time to rotate vehicle
time_to_turn = 5

# Set USB Port for serial communication
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.flush()
send_binary = ''


# model = nn.AITONeuralNetwork(input_layer_size=1,secret_layer_size=1,secret_layer_count=1,generation_count=1)
# model = nn.AITONeuralNetwork.load_model()
def send_data_to_engines(powers):
    global send_binary
    if powers is None:
        return
    for data in powers:
        data = str("{:08b}".format(data, 'b'))

        if data[0] == '-':
            data = '1' + data[1:]
        else:
            pass
        send_binary += str(data)

        # Send the string. Make sure you encode it before you send it to the Arduino.
    ser.write(send_binary.encode('utf-8'))

    send_binary = ''
    # Do nothing for 500 milliseconds (0.5 seconds)
    time.sleep(0.5)

    # Receive data from the Arduino
    receive_string = ser.readline().decode('utf-8').rstrip()

    # Print the data received from Arduino to the terminal
    print("------------")
    print(powers)
    print(receive_string)


def normalize_data(data):
    array_data = np.array(data)
    normalized_data = array_data / np.sum(array_data)
    # total_data = multiplied = list(np.multiply(numbers1, numbers2))
    return normalized_data


def rotate_right(start_time):
    end_time = start_time + time_to_turn

    send_data_to_engines(turn_right_vector)
    # while int(time.time()) < end_time:
    #     send_data_to_engines(stop_vector)


def rotate_random(start_time):
    end_time = start_time + random.randint(1, time_to_turn * 2)

    send_data_to_engines(right_vector * random.choice([-1, 1]))
    # while int(time.time()) < end_time:
    #     send_data_to_engines(stop_vector)


def go_forward():
    send_data_to_engines(forward_vector)


def calculate_engines_power(input):
    # y = model.predict([162.46283326, 346.14933504, 109.24856128, 41.12214409])

    y = model.predict(input)
    return y


def stop_all_functions():
    return stop_vector


def set_task():
    global model

    # switcher = {
    #     1: "SitOnCircle1.dat",
    #     2: "SitOnCircle2.dat",
    #     3: "SitOnCircle3.dat",
    #     4: "SitOnCircle4.dat",
    #     5: "SitOnCircle5.dat",
    #     6: "SitOnCircle6.dat"
    # }

    # model.load_model(switcher.get(argument, "Invalid Task"))
    model = model.load_model('Models/SitOnCircle28.dat')
    # return switcher.get(argument, "Invalid Task")


def select_vector(power_vector):

    index = abs(list(power_vector).index(max(power_vector)))
    if power_vector[index] > 0:
        sign = 1
    else:
        sign = - 1
    if index is 0:
        print(str(sign) + " Go Forward")
        return sign * forward_vector
    if index is 1:
        print(str(sign) + " Go Right")
        return sign * right_vector
    if index is 2:
        print(str(sign) + " Turn  right")
        return sign * turn_right_vector
    if index is 3:
        print(" Go Down")
        return True
