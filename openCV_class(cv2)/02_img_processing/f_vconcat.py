# 같은 이미지를 세로로 연결 해보자.
import cv2 as cv
import numpy as np

im1 = cv.imread("../img/apple.jpg")
im2 = cv.imread("../img/Lenna.png")

print(f'apple.jpg shape ={im1.shape}  Lenna.png shape ={ im2.shape}'  )

im_v  = cv.vconcat([im1, im1])
cv.imwrite("img_res/v_img.jpg" ,im_v)

im_v02=np.tile(im1,(2,1,1))
cv.imwrite("img_res/v_img02.jpg",im_v02)


im_v03=np.tile(im2,(2,1,1))
cv.imwrite("img_res/v_img03.jpg",im_v03)