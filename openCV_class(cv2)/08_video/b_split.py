import cv2

# 주어진 영상을  5초 단위로 분할해서 파일로 저장하고 싶다.
def split_video_into_intervals(input_filename, interval=5):
    cap = cv2.VideoCapture(input_filename)

    # 비디오의 총 프레임 수와 초당 프레임 수(fps) 리턴
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # 코덱과 VideoWriter 객체를 설정
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # 각 분할된 비디오의 프레임 범위를 계산
    frames_per_interval = fps * interval
    intervals = total_frames // frames_per_interval

    for i in range(intervals):
        output_filename = f"res_mp4/split_{i+1}.mp4"
        out =cv2.VideoWriter(output_filename, fourcc, fps, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                                           int(cap.get(4))))

        for j in range(frames_per_interval):
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)

        out.release()

    cap.release()

# 5초 단위로 'people_dancing.mp4' 비디오를 분할
split_video_into_intervals('img/people_dancing.mp4', 5)
