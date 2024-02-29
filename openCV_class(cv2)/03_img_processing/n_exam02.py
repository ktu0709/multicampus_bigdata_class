'''
1.사과 이미지를 채널 분리를 한다.
2. 레나 이미지를 채널 분리를 한다.

3. 두개의 이미지의 사이즈를  동일 하게 조정한 후  사과의 B  , 레나 R,  사과의 G
값을 병합해서 결과를 확인 한다.

'''
import cv2


apple_image = cv2.imread('../img/apple.jpg')
lena_image = cv2.imread('../img/Lenna.png')

#1.사과 이미지를 채널 분리를 한다.
apple_b, apple_g, apple_r = cv2.split(apple_image)
lena_b, lena_g, lena_r = cv2.split(lena_image)

#2. 사이즈를 조절 한다.
apple_b = cv2.resize(apple_b, (lena_image.shape[1], lena_image.shape[0]))
apple_g = cv2.resize(apple_g, (lena_image.shape[1], lena_image.shape[0]))

#3. 사과의 B, 레나의 R, 사과의 G
merged_image = cv2.merge((apple_b, lena_r, apple_g))

# 결과 확인
cv2.imshow('Merged Image', merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

