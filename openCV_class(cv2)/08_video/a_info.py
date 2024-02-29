import cv2
cap = cv2.VideoCapture(0)
# 비디오의 기본 정보를 리턴
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# 기본 정보를 출력
print(f'Width: {width}')
print(f'Height: {height}')
print(f'Frames Per Second: {fps}')
print(f'Total Frames: {total_frames}')

# 동영상의 총 길이를 계산, 출력
total_duration = total_frames / fps
print(f'Total Duration: {total_duration:.2f} seconds')


cap.release()
