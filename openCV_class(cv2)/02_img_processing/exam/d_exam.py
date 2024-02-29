#사과,레나,레나
#사과,사과,레나

import cv2 as cv
import numpy as np


im1 = cv.imread('../../img/apple.jpg')
im2 = cv.imread('../../img/Lenna.png')

#사과,레나,레나
def S_concat(im_list, interpolation=cv.INTER_CUBIC):
    # 가장 큰 폭과 높이를 찾는다.
    w_max = min(im.shape[1] for im in im_list)
    h_max = min(im.shape[0] for im in im_list)

    # 모든 이미지의 폭과 높이를 가장 큰 폭과 높이에 맞게 리 사이즈한다.
    im_list_resize = [cv.resize(im, (w_max, h_max), interpolation=interpolation) for im in im_list]

    # 디버깅: 각 이미지의 차원, 행의 수, 데이터 타입을 출력한다.
    for i, im in enumerate(im_list_resize):
        print(f"Image {i}: dims = {im.ndim}, shape = {im.shape}, dtype = {im.dtype}")

        # 모든 리사이즈된 이미지를 가로로 연결한다.
    return cv.hconcat(im_list_resize)

im_h = S_concat([im1, im2, im2])
cv.imwrite("s_concat.jpg", im_h)

#사과,사과,레나
def B_concat(im_list, interpolation=cv.INTER_CUBIC):  # 2) 매개인자로 이미지를 받는다.

    # 가장 큰 폭과 높이를 찾는다.
    w_max = max(im.shape[1] for im in im_list)
    h_max = max(im.shape[0] for im in im_list)

    # 모든 이미지의 폭과 높이를 가장 큰 폭과 높이에 맞게 리 사이즈한다.
    im_list_resize = [cv.resize(im, (w_max, h_max), interpolation=interpolation) for im in im_list]

    # 디버깅: 각 이미지의 차원, 행의 수, 데이터 타입을 출력한다.
    for i, im in enumerate(im_list_resize):
        print(f"Image {i}: dims = {im.ndim}, shape = {im.shape}, dtype = {im.dtype}")

        # 모든 리사이즈된 이미지를 가로로 연결한다.
    return cv.hconcat(im_list_resize)

im_h = B_concat([im1, im1, im2])
cv.imwrite("B_concat.jpg", im_h)