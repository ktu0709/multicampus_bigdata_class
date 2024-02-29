# 해리스 검출을 이용해서 영상을 출력 해보자.
import cv2
import numpy as np

filename = 'img/people.mp4'
#
outpath = 'img/people_corner_harris.mp4'
#outpath = 'img/my_corner_harris.mp4'
vidcap = cv2.VideoCapture(filename)

w = int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fps = 30

fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # 코덱
writer = cv2.VideoWriter(outpath, fmt, fps, (w, h))  # 출력기록 파일 , 코덱 , fps, 크기

# 코너 검출

while True:
    grabbed_frame, frame = vidcap.read()
    if frame is None:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    dst = cv2.cornerHarris(gray, 2, 3, 0.05)

    dst = cv2.dilate(dst, None, iterations=2)
    frame[dst > 0.01 * dst.max()] = [0, 0, 255]

    frame = cv2.resize(frame, (w, h))  # 영상 사이즈 재정의 하지 않으면 출력
    writer.write(frame)

    cv2.imshow('Frame', frame)
    key = cv2.waitKey(5)
    if key == 27:
        break

vidcap.release()
writer.release()