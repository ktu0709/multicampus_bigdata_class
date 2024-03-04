import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/face1.jpg')

mask = np.zeros(img.shape[:2], np.uint8)

# bgdModel과 fgdModel을 생성. grabCut 내부에서 사용될 배열
bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)

# ROI 설정.  이미지 전체를 대상
rect = (10, 10, img.shape[1]-10, img.shape[0]-10)

# grabCut 실행
cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

# 마스크 업데이트. 2와 3은 물체의 전경 (foreground)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# 이미지에 새로운 마스크를 곱해 결과를 리턴
result = img * mask2[:, :, np.newaxis]

result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 결과 표시
plt.subplot(121)
plt.imshow(img)
plt.title('Original')
plt.axis('off')

plt.subplot(122)
plt.imshow(result)
plt.title('GrabCut Segmentation')
plt.axis('off')

plt.show()
