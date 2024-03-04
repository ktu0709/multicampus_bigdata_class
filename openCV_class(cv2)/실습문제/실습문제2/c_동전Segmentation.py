import cv2
import numpy as np
from matplotlib import pyplot as plt

# Create a 2x5 subplot array
fig, axes = plt.subplots(2, 5, figsize=(20, 8))
axes = axes.ravel()

# 1. 이미지 로딩
img = cv2.imread('coin.jpg', 0) # 1 빈 칸
axes[0].imshow(img, cmap='gray')
axes[0].set_title('1. Original Image')

# 2. OTSU 이진화
ret, bin_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) # 2 빈 칸
axes[1].imshow(bin_img, cmap='gray')
axes[1].set_title('2. OTSU Binary Image')

# 4. 이미지에 포함된 작은 노이즈 삭제
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(bin_img, cv2.MORPH_OPEN, kernel, iterations=2) # 3 빈 칸
axes[2].imshow(opening, cmap='gray')
axes[2].set_title('4. Noise Removal')

# 5. 배경 추출
sure_bg = cv2.dilate(opening, kernel, iterations=2) # 4 빈 칸
axes[3].imshow(sure_bg, cmap='gray')
axes[3].set_title('5. Background Extraction')

# 6. 거리 변환
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5) # 5 빈 칸
axes[4].imshow(dist_transform, cmap='gray')
axes[4].set_title('6. Distance Transform')

# 7. 전경 추출
ret, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0) # 6 빈 칸
axes[5].imshow(sure_fg, cmap='gray')
axes[5].set_title('7. Foreground Extraction')

# 8. 배경도 전경도 아닌 값 추출
sure_fg = np.uint8(sure_fg)
res = cv2.subtract(sure_bg, sure_fg) # 7 빈 칸

axes[6].imshow(res, cmap='gray')
axes[6].set_title('8. Unknown Region')

# 9. 영역 라벨
ret, markers = cv2.connectedComponents(sure_fg)
axes[7].imshow(markers)
axes[7].set_title(f'9. Connected Components (Coins: {ret-1})')
print(f" {ret-1} 동전의 개수는 개 입니다.")

# 10. Watershed
markers = markers + 1
markers[res == 255] = 0
img_colored = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
markers = cv2.watershed(img_colored, markers)
img_colored[markers == -1] = [255, 0, 0]
axes[8].imshow(cv2.cvtColor(img_colored, cv2.COLOR_BGR2RGB))
axes[8].set_title('10. Watershed')

for ax in axes:
 ax.axis('off')


plt.show()
