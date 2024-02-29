# 4-3    높이가  다른 이미지를 가로로 연결해보자   cv.hconcat()
import cv2 as cv
import numpy as np

im1 = cv.imread('../img/apple.jpg')
im2 = cv.imread('../img/Lenna.png')

# 함수 선언  resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])

# im.shape [0]는 높이 ,  [1] 폭
def my_hresize(im_list, interpolation=cv.INTER_CUBIC):
    # 1. 높이가 가장 작은 값을 리턴 받자.
    h_min = min(im.shape[0] for im in im_list)

    # 2.폭의 사이즈를   재조정
    im_list_resize = [cv.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min),
                                interpolation=interpolation) for im in im_list]

    return cv.hconcat(im_list_resize)  # 결합해서 리턴


im_h = my_hresize([im1, im2, im1])

cv.imwrite("img_res/h_img_resize.jpg", im_h)