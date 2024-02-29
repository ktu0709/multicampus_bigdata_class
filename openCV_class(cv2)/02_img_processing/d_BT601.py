import cv2 as cv
#  BT.601   = RGB에서 Y 값을 산출하는 공식  = RGB 컬러 이미지를 흑백으로 변환하는 경우, 신호 Y 값을 산출

#  BT.601이란 ? 일반적인 사람의 시각 특성을 고려한 것으로 가장 밝게 느껴 지는 G(녹색)의 계수가 커지는 것을 확인

#   Y   =  0.299* R    +    0.587 *  G     +  0.114 *  B

im = cv.imread("../img/Lenna.png")
print(type(im))
print(im.shape)  #행, 열, 색상  =  높이 , 폭, 채널
print(im.dtype)

im_gray  = Y= 0.299* im[:,:,2]    +    0.587 *  im[:,:,1]     +  0.114 *   im[:,:,0]

print(type(im_gray))
print(im_gray.shape)  #행, 열, 색상  =  높이 , 폭, 채널
print(im_gray.dtype)

cv.imwrite('img_res/Lenna_Y.jpg', im_gray)
