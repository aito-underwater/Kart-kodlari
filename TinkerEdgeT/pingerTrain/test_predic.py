 import numpy as np
import tensorflow
from tensorflow.keras.preprocessing import image
model=tensorflow.keras.models.load_model('../Models/model_pinger.h5')
test_image=image.load_img('t1.png',target_size=(256,256))
test_image=np.expand_dims(test_image,axis=0)
result=model.predict(test_image)

if result[0][1]==1:
   print("other")
elif result[0][0]==1:
    print("pinger")
