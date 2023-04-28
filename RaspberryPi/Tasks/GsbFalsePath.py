import time

import numpy as np

import EnginePower

timer = 0
turn = 5
flag = True

timer = time.time() + 5

while time.time() < timer:
    EnginePower.send_data_to_engines([0,0,0,0,0,0])

EnginePower.send_data_to_engines(EnginePower.stop_vector)

turntimer = time.time() + EnginePower.time_to_turn
while True:
    a = int(input("1. Forward_vector \n"
                  "2. Right_vector \n"
                  "3. Left_vector \n"
                  "4. Turn_right_vector \n"
                  "5. Turn_left_vector \n"
                  "6. Down_vector \n"
                  "7. Stop_vector \n"
                  "8. All_vector \n"
                  "9. Stable_vector \n"
                  ))

    if a == 1:
        while True:
            timer = time.time() + 20

            while time.time() < timer:
                EnginePower.send_data_to_engines(EnginePower.forward_vector)

            timer = time.time() + 6

            while time.time() < timer:
                EnginePower.send_data_to_engines(EnginePower.turn_right_vector)

            timer = time.time() + 20

            while time.time() < timer:
                EnginePower.send_data_to_engines(EnginePower.forward_vector)

            timer = time.time() + 6

            while time.time() < timer:
                EnginePower.send_data_to_engines(EnginePower.turn_right_vector)

            timer = time.time() + 4

            while time.time() < timer:
                EnginePower.send_data_to_engines(EnginePower.forward_vector)




