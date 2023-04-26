import time

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import ImageDataGenerator

######## Veri ön hazılık (Basit)#######
train_datagen = ImageDataGenerator(rescale=1 / 255, horizontal_flip=True, rotation_range=75)
test_datagen = ImageDataGenerator(rescale=1 / 255)
batch_size = 8
train_generator = train_datagen.flow_from_directory(
    'pinger/train',
    target_size=(1280, 720),
    batch_size=batch_size,
    classes=['pinger', 'other'],
    class_mode='categorical')

test_generator = test_datagen.flow_from_directory(
    'pinger/test',
    target_size=(1280, 720),
    batch_size=batch_size,
    classes=['pinger', 'other', ],
    class_mode='categorical')

import tensorflow as tf

##3 CNN sıralı model oluşturma(ekstra RNN, LSTM, R-CNN
model = tf.keras.models.Sequential([
    # input layer
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(1280, 720, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),  ## gausslama mantığı
    # hidden layer 1
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),

    # hidden layer 2
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),

    # hidden layer 3
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Flatten(),  ## matematiksel olarak model eğitim bilgilerini dizi haline çevirme

    # Multiconnectir full Connector

    tf.keras.layers.Dense(256, activation='relu'),

    # Output Layer
    tf.keras.layers.Dense(2, activation='relu')
    # 2 den daha fazla sınıflarda  relu yerine softmax aktivasyon fonksiyonu tercih edilir

])

model.summary()

# Model Optimizasyonu
from tensorflow.keras.optimizers import RMSprop

opt = tf.keras.optimizers.RMSprop(lr=0.001)  # Adam(learning_rate=0.001)

model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['acc'])  # accuracy

epoch = 75
tarihce = model.fit(
    train_generator,
    epochs=epoch,
    steps_per_epoch=25,
    shuffle=True,
    validation_data=test_generator,
    validation_steps=10,
    verbose=1)

model.save('model_pinger_75_25.h5')
# kamerayı dene bitti eğitimler sana atmıştım fotoları denemek için dün