import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지를 그레이스케일로 읽기
img = cv2.imread('img/trail.jpg', 0)


hist = cv2.calcHist([img], [0], None, [256], [0, 256]) # ranges = 픽셀값의 범위


plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
