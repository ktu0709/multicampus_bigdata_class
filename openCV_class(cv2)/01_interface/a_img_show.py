import cv2  as cv

img_file = "../img/apple.jpg"
img = cv.imread(img_file,-1) #컬러로 읽어서 해당 속성의 숫자 크기로 리턴
r_img = cv.cvtColor(img,cv.COLOR_GRAY2RGB)


h,w = img.shape
r_h,r_w,r_ch = r_img.shape


print(h,w)
print(r_h,r_w,r_ch)



if img is not None:
  cv.imshow('MyImg', img) #이미지보기
  cv.imshow('RImg', r_img)

  cv.waitKey() # 대기
  #cv.destroyAllWindows() # 모든 리소스 해제
else:
    print('No image file.')
    