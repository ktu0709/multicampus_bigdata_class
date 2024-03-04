import cv2 as cv
import numpy as np
SZ=20
bin_n = 16 # Number of bins
affine_flags = cv.WARP_INVERSE_MAP|cv.INTER_LINEAR

# 이미지를  숫자의 위치나 각도의 차이를 줄여서 비스듬히 정렬 시킨다.
def deskew(img):
    m = cv.moments(img)
    if abs(m['mu02']) < 1e-2:
        return img.copy()
    skew = m['mu11']/m['mu02']
    M = np.float32([[1, skew, -0.5*SZ*skew], [0, 1, 0]])
    img = cv.warpAffine(img,M,(SZ, SZ),flags=affine_flags)
    return img

# HOG 특징 추출  : 이미지 내부에 그래디언트 방향을 히스토그램으로 표현
def hog(img):
    gx = cv.Sobel(img, cv.CV_32F, 1, 0)   #x,y방향으로  그래디언트 계산
    gy = cv.Sobel(img, cv.CV_32F, 0, 1)

    mag, ang = cv.cartToPolar(gx, gy)
    #각도로 양자화 bin_n   = 16
    bins = np.int32(bin_n*ang/(2*np.pi))    # quantizing binvalues in (0...16)

    # 셀분할 : 이미지를 4개의 셀로 분할하고, 각셀에 대한 그라디언트 방향(bins)과 mag를 분리한다.
    bin_cells = bins[:10,:10], bins[10:,:10], bins[:10,10:], bins[10:,10:]
    mag_cells = mag[:10,:10], mag[10:,:10], mag[:10,10:], mag[10:,10:]
    #  셀분할 영역의  그라디언트 방향의 히스토그램을 계산 함
    # mag_cells  :  히스토그램 가중치
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    # 4개의 셀을 병합
    hist = np.hstack(hists)     # hist is a 64 bit vector
    return hist   # 64차원의 HOG 특징벡터를 계산 후 리턴

img = cv.imread(cv.samples.findFile('img/digit0.jpg'),0)
if img is None:
    raise Exception("we need the digits.png image from samples/data here !")

new_height = (img.shape[0] // 50) * 50
new_width = (img.shape[1] // 100) * 100
img = cv.resize(img, (new_width, new_height))

# 이미지를 로드해서 50*100 셀로 분할 후  , 훈련데이터와 테스트 데이터로 사용
cells = [np.hsplit(row,100) for row in np.vsplit(img,50)]
# First half is trainData, remaining is testData
train_cells = [ i[:50] for i in cells ]
test_cells = [ i[50:] for i in cells]

deskewed = [list(map(deskew,row)) for row in train_cells] # 이미지 왜곡함수 호출 결과
hogdata = [list(map(hog,row)) for row in deskewed]  # Hog적용 한 결과
print(deskewed)
print(hogdata)
print('=================================')

trainData = np.float32(hogdata).reshape(-1,64)
responses = np.repeat(np.arange(10),250)[:,np.newaxis]

svm = cv.ml.SVM_create()
svm.setKernel(cv.ml.SVM_LINEAR)  # 선형 커널 : 두벡터 사이의 단순한 내적
svm.setType(cv.ml.SVM_C_SVC)  # 분류
svm.setC(2.67) # 오분류 값 지정
#svm.setGamma(5.383)   # RBF(Radial Basis Function), 다항식 등의 비선형 커널에 사용됨
#학습
svm.trainAuto(trainData, cv.ml.ROW_SAMPLE, responses )
svm.save('svm_data.dat')
deskewed = [list(map(deskew,row)) for row in test_cells]
hogdata = [list(map(hog,row)) for row in deskewed]
testData = np.float32(hogdata).reshape(-1,bin_n*4)
#예측
result = svm.predict(testData)[1]

#성능 측정
mask = result==responses
correct = np.count_nonzero(mask)
print(correct*100.0/result.size)