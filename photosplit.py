import libraries
np=libraries.np
cv2=libraries.cv2

img = cv2.imread("images/fishing.jpg")
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
b = cv2.split(img) #разделения на слоя



#img = cv2.merge([r,b,g])
cv2.imshow("result",img)
cv2.waitKey(0)



