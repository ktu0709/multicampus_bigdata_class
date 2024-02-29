import cv2      #  설치된 cv2 모듈을  참조하겠다.

img_file = "../img/apple.jpg"
img = cv2.imread(img_file,cv2.IMREAD_REDUCED_COLOR_2) #그레이 스케일로 읽기  =  회색조

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    #cv2.destroyAllWindows()
else:
    print('No image file.')
    