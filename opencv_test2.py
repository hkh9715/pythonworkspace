import cv2
frame = cv2.imread('C:\Users\한건희\Desktop\pythonworkspace\solidWhiteCurve.jpg')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_blue = np.array([60, 40, 40])
upper_blue = np.array([150, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
edges = cv2.Canny(mask, 200, 400)

cv2.imshow('edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()