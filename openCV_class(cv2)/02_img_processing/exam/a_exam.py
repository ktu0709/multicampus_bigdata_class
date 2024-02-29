import numpy as np
import cv2

red_img = np.zeros((200,200,3),dtype=np.uint8)

red_img[0:50,:] = [0,0,255]

cv2.imwrite('img_res.jpg',red_img)

cv2.imshow("img_res.jpg",red_img)
cv2.waitKey(0)
cv2.destroyAllWindows()