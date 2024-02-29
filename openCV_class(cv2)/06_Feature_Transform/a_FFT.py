import numpy as np
import cv2
from matplotlib import pyplot as plt

# 이미지 읽기
image = cv2.imread('img/apple.jpg', cv2.IMREAD_GRAYSCALE)

'''
cv2.imshow('test',image)
cv2.waitKey()
'''

# 푸리에 변환
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)  # 주파수 이동

# 실수(짝수 = 코사인 )부= 평균밝기 와  /  허수(홀수 = 사인 )부 = 위상   분리
f_real = fshift.real
f_imag = fshift.imag

#로그 스케일링 없이 이 값을 그대로 시각화하면 저주파 영역만 강조되어 나머지 영역은 구분하기 어렵다.
#로그작업
magnitude_spectrum = np.log(np.abs(fshift)+1)
real_spectrum = np.log(np.abs(f_real)+1)
imag_spectrum = np.log(np.abs(f_imag)+1)


plt.subplot(141),plt.imshow(image, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

#전체 주파수 스펙트럼(로그스케일 작용)
plt.subplot(142),plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

#실수(짝수)부 주파수 스펙트럼 (로그 스케일링 적용)
plt.subplot(143),plt.imshow(real_spectrum, cmap='gray')
plt.title('Real part'), plt.xticks([]), plt.yticks([])

#허수(홀수)부 주파수 스펙트럼 (로그 스케일링 적용)
plt.subplot(144),plt.imshow(imag_spectrum, cmap='gray')
plt.title('Imaginary part'), plt.xticks([]), plt.yticks([])

plt.show()
