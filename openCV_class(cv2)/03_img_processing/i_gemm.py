import cv2 as cv
import numpy as np

# 두 개의 2x2 행렬 생성
src1 = np.array([[1, 2],
                       [3, 4]], dtype=np.float32)
src2 = np.array([[5, 6],
                       [7, 8]], dtype=np.float32)

# 행렬 곱셈 수행 (src1 * src2)
alpha = 1.0
dst = cv.gemm(src1, src2, alpha, None, 0.0, None)

print("Result:")
print(dst)

'''
 일반 행렬 곱셉 
cv2.gemm(src1, src2, alpha, src3, beta, dst[, flags])
src1: 첫 번째 행렬 (M x N)
src2: 두 번째 행렬 (N x K)
alpha: 첫 번째 행렬과 두 번째 행렬의 곱에 적용될 스칼라 값
src3: 세 번째 행렬 (선택적, 추가 항)
beta: 세 번째 행렬에 적용될 스칼라 값 (선택적)
dst: 출력 행렬 (M x K)
flags: 연산 플래그 (예: cv2.GEMM_1_T는 첫 번째 행렬을 전치)
'''

