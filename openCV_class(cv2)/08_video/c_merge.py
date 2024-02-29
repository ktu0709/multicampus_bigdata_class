import cv2
import os


def merge_videos(video_folder):
    video_files = [f for f in sorted(os.listdir(video_folder))  if f.endswith(".mp4")]
    if len(video_files) == 0:
        print("No video files found in the folder.")
        return

    # 첫 번째 비디오 파일을 사용하여 fps와 frame size를 리턴
    sample = cv2.VideoCapture(os.path.join(video_folder, video_files[0]))
    fps = int(sample.get(cv2.CAP_PROP_FPS))
    frame_size = (int(sample.get(cv2.CAP_PROP_FRAME_WIDTH)), int(sample.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    # 병합된 비디오를 저장할 VideoWriter 객체를 생성
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('res_mp4/merged_video.mp4', fourcc, fps, frame_size)

    for video_file in video_files:
        cap = cv2.VideoCapture(os.path.join(video_folder, video_file))

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)

        cap.release()

    out.release()


# 'res_mp4' 폴더 안의 비디오 파일을 병합
merge_videos('res_mp4')
