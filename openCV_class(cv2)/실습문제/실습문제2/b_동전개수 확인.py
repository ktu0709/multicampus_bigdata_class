# 필요한 라이브러리를 불러옵니다.
import cv2
import numpy as np
from matplotlib import pyplot as plt

# . 이미지를 로드합니다
img = cv2.imread('coin.jpg', 0)

# OTSU . ( 이진화를 수행합니다 빈 칸 1)
ret, bin_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 작은 노이즈를 제거합니다 빈 . ( 2) 칸
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(bin_img, cv2.MORPH_OPEN, kernel, iterations=2)

# . ( 배경을 추출합니다 빈 칸 3)
sure_bg = cv2.dilate(opening, kernel, iterations=2)

# 거리 변환을 수행합니다 빈 . ( 4) 칸
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

# 거리 변환 결과를 사용하여 전경을 추출합니다 빈 . ( 5) 칸
ret, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)

# 전경과 배경이 아닌 것을 추출합니다.
sure_fg = np.uint8(sure_fg)
res = cv2.subtract(sure_bg, sure_fg)

# 영역 라벨링을 수행하고 라벨의 개수를 구합니다 빈 . ( 6) 칸
ret, markers = cv2.connectedComponents(sure_fg)

# 실제 동전의 개수를 출력합니다 빈 . ( 7) 칸
print(f"동전의 개수는 {ret-1} 입니다.")