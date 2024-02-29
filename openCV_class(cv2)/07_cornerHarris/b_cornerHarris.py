import cv2
import numpy as np
from matplotlib import pyplot as plt

# 이미지 로드 및 그레이스케일 변환
filename = 'img/house_01.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# 해리스 코너 검출
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None, iterations=3)  # 코너 위치 확장

print(dst)

# 코너 위치에 빨간색 표시
img[dst > dst.mean()] = [0, 0, 255]
#print( 0.05 * dst.max() ,   dst.max()   )

# 이미지 시각화
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Harris Corners')

plt.subplot(1, 2, 2)
plt.imshow(dst, cmap='gray')
plt.title('Harris Response')

plt.show()

