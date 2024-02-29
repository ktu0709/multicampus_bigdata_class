'''
문제 3: 모폴로지 연산을 이용한 엣지 정제
1) 엣지 검출 결과를 정제하여 더욱 명확한 객체의 윤곽선을 얻는다.
2) 문제 2에서 생성된 엣지 이미지에 모폴로지 연산을 적용한다.
3) cv2.dilate와 cv2.erode 함수를 이용하여 엣지를 각각 팽창시킨 후 침식시켜서 정제된 엣지를 생성후
 결과 이미지는 refined_edges_apple.jpg로 저장한다.
'''

import cv2
import numpy as np

img = cv2.imread('apple_edges.jpg', cv2.IMREAD_GRAYSCALE)

k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))


dst = cv2.dilate(img, k)
erosion = cv2.erode(dst, k)
opening = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k)


merged = np.hstack((img, dst,erosion))
#cv2.imshow('',merged)
cv2.imshow('',opening)

cv2.waitKey(0)
cv2.destroyAllWindows()