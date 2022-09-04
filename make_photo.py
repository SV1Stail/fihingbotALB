from pickletools import uint8
import libraries
np=libraries.np
cv2=libraries.cv2

photo = np.zeros((720,1280,3), dtype="uint8")


#bgr = blue, green, red
#photo[:]=50,60,30
cv2.rectangle(photo,(10,10),(200,200),(10,100,50),thickness=3)
cv2.putText(photo, "в работе", (20,40),cv2.FONT_HERSHEY_COMPLEX,1,(110,50,20), 2)

cv2.imshow("photo", photo)
cv2.waitKey(0)
