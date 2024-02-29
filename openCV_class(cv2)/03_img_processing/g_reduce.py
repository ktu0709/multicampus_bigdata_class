import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지를 그레이스케일로 불러온다
img = cv2.imread('../img/Lenna.png', cv2.IMREAD_GRAYSCALE)

# 이미지의 각 행의 합계를 계산한다
row_sum = cv2.reduce(img, dim=1, rtype=cv2.REDUCE_SUM, dtype=cv2.CV_32F)

# 이미지의 각 열의 합계를 계산한다
col_sum = cv2.reduce(img, dim=0, rtype=cv2.REDUCE_SUM, dtype=cv2.CV_32F)

# 결과를 시각화한다
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Row Sum')
plt.plot(row_sum)

plt.subplot(1, 3, 3)
plt.title('Column Sum')
plt.plot(col_sum.flatten())  # 1차원으로 만들기

plt.show()
