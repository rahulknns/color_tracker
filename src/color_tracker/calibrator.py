import cv2 as cv
import numpy as np

def calibrate(img,color_lower,color_higher, z = 1,a = 1):
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    threshold_image = cv.inRange(hsv,color_lower,color_higher)
    cv.imshow('threshold_image',threshold_image)
    co_ordinates = np.where(threshold_image == 255)
    x_min = np.min(co_ordinates[0])
    x_max = np.max(co_ordinates[0])
    y_min = np.min(co_ordinates[1])
    y_max = np.max(co_ordinates[1])
    a_observed = ( (x_max-x_min) + (y_max-y_min) )/2
    zp = z*a_observed/a
    cv.waitKey(0)
    cv.destroyAllWindows()
    return zp