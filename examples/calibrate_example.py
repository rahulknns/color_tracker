from color_tracker.calibrator import calibrate
import cv2 as cv
import numpy as np
print(calibrate(cv.imread('blue.jpg'),np.array([110,100,100]),np.array([130,255,255]),a=5.5,z=25))