from moviepy.editor import VideoFileClip


def separate_audio_and_video(video_filename):
    clip = VideoFileClip(video_filename)

    # 비디오만 있는 새 파일 생성
    clip.without_audio().write_videofile("res_mp4/video_only.mp4")

    # 오디오만 있는 새 파일 생성
    clip.audio.write_audiofile("res_mp4/audio_only.wav")


# 'people_dancing.mp4' 파일에서 영상과 소리를 분리
separate_audio_and_video("img/people_dancing.mp4")


'''
C:\pywork\myenv\Scripts\python.exe C:\pywork\CV32\08_video\e_img_wave_split.py 
Moviepy - Building video res_mp4/video_only.mp4.
Moviepy - Writing video res_mp4/video_only.mp4
시간 진행률         현재프레임/전체프레임    [현재진행시간 < 필요한시간 , 초당 9.75프레임  , 현재 추가정보 없다.]
t:  61%|██████▏   | 447/727            [01:10<00:28,            9.75it/s,         now=None]

'''