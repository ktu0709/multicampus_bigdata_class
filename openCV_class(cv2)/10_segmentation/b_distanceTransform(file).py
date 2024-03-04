import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../img/apple.jpg', 0)

_, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

dist_transform = cv2.distanceTransform(binary_img, cv2.DIST_L2, 5)

cv2.imwrite('res/binary_apple.jpg', binary_img)
cv2.imwrite('res/dist_transform_apple.jpg', dist_transform)

np.savetxt("res/binary_apple.csv", binary_img, delimiter=",")
np.savetxt("res/dist_transform_apple.csv", dist_transform, delimiter=",")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Binary Image')
plt.imshow(binary_img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Distance Transform')
plt.imshow(dist_transform, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
