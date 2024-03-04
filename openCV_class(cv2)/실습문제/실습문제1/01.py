import cv2
# XML 파일을 로드하여 Haar Cascade 분류기 객체를 생성합니다.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 웹캠에서 영상을 캡처합니다.
cap = cv2.VideoCapture(0)

while True:
    # 웹캠의 현재 프레임을 가져옵니다.
    ret, frame = cap.read()

    # 현재 프레임을 그레이스케일로 변환합니다.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 분류기를 사용하여 얼굴을 감지합니다.
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # 감지된 각 얼굴에 대하여 Bounding Box를 그립니다.
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # 현재 프레임에 감지된 얼굴과 Bounding Box를 출력합니다.
    cv2.imshow('Face Detection', frame)

    # 'q' 키를 누르면 루프에서 빠져나옵니다.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠을 해제하고 모든 창을 닫습니다.
cap.release()
cv2.destroyAllWindows()