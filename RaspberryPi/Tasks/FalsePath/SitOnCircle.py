import time

import RaspberryPi.Tasks.EnginePower as EnginePower
import numpy as np
timer = 0
while True:
    timer = time.time()

    if timer < 10:
        EnginePower.send_data_to_engines(EnginePower.turn_right_vector)
    elif timer > 20:
        EnginePower.send_data_to_engines(EnginePower.forward_vector)
    elif timer > 30:
        EnginePower.send_data_to_engines(EnginePower.down_vector)
    elif timer > 40:
        EnginePower.send_data_to_engines(EnginePower.stop_vector)
