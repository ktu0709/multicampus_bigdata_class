import cv2 as cv
import numpy as np

def my_resize_horizontal(im_list, interpolation=cv.INTER_CUBIC):
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

# 이미지를 불러온다.
im1 = cv.imread('../img/apple.jpg')
im2 = cv.imread('../img/Lenna.png')

# 가로로 연결된 이미지를 생성한다.
im_h = my_resize_horizontal([im1, im2, im1])

# 결과를 저장한다.
if im_h is not None:
    cv.imwrite("img_res/hi_img_resize.jpg", im_h)
