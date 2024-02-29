import cv2

#1 비디오 캡처하기
cap = cv2.VideoCapture(0) #0은 기본 카메라

while True:
    ret , frame =cap.read()
    if ret :
        cv2.imshow('me',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#2 웹캠 카메라 설정

cap.release()
cv2.destroyAllWindows()