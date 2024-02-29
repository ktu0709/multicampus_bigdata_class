import cv2

img_file = "../img/apple.jpg"
save_file = '../img/apple_gray.jpg'

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  #그레이 스케일로 로드
cv2.imshow(img_file, img)  # 회색이미지 결과를 보여줌

cv2.imwrite(save_file, img) #파일로 저장, 포맷은 확장에 따름
cv2.waitKey()

#  apple.jpg   -> apple02.jpg     :  사과이미지를 읽어서  apple02.jpg로 저장
img = cv2.imread(img_file, 1)  #  -> Mat | ndarray[Any, dtype[generic]] | ndarray
cv2.imwrite("../img/apple02.jpg", img)

print(  img , type(img), type ( img_file ))


#cv2.destroyAllWindows()
