import cv2


body_cascade = cv2.CascadeClassifier('img/haarcascade_fullbody.xml')   # 객체의 명암패턴을 사용하는 강한 분류기
                                                                       # https://github.com/opencv/opencv/tree/4.x/data

cap = cv2.VideoCapture('img/people.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Video file finished or Error.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    bodies = body_cascade.detectMultiScale(gray, 1.2, 5)
    print(bodies)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, 'Person', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2,
                    lineType=cv2.LINE_AA)


    cv2.imshow('Human Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
