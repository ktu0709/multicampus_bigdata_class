from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import moviepy.video.fx.all as vfx
def merge_videos(video_folder):
    video_files = [f for f in sorted(os.listdir(video_folder)) if f.endswith(".mp4")]
    if len(video_files) == 0:
        print("No video files found in the folder.")
        return

    clips = []
    for video_file in video_files:
        vf = VideoFileClip(os.path.join(video_folder, video_file))
        vf = vf.fx(vfx.resize,width=200  )  #길이조정
        clips.append(vf)

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("res_mp4/merged_video.mp4", codec="libx264" , fps=30) #코덱, 프레임 조정

# 'res_mp4' 폴더 안의 비디오 파일을 병합
merge_videos('res_mp4')
