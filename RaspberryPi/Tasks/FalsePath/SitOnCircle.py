import sys

# setting path
sys.path.append('../Tasks')

import time

from Tasks.EnginePower import EnginePower

timer = 0

permTimer = time.time()

i = 10
while True:
    timer = time.time()

    if timer < permTimer + i * 1:
        EnginePower.send_data_to_engines(EnginePower.turn_right_vector)
    elif timer < permTimer + i * 2:
        EnginePower.send_data_to_engines(EnginePower.forward_vector)
    elif timer < permTimer + i * 3:
        EnginePower.send_data_to_engines(EnginePower.down_vector)
    elif timer < permTimer + i * 4:
        EnginePower.send_data_to_engines(EnginePower.stop_vector)
