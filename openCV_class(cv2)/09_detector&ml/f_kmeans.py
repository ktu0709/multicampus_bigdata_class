import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread("../img/apple.jpg")

print(image.shape)# (270, 223, 3)
# 이미지 크기 및 차원을 얻기
height, width, _ = image.shape  # (270, 223, 3)

# 이미지의 RGB 값을 특성으로 사용하기 위해 배열 변경
data = image.reshape((-1, 3))  #RGB 값을 하나의 행으로 갖는 2차원 배열을 만든다.
data = np.float32(data)
#print(data.shape)  -> (60210, 3)  ex)원본 이미지 크기 (100,100,3)    100*100  , 3

K = 2 # 클러스터의 수 (사과와 배경)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.1)
_, labels, centers = cv2.kmeans(data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# 레이블링된 결과로 이미지 분할
centers = np.uint8(centers)
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape(image.shape)


cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
