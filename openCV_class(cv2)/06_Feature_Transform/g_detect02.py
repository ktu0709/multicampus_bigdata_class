import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = "img/kim.png"
image = cv2.imread(image_path, 0)

# SIFT
sift = cv2.SIFT_create(nfeatures=5)
keypoints_sift = sift.detect(image, None)



# ORB
orb = cv2.ORB_create()
keypoints_orb = orb.detect(image, None)


# FAST
fast = cv2.FastFeatureDetector_create()
keypoints_fast = fast.detect(image, None)[:5]

img_sift = cv2.drawKeypoints(image, keypoints_sift, None, flags=4)
plt.imshow(cv2.cvtColor(img_sift, cv2.COLOR_BGR2RGB))
plt.title('SIFT')
plt.axis('off')
plt.show()


img_sift = cv2.drawKeypoints(image, keypoints_orb, None, flags=4)
plt.imshow(cv2.cvtColor(img_sift, cv2.COLOR_BGR2RGB))
plt.title('ORB')
plt.axis('off')
plt.show()

img_sift = cv2.drawKeypoints(image, keypoints_fast, None, flags=4)
plt.imshow(cv2.cvtColor(img_sift, cv2.COLOR_BGR2RGB))
plt.title('FAST')
plt.axis('off')
plt.show()