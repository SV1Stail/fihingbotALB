from pickletools import uint8
from turtle import circle
import libraries
np=libraries.np
cv2=libraries.cv2

img_clear = np.zeros((350,350), dtype="uint8")

circle=cv2.circle(img_clear.copy(),(0,0),50,255,-1)
square = cv2.rectangle(img_clear.copy(),(25,25),(250,300), 255,-1)
img_clear=cv2.bitwise_xor(square,circle)

cv2.imshow("result",img_clear)
cv2.waitKey(0)


