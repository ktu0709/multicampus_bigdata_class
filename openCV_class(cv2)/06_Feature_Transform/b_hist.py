import cv2
import matplotlib.pyplot as plt

'''
히스토그램   ->  이미지 대비 향상  
평활화    ->  누적 분포함수  
equalizeHist() -> 이미지히스토그램 -> 누적 분포함수  -> 새로운 픽셀값에 할당  
x축 : 픽셀값(0~ 255) ,  y축 : 픽셀값의 빈도수  
단, 컬러 이미지에 적용하게 되면 색상 왜곡이 발생할 수 있다.  
'''

# 이미지 로드 및 히스토그램 평활화
img = cv2.imread("img/apple.jpg",0)
res = cv2.equalizeHist(img)

# 원본 이미지와 결과 이미지 표시
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(res, cmap='gray')
plt.title('Histogram Equalized Image')
plt.axis('off')

# 원본 이미지의 히스토그램
plt.subplot(2, 2, 3)
plt.hist(img.ravel(), 256, [0,256])
plt.title('Histogram of Original Image')

# 평활화된 이미지의 히스토그램
plt.subplot(2, 2, 4)
plt.hist(res.ravel(), 256, [0,256])
plt.title('Histogram of Equalized Image')

plt.tight_layout()
plt.show()
