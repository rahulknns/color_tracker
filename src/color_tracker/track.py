import color_tracker.rotation as rot
import cv2 
import numpy as np

class Tracker:
    def __init__(self,color_lower,color_higher,camera_yaw = 0,camera_pitch = 0,camera_roll = 0,zp = 1):
        self.color_lower = color_lower
        self.color_higher = color_higher
        self.camera_yaw = camera_yaw
        self.camera_pitch = camera_pitch
        self.camera_roll = camera_roll
        self.zp = zp
        self.r1 = rot.r1(self.camera_roll)
        self.r2 = rot.r2(self.camera_pitch)
        self.r3 = rot.r3(self.camera_yaw)
    
    def getColourPosition(self,image,x = None,y = None,z = None):
        xp,yp = self.getPixelPosition(image)
        if xp is None or yp is None:
            return None,None,None
        xpt,ypt,zpt = self.transformAxes(np.array([xp,yp,self.zp]))
        if x is not None:
            try:
                y = x*ypt/xpt
                z = x*zpt/xpt
            except ZeroDivisionError:
                y = None
                z = None
        elif y is not None:
            try:
                x = y*xpt/ypt
                z = y*zpt/ypt
            except ZeroDivisionError:
                x = None
                z = None
        elif z is not None:
            try:
                x = z*xpt/zpt
                y = z*ypt/zpt
            except ZeroDivisionError:
                x = None
                y = None
        return x,y,z


    def getPixelPosition(self,image):
        hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        threshold_image = cv2.inRange(hsv,self.color_lower,self.color_higher)
        ys,xs = np.where(threshold_image == 255)
        if xs.size == 0 or ys.size == 0:
            return None,None
        x = np.mean(xs)
        y = np.mean(ys)
        return x,y
    
    def transformAxes(self,co_ordinates):
        co_ordinates_t = np.matmul(self.r1,np.matmul(self.r2,np.matmul(self.r3,co_ordinates)))
        return co_ordinates_t