import cv2

import numpy as np
from sklearn import preprocessing
import csv

def NormalizeData(data):
    sumOfData = sum(data)
    returnArr = []
    for i in data:
        returnArr.append(i/sumOfData)
    return returnArr

def select_vector():
    forward_vector = [0, 0, 100, 100, 100, 100]
    right_vector = [0, 0, 100, -100, -100, 100]
    turn_right_vector = [0, 0, 100, -100, 100, -100]
    down_vector = [100, 100, 0, 0, 0, 0]
    stop_vector = [0, 0, 0, 0, 0, 0]
    all_vector = [100, 100, 100, 100, 100, 100]
    switcher = {
        1: [1, 0, 0, 0],
        2: [0, 1, 0, 0],
        3: [0, 0, 1, 0],
        4: [-1, 0, 0, 0],
        5: [0, -1, 0, 0],
        6: [0, 0, -1, 0],
        7: [0, 0, 0, 1],
        7: [0, 0, 0, -1]
    }

    selected_vector = input('1 - forward\n'
                            '2 - right\n'
                            '3 - rotate_right_vector\n'
                            '4 - backward\n'
                            '5 - left\n'
                            '6 - rotate_left_vector\n'
                            '7 - down\n'
                            '8 - up\n'
                            )

    return switcher.get(int(selected_vector), "Invalid value")


def save_data(x, y):
    with open('Datas/HitToTinger_mustafa.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        vectors = select_vector()
        formater = [x, y, vectors[0], vectors[1], vectors[2], vectors[3]]
        spamwriter.writerow(formater)


frame = cv2.imread('pingerTrain/pinger/train/pinger/(183).png')

# model=tensorflow.keras.models.load_model('Models/model_pinger_50_5.h5')
# ------------------------ Pinger tanıma -----------------------------------
#
# test_image = cv2.resize(frame, (720,1280))
# test_image = np.expand_dims(test_image, axis=0)
# result = model.predict(test_image)
# print(result[0][0])
# # ------------------------ Pinger tanıma -------------------------------------


hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# [22, 60, 200]
yellow_lower = np.array([22, 60, 0])  # Hue value of 30 corresponds to 1A9400 color
yellow_upper = np.array([70, 255, 255])

yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

kernal = np.ones((5, 5), "uint8")

yellow_mask = cv2.dilate(yellow_mask, kernal)
res_yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
centerCorr = [[], [],[]]
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if (area > 100):
        x, y, w, h = cv2.boundingRect(contour)
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (40, 100, 120), 2)

        center = ((x + w) // 2, (y + h) // 2)
        centerHeight = h

        # if result[0][0] > result[0][1] :1
        centerCorr[0].append(x)
        centerCorr[1].append(y)
        centerCorr[2].append(area)
        # cv2.putText(frame, "Yellow Colour" + str(center), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1,
        #             (40, 100, 120),
        #             2)
# center = [[1,5],[1,5]]
# center[1][:]
centerCorr[2] = NormalizeData(centerCorr[2])

totalCoor = [0,0]
for i in range(len(centerCorr[0])):

    totalCoor[0] += (centerCorr[0][i] * centerCorr[2][i])
    totalCoor[1] += (centerCorr[1][i] * centerCorr[2][i])

if len(contours) > 1:
    print(len(contours))
    print(totalCoor[0],totalCoor[1])
    # su=[sum(i) for i in square]

    cv2.imshow("Yellow Detection in Real- Time", frame)
    cv2.waitKey(5000)

    save_data(int(totalCoor[0]),int(totalCoor[1]))

if cv2.waitKey(10) & 0xFF == ord('q'):
    cap.relase()
    cv2.destroyAllWindows()

# ------------------------- Sarı tanıma ------------------------------------
