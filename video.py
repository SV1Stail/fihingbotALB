from ast import If
from socket import if_indextoname
from tkinter import Image
import cv2

cap = cv2.VideoCapture("video/cars.m4v")

while True :
    success, image = cap.read()
    cv2.imshow("cars", image)
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break