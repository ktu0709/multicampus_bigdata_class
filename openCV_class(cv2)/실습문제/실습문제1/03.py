import cv2
import numpy as np
# 이미지 불러오기
image = cv2.imread('image.jpg')

# 그레이스케일로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이진화
_, binary_img = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

# 윤곽선 찾기
contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# SIFT 객체 생성
sift = cv2.SIFT_create()

# 객체를 탐지하고 라벨링
for i, contour in enumerate(contours):
    x, y, w, h = cv2.boundingRect(contour)
    roi = gray[y:y+h, x:x+w]

    # 특징점 추출
    keypoints, descriptors = sift.detectAndCompute(roi, None)

    # 원래 이미지에 특징점 표시 (라벨링을 위한 예)
    for point in keypoints:
        transformed_x, transformed_y = int(x + point.pt[0]), int(y + point.pt[1])
        cv2.circle(image, (transformed_x, transformed_y), 3, (0, 255, 0), -1)

    # 라벨 표시 (여기서는 i를 라벨로 사용)
    cv2.putText(image, str(i), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)


# 결과 이미지 표시
cv2.imshow('Labeled Objects with Keypoints', image)
cv2.waitKey(0)
cv2.destroyAllWindows()