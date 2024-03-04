import numpy as np
import cv2 as cv
# https://docs.opencv.org/4.x/d1/d5c/tutorial_py_kmeans_opencv.html
# kmeans 클러스터링 알고리즘을 사용해서 이미지 색상을 k개의 그룹으로 분류 하자.
img = cv.imread('img/sample.jpg')
Z = img.reshape((-1,3))  # (N,3)  = (픽셀수, RGB 색상채널)
print(Z)
# convert to np.float32
Z = np.float32(Z)
print(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
ret,label,center=cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
cv.imshow('res2',res2)
cv.waitKey(0)
cv.destroyAllWindows()
# 양자화  :   데이터 압축 , 계산 복잡감소 , 노이즈 제거 , 분석(색상, 질감정보 = 객체 검출, 세그멘테이션 작업 편리) , 시각화
# ex) 리소스 사용 최적화  = 메모리 및 연산 리소스 제한