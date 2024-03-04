import cv2
import numpy as np

# 이미지 로드
image = cv2.imread("../img/apple.jpg")

# 평균 이동 필터링  = 객체 추적 = 블러링과 노이즈 제거를 동시에 사용한다
filtered_img = cv2.pyrMeanShiftFiltering(image, 30, 51)  #공간 윈도우 반지름 , 색상윈도우반지름
# 공간 윈도우 반지름  :  각 픽셀 주변 반지름 30 픽셀의 원 안에서 알고리즘이 적용
# 색상윈도우반지름   : 공간 윈도우 30안에서 유클리디안 거리가 51이내인 모든 픽셀을 같은 세그먼트로 간주한다.


# 결과 표시
cv2.imshow("Original", image)
cv2.imshow("Filtered", filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
