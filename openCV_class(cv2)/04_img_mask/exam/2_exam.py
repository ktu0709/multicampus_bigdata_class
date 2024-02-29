'''
문제 2: 엣지 검출을 통한 객체 윤곽 추출
1) 사과 이미지에서 객체의 윤곽(엣지)을 검출한다.
2) 사과 이미지를 불러와서 엣지 검출을 수행한다.
3)cv2.Canny 함수를 사용하여 엣지를 검출하고, 검출된 엣지만을 포함하는 새 이미지를 생성한다.
   결과 이미지는 apple_edges.jpg로 저장한다.
'''

import cv2
import numpy as np

img = cv2.imread('apple.jpg')

# 그레이 스케일 이미지로 변환
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(img, 100, 200)

cv2.imwrite('apple_edges.jpg', edges)
cv2.imshow('Canny Edge', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()