import cv2
import numpy as np
# 이미지의 지역적인 부분을 왜곡하는 기술
#어핀 변환은 이동, 회전, 스케일링 등의 기본적인 변환을 조합하여 구현되며, 전체 이미지에 균일하게 적용
image = cv2.imread('../img/apple.jpg')

# 변환 전, 후 점들
pts1 = np.float32([[50,50], [200,50], [50,200]])
pts2 = np.float32([[10,100], [200,50], [100,250]])

# 변환 행렬 구하기
M = cv2.getAffineTransform(pts1, pts2)

# Affine 변환 적용
dst = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# 결과 보기
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
