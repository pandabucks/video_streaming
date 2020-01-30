import socket
import numpy as np
import cv2

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("localhost", 5200))

print("connection established")

while(1):
    data = soc.recv(921600)
    data = np.frombuffer(data,dtype=np.uint8)

    data = np.reshape(data, (480, 640,3))

    cv2.imshow("",data);

    k = cv2.waitKey(1)
    if k== 13 :
        break

cv2.destroyAllWindows()
