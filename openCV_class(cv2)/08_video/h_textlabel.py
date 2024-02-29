import cv2

# 비디오를 읽어옵니다.
cap = cv2.VideoCapture("img/people_dancing.mp4")

# 비디오 저장을 위한 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('img/people_dancing_labeled.mp4', fourcc, 30.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.putText(frame, 'Dancing', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        out.write(frame)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
