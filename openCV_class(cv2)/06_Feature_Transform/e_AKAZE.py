import cv2
import matplotlib.pyplot as plt

def load_images(img_path1, img_path2):
    return cv2.imread(img_path1, 0), cv2.imread(img_path2, 0)

def compute_akaze_features(img):
    akaze = cv2.AKAZE_create() #비선형 공간 스케일링을 목적으로
    return akaze.detectAndCompute(img, None)

def match_features(des1, des2):  # 매칭 확인
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)  # 템플릿 매칭 메소드 / FLANN등
    matches = bf.match(des1, des2)
    return sorted(matches, key=lambda x: x.distance)

def draw_matches(img1, kp1, img2, kp2, matches):
    return cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=2)

def show_image(img):
    plt.figure(figsize=(15, 15))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('AKAZE Feature Matching')
    plt.axis('off')
    plt.show()

def main():
    img1, img2 = load_images("img/kim.png", "img/kim_90.png")
    print("img1 shape:", img1.shape)
    print("img2 shape:", img2.shape)

    kp1, des1 = compute_akaze_features(img1)
    kp2, des2 = compute_akaze_features(img2)
    matches = match_features(des1, des2)
    img_matches = draw_matches(img1, kp1, img2, kp2, matches[:10])
    show_image(img_matches)

    print("Number of matches:", len(matches))
    print("First match:", matches[0])
    print("Distances:")
    for i in matches:
        print(i.distance)

if __name__ == "__main__":
    main()
