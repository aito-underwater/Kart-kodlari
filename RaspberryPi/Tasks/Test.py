import EnginPower


while True:
    a = input("1. Forward_vector \n"
              "1. Forward_vector \n"
              "1. Forward_vector \n"
              "1. Forward_vector \n"
              "1. Forward_vector \n"
              "1. Forward_vector \n")
    if a == 1:
        EnginPower.send_data_to_engines(EnginPower.forward_vector)
    if a == 2:
        EnginPower.send_data_to_engines(EnginPower.right_vector)
    if a == 3:
        EnginPower.send_data_to_engines(EnginPower.turn_right_vector)
    if a == 4:
        EnginPower.send_data_to_engines(EnginPower.down_vector)
    if a == 5:
        EnginPower.send_data_to_engines(EnginPower.stop_vector)
