'''
2. 이미지 회전과 상하 좌우 반전

회전 : cv.rotate(ndarray , rotate_code) , np.rot90()

상하 좌우 반전 : cv.flip(ndarray , flip_code) , np.flip()
                 flip_code=0 상하 반전 ,    flip_code > 0  좌우 반전  ,flip_code< 0
'''
# 이미지 회전을 해보자.
import cv2 as cv
import matplotlib.pyplot as plt

# 이미지 불러오기
image = cv.imread('../img/Lenna.png')
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # OpenCV는 BGR을 사용하므로 RGB로 변환

# 회전된 이미지 생성
rotate_90_clockwise = cv.rotate(image_rgb, cv.ROTATE_90_CLOCKWISE)
rotate_180 = cv.rotate(image_rgb, cv.ROTATE_180)
rotate_90_counterclockwise = cv.rotate(image_rgb, cv.ROTATE_90_COUNTERCLOCKWISE)

# 이미지와 제목을 튜플로 묶어 배열로 저장
images = [
    (image_rgb, "Original"),
    (rotate_90_clockwise, "Rotate 90 Clockwise"),
    (rotate_180, "Rotate 180"),
    (rotate_90_counterclockwise, "Rotate 90 Counterclockwise")
]

fig, axes = plt.subplots(1, len(images), figsize=(20, 5))

# 배열을 순회하며 이미지와 제목을 설정
for ax, (img, title) in zip(axes, images):
    ax.imshow(img)
    ax.set_title(title)
    ax.axis('off')

plt.show()
