import cv2
import numpy as np

# 1. 이미지 읽기
img = cv2.imread('img/apple_all.jpg')

# 2. 그레이스케일 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. 이진화
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imwrite('img_res/01_threshold.jpg', thresh)

# 4. 노이즈 제거
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=5)
cv2.imwrite('img_res/02_opening.jpg', opening)

# 5. 거리 변환 계산
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
cv2.imwrite('img_res/03_distance_transform.jpg', dist_transform)

# 6. 확실한 전경
_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

# 7. 확실한 배경
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# 8. 알려지지 않은 영역
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# 9. Marker 생성
_, markers = cv2.connectedComponents(sure_fg)
# retval(배경포함된 개수) , labels(라벨링된 이미지)= cv2.connectedComponents(이진이미지)
# 배경은  0으로 라벨링된다.
# ex) 검정배경에 하얀색 동그라미 2  = 2개의 객체+ 배경1 = 3 = retval
markers = markers + 1
markers[unknown == 255] = 0
print(markers)

# 10. 워터셰드 알고리즘 적용
cv2.watershed(img, markers)
img[markers == -1] = [0, 0, 255]

# 11. 결과 저장
cv2.imwrite('img_res/04_watershed_output.jpg', img)

# 12. 결과 표시
cv2.imshow('Watershed Segmentation', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
