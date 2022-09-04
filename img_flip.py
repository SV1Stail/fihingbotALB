
import libraries
np=libraries.np
cv2=libraries.cv2

img = cv2.imread("images/fishing.jpg")
def rotate (img_param, angle):
    height, width=img_param.shape[:2]
    point= (width//2,height//2)

    matritsa = cv2.getRotationMatrix2D(point,angle,1) #в этой строке происходит вращение
    return cv2.warpAffine(img_param, matritsa, (height,width))

def move(img_param, x, y):
    matirtsa2=np.float32([1,0,x],[0,1,y])
    return cv2.warpAffine(img_param,matirtsa2, (img_param.shape(1),img_param.shape(0)))
img =rotate(img,30 )

cv2.imshow("result", img)
cv2.waitKey(0)
