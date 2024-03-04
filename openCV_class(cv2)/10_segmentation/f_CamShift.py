import cv2
import numpy as np

cap = cv2.VideoCapture(0)

x, y, w, h = 300, 200, 100, 50
track_window = (x, y, w, h)

# Region of Interest (ROI) 설정
ret, frame = cap.read()
roi = frame[y:y + h, x:x + w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# 터미널 조건 설정   : CamShift 의 종료 조건 설정
#term_crit = (cv2.TERM_CRITERIA_EPS   = 정확도 허용 오차   | cv2.TERM_CRITERIA_COUNT = 반복횟수   , 10, 1)
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        #CamShift (객체 색상분포,추적하는 윈도우위치, 종료조건)   알고리즘 적용  : 객체 추적 알고리즘
        # ->  ret :  추적한 객체의 위치를 나타내는 회전하는 사각형  ,  track_window : 새로운 추적 윈도우 위치, 크기
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)


        # 결과를 그리기 위한 정보
        pts = cv2.boxPoints(ret)
        pts = pts.astype(int)

        final_image = cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

        cv2.imshow("CamShift Tracking", final_image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

cv2.destroyAllWindows()
cap.release()
