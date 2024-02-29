import cv2 as cv
import numpy as np

# 이미지 불러와서 HSV로  분리하고 싶다.
im1 = cv.imread('../img/apple.jpg')
im2 = cv.imread('../img/Lenna.png')

# im1과 im2의 shape이 다르다면, 둘 중 하나를 다른 하나에 맞춰서 리사이즈해야 합니다.
if im1.shape != im2.shape:
    im2 = cv.resize(im2, (im1.shape[1], im1.shape[0]))

### 색상공간 바꾸기
hsv1 = cv.cvtColor(im1, cv.COLOR_BGR2HSV)
hsv2 = cv.cvtColor(im2, cv.COLOR_BGR2HSV)

# 채널 분리
h1, s1, v1 = cv.split(hsv1)
h2, s2, v2= cv.split(hsv2)

# 채널 병합  H(색조),  S(채도), V(명도)
merged = cv.merge((h1, s1, v2))


# 결과 이미지 화면에 출력
cv.imshow("Merged Image", merged)

# 키보드 입력을 기다림
cv.waitKey(0)

# 모든 윈도우 창을 닫음
cv.destroyAllWindows()
