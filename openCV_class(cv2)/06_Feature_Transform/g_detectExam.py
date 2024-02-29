import cv2
import numpy as np
def detect_and_draw_keypoints(image_path):

    image = cv2.imread(image_path, 0)
    detectors = {
        'SIFT': cv2.SIFT_create(nfeatures=5),
        'ORB': cv2.ORB_create(),
        'FAST': cv2.FastFeatureDetector_create()
    }

    for name, detector in detectors.items():
        if name == 'FAST':
            keypoints = detector.detect(image, None)[:5]
        else:
            keypoints = detector.detect(image, None)

        keypoint_image = cv2.drawKeypoints(image, keypoints, None)
        cv2.imshow(f"{name} Keypoints", keypoint_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = "img/apple.jpg"
detect_and_draw_keypoints(image_path)

