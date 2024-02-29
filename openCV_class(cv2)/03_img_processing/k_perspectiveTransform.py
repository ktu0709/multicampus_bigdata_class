# 이미지에서 특정 영역을 추출하거나 이미지를 다른 시점에서 보기 위한 함수
#3x3 투영 행렬을 사용하여 점의 집합을 다른 투영으로 변환
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 불러오기
image = cv2.imread('../img/Lenna.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 원본 이미지에 적용할 4개의 점 (왼쪽 상단, 오른쪽 상단, 왼쪽 하단, 오른쪽 하단)
pts1 = np.float32([[50, 50],
                   [200, 50],
                   [50, 200],
                   [200, 200]])

# 결과 이미지에서 위의 4개의 점에 대응하는 점
pts2 = np.float32([[10, 100],
                   [200, 50],
                   [100, 250],
                   [300, 200]])

# 투영 행렬 계산
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# 투영 변환 수행 : 투영 변환 매트릭스와 원본 이미지를 인수로 받아 투영 변환을 수행
result = cv2.warpPerspective(image, matrix, (450, 300))
result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

# Matplotlib를 사용하여 원본 이미지와 결과 이미지를 나란히 표시
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_rgb)

plt.subplot(1, 2, 2)
plt.title("Perspective Transformation")
plt.imshow(result_rgb)

plt.show()







