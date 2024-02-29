import cv2
import numpy as np

#캐니 엣지 검출기 -> 허프 선 검츨
img = cv2.imread('img/dave.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

lines = cv2.HoughLines(edges, 1, np.pi/90, 100)

print(lines)
if lines is not None:
    for line in lines:
        for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imwrite('img/houghlines.jpg', img)
cv2.imshow('edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()