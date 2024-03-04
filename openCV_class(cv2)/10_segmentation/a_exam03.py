import cv2
import numpy as np

#이미지 생성
image  = np.zeros((5,5) ,dtype= np.uint8)
image[2,2] = 1
#cv2.circle(image,(200,200) ,50,255, -1)

#거리변환 수행
dist_transform  = cv2.distanceTransform(image,cv2.DIST_L2, 3) #픽셀이 전경픽셀(1)로 부터 떨어진 거리 리턴

# 거리 변환 결과 정규화추가
norm_transform = (
    cv2.normalize(dist_transform, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U))

print(image)
print(dist_transform)
print(norm_transform)


