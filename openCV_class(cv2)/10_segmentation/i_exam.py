import cv2
import numpy as np

image  = np.zeros((400,400) ,dtype= np.uint8)

cv2.circle(image,(100,100) ,50,255, -1)
cv2.circle(image,(200,200) ,50,255, -1)
cv2.circle(image,(300,300) ,50,255, -1)

#노이즈 제거
image = cv2.medianBlur(image,5)

#거리변환 수행
dist_transform  = cv2.distanceTransform(image,cv2.DIST_L2, 5)
print(dist_transform)

# 거리 변환 결과 정규화추가
norm_transform = (
    cv2.normalize(dist_transform, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U))

# 거리계산 구한 값으로 임계값을 지정한 이미지
_,local_maxima  = cv2.threshold(dist_transform, 0.1*dist_transform.max(),255,cv2.THRESH_BINARY  )
print(local_maxima)
# 마커
local_maxima = np.uint8(local_maxima)
_, markers = cv2.connectedComponents(local_maxima)
#워터셰드
cv2.watershed(cv2.cvtColor(image, cv2.COLOR_GRAY2BGR), markers)

# 라벨링된 객체 개수 카운트 (0은 배경이므로 제외)
unique_markers = np.unique(markers)
object_count = len(unique_markers) - 1  # 배경을 제외하고 카운트

print(f"개수 : {object_count} ")

cv2.imshow('o_img' , image)
cv2.imshow('norm_transform' , norm_transform)
cv2.waitKey(0)
cv2.destroyAllWindows()
