import cv2
import numpy as np

file_name = "../img/apple.jpg"
img = cv2.imread(file_name,0)

# 프리윗 커널 생성
gx_k = np.array([[-1,0,1],
                 [-1,0,1],
                 [-1,0,1]])

gy_k = np.array([[-1,-1,-1],
                 [0,0,0],
                 [1,1,1]])

# 프리윗 커널 필터 적용
edge_gx = cv2.filter2D(img, -1, gx_k)
edge_gy = cv2.filter2D(img, -1, gy_k)

print(edge_gx)
print(edge_gy)
np.savetxt('res/apple_gx.txt',edge_gx,fmt='%d')
merged = np.hstack((img, edge_gx, edge_gy, edge_gx+edge_gy))
cv2.imshow('prewitt', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()