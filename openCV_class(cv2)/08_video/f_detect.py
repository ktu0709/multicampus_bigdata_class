from moviepy.editor import VideoFileClip
import cv2
import numpy as np


def extract_audio(video_filename, audio_filename):
    clip = VideoFileClip(video_filename)
    clip.audio.write_audiofile(audio_filename)


def extract_harris_corners(video_filename):
    cap = cv2.VideoCapture(video_filename)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)

        dst = cv2.cornerHarris(gray, 2, 3, 0.04)
        frame[dst > 0.01 * dst.max()] = [0, 0, 255]

        cv2.imshow('Harris Corners', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# 소리를 'audio_only.wav'로 추출
#extract_audio('people_dancing.mp4', 'audio_only.wav')

# 해리스 코너를 추출하여 화면에 표시
extract_harris_corners('img/people.mp4')

