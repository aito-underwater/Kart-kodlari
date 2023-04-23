import cv2
import numpy as np
import tensorflow

model = tensorflow.keras.models.load_model('../Models/model_pinger.h5')

frameWidth = 256
frameHeight = 256

cap = cv2.VideoCapture(0)

while True:
    succsess, img = cap.read()
    # test_image=image.load_img(img,target_size=(256,256))
    test_image = cv2.resize(img, (frameWidth, frameHeight))
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)
    if result[0][0] == 1:
        print("pinger")
    elif result[0][1] == 1:
        print("other")
    cv2.imshow("video1", img)
    # time.sleep(1)
    if cv2.waitKey(25) & 0XFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
