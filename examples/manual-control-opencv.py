# simple example demonstrating how to control a Tello using your keyboard.
# For a more fully featured example see manual-control-pygame.py
# 
# Use W, A, S, D for moving, E, Q for rotating and R, F for going up and down.
# When starting the script the Tello will takeoff, pressing ESC makes it land
#  and the script exit.

from djitellopy import Tello
import cv2, math, time

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()

while True:
    # In reality you want to display frames in a seperate thread. Otherwise
    #  they will freeze while the drone moves.
    img = frame_read.frame
    cv2.imshow("drone", img)

    key = cv2.waitKey(5) & 0xff
    if key == ord(msvcrt.getch()) == 27: # ESC
        break
    elif key == 38:
        tello.move_forward(30)
    elif key == 40:
        tello.move_back(30)
    elif key == 37:
        tello.move_left(30)
    elif key == 39:
        tello.move_right(30)
    elif key == ord('d'):
        tello.rotate_clockwise(90)
    elif key == ord('a'):
        tello.rotate_counter_clockwise(90)
    elif key == ord('w'):
        tello.move_up(30)
    elif key == ord('s'):
        tello.move_down(30)

tello.land()