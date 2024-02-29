import numpy as np
import cv2

blue_img = np.zeros((200,200,3),dtype=np.uint8)

blue_img[:,:] = [255,0,0]

#파란색 사각형 안에 빨간색 사각형
blue_img[75:100,50:150] = [0,0,255]

lower_red = np.array([0,0,200])
upper_red = np.array([50,50,255])

#4 범위에 해당하는 마스크 설정
mask = cv2.inRange(blue_img,lower_red,upper_red)
print(mask)


#5 마스크를 사용해서 원본이미지에서 빨강색 부분만 추출
red_part = cv2.bitwise_and(blue_img,blue_img,mask=mask)


cv2.imwrite('blue_res.jpg',blue_img)
cv2.imwrite('mask.jpg',red_part)
cv2.imshow("mask.jpg",mask)
cv2.imshow("mask.jpg",blue_img)
cv2.waitKey(0)
cv2.destroyAllWindows()