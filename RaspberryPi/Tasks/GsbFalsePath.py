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
        timer = time.time() + 15

        while time.time() < timer:
            EnginePower.send_data_to_engines(EnginePower.forward_vector)

        EnginePower.send_data_to_engines(EnginePower.stop_vector)

    if a == 2:
        timer = time.time() + 5
        while time.time() < timer:
            EnginePower.send_data_to_engines(EnginePower.right_vector)

        EnginePower.send_data_to_engines(EnginePower.stop_vector)
    if a == 3:
        timer = time.time() + 5
        while time.time() < timer:
            EnginePower.send_data_to_engines(np.negative(EnginePower.right_vector))

        EnginePower.send_data_to_engines(EnginePower.stop_vector)
    if a == 4:
        timer = time.time() + 5
        while time.time() < timer:
            EnginePower.send_data_to_engines(EnginePower.turn_right_vector)

        EnginePower.send_data_to_engines(EnginePower.stop_vector)
    if a == 5:
        timer = time.time() + 5
        while time.time() < timer:
            EnginePower.send_data_to_engines(np.negative(EnginePower.turn_right_vector))

        EnginePower.send_data_to_engines(EnginePower.stop_vector)

    if a == 6:
        timer = time.time() + 5
        while time.time() < timer:
            EnginePower.send_data_to_engines(EnginePower.down_vector)

        EnginePower.send_data_to_engines(EnginePower.stop_vector)
    if a == 7:
        EnginePower.send_data_to_engines(EnginePower.stop_vector)
    if a == 8:
        if flag:
            EnginePower.send_data_to_engines(EnginePower.all_vector)
            flag = False
        else:
            EnginePower.send_data_to_engines(EnginePower.all_vector2)
            flag = True
    if a == 9:
        EnginePower.send_data_to_engines(EnginePower.stable_vector)

    if a == 0:
        timer = time.time() + 10

        while time.time() < timer:
            EnginePower.send_data_to_engines(EnginePower.stable_vector2)

        timer = time.time() + 25
        while time.time() < timer:
            EnginePower.send_data_to_engines(EnginePower.forward_vector)

        EnginePower.send_data_to_engines(np.negative(EnginePower.stop_vector))
