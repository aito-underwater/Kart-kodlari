import EnginPower
import numpy as np
while True:
    a = int(input("1. Forward_vector \n"
                  "2. Right_vector \n"
                  "3. Left_vector \n"
                  "4. Turn_right_vector \n"
                  "5. Turn_left_vector \n"
                  "7. Down_vector \n"
                  "8. Stop_vector \n"
                  "9. All_vector \n"
                  "0. Stable_vector \n"
                  ))

    if a == 1:
        EnginPower.send_data_to_engines(EnginPower.forward_vector)
    if a == 2:
        EnginPower.send_data_to_engines(EnginPower.right_vector)
    if a == 3:
        EnginPower.send_data_to_engines(np.negative(EnginPower.right_vector))
    if a == 4:
        EnginPower.send_data_to_engines(EnginPower.turn_right_vector)
    if a == 5:
        EnginPower.send_data_to_engines(np.negative(EnginPower.turn_right_vector))
    if a == 6:
        EnginPower.send_data_to_engines(EnginPower.down_vector)
    if a == 7:
        EnginPower.send_data_to_engines(EnginPower.down_vector )
    if a == 8:
        EnginPower.send_data_to_engines(EnginPower.stop_vector)
    if a == 9:
        EnginPower.send_data_to_engines(EnginPower.all_vector)
    if a == 0:
        EnginPower.send_data_to_engines(EnginPower.stable_vector)
print("dasdsad")