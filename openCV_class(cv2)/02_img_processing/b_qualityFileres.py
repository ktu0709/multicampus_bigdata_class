import os
import cv2

image_dir = 'img_res/'
files = os.listdir(image_dir)

# 이미지 파일만 골라내기
image_files = [f     for f in files  if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')]


# 각 이미지 파일의 정보를 출력합니다.
for image_file in image_files:
    img = cv2.imread(os.path.join(image_dir, image_file))
    # 파일 크기 구하기 (바이트 단위)
    file_size = os.path.getsize(os.path.join(image_dir, image_file))
    print(f"=== {image_file} ===")
    print(f"File Size: {file_size} bytes")
    print(f"Shape: {img.shape}")
    print(f"Data Type: {img.dtype}")
    print("-----------------------")
