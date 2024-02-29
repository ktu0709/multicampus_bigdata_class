import cv2

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

# BFMatcher 객체를 생성하고, 키포인트 간의 거리를 측정한다.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)


# 디스크립터 간의 매칭을 수행한다.
matches = bf.match(des1, des2)

# 매칭 결과를 거리에 따라 정렬한다.
matches = sorted(matches, key = lambda x:x.distance)

# 매칭 결과를 그린다. 두이미지 사이에 매칭된 키포인트를 하나의 이미지에 나란히 표시하여 그리는 메소드
img3 = cv2.drawMatches(img1, kp1, 
                       img2, kp2, 
                       matches[:10],  #DMatch 객체의 리스트 : 일반적인 매칭 알고리즘 BFMatcher , FLANN 사용
                       None, 
                       flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# 결과를 출력한다.
cv2.imshow('Feature Matching', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
