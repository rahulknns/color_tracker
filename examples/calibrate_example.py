from color_tracker.calibrator import calibrate
import cv2 as cv
import numpy as np
calibrate(cv.imread('blue.png'),np.array([110,100,100]),np.array([130,255,255]))