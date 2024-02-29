# red_img 이미지에서 b,g,r만 각각 추출해서 r.txt,g,txt,b.txt로 저장해보자

import numpy as np
import cv2

img = cv2.imread("../../img/apple.jpg")
print(img)

img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
H,S,V = cv2.split(img)

np.savetxt('b.txt',H,fmt='%d')
np.savetxt('g.txt',S,fmt='%d')
np.savetxt('R.txt',V,fmt='%d')
