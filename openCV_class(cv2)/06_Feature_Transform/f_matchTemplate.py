import cv2
import numpy as np
from matplotlib import pyplot as plt

def match_and_draw_boxes(img, templ, threshold=0.9):
    # 템플릿 매칭 수행
    result = cv2.matchTemplate(img, templ, cv2.TM_CCOEFF_NORMED)
    #각 픽셀위치의 유사도 (정규화된 상관관계 결과값)
    print(result,  threshold)
    # 유사도가 threshold 이상인 위치와 점수를 리턴
    positions = np.where(result >= threshold)
    print(f'cv2.minMaxLoc(result)={cv2.minMaxLoc(result)}') #자동 최대값 및 해당위치 (최적의 매칭위치)
    scores = result[positions]


    # Bounding box 좌표 계산 (x1, y1, x2, y2)
    boxes = []
    h, w = templ.shape[:2]
    for y, x in zip(*positions):
        boxes.append([x, y, x + w - 1, y + h - 1])
    boxes = np.array(boxes)

    # Bounding box 그리기
    draw_boxes(img, boxes)

def draw_boxes(img, boxes):
    dst = img.copy()
    for x1, y1, x2, y2 in boxes:
        cv2.rectangle(dst, (x1, y1), (x2, y2), color=(255, 0, 0), thickness=2)
    plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
    print("Number of boxes:", len(boxes))
    plt.show()

if __name__ == '__main__':
    img = cv2.imread("img/puppy.jpg")
    templ = cv2.imread("img/sample_puppy.jpg")
    match_and_draw_boxes(img, templ)
