# << 임계값 지정해서   이미지를  확인 해보자>>
import cv2 as cv
import matplotlib.pyplot as plt

# 이미지를 불러온다.
image = cv.imread('../img/apple.jpg')

# 이미지를 그레이스케일로 변환한다.
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# 임계값을 적용한다. 여기서는 128을 기준으로 임계값을 적용하였다.
# 128 이하의 값은 0으로, 128 초과의 값은 255로 설정한다.
ret, thresh1 = cv.threshold(gray_image, 128, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(gray_image, 128, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(gray_image, 128, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(gray_image, 128, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(gray_image, 128, 255, cv.THRESH_TOZERO_INV)

# 결과를 Matplotlib를 사용하여 출력한다.
titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [gray_image, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()
