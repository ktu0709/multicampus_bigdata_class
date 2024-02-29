import numpy as np
import cv2


apple = cv2.imread('../../img/apple.jpg')

#1 색공간 변환 해보자 . HSV
hsv_img = cv2.cvtColor(apple,cv2.COLOR_BGR2HSV)

lower_red = np.array([0,100,100])
upper_red = np.array([10,255,255])


#4 범위에 해당하는 마스크 설정
mask = cv2.inRange(hsv_img,lower_red,upper_red)
print(mask)


#5 마스크를 사용해서 원본이미지에서 빨강색 부분만 추출
red_part = cv2.bitwise_and(hsv_img,hsv_img,mask=mask)
#cv2.imwrite('hsv_img.png',hsv_img)

cv2.imshow("red_part",red_part)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("hsv_img",hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()