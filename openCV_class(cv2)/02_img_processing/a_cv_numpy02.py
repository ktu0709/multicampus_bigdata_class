import numpy as np
import cv2

# 이미지 시각화 사용자 함수
def show_image(img, title="Image"):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# np.zeros() - 검은색 이미지 생성
zeros_img = np.zeros((300, 300), dtype=np.uint8)
show_image(zeros_img, "Zeros Image")

# np.ones() - 어두운 회색 이미지 생성
ones_img = np.ones((300, 300), dtype=np.uint8) * 255
show_image(ones_img, "Ones Image")

# np.full() - 밝은 회색 이미지 생성
full_img = np.full((300, 300), 200, dtype=np.uint8)
show_image(full_img, "Full Image")

# np.eye() - 대각선 흰색 선 이미지 생성
eye_img = np.eye(300, 300, dtype=np.uint8) * 255
show_image(eye_img, "Eye Image")

flipped_eye_array = np.fliplr(eye_img)
show_image(flipped_eye_array, "flipped_eye_array")

combined_img  = np.hstack(( eye_img, flipped_eye_array         ))
show_image(combined_img, "combined_img")

# np.linspace() - 그라데이션 이미지 생성
linspace_img = np.linspace(0, 255, 300, dtype=np.uint8)
linspace_img = np.tile(linspace_img, (300, 1))
show_image(linspace_img, "Linspace Image")



# np.arange() - 줄무늬 이미지 생성
arange_img = (np.arange(300*300) % 255).reshape(300, 300).astype(np.uint8)
show_image(arange_img, "Arange Image")
