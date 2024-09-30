# -*- coding: utf-8 -*-

import time
from pinpong.board import *
from pinpong.extension.unihiker import *
import serial

arduino = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust this to your correct port
# arduino = serial.Serial('/dev/ttyACM0', 9600)  # Adjust this to your correct port
time.sleep(1)  # Give time for the connection to establish

Board().begin()  # Initialize the UNIHIKER



# Adjust these values based on your testing
FORWARD_THRESHOLD = 0.5
BACKWARD_THRESHOLD = -0.5
TURN_THRESHOLD = 0.2

def move_forward():
    print("Moving backwartd")
    arduino.write(b'B\n')  # Sending 'STOP' command to Arduino


def move_backward():
    print("Moving forward")
    arduino.write(b'F\n')  # Sending 'STOP' command to Arduino


def turn_left():
    print("Turning Left")
    arduino.write(b'L\n')  # Sending 'STOP' command to Arduino


def turn_right():
    print("Turning Right")
    arduino.write(b'R\n')  # Sending 'STOP' command to Arduino


def stop():
    print("Stopping")
    arduino.write(b'S\n')  # Sending 'STOP' command to Arduino


while True:
    x_acc = accelerometer.get_x()
    y_acc = accelerometer.get_y()
    z_acc = accelerometer.get_z()
    strength = accelerometer.get_strength()
    
    x_gyro = gyroscope.get_x()
    y_gyro = gyroscope.get_y()  # Using Y-axis for turning

    # Print the raw sensor values for debugging
    print(f"Acc: X={x_acc:.2f}, Y={y_acc:.2f}, Z={z_acc:.2f}, Strength={strength:.2f}")
    print(f"Gyro: X={x_gyro:.2f}, Y={y_gyro:.2f}")
    
    # Control logic based on accelerometer values
    if x_acc > FORWARD_THRESHOLD:
        move_forward()
    elif x_acc < BACKWARD_THRESHOLD:
        move_backward()
    else:
        stop()
    
    # Control logic based on gyroscope values for turning
    if y_gyro > TURN_THRESHOLD:  # Right turn
        turn_right()
    elif y_gyro < -TURN_THRESHOLD:  # Left turn
        turn_left()
    
    print("------------------")
    time.sleep(1)
