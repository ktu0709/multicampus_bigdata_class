import cv2
import numpy as np

#https://docs.opencv.org/4.9.0/db/d39/classcv_1_1DescriptorMatcher.html
#BFMatcher  :  특징이 얼마나 유사한지를 확인 -> 두 이미지의 특징점이 무차별 대입 방식 [임계값 없다]
#FLANN : 최근접 이웃 탐색 알고리즘을 사용 -> 무작위 트리 기반

# 이미지를 읽어온다.
img1 = cv2.imread('img/apple.jpg', cv2.IMREAD_GRAYSCALE)  # 원본 이미지
img2 = cv2.imread('img/apples.jpg', cv2.IMREAD_GRAYSCALE)  # 비교 대상 이미지

# ORB 디텍터를 생성한다.
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

index_params =dict(algorithm = None)
search_params =dict(checks = 50)

fl = cv2.FlannBasedMatcher(index_params, search_params)

des1 = des1.astype(np.float32)
des2 = des2.astype(np.float32)


matches = fl.knnMatch(des1,des2,k=2)
print(matches)

'''
for i,(m,n) in enumerate(matches):
    print(f'매칭 페어 {i}')
    print(f'첫번째 매칭 (m) - {m.distance} {m.imgIdx} {m.queryIdx} {m.trainIdx}')
    print(f'두번째 매칭 (n) - {n.distance} {n.imgIdx} {n.queryIdx} {n.trainIdx}')
'''

good_match =[]
for m,n in matches:
    if m.distance < 0.75 * n.distance:
        good_match.append(m)


# 매칭 결과를 그린다. 두이미지 사이에 매칭된 키포인트를 하나의 이미지에 나란히 표시하여 그리는 메소드
img3 = cv2.drawMatches(img1, kp1, 
                       img2, kp2, 
                       good_match,  #DMatch 객체의 리스트 : 일반적인 매칭 알고리즘 BFMatcher , FLANN 사용
                       None, 
                       flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# 결과를 출력한다.
cv2.imshow('Feature Matching', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
