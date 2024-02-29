#goodFeaturesToTrack 을 이용해서 영상을 출력 해보자.(Shi- Tomasi 코너 감지   )
import cv2
import numpy as np
from matplotlib import pyplot as plt
#print(cv2.goodFeaturesToTrack)

filename = 'img/house_01.jpg'

img  = cv2.imread(filename)
gray  = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)

# maxCorners 파람값으로 튜닝
corners = cv2.goodFeaturesToTrack(gray, 100000000, 0.01,10 )
corners = np.int0(corners)

print(type(corners) )
print(corners)

for i in corners:
     x,y = i.ravel()  # 1차원 변경    /   reshape() 다차원으로 변경 / flatten()_ 다차원 복사본 원본X
     cv2.circle(img,(x,y), 3,255,-1)

plt.imshow(img), plt.show()