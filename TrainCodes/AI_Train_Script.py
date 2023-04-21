import numpy as np
import pandas as pd
import sys
from RaspberryPi.Tasks.Algorithms.NeuralNetwork import AITONeuralNetwork as nn


input_layer_size = 2
secret_layer_size = 4
secret_layer_count = 16
generation_count = 20


df = pd.read_csv('Datas/mustafa_test2.csv')


print()
x = np.array(df.iloc[:,0:2])

y = np.array(df.iloc[:,2:6])

# df = np.array(pd.DataFrame(df, columns = ["X","Y","forward","right","rotate","down"]))

# y = [] # test Data


# k = 0
# for i in df:
#     y.append([])
#     for j in range(len(i)):
#         y[k].append(round(random.uniform(-10.0, 10.0),5))
#     k = k +1


test_nn = nn(input_layer_size, secret_layer_size, secret_layer_count,
             generation_count)
test_nn.set_up()


test_nn.fit(input_x=x,
            output_y=y, iteration=1, genetic_iteration=1)

test_nn.save_model('Models/SitOnCircle_mustafa_16_1.dat')



test_nn.fit(input_x=x,
            output_y=y, iteration=10, genetic_iteration=1)

test_nn.save_model('Models/SitOnCircle_mustafa_16_2.dat')



test_nn.fit(input_x=x,
            output_y=y, iteration=100, genetic_iteration=1)

test_nn.save_model('Models/SitOnCircle_mustafa_16_2.dat')



test_nn.fit(input_x=x,
            output_y=y, iteration=1000, genetic_iteration=1)

test_nn.save_model('Models/SitOnCircle_mustafa_16_3.dat')



test_nn.fit(input_x=x,
            output_y=y, iteration=10000, genetic_iteration=1)

test_nn.save_model('Models/SitOnCircle_mustafa_16_4.dat')



test_nn.fit(input_x=x,
            output_y=y, iteration=1, genetic_iteration=10)

test_nn.save_model('Models/SitOnCircle_mustafa_16_5.dat')



test_nn.fit(input_x=x,
            output_y=y, iteration=10, genetic_iteration=10)

test_nn.save_model('Models/SitOnCircle_mustafa_16_6.dat')



test_nn.fit(input_x=x,
            output_y=y, iteration=100, genetic_iteration=10)

test_nn.save_model('Models/SitOnCircle_mustafa_16_7.dat')



test_nn.fit(input_x=x,
            output_y=y, iteration=1000, genetic_iteration=10)

test_nn.save_model('Models/SitOnCircle_mustafa_16_8.dat')



test_nn.fit(input_x=x,
            output_y=y, iteration=10, genetic_iteration=100)

test_nn.save_model('Models/SitOnCircle_mustafa_16_9.dat')



test_nn.fit(input_x=x,
            output_y=y, iteration=100, genetic_iteration=100)

test_nn.save_model('Models/SitOnCircle_mustafa_16_10.dat')




# Hangi dosyada çaışıyorsak o dosyanın tolu üzerinden işlem yapmamız gerekiyor
# test_nn = test_nn.load_model("AITO1.dat")
# test_nn = test_nn.load_model()

predict = test_nn.predict(
    [
        [1635, 375],
        [975, 525],


    ])

print(predict)

