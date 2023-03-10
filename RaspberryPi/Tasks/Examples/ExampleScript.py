import random

from RaspberryPi.Tasks.Algorithms.NeuralNetwork import AITONeuralNetwork as nn
import pandas as pd
import numpy as np

input_layer_size = 4
secret_layer_size = 4
secret_layer_count = 2
generation_count = 1


df = pd.read_csv('../Datas/ExampleData.csv', index_col=0)

df = np.array(pd.DataFrame(df, columns = ["volt","rotate","pressure","vibration"]))


y = [] # test Data
k = 0
for i in df:
    y.append([])
    for j in range(len(i)):
        y[k].append(round(random.uniform(-10.0, 10.0),5))
    k = k +1


test_nn = nn(input_layer_size, secret_layer_size, secret_layer_count,
                                generation_count)
test_nn.set_up()
print((df[2]))
print((y[2]))
test_nn.fit(input_x=df,
             output_y=y, iteration=2, genetic_iteration=10)

y = test_nn.predict([162.46283326, 346.14933504, 109.24856128,  41.12214409])


print(y)