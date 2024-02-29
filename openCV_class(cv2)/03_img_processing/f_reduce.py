'''
cv2.reduce() 함수는 행 또는 열의 차원을 줄여주는 작업을 수행합니다.
예를 들어, 모든 행을 더하거나 모든 열의 평균을 구하는 등의 작업을 수행할 수 있습니다.
'''
import cv2
import numpy as np

# 랜덤으로 3x3 크기의 행렬을 생성
src = np.random.randint(0, 10, (3, 3)).astype(np.float32)
print("Original Matrix:")
print(src)

# 행을 더하는 작업
reduce_row_sum = cv2.reduce(src, dim=0, rtype=cv2.REDUCE_SUM)
print("Row sum:")
print(reduce_row_sum)

# 열을 더하는 작업
reduce_col_sum = cv2.reduce(src, dim=1, rtype=cv2.REDUCE_SUM)
print("Column sum:")
print(reduce_col_sum)

# 열의 평균을 구하는 작업
reduce_col_avg = cv2.reduce(src, dim=1, rtype=cv2.REDUCE_AVG)
print("Column average:")
print(reduce_col_avg)
