# 1. 5*5  크기의 이미지를 만들자 . 모든픽셀을 1로 채우자.  np.ones
# 2. 3*3 크기를 만들자, 마스크의 중앙에 1을 놓고 나머지는 0으로 채우자. np.zeros
#3. 생성된 이미지에 마스크를 적용하고 결과를 c.png로 저장 결과를 출력하자. cv2.filter2D


import cv2
import numpy as np


original_image = np.ones((5,5),dtype=np.uint8)

print(original_image)
mask = np.zeros((3,3),dtype=np.uint8)
mask[1,1]=1
cv2.imwrite('mask.png',mask*255)

result_image=cv2.filter2D(original_image,-1,mask)
cv2.imwrite('c.png',result_image*255)

bit_image = cv2.bitwise_and(original_image,result_image*255)
cv2.imwrite('d_bit_image.png',bit_image)