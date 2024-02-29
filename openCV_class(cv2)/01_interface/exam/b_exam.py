# red_img 이미지에서 b,g,r만 각각 추출해서 r.txt,g,txt,b.txt로 저장해보자

import numpy as np
import cv2

img = cv2.imread("red_img.png")
#print(img)

B,G,R = cv2.split(img)

np.savetxt('b.txt',B,fmt='%d')
np.savetxt('g.txt',G,fmt='%d')
np.savetxt('R.txt',R,fmt='%d')
