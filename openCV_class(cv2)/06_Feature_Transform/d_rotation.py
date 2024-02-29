import cv2
import numpy as np

def rotate_with_cv2_rotate(image_path, save_path):
    img = cv2.imread(image_path)
    rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  #주어진 각도만큼 이미지 회전
    cv2.imwrite(save_path, rotated_img)


def rotate_with_cv2_warpAffine(image_path, save_path):
    img = cv2.imread(image_path)
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 90, 0.5) # 회전중심, 각도, 스케일
    rotated_img = cv2.warpAffine(img, M, (w, h)) # 회전 행렬을 기준으로 회전,
    cv2.imwrite(save_path, rotated_img)

if __name__ == '__main__':
    # 함수 호출 예
    rotate_with_cv2_rotate('img/kim.png', 'img/kim_90.png')
    rotate_with_cv2_warpAffine('img/kim.png', 'img/kim_90_warpAffine.png')
