#!/usr/bin/env python3

'''
always getting the most recent frame of a camera
================================================
Usage:
------
    freshest_camera_frame.py
Keys:
-----
    ESC   - exit
'''

# Python 2/3 compatibility
from __future__ import print_function

import struct
import threading
import time
import serial
import cv2
import numpy as np

# time.sleep(20)

print("Camera starting...")
ser = serial.Serial('/dev/ttymxc0', 115200, timeout=None)  # replace ttyS1 with the appropriate serial port
message = ''


def send_data(a, b):
    #    # package = b''
    #    ser.flush()
    # for i in cor:
    package = struct.pack('!ii', a, b)
    print(struct.unpack('!ii', package))

    # Sent string value,but if tests shows us it is wrong turn it on btye
    ser.write(package)
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    # Do nothing for 500 milliseconds (0.5 seconds)
    # time.sleep(0.5)


# also acts (partly) like a cv.VideoCapture
class FreshestFrame(threading.Thread):
    def __init__(self, capture, name='FreshestFrame'):
        self.capture = capture
        assert self.capture.isOpened()

        # this lets the read() method block until there's a new frame
        self.cond = threading.Condition()

        # this allows us to stop the thread gracefully
        self.running = False

        # keeping the newest frame around
        self.frame = None

        # passing a sequence number allows read() to NOT block
        # if the currently available one is exactly the one you ask for
        self.latestnum = 0

        # this is just for demo purposes
        self.callback = None

        super().__init__(name=name)
        self.start()

    def start(self):
        self.running = True
        super().start()

    def release(self, timeout=None):
        self.running = False
        self.join(timeout=timeout)
        self.capture.release()

    def run(self):
        counter = 0
        while self.running:
            # block for fresh frame
            (rv, img) = self.capture.read()
            assert rv
            counter += 1

            # publish the frame
            with self.cond:  # lock the condition for this operation
                self.frame = img if rv else None
                self.latestnum = counter
                self.cond.notify_all()

            if self.callback:
                self.callback(img)

    def read(self, wait=True, seqnumber=None, timeout=None):
        # with no arguments (wait=True), it always blocks for a fresh frame
        # with wait=False it returns the current frame immediately (polling)
        # with a seqnumber, it blocks until that frame is available (or no wait at all)
        # with timeout argument, may return an earlier frame;
        #   may even be (0,None) if nothing received yet

        with self.cond:
            if wait:
                if seqnumber is None:
                    seqnumber = self.latestnum + 1
                if seqnumber < 1:
                    seqnumber = 1

                rv = self.cond.wait_for(lambda: self.latestnum >= seqnumber, timeout=timeout)
                if not rv:
                    return (self.latestnum, self.frame)

            return (self.latestnum, self.frame)


def main():
    # model = tensorflow.keras.models.load_model('/Models/model_pinger.h5')

    frameWidth = 1280
    frameHeight = 720

    # open some camera
    cap = cv2.VideoCapture('rtsp://admin:123456@192.168.1.237/H264?ch=1&subtype=0')
    # cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 60)
    # wrap it
    fresh = FreshestFrame(cap)

    # a way to watch the camera unthrottled
    def callback(img):
        pass

    # main thread owns windows, does waitkey

    fresh.callback = callback

    # main loop
    # get freshest frame, but never the same one twice (cnt increases)
    # see read() for details
    cnt = 0
    while True:
        try:
            cnt = cnt + 1
            # test that this really takes NO time
            # (if it does, the camera is actually slower than this loop and we have to wait!)
            t0 = time.perf_counter()
            ret, frame = fresh.read(seqnumber=cnt)
            dt = time.perf_counter() - t0
            if dt > 0.010:  # 10 milliseconds
                print("NOTICE: read() took {dt:.3f} secs".format(dt=dt))

            # let's pretend we need some time to process this frame
            print("processing {cnt}...".format(cnt=cnt), end=" ", flush=True)

            # -------------------------- Sarı tanıma ----------------------------------

            hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            yellow_lower = np.array([22, 60, 200], np.uint8)
            yellow_upper = np.array([60, 255, 255], np.uint8)
            yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

            kernal = np.ones((5, 5), "uint8")

            yellow_mask = cv2.dilate(yellow_mask, kernal)
            res_yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

            _, contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            if len(contours) > 0:
                for pic, contour in enumerate(contours):

                    area = cv2.contourArea(contour)

                    if (area > 300):
                        x, y, w, h = cv2.boundingRect(contour)
                        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (40, 100, 120), 2)

                        center = ((x + w) // 2, (y + h) // 2)

                        send_data((x + w) // 2, (y + h) // 2)
                        print((x + w) // 2, (y + h) // 2)
                        # cv2.putText(imageFrame, "Yellow Colour" + str(center), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        #             (40, 100, 120),
                        #             2)

            # cv2.imshow("Yellow Detection in Real- Time", imageFrame)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                cap.relase()
                cv2.destroyAllWindows()
                break

            # ------------------------- Sarı tanıma ------------------------------------

            # ------------------------ Pinger tanıma -----------------------------------

            # test_image = cv2.resize(frame, (frameWidth, frameHeight))
            # test_image = np.expand_dims(test_image, axis=0)
            # result = model.predict(test_image)

            # ------------------------ Pinger tanıma -------------------------------------

            # ------------------------ Yapay zekanın çalıştığı kısım --------------------

            # if result[0][0] == 1 and (x is not None and y is not None):
            #         pass

            # ------------------------ Yapay zekanın çalıştığı kısım --------------------

            # this keeps both imshow windows updated during the wait (in particular the "realtime" one)
        except  Exception as e:
            # ser.write("<------------------Error------------------->")
            print(e)
            print("<--- Error --->")
        print("done!")

    fresh.release()


if __name__ == '__main__':
    main()
