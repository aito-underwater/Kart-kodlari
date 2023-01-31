import serial

ser = serial.Serial("/dev/ttyAMA0", 9600)

class TestStruct:
    def _init_(self, degree, speed, reset, dim):
        self.degree = degree
        self.speed = speed
        self.reset = reset
        self.dim = dim

test_struct = TestStruct(0, 0, 0, 10)

while True:
    incoming_data = ser.readline()
    if incoming_data:
        test_struct.degree = int(incoming_data)
    ser.write(test_struct._dict_)
    ser.flush()
    time.sleep(0.1)