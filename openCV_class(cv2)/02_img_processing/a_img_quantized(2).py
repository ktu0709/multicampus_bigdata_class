import cv2
import numpy as np
import matplotlib.pyplot as plt

#양자화 -> 색상 감소화 -> 이미지 파일 크기 축소 [노이즈 감소 확인 : 경계선 확인]
# --> 양자화를 통해 생성된 제한된 색상 집합은 색상 팔레트로 사용되며 웹 , 그래픽 , 게임 개발에 사용된다
#<<양자화 후 저장된 파일의 크기, 색상정보 등을 파일로 저장 후 출력 >>

# 이미지 로드 및 그레이스케일로 변환
img = cv2.imread('../../img/apple.jpg', cv2.IMREAD_GRAYSCALE)

# 균일 양자화  : 모든 픽셀을 같은 간격( 64)
# np.floor() 결과값 소수점아래 버림
uniform_quantized = np.floor(img / 64) * 64     # 모든 픽셀을   64

# 비균일 양자화 (예: 로그 양자화)
#Scaling factor = 255/log(1+255) ≈ 46.62
#  작은 픽셀은 더 작고 촘촘하게 양자화가 되고 , 큰픽셀은 더 크고 넓은 간격으로 양자화가 된다.
# - 46.62를 곱해서 0 ~ 255 범위에 맞게 조정하기 위함

#  - << 로그 함수를 적용하게 되면 값들이 0에 가까운 실수값으로 변환>>
#  최대픽셀값 255  -> 로그함수  -> 255
non_uniform_quantized = np.log1p(img) * 46.62  # log1p 함수는 log(1+x)를 계산
non_uniform_quantized = np.uint8(non_uniform_quantized)

# 그래프 그리기
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
images = [img, uniform_quantized, non_uniform_quantized]
titles = ['Original', 'Uniform Quantization', 'Non-Uniform Quantization']

for ax, img, title in zip(axes, images, titles):
    ax.imshow(img, cmap='gray')
    ax.set_title(title)
    ax.axis('off')
plt.show()
