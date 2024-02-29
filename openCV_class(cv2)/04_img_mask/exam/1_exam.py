'''
문제 1: 블러링을 이용한 배경 제거
 1)사과 이미지의 배경을 블러링 처리하여 객체(사과)를 더욱 돋보이게 만든다
 2)사과 이미지를 불러와서 배경을 블러링 처리한다.
 3)cv2.GaussianBlur 함수를 사용하여 이미지에 가우시안 블러링을 적용하고, 사과 부분은 원본 그대로 유지한다.
   결과 이미지는 blurred_background_apple.jpg로 저장한다.
'''

import cv2
import numpy as np
img = cv2.imread('apple.jpg')
#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(img,(3,3),0)

merged = np.hstack((img, blur))
cv2.imwrite('blurred_background_apple.jpg', merged)
cv2.imshow('gaussian blur', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()