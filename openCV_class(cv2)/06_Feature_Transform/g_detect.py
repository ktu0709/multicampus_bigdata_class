import cv2
import numpy as np


image_path = "img/kim.png"
image = cv2.imread(image_path, 0)

# SIFT
sift = cv2.SIFT_create(nfeatures=5)
keypoints_sift = sift.detect(image, None)
with open("img/sift_features.txt", "w") as f:
    for point in keypoints_sift:
        f.write(str(point.pt) + "\n")

# ORB
orb = cv2.ORB_create()
keypoints_orb = orb.detect(image, None)
with open("img/orb_features.txt", "w") as f:
    for point in keypoints_orb:
        f.write(str(point.pt) + "\n")

# FAST
fast = cv2.FastFeatureDetector_create()
keypoints_fast = fast.detect(image, None)[:5]
with open("img/fast_features.txt", "w") as f:
    for point in keypoints_fast:
        f.write(str(point.pt) + "\n")
