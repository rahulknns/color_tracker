import cv2 as cv
import numpy as np
import color_tracker.track as track

tracker = track.Tracker(np.array([110,100,100]),np.array([130,255,255]),zp = 1343.1818181818182)
camera = cv.VideoCapture(0)
try:
    while True:
        _,frame = camera.read()
        frame = cv.flip(frame,1)
        x,y,z = tracker.getColourPosition(frame,z = 25)
        print(x,y,z)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    camera.release()
    cv.destroyAllWindows()