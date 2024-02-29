import cv2
import numpy as np


image = cv2.imread('img/arc_warden.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.medianBlur(gray, 7)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
                           param1=100, param2=30, minRadius=70, maxRadius=100)

print(circles)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)


cv2.imshow('Glasses Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
