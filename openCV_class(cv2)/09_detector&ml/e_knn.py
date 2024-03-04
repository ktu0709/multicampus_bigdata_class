import cv2
import numpy as np
'''
  << 이미지 내의 사과와 배경을 분류  >>
1)이미지 불러오기: OpenCV의 cv2.imread() 함수를 사용하여  이미지 로드
2)레이블링: 몇몇 픽셀이 사과인지, 배경인지 수동으로 레이블을 지정.
3)특성 추출: 이미지에서 사용할 특성을 추출  RGB 색상 값 추출
4)모델 학습: cv2.ml.KNearest_create()와 train() 함수를 사용하여 k-NN 모델을 학습
5)분류: 학습된 모델을 사용하여 이미지의 모든 픽셀을 분류
'''
# 이미지 불러오기
image = cv2.imread("../img/apple.jpg")
height, width, _ = image.shape

# 이미지를 1차원 배열로 변환 (특성 추출)
data = image.reshape((-1, 3))
data = np.float32(data)

# 수동으로 레이블링
# 여기서는 이미지의 좌측 상단 10x10 영역을 배경(0), 우측 하단 10x10 영역을 사과(1)로 가정
labels_background = np.zeros((100, 1), dtype=np.int32)
labels_apple = np.ones((100, 1), dtype=np.int32)

train_data_background = data[0:100, :]
train_data_apple = data[-100:, :]
train_data = np.vstack([train_data_background, train_data_apple])
train_labels = np.vstack([labels_background, labels_apple])

print(train_data ,  "=====>" ,  train_labels  )
# k-NN 모델 생성 및 학습
knn = cv2.ml.KNearest_create()
knn.train(train_data, cv2.ml.ROW_SAMPLE, train_labels)

# 이미지의 모든 픽셀을 분류
ret, results, neighbours, dist = knn.findNearest(data, k=3)

# 분류 결과를 이미지로 변환
segmented_image = results.reshape((height, width, 1))
segmented_image = np.uint8(segmented_image * 255)

# 결과 출력
cv2.imshow("Original", image)
cv2.imshow("Segmented", segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
