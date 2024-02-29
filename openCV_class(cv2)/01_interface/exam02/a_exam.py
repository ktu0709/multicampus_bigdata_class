#1.레나이미지를  컬러로 로드 한다  def load_image():
#2.그레이스케일로 색 공간을 변경 후  g_lenna.png로 저장한다.  def convert_to_grayscale():
#3.cv2의 resize()를 활용해서 200*200 으로 변경 후  r_lenna.png로  저장한다. def resize_and_save():
#4.트랙바를 사용해서 밝기를 조정한다.  def adjust_brightness(x):
import cv2
import numpy as np

# 이미지 로드 함수
def load_image():
    #pass
    global img
    img = cv2.imread('../../img/Lenna.png')
    return img

# 그레이스케일로 변경 및 저장 함수
def convert_to_grayscale():
    #pass
    resize_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 그레이 스케일로 읽기  =  회색조
    cv2.imwrite('g_lenna.png',resize_img)

# 이미지 리사이즈 및 저장 함수
def resize_and_save():
   #pass
   img_file = "../../img/Lenna.png"
   img = cv2.imread(img_file,-1)
   img = cv2.resize(img, [200, 200])
   cv2.imwrite('r_lenna.png', img)

# 밝기 조정 콜백 함수
def adjust_brightness(x):
   #pass
   brightness = cv2.getTrackbarPos('Brightness','image')-50
   adjust = np.clip(img+brightness,0,255).astype(np.uint8)
   cv2.imshow('image',adjust)



if __name__ == '__main__':
    #img = cv2.imread('../../img/Lenna.png')  # 레나 이미지 로드
    img = load_image()
    cv2.imshow('image', img)

    convert_to_grayscale()
    resize_and_save()

    # 트랙바 생성
    cv2.createTrackbar('Brightness', 'image', 50, 100, adjust_brightness)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
