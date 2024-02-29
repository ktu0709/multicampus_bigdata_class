import cv2
import numpy as np

img = cv2.imread('../img/Lenna.png')

#가우시안 1D 커널생성
k2 = cv2.getGaussianKernel(3, 1.5)

#2d 가우시안 커널 생성(1D 커널을 외적으로 만들어서 적용해보자
gauss_2D = np.outer(k2,k2.T)

#filter2D 함수를 적용해서 가우시안 커널 적용
blur2 = cv2.filter2D(img, -1, gauss_2D)


merged = np.hstack((img, blur2))
cv2.imshow('gaussian blur', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()