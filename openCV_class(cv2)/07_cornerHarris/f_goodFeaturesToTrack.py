#Shi- Tomasi 코너특징을 이용해서 영상을 출력 해보자.
import cv2
import numpy as np


filename = 'img/people.mp4'
outpath = 'people_corner_tomasi02.mp4'

vidcap = cv2.VideoCapture(filename)

w = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = 30

fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  #코덱  cv2.VideoWriter_fourcc(*'mp4')
writer = cv2.VideoWriter(outpath, fmt, fps, (w, h)) #출력기록 파일 , 코덱 , fps, 크기


# 코너 검출

while True:
    grabbed_frame, frame = vidcap.read()
    if frame is None:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
##################################
    corners = cv2. goodFeaturesToTrack(gray, maxCorners=10000, qualityLevel=0.001 , minDistance = 5)
    #corners = cv2. goodFeaturesToTrack(gray, maxCorners=100, qualityLevel=0.1 , minDistance = 10)
    corners = np.int0(corners)

    print(type(corners))
    for i in corners:
         x,y = i.ravel()  # 1차원 변경    /   reshape() 다차원으로 변경 / flatten()_ 다차원 복사본 원본X
         cv2.circle(frame,(x,y), 5, [0,0,255],-1)

###########################################
    frame = cv2.resize(frame,(w, h))  #영상 사이즈 재정의 하지 않으면 출력
    writer.write(frame)


    cv2.imshow('Frame', frame)
    key = cv2.waitKey(5)
    if key == 27:
        break

vidcap.release()
writer.release()