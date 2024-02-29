import cv2, time
import numpy as np

img = cv2.imread("../img/apple.jpg")

# 케니 엣지 적용 [다단계 알고리즘]  :
# 노이즈 제거  ( 가우시안 블러링)  ,
# 그라디언트 계산(소벨커널), 이중 임계값 , 비최대억제 (그라디언트계산 한것중 가장큰 값만 유지하고 나머지 0)
# 엣지 추적  :  비 최대억제값 연결
edges = cv2.Canny(img,100,200)

# 결과 출력
cv2.imshow('Original', img)
cv2.imshow('Canny', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
