import cv2

import numpy as np
import struct
import csv




def select_vector():

    forward_vector = [0, 0, 100, 100, 100, 100]
    right_vector = [0, 0, 100, -100, -100, 100]
    turn_right_vector = [0, 0, 100, -100, 100, -100]
    down_vector = [100, 100, 0, 0, 0, 0]
    stop_vector = [0, 0, 0, 0, 0, 0]
    all_vector = [100, 100, 100, 100, 100, 100]
    switcher = {
        1: [1,0,0,0],
        2: [0,1,0,0],
        3: [0,0,1,0],
        4: [-1,0,0,0],
        5: [0,-1,0,0],
        6: [0,0,-1,0],
        7: [0,0,0,1]
    }

    selected_vector =input( '1 - forward\n'
                            '2 - right\n'
                            '3 - rotate_right_vector\n'
                            '4 - backward\n'
                            '5 - left\n'
                            '6 - rotate_left_vector\n'
                            '7 - down\n')

    return switcher.get(int(selected_vector), "Invalid value")


def save_data(x,y):
<<<<<<< HEAD
    with open('ismail_test.csv', 'a', newline='') as csvfile:
=======
    with open('mustafa_test.csv', 'a', newline='') as csvfile:
>>>>>>> 54f583ca17d22e02358898dfe988fc5b0819a770
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        vectors = select_vector()
        formater = [x, y,vectors[0],vectors[1],vectors[2],vectors[3]]
        spamwriter.writerow(formater)


def send_data(cor):
    package = b''

    for i in cor:
        package += struct.pack('!i', i)
        print(package)

    # # Sent string value,but if tests shows us it is wrong turn it on btye
    # ser.write(package.encode('utf-8'))
    #
    # # Do nothing for 500 milliseconds (0.5 seconds)
    # time.sleep(0.5)


<<<<<<< HEAD
frame = cv2.imread('./images/(214).png')
=======
frame = cv2.imread('./images/(180).png')
>>>>>>> 54f583ca17d22e02358898dfe988fc5b0819a770
# frame = cv2.flip(frame, 1)
hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


# redx
lower_red = np.array([136, 87, 111])
upper_red = np.array([180, 255, 255])
red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
colorful_frame = frame
frame = cv2.bitwise_and(frame, frame, mask = red_mask)

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.blur(gray, (3, 3))
detected_circles = cv2.HoughCircles(gray_blurred,
                   cv2.HOUGH_GRADIENT, 10 *3, 100 * 30, param1 = 250,
               param2 = 250, minRadius = 1, maxRadius = 1000)


if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        cv2.circle(frame, (a, b), r, (0, 255, 0), 2)
        cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)

        print (a,b)


# send_data(center)
cv2.imshow("Red", colorful_frame)
cv2.waitKey(5000)
if a is not None and b is not None:
    save_data(a, b)


cv2.destroyAllWindows()

# send_data((1, 2, 404, 5))



