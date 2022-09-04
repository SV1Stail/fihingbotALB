import cv2

img= cv2.imread("images/fishing.jpg")
img=cv2.resize(img,(img.shape[1]//3,img.shape[0]//3))
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("fishing",img)


print(img.shape)

cv2.waitKey(0)