import time

import EnginePower

timer = 0

permTimer = int(time.time())

i = 8
while True:
    timer = int(time.time())
    if timer < (permTimer + i * 6):
        EnginePower.send_data_to_engines(EnginePower.stop_vector)
    elif timer < (permTimer + i * 7):
        EnginePower.send_data_to_engines(EnginePower.turn_right_vector)
    elif timer < (permTimer + i * 8):
        EnginePower.send_data_to_engines(EnginePower.forward_vector)
    elif timer < (permTimer + i * 10):
        EnginePower.send_data_to_engines(EnginePower.down_vector)
    elif timer < (permTimer + i * 11):
        EnginePower.send_data_to_engines(EnginePower.stop_vector)
