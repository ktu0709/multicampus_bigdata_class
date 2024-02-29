import cv2 as cv
import numpy as np

# 이미지 불러오기
im1 = cv.imread('../img/bg.jpg')
im2 = cv.imread('../img/Lenna.png')

# im1과 im2의 shape이 다르다면, 둘 중 하나를 다른 하나에 맞춰서 리사이즈해야 합니다.
if im1.shape != im2.shape:
    im2 = cv.resize(im2, (im1.shape[1], im1.shape[0]))

# 채널 분리
r1, g1, b1 = cv.split(im1)
r2, g2, b2 = cv.split(im2)

# 채널 병합: im1의 빨간색 채널, im2의 녹색 채널, im1의 파란색 채널을 병합
merged = cv.merge((r1, g1, b2))


# 결과 이미지 화면에 출력
cv.imshow("Merged Image", merged)

# 키보드 입력을 기다림
cv.waitKey(0)

# 모든 윈도우 창을 닫음
cv.destroyAllWindows()
