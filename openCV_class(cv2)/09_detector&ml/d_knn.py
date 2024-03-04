import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#https://docs.opencv.org/4.x/d5/d26/tutorial_py_knn_understanding.html

# 비지도 학습 분류 모델,
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
print(f'x={trainData}')  #-> 무작위 학습 데이터   X

responses = np.random.randint(0,2,(25,1)).astype(np.float32)
print(f'y={responses}')   #-> 정답 데이터   y

red = trainData[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')

blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')
plt.show()

#새로운 데이터 레이블 생성
newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)   # [[52. 20.]]  =0
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')
print(newcomer)

#k개의 인수만큼 이웃을 찾아서 같은 분류로 묶겠다.
knn = cv.ml.KNearest_create()
knn.train(trainData, cv.ml.ROW_SAMPLE, responses)  #학습
ret, results, neighbours ,dist = knn.findNearest(newcomer, 6)

print( "result: {}\n".format(results) )
print( "neighbours: {}\n".format(neighbours) )
print( "distance: {}\n".format(dist) )
plt.show()