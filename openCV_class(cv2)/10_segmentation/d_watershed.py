'''
픽셀을 높고 낮은 지점으로 나누고, 그 다음에 '물'을 채워 나가면서 분할 경계를 찾는  기법
<가장자리 감지와 임계값 처리를 사용 하여 초기 분할 지점을 찾아 분리한다.>
[단계]
1. 원본 이미지를 로드하고 그레이스케일로 변환.
2. 이진화를 적용하여 전경과 배경을 분리
3. 노이즈를 제거
4. 배경과 전경 영역을 확실히 구분
5. cv2.watershed()를 적용하여 객체를 분할
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 읽기
img = cv2.imread('../img/apple.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이진화
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 노이즈 제거
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# 배경영역    : 노이즈를 제거 하게 되면  dilate 연산을 통해  배경을 확장하게 된다.
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# 전경영역 :거리변환 이미지를 적용한 전경영역을 구분하기 위해 임계값 처리를 수행한다.
# 거리의 최대값의 0.7배를 임계값으로 설정한다.
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

#영역계산
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# 마커라벨
_, markers = cv2.connectedComponents(sure_fg)

#확실한 배경이 0이 아닌 1이 되도록 모든 라벨에 1을 추가
markers = markers + 1

# 알 수 없는 영역을 0으로 표시
markers[unknown == 255] = 0

# watershed(유역을 적용)
cv2.watershed(img, markers)

#경계 표시
img[markers == -1] = [255, 0, 0]

# 전체 출력
images = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB), gray, thresh, opening, sure_bg, sure_fg, unknown, cv2.cvtColor(img, cv2.COLOR_BGR2RGB)]
titles = ['Original', 'Gray', 'Threshold', 'Opening', 'Sure Background', 'Sure Foreground', 'Unknown', 'Watershed']

fig, axes = plt.subplots(1, 8, figsize=(20, 20))

for ax, img, title in zip(axes, images, titles):
    if len(img.shape) == 3:
        ax.imshow(img)
    else:
        ax.imshow(img, cmap='gray')
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.show()

cv2.imwrite('res/apple_watershed.jpg', img)






