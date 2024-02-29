import cv2
import numpy as np

# 이미지 불러오기
img = cv2.imread('../img/apple.jpg')

# 변환 유형들
transformations = [
    ("RGB2GRAY", cv2.COLOR_RGB2GRAY),
    ("RGB2XYZ", cv2.COLOR_RGB2XYZ),
    ("RGB2YCrCb", cv2.COLOR_RGB2YCrCb),
    ("RGB2HSV", cv2.COLOR_RGB2HSV),
    ("RGB2HLS", cv2.COLOR_RGB2HLS),
    ("RGB2Lab", cv2.COLOR_RGB2Lab),
    ("RGB2Luv", cv2.COLOR_RGB2Luv)
]

# 변환된 이미지들을 저장할 리스트
transformed_images = []

for name, flag in transformations:
    transformed = cv2.cvtColor(img, flag)
    # 1채널 이미지의 경우 3채널로 변경 (시각화를 위해)
    if transformed.ndim == 2:
        transformed = cv2.cvtColor(transformed, cv2.COLOR_GRAY2RGB)
    transformed_images.append((name, transformed))

# 시각화
for name, image in transformed_images:
    cv2.imshow(name, image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
