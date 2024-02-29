'''
감마 보정은 이미지의 픽셀 값을 지수 함수를 사용하여 조정
이미지의 전반적인 밝기를 변경하여 이미지의 대비를 높인다.
  O=(I/255.0)γ ×255
O는 출력 픽셀 값, I는 입력 픽셀 값,γ는 감마 값
'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 이미지 불러오기
image = cv.imread('../img/Lenna.png')

# 이미지가 제대로 불러와졌는지 확인
if image is None:
    print("Image not found!")
    exit()

# OpenCV의 BGR을 RGB로 변환
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# float32 타입과 정규화를 적용
image = image.astype(np.float32) / 255.0

# 감마 값 설정
gamma = 1.5

# 감마 보정 적용
image_gamma_corrected = np.power(image, gamma)

# 시각화
plt.figure(figsize=(10, 10))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(image_gamma_corrected)
plt.title(f'Gamma Corrected Image (gamma={gamma})')
plt.axis('off')

plt.show()

