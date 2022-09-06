import libraries
np=libraries.np
cv2=libraries.cv2

img = cv2.imread("images/fishing.jpg")

b,g,r = cv2.split(img)



img = cv2.merge([r,b,g])
cv2.imshow("result",img)
cv2.waitKey(0)



