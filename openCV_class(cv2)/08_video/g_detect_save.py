from moviepy.editor import VideoFileClip
import cv2
import numpy as np
import wave #속성값에 메소드로 리턴받고 싶을 때 사용 / 오디오 파일
import pandas as pd  #데이터의 내용을 표로 만들어서 sql 조건 구문을 편하게 사용한다.
# 소리 추출 -> 특징추출  MFCC 스펙트롬 추출
#   시간처리 도메인 추출  / 비트 ,템포  / 고주파, 저주파값
def extract_audio(video_filename, audio_filename):
    clip = VideoFileClip(video_filename)
    clip.audio.write_audiofile(audio_filename)

    with wave.open(audio_filename, 'r') as wav_file:
        framerate = wav_file.getframerate() # 초당 샘플수
        nframes = wav_file.getnframes()  #전체 샘플수
        duration = nframes / float(framerate)  #전체길이를  초단위로 리턴

    audio_features = {
        "framerate": framerate,
        "nframes": nframes,
        "duration": duration
    }

    audio_df = pd.DataFrame([audio_features])
    audio_df.to_csv('audio_features.csv', index=False)


# 해리스 코너 추출
def extract_harris_corners(video_filename):
    cap = cv2.VideoCapture(video_filename)

    harris_data = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)

        dst = cv2.cornerHarris(gray, 2, 3, 0.04)
        corners = np.argwhere(dst > 0.01 * dst.max())

        for corner in corners:
            y, x = corner
            harris_data.append({"x": x, "y": y})

    harris_df = pd.DataFrame(harris_data)
    harris_df.to_csv('harris_corners.csv', index=False)

    cap.release()
    cv2.destroyAllWindows()


# 소리를 'audio_only.wav'로 추출
extract_audio('img/people_dancing.mp4', 'img/audio_only.wav')

# 해리스 코너를 추출하여 CSV 파일로 저장
extract_harris_corners('img/people_dancing.mp4')
