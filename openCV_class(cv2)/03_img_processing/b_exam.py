import cv2

image = cv2.imread('../img/apple.jpg')
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

M = cv2.getRotationMatrix2D(center, 45, 1.0)
#회전, 이동, 크기조절, 기울기
rotated_image = cv2.warpAffine(image, M, (w, h))

while True:
    cv2.imshow('Tiled Image', rotated_image)
    if cv2.waitKey(1) & 0xFF  == ord('q'):
        break

cv2.destroyAllWindows()