from pickletools import uint8
import libraries
np=libraries.np
cv2=libraries.cv2




img = cv2.imread("images/fishing.jpg")
new_image= np.zeros(img.shape,dtype="uint8") #массив из чёрных точек по размеру исходного изображения

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #перекрасил изображение в серый цвет
img=cv2.GaussianBlur(img, (3,3),0)#размытие
img=cv2.Canny(img, 60, 80)#выделил края
#
contur, ierarhia = cv2.findContours(img, cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)#вытащил точки контуров и их иерархию

cv2.drawContours(new_image,contur,-1, (0,255,255), 1)#создал новое изображение на чёрном фоне по точкам контуров

cv2.imshow("result",new_image)#вывел изображение
cv2.waitKey(0)#изображеине показано бесконечно пока процесс не будет прерван
