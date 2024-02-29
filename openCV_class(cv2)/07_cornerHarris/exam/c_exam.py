import cv2
import numpy as np
import pandas as pd
#https://moviepy.readthedocs.io/en/latest/index.html


filename = '../img/people.mp4'

#1 filename = 'img/people.mp4'을 읽어서 특징 추출한 값을 csv로 저장한다
#2 단 특징점 추출 알고리즘 ORB로 구현해 보자
vidcap = cv2.VideoCapture(filename)

w = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = 30

fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # 코덱


feature_data = []

while True:
    grabbed_frame, frame = vidcap.read()
    if frame is None:
        break

    orb = cv2.ORB_create()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = np.float32(gray)

    kp= orb.detect(frame, None)
    for point in kp:
        feature_data.append([point.pt[0],point.pt[1],point.size,point.angle])

vidcap.release()
df_feature = pd.DataFrame(feature_data,columns=['x','y','size','Angle'])
df_feature.to_csv('c_exam.csv')







