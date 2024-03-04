#"모핑(morphing)"은 일반적으로 두 개 이상의 이미지를 서로 자연스럽게 변형하여 결합하는 과정
import cv2
import numpy as np

# 이미지 불러오기
face1 = cv2.imread('img/face1.jpg')
face2 = cv2.imread('img/face2.jpg')

# 두 이미지의 크기와 위치가 같아야 함
if face1.shape != face2.shape:
    print("이미지의 크기와 형식이 같아야 합니다.")
    exit()

# 모핑 파라미터 (0~1 사이의 값)
alpha = 0.3  # face1에 대한 가중치
beta = 1.0 - alpha  # face2에 대한 가중치

# 모핑 수행
morphed_face = cv2.addWeighted(face1, alpha, face2, beta, 0)

# 결과 보기
cv2.imshow('Face1', face1)
cv2.imshow('Face2', face2)
cv2.imshow('Morphed Face', morphed_face)
cv2.waitKey(0)
cv2.destroyAllWindows()
