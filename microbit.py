
from microbit import *

# Define the pins for the motor driver
motor_pin1 = pin0
motor_pin2 = pin1
motor_pin3 = pin2
motor_pin4 = pin3

# Define the pins for the remote control
button_forward = pin8
button_backward = pin12
button_left = pin13
button_right = pin14

# Define the motor control functions
def move_forward():
    motor_pin1.write_digital(1)
    motor_pin2.write_digital(0)
    motor_pin3.write_digital(1)
    motor_pin4.write_digital(0)

def move_backward():
    motor_pin1.write_digital(0)
    motor_pin2.write_digital(1)
    motor_pin3.write_digital(0)
    motor_pin4.write_digital(1)

def turn_left():
    motor_pin1.write_digital(0)
    motor_pin2.write_digital(1)
    motor_pin3.write_digital(1)
    motor_pin4.write_digital(0)

def turn_right():
    motor_pin1.write_digital(1)
    motor_pin2.write_digital(0)
    motor_pin3.write_digital(0)
    motor_pin4.write_digital(1)

def stop():
    motor_pin1.write_digital(0)
    motor_pin2.write_digital(0)
    motor_pin3.write_digital(0)
    motor_pin4.write_digital(0)

# Main loop
while True:
    if button_forward.read_digital() == 1:
        move_forward()
    elif button_backward.read_digital() == 1:
        move_backward()
    elif button_left.read_digital() == 1:
        turn_left()
    elif button_right.read_digital() == 1:
        turn_right()
    else:
        stop()
