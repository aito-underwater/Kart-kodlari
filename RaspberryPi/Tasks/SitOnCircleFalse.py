import time
import numpy as np
import EnginePower

timer = 0

permTimer = int(time.time())

i = 8
# while True:
#     timer = int(time.time())
#     if timer < (permTimer + i * 1):
#         EnginePower.send_data_to_engines(EnginePower.stop_vector)
#     elif timer < (permTimer + (i * 2) / 3):
#         EnginePower.send_data_to_engines(EnginePower.turn_right_vector)
#     elif timer < (permTimer + i * 3):
#         EnginePower.send_data_to_engines(EnginePower.forward_vector)
#     elif timer < (permTimer + i * 8):
#         EnginePower.send_data_to_engines(EnginePower.down_vector)
#     elif timer < (permTimer + i * 9):
#         EnginePower.send_data_to_engines(EnginePower.stop_vector)

while True:
    timer = int(time.time())
    if timer < (permTimer + i * 1):
        EnginePower.send_data_to_engines(EnginePower.stop_vector)
    elif timer < (permTimer + i * 3):
        EnginePower.send_data_to_engines(np.add(EnginePower.forward_vector, EnginePower.stable_vector))
    elif timer < (permTimer + i * 5):
        EnginePower.send_data_to_engines(EnginePower.down_vector)
    elif timer < (permTimer + i * 7):
        EnginePower.send_data_to_engines(EnginePower.stop_vector)
