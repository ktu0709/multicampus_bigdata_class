import cv2

img = cv2.imread('../img/bg.jpg')

cv2.line(img, (50, 50), (150, 50), (255,0,0))   # 파란색 1픽셀 선


cv2.line(img, (200, 50), (300, 50), (250,200,0))   # 파란색 1픽셀 선
cv2.line(img, (350, 50), (450, 50), (0,0,255))   # 파란색 1픽셀 선

# 하늘색(파랑+초록) 10픽셀 선
cv2.line(img, (100, 100), (400, 100), (255,255,0), 10)


cv2.line(img, (100, 350), (400, 350), (0,0,255), 20,cv2.LINE_8)
cv2.line(img, (100, 400), (400, 400), (0,0,255), 30,cv2.LINE_4)
cv2.line(img, (100, 450), (400, 450), (0,0,255), 40,cv2.LINE_AA)


cv2.imshow('lines', img)
cv2.waitKey(0)

cv2.destroyAllWindows()