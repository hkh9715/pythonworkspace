import numpy as np
import cv2

def cornerDetect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imgray = np.float32(gray)
    dst = cv2.cornerHarris(imgray, 2, 3, 0.001)
    dst = cv2.dilate(dst, None)
    img2[dst>0.01*dst.max()]=[0, 0, 255]
    return cornerDetect


img = cv2.imread('ps2.0/training/20160725-3-1.jpg')
img2 = np.copy(img)
corner_image = cornerDetect(img2)
cv2.imshow('Harris', corner_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
