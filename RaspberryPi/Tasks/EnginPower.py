import random
import time


import numpy as np
import serial  # Module needed for serial communication

from Algorithms import NeuralNetwork as nn

input_layer_size = 4
secret_layer_size = 4
secret_layer_count = 2
generation_count = 1

model = nn.AITONeuralNetwork(input_layer_size, secret_layer_size, secret_layer_count,
                             generation_count)

# Main movement vectors
forward_vector = [100, 100, 100, 100, 0, 0]
right_vector = [100, -100, -100, 100, 0, 0]
turn_right_vector = [100, -100, 100, -100, 0, 0]
down_vector = [0, 0, 0, 0, 100, 100]
stop_vector = [0, 0, 0, 0, 0, 0]
stop_vector = [100, 100, 100, 100, 100, 100]
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

    send_data_to_engines(right_vector)
    while int(time()) < end_time:
        send_data_to_engines(stop_vector)


def rotate_random(start_time):
    end_time = start_time + random.randint(1, time_to_turn * 2)

    send_data_to_engines(right_vector * choice([-1, 1]))
    while int(time()) < end_time:
        send_data_to_engines(stop_vector)


def go_forward():
    send_data_to_engines(forward_vector)


def calculate_engines_power(input):
    # y = model.predict([162.46283326, 346.14933504, 109.24856128, 41.12214409])
    y = model.predict(input)
    flag = y[len(y) - 1]
    if flag == 1:
        return True
    else:
        return y[0:len(y) - 1]


def stop_all_functions():
    return stop_vector


def change_task(argument):
    global model
    print(model)
    switcher = {
        1: "PassThroughCircle.dat",
        2: "SitOnCircle.dat",
        3: "HitPinger.dat"
    }
    # model.load_model("SitOnCircle.dat")
    model.load_model(switcher.get(argument, "Invalid Task"))

    # return switcher.get(argument, "Invalid Task")
