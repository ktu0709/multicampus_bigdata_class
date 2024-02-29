import cv2
#2 비디오 파일 재생하기

v_file = ',,/img/people.mp4'

#1 비디오 캡처하기
cap = cv2.VideoCapture(v_file) #0은 기본 카메라

while True:
    ret , frame =cap.read()
    if ret :
        cv2.imshow('me',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#2 웹캠 카메라 설정

cap.release()
cv2.destroyAllWindows()