'''
1 apple.jpg 이미지를 컬러로 로드
2 이미지를 HSV 색 공간으로 변환하고 hsv_apple.png로 저장
3. 이미지의 크기를 300x300으로 조정하고 resized_apple.png로 저장
4. 트랙바를 사용하여 이미지의 채도(Saturation)를 조정한다.
'''

import cv2
import numpy as np

img = cv2.imread("apple.jpg")


#2
hsv_img = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
cv2.imwrite('resized_apple.png', hsv_img)



#3
resize_img = cv2.resize(img, [300, 300])
cv2.imwrite('resized_apple.png', resize_img)

#4

def adjust_brightness(x):
   #pass
   saturation = cv2.getTrackbarPos('Saturation','image')-50
   hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

   hsv_img[:,:,1] = cv2.add(hsv_img[:,:,1],saturation)
   adjusted_img=cv2.cvtColor(hsv_img)