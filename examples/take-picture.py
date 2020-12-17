import ffmpeg
import cv2
from djitellopy import Tello
import imutils
import time


tello = Tello()
tello.connect()

tello.streamon()

time.sleep(1 / 60)

frame_read = tello.get_frame_read()

tello.takeoff()

while True:
    frame = frame_read.frame

    frame = imutils.resize(frame, width=400)
    H, W, _ = frame.shape

    cv2.imwrite("picture.png", frame)
    # cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.imshow("Face Tracking", frame)    

    key = cv2.waitKey(5) & 0xff
    if key == ord('q'): # ESC
        tello.streamoff()
        break
    elif key == ord('i'):
        tello.move_forward(30)
    elif key == ord('k'):
        tello.move_back(30)
    elif key == ord('j'):
        tello.move_left(30)
    elif key == ord('l'):
        tello.move_right(30)
    elif key == ord('d'):
        tello.rotate_clockwise(90)
    elif key == ord('a'):
        tello.rotate_counter_clockwise(90)
    elif key == ord('w'):
        tello.move_up(30)
    elif key == ord('s'):
        tello.move_down(30)
    # elif key == ord('o'):
    #     tello.takeoff
    # elif key == ord('p'):
    #     tello.land
 
frame.release()
cv2.destroyAllWindows()



