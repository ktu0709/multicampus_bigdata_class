#임의의 이미지를 생성해 보자
#numpy.zeros(크기,타입)

import numpy as np
import cv2

red_img = np.zeros((100,100,3),dtype=np.uint8)
#print(red_img)
#red_img[:,:] = [0,0,255] #B,G,R
red_img[0,0] = [255,0,0]  #B,G,R
red_img[0,1] = [0,0,255]  #B,G,R

red_img[:,:] = [0,0,255]  #B,G,R
red_img[:,50] = [0,255,0]


#48~52라인 모든 컬러 그린
red_img[48:52,:] = [0,255,0]
print(red_img.shape)
print(red_img[50,50])
cv2.imwrite('red_img.png',red_img)
