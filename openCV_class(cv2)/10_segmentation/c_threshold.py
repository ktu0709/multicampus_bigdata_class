import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../img/apple.jpg', 0)

_, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)
thresh3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


plt.figure(figsize=(15,5))
plt.subplot(1, 4, 1)
plt.imshow(img, 'gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(thresh1, 'gray')
plt.title('Global Thresholding')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(thresh2, 'gray')
plt.title('Adaptive Mean Thresholding')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(thresh3, 'gray')
plt.title('Adaptive Gaussian Thresholding')
plt.axis('off')

plt.show()
