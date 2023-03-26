import time

import numpy as np

import RaspberryPi.Tasks.EnginePower as EnginePower

timer = 0
permTimer = time.time()
i = 10
while True:
    timer = time.time()

    if timer < permTimer + i * 1:
        EnginePower.send_data_to_engines(EnginePower.stop_vector)

    elif timer < permTimer + i * 2:
        EnginePower.send_data_to_engines(EnginePower.forward_vector)

    elif timer < permTimer + i * 3:
        EnginePower.send_data_to_engines(np.negative(EnginePower.forward_vector))

    elif timer < permTimer + i * 4:
        EnginePower.send_data_to_engines(EnginePower.right_vector)

    elif timer < permTimer + i * 5:
        EnginePower.send_data_to_engines(np.negative(EnginePower.right_vector))

    elif timer < permTimer + i * 6:
        EnginePower.send_data_to_engines(EnginePower.turn_right_vector)

    elif timer < permTimer + i * 7:
        EnginePower.send_data_to_engines(np.negative(EnginePower.turn_right_vector))

    elif timer < permTimer + i * 8:
        EnginePower.send_data_to_engines(EnginePower.down_vector)

    elif timer < permTimer + i * 9:
        EnginePower.send_data_to_engines(EnginePower.up_vector)

    else:
        EnginePower.send_data_to_engines(EnginePower.stop_vector)
