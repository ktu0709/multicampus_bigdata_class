import cv2
import numpy as np
from matplotlib import pyplot as plt

filename = 'img/house_01.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


configs = [
    {"maxCorners": 4, "qualityLevel": 0.01, "minDistance": 10},
    {"maxCorners": 10, "qualityLevel": 0.01, "minDistance": 200},
    {"maxCorners": 100, "qualityLevel": 0.1, "minDistance": 10}
]

plt.figure(figsize=(15, 5))

for i, config in enumerate(configs):
    temp_img = img.copy()
    corners = cv2.goodFeaturesToTrack(
        gray, 
        maxCorners=config['maxCorners'], 
        qualityLevel=config['qualityLevel'], 
        minDistance=config['minDistance']
    )
    corners = np.int0(corners)
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(temp_img, (x, y), 5, [0, 0, 255], -1)

    plt.subplot(1, len(configs), i+1)
    plt.imshow(cv2.cvtColor(temp_img, cv2.COLOR_BGR2RGB))
    plt.title(f"maxCorners: {config['maxCorners']}, qualityLevel: {config['qualityLevel']}, minDistance: {config['minDistance']}")

plt.show()
