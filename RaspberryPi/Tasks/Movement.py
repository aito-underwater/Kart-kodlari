import time

import numpy as np

import EnginePower

timer = 0
permTimer = time.time()
i = 3
while True:
    timer = time.time()

    if timer < permTimer + i * 1:
        EnginePower.send_data_to_engines(EnginePower.stop_vector)

    elif timer < permTimer + i * 2:
        EnginePower.send_data_to_engines(EnginePower.stable_vector)

    elif timer < permTimer + i * 4:
        EnginePower.send_data_to_engines(np.add(EnginePower.stable_vector, EnginePower.forward_vector))

    elif timer < permTimer + i * 6:
        EnginePower.send_data_to_engines(np.add(EnginePower.turn_right_vector, EnginePower.stable_vector))

    elif timer < permTimer + i * 7:
        EnginePower.send_data_to_engines(np.add(EnginePower.stable_vector + EnginePower.forward_vector))

    elif timer < permTimer + i * 10:
        EnginePower.send_data_to_engines(EnginePower.stop_vector)
