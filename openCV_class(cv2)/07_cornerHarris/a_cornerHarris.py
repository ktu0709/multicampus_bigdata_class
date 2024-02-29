import cv2
import numpy as np
import matplotlib.pyplot as plt


filename = 'img/chess.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# 해리스 코너 검출
dst = cv2.cornerHarris(gray, 2, 3, 0.05)
#dst = cv2.dilate(dst, None, iterations=3)  # 코너 위치 확장(이미지의 전경 객체를 팽창 = 작은 구멍이나 갭채우기)

# 코너 위치에 빨간색 표시
img[dst > 0.01 * dst.max()] = [0, 0, 255]

# 이미지 시각화
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Harris Corners')

plt.subplot(1, 2, 2)
plt.imshow(dst, cmap='gray')
plt.title('Harris Response')

plt.show()
