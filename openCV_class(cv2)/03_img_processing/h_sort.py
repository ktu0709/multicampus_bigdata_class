import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

 # 로봇 공정  : 시스템 판별 그래프 ( 불량시스템 탐지 속에 각 대상의 불량품 추출  )
 # 전기료 확인
def show(im):
    # 0: 행 기준 정렬, 1: 열 기준 정렬
    # cv.SORT_EVERY_ROW: 각 행을 개별적으로 정렬
    # cv.SORT_EVERY_COLUMN: 각 열을 개별적으로 정렬
    # cv.SORT_ASCENDING: 오름차순 정렬
    # cv.SORT_DESCENDING: 내림차순 정렬

    row_sort = cv.sort(im, 0, cv.SORT_EVERY_ROW + cv.SORT_ASCENDING)
    col_sort = cv.sort(im, 1, cv.SORT_EVERY_COLUMN + cv.SORT_ASCENDING)

    plt.subplot(131), plt.imshow(im, cmap='gray'), plt.title('Original')
    plt.subplot(132), plt.imshow(row_sort, cmap='gray'), plt.title('Row Sort')
    plt.subplot(133), plt.imshow(col_sort, cmap='gray'), plt.title('Col Sort')
    plt.show()


def show02():
    im = cv.imread('../img/Lenna.png', cv.IMREAD_GRAYSCALE)
    if im is not None:
        show(im)
    else:
        print("Could not read image.")



test_im = np.random.randint(0, 256, (100, 100), dtype=np.uint8)

show(test_im)
show02()
