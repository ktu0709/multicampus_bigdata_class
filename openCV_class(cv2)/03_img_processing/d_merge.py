import cv2 as cv
import matplotlib.pyplot as plt

# 이미지 불러오기
im1 = cv.imread('../img/apple.jpg')

# 채널 분리
b, g, r = cv.split(im1)  #  im [: ,:,(1,0)] = 0

#수동채널    x,y,(b,g,r)
b = im1[:,:,0]
g= im1[:,:,1]
r= im1[:,:,2]

# im1 [:,:,1] =  0  green  채널을 모두  0으로 하겠다.
im1 [:,:,2] =  0  #red  채널을 모두  0으로 하겠다.

# 채널 병합
merged_im1 = cv.merge([b, g, r])

# matplotlib을 이용한 시각화
plt.figure(figsize=(5, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv.cvtColor(im1, cv.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Merged Image')
plt.imshow(cv.cvtColor(merged_im1, cv.COLOR_BGR2RGB))

plt.show()
