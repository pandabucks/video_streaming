import socket
import numpy as np
import cv2
import time

cam = cv2.VideoCapture(0)

while (True):
    # getting 1 frame
    flag, img = cam.read()
    if not flag:
        break

    frame = cv2.resize(img, dsize=(640, 480))

    key = cv2.waitKey(1)
    if key == 13 :
        break

    cv2.imshow('Frame', frame)

cam.releace()
cv2.destroyAllWindows()