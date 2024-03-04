import cv2

img = cv2.imread('img/shape.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

# 흰색 객체 외곽선 검출 ver.3.X / ver 4.X (이진이미지 바로 사용)
#findContours (대상이미지, mode 윤곽을 찾는 방법 , method : 윤곽포인트 근사화하는 방법
# mode python : cv.RETR_EXTERNAL(바깥쪽 윤곽) , cv.RETR_LIST(계층구조X), cv.RETR_CCOMP(구멍 포함) , cv.RETR_TREE
# method python : cv.CHAIN_APPROX_NONE , cv.CHAIN_APPROX_SIMPLE(수직선 , 수평선, 대각선의 세그멘테이션 압축해서 끝점만 리턴한다)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('Shape Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()