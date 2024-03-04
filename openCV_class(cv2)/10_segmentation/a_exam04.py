import cv2
import numpy as np
#  5*5 크기의 검은 색 이미지를 만들고  중앙에 전경 픽셀을 추가한 후  거리 변환을 계산해 보자.
# 이미지 중심에서 1이 아닌 픽셀까지의 유클리디언 거리
# 중심 위치에 픽셀은 0 이고 , 그 주변의 1로 이루어진 픽셀까지의 거리는 0.955로 표시되고
# 모서리 부분은 1.369의 값을 리턴한다

image = np.array([
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0]], dtype=np.uint8)

dist_transform = cv2.distanceTransform(image, cv2.DIST_L2, 3)
normalized_dist_transform = cv2.normalize(dist_transform, None, 0, 255, cv2.NORM_MINMAX)

print(dist_transform)