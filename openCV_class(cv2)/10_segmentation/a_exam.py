import cv2
import numpy as np

#이미지 생성
image  = np.zeros((400,400) ,dtype= np.uint8)
print(image)
cv2.circle(image,(200,200) ,100,255, -1)

#거리변환 수행
dist_transform  = cv2.distanceTransform(image,cv2.DIST_L2, 5)
print(dist_transform)

# 거리 변환 결과 정규화추가
norm_transform = (
    cv2.normalize(dist_transform, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U))

cv2.imshow('o_img' , image)
cv2.imshow('norm_transform' , norm_transform)
cv2.waitKey(0)
cv2.destroyAllWindows()
