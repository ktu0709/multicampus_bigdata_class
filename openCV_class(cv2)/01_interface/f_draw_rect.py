import cv2

img = cv2.imread('../img/bg.jpg')

# 좌상, 우하 좌표로 사각형 그리기, 선 두께는 default 1
cv2.rectangle(img, (50, 50), (150, 150), (255,0,0) )

cv2.rectangle(img, (300, 300), (200, 200), (255,150,50) ,10)

cv2.rectangle(img, (400, 200), (200, 450), (0,0,200) ,-1)

cv2.imshow('rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()