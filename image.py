import libraries
np=libraries.np
cv2=libraries.cv2

img= cv2.imread("images/fishing.jpg")
img=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img=cv2.Canny(img,50,50)
matritsa=np.ones((5,5), np.uint0)


cv2.imshow("fishing",img)


print(img.shape)

cv2.waitKey(0)