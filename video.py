from pickletools import uint8
import libraries
np=libraries.np
cv2=libraries.cv2

cap = cv2.VideoCapture("video/cars.m4v")

while True :
    success, image = cap.read()
    image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image=cv2.Canny(image, 150,150)


    cv2.imshow("cars", image)



    if cv2.waitKey(30) & 0xFF==ord("q"):
        break