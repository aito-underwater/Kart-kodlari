import serial  # Module needed for serial communication
import time  # Module needed to add delays in the code

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

ser.flush()

# Infinite loop
while (1):
    send_float = [1.2,2.2,3.3,4.4,5.5,6.6]

   # Send the string. Make sure you encode it before you send it to the Arduino.
    ser.write(send_float)

    # Do nothing for 500 milliseconds (0.5 seconds)
    time.sleep(0.5)

    # Receive data from the Arduino
    receive_string = ser.readline().decode('utf-8').rstrip()

    # Print the data received from Arduino to the terminal
    print(receive_string)
