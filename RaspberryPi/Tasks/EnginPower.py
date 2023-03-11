from Algorithms import NeuralNetwork as nn

input_layer_size = 4
secret_layer_size = 4
secret_layer_count = 2
generation_count = 1

model = nn.AITONeuralNetwork(input_layer_size, secret_layer_size, secret_layer_count,
                             generation_count)


# model = nn.AITONeuralNetwork(input_layer_size=1,secret_layer_size=1,secret_layer_count=1,generation_count=1)
# model = nn.AITONeuralNetwork.load_model()

def get_engines_power():
    y = model.predict([162.46283326, 346.14933504, 109.24856128, 41.12214409])


def stop_all_functions():
    return [50, 50, 50, 50, 50, 50]


def change_task(argument):
    global model
    print(model)
    switcher = {
        1: "PassThroughCircle.dat",
        2: "SitOnCircle.dat",
        3: "HitPinger.dat"
    }
    # model.load_model("SitOnCircle.dat")
    model.load_model(switcher.get(argument, "Invalid Task"))

    # return switcher.get(argument, "Invalid Task")


