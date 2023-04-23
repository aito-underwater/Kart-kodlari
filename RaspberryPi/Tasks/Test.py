import EnginePower
import time
import numpy as np

timer = 0
turn = 5
flag = True
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

    #    EnginePower.send_data_to_engines(EnginePower.stop_vector)



    print("dsad")
    if a == 1:
        timer = time.time() + 5

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
            EnginePower.send_data_to_engines(EnginePower.left_vector)

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
        timer = time.time() + 2

        while time.time() < timer:
            EnginePower.send_data_to_engines(EnginePower.down_vector)

        timer = time.time() + 8
        while time.time() < timer:
            EnginePower.send_data_to_engines(EnginePower.forward_vector)
        EnginePower.send_data_to_engines(np.negative(EnginePower.stop_vector))
    #
    # if a == 1:
    #     EnginePower.send_data_to_engines(EnginePower.forward_vector)
    # if a == 2:
    #     EnginePower.send_data_to_engines(EnginePower.right_vector)
    # if a == 3:
    #     EnginePower.send_data_to_engines(np.negative(EnginePower.right_vector))
    # if a == 4:
    #     EnginePower.send_data_to_engines(EnginePower.turn_right_vector)
    # if a == 5:
    #     EnginePower.send_data_to_engines(np.negative(EnginePower.turn_right_vector))
    # if a == 6:
    #     EnginePower.send_data_to_engines(EnginePower.down_vector)
    # if a == 7:
    #     EnginePower.send_data_to_engines(EnginePower.stop_vector)
    # if a == 8:
    #     EnginePower.send_data_to_engines(EnginePower.all_vector)
    # if a == 9:
    #     EnginePower.send_data_to_engines(EnginePower.stable_vector)
    # if a == 0:
    #     timer = time.time() + 5
    #     while time.time() <timer:
    #         EnginePower.send_data_to_engines(EnginePower.down_vector)
    #     EnginePower.send_data_to_engines(np.negative(EnginePower.down_vector))

    # -----------------------------------------------------------
    # if a == 1:
    #     EnginePower.send_data_to_engines(EnginePower.vector_1)
    # if a == 2:
    #     EnginePower.send_data_to_engines(EnginePower.vector_2)
    # if a == 3:
    #     EnginePower.send_data_to_engines(EnginePower.vector_3)
    # if a == 4:
    #     EnginePower.send_data_to_engines(EnginePower.vector_4)
    # if a == 5:
    #     EnginePower.send_data_to_engines(EnginePower.vector_5)
    # if a == 6:
    #     EnginePower.send_data_to_engines(EnginePower.vector_6)
    # if a == 7:
    #     EnginePower.send_data_to_engines(EnginePower.stop_vector)
    #
    # # if a == 8:
    # #     EnginePower.send_data_to_engines(2 * EnginePower.vector_1[:, 0])
    # # if a == 9:
    # #     EnginePower.send_data_to_engines(2 * EnginePower.vector_2[:, 0])
    # # if a == 10:
    # #     EnginePower.send_data_to_engines(2 * EnginePower.vector_3[:, 0])
    # # if a == 11:
    # #     EnginePower.send_data_to_engines(2 * EnginePower.vector_4[:, 0])
    # # if a == 12:
    # #     EnginePower.send_data_to_engines(2 * EnginePower.vector_5[:, 0])
    # # if a == 13:
    # #     EnginePower.send_data_to_engines(2 * EnginePower.vector_6[:, 0])
