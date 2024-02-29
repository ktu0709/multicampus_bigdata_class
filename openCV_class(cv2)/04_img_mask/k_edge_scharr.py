import cv2
import numpy as np

#Tip : 엣지 검출 -> 이미지의 밝기 변화율이 급격한 부분을 찾는 작업 , 경계 또는 윤곽
#소벨 : 이미지 + 미분
# Scharr : 소벨 + 엣지방향 + 강도
img = cv2.imread("../img/apple.jpg")

gx_k = np.array([[-3,0,3], [-10,0,10],[-3,0,3]])
gy_k = np.array([[-3,-10,-3],[0,0,0], [3,10,3]])
edge_gx = cv2.filter2D(img, -1, gx_k)
edge_gy = cv2.filter2D(img, -1, gy_k)

#소벨 연산의 확장형
scharrx = cv2.Scharr(img, -1, 1, 0)
scharry = cv2.Scharr(img, -1, 0, 1)

merged1 = np.hstack((img, edge_gx, edge_gy))
merged2 = np.hstack((img, scharrx, scharry))
merged = np.vstack((merged1, merged2))
cv2.imshow('Scharr', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
