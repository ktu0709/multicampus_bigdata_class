'''
cv2.flip() 함수를 사용하여 이미지를 수평, 수직, 또는 양방향으로 뒤집을 수 있습니다.
이 함수는 뒤집기 코드를 인자로 받으며, 수평 뒤집기는 1, 수직 뒤집기는 0, 그리고 양방향 뒤집기는 -1입니다
'''
import cv2 as cv
import matplotlib.pyplot as plt

# 이미지 불러오기
image = cv.imread('../img/Lenna.png')
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # OpenCV는 BGR을 사용하므로 RGB로 변환

# 뒤집힌 이미지 생성
flip_horizontal = cv.flip(image_rgb, 1)
flip_vertical = cv.flip(image_rgb, 0)
flip_both = cv.flip(image_rgb, -1)

# Matplotlib을 사용하여 이미지 출력
fig, axes = plt.subplots(1, 4, figsize=(10, 5))

axes[0].imshow(image_rgb)
axes[0].set_title("Original")
axes[0].axis('off')

axes[1].imshow(flip_horizontal)
axes[1].set_title("Flip Horizontal")
axes[1].axis('off')

axes[2].imshow(flip_vertical)
axes[2].set_title("Flip Vertical")
axes[2].axis('off')

axes[3].imshow(flip_both)
axes[3].set_title("Flip Both")
axes[3].axis('off')

plt.show()
