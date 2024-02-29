import cv2

img = cv2.imread('../img/bg.jpg')

# 원점(150,150), 반지름 100
cv2.circle(img, (150, 150), 100, (255,0,0))


cv2.circle(img, (300, 150), 70, (0,200,0))


cv2.ellipse(img,(50,300),(50,50),0,181,360,(0,0,200))
cv2.ellipse(img,(200,300),(50,50),15,0,360,(0,0,100))

'''
void cv::ellipse	(	InputOutputArray 	img,
Point 	center,
Size 	axes,
double 	angle,
double 	startAngle,
double 	endAngle,
const Scalar & 	color,
int 	thickness = 1,
int 	lineType = LINE_8,
int 	shift = 0 
)	
'''


cv2.imshow('circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()