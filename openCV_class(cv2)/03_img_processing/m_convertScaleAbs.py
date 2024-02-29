import cv2
import matplotlib.pyplot  as plt

# 이미지 로드
image = cv2.imread('../img/apple.jpg', cv2.IMREAD_GRAYSCALE)

# 이미지 처리
img1 = cv2.convertScaleAbs(image, alpha=1.2, beta=0)   # 밝기 조절
img2 = cv2.convertScaleAbs(image, alpha=1, beta=100)    # 대비 조절
img3 = cv2.GaussianBlur(image, (5, 5), 0)   # 가우시안 블러

# 이미지들과 타이틀 리스트 생성
images = [image, img1, img2, img3]
titles = ['Original', 'Brightness Adjusted', 'Contrast Adjusted', 'Gaussian Blur']

# 시각화
plt.figure(figsize=(5, 5))

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
