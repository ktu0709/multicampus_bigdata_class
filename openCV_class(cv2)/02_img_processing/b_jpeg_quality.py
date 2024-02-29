import cv2
import matplotlib.pyplot as plt
import numpy as np

# 원본 이미지 불러오기
original = cv2.imread("../../img/Lenna.png")
original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)  # BGR to RGB

# 다양한 품질로 이미지 저장  -> 지정된 params를 통해 양자화 하겠다.   0 ~ 100까지 값으로 압축률을 지정한다.
# jpeg압축은 양자화 행렬을 사용하여 고주파 성분(경계선, 노이즈, 글자 등의 밝기 변화 빠른것 ) 을 줄이는데 있다.
cv2.imwrite("img_res/quality_90.jpg", original, [cv2.IMWRITE_JPEG_QUALITY, 90])
cv2.imwrite("img_res/quality_50.jpg", original, [cv2.IMWRITE_JPEG_QUALITY, 50])
cv2.imwrite("img_res/quality_10.jpg", original, [cv2.IMWRITE_JPEG_QUALITY, 10])

# 압축한 이미지 불러오기
img_90 = cv2.imread("img_res/quality_90.jpg")
img_90 = cv2.cvtColor(img_90, cv2.COLOR_BGR2RGB)

img_50 = cv2.imread("img_res/quality_50.jpg")
img_50 = cv2.cvtColor(img_50, cv2.COLOR_BGR2RGB)

img_10 = cv2.imread("img_res/quality_10.jpg")
img_10 = cv2.cvtColor(img_10, cv2.COLOR_BGR2RGB)

# 원본 이미지와 압축한 이미지 비교
plt.figure(figsize=(10, 10))

plt.subplot(1, 4, 1)
plt.imshow(original)
plt.title("Original")

plt.subplot(1, 4, 2)
plt.imshow(img_90)
plt.title("Quality 90")

plt.subplot(1, 4, 3)
plt.imshow(img_50)
plt.title("Quality 50")

plt.subplot(1, 4, 4)
plt.imshow(img_10)
plt.title("Quality 10")

plt.show()
