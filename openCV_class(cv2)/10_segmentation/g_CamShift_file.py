import cv2
import numpy as np
import csv

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
# CSV 파일 초기화
with open('res/face_movement.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['frame', 'x', 'y', 'width', 'height'])

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Haar Cascade를 사용하여 초기 얼굴 위치를 찾는다
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        track_window = (x, y, w, h)

        # CamShift 알고리즘 적용
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, np.array((0., 60., 32.)), np.array((180., 255., 255.)))

        term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
        ret, track_window = cv2.CamShift(mask, track_window, term_crit)

        # 결과를 그린다 (회전된 사각형)
        pts = cv2.boxPoints(ret)
        #pts = np.int0(pts)  -> pts = np.asarray(pts, dtype=np.int32)
        pts = pts.astype(int)
        img2 = cv2.polylines(frame, [pts], True, 255, 2)

        # CSV 파일에 결과 저장
        with open('res/face_movement.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([frame_count, track_window[0], track_window[1], track_window[2], track_window[3]])

        frame_count += 1

        # 결과를 보여준다
        cv2.imshow('CamShift Tracking', img2)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()
