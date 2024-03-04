import cv2
import numpy as np
import matplotlib.pyplot as plt
'''
1. 객체 내부에서 거리 계산시 유용 
2. 이진 이미지에서 각 픽셀의 값이 0인 위치로 부터 가장 가까운 픽셀의 값이 255인 위치까지의 거리를 계산
3. 거리 변환의 결과는 원본 이진 이미지에서 각 픽셀이 '1' (또는 255, 흰색)로부터 얼마나 떨어져 있는 지를 나타냄
'''
img = cv2.imread('img/a.jpg', 0)

# 이진화
_, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)


# 거리 변환 적용  : 가장 가까운 배경 픽셀의 거리를 계산
dist_transform = cv2.distanceTransform(binary_img, cv2.DIST_L2, 3)
#  cv2.DIST_L1, cv2.DIST_L2 , cv2.DIST_C
# maskSize  3 또는 5
normalized = cv2.normalize(dist_transform, None, 0,
                           255, cv2.NORM_MINMAX, cv2.CV_8U)
print(img)
print(binary_img)
# 결과 출력
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Binary Image')
plt.imshow(binary_img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Distance Transform')
plt.imshow(normalized, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
