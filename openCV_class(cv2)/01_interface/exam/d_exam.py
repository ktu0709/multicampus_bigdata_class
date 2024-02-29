# red_img 이미지에서 b,g,r만 각각 추출해서 r.txt,g,txt,b.txt로 저장해보자

import numpy as np
import cv2

img = cv2.imread("../../img/apple.jpg")

value = np.ones_like(img)*50

#print(img)


plus_img = cv2.add(img,value)
min_img = cv2.subtract(img,value)


cv2.imshow('myimg',img)
cv2.imshow('plus',plus_img)
cv2.imshow('min',min_img)
cv2.waitKey(0)
cv2.destroyAllWindows()