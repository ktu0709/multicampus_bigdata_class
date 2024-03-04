import numpy as np
import cv2 as cv

cap = cv.VideoCapture("img/slow_traffic_small.mp4")
# take first frame of the video
ret,frame = cap.read()

# 비디오의 첫프레임을 읽고 추적할 초기영역 (ROI)를 설정한다.
x, y, w, h = 300, 200, 100, 50 # simply hardcoded the values
track_window = (x, y, w, h)

# set up the ROI(Initial Frame and Region of Interest) for tracking
# ROI를 색공간으로 변화하고 마스크를 적용한다.
roi = frame[y:y+h, x:x+w]
hsv_roi =  cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))

#ROI 색상 히스토그램을 계산하고 정규화한다.  -> 히스토그램은 다음프레임에서 객체의 위치를 찾을 때 사용한다.
#Hsv / Hue 0~ 179
roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by at least 1 pt
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )

###### cv2.calcHist (Hue 채널 히스토그램)  -> cv.normalize  ->  cv.calcBackProject(역투영)
while(1):
    ret, frame = cap.read()

    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        #히스토그램을 역투영 ( 동일한 색상 분포를 가진 영역을 찾아 준다)
        dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # apply camshift to get the new location  -> 객체 추적 시작
        #ret : 추적대상의 위치, 크기, 회전각도를 나타내는 사각형((x_center,y_center),(w,h), angle)
        #track_window :  (x,y,w,h)
        ret, track_window = cv.CamShift(dst, track_window, term_crit)
        print(ret)
        # Draw it on image
        pts = cv.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv.polylines(frame,[pts],True, 255,2)
        cv.imshow('img2',img2)

        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break
