import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny


image = cv2.imread('solidWhiteCurve.jpg')
lane_image = np.copy(image)
canny =  canny(lane_image)
# print(image)
# canny2 = cv2.Canny(blur, 50, 300)
# cv2.imshow('lane_image', lane_image)
plt.imshow(canny)
# cv2.imshow('canny2', canny2)
plt.show()

# [100, height], [400, 200], [800, height]