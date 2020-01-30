import sys
import cv2
import numpy as np
import socket
import configparser

config = configparser.ConfigParser()
config.read("./config.ini")

FPS = 30
INDENT = '    '

# Network parameter
SERVER_HOST = config.get('server', 'ip')
SERVER_PORT = int(config.get('server', 'port'))

# Packet parameter
HEADER_SIZE = int(config.get('packet', 'header_size'))

# Image parameter
IMAGE_WIDTH = int(config.get('packet', 'image_width'))
IMAGE_HEIGHT = int(config.get('packet', 'image_height'))
IMAGE_QUALITY = 30

# socket connection
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((SERVER_HOST, SERVER_PORT))

print("connection established")

# Viewer 
while True:
    data = soc.recv(IMAGE_HEIGHT * IMAGE_WIDTH * 3)

    # decord image
    img = np.frombuffer(data,dtype=np.uint8)
    img = cv2.imdecode(img, 1)

    img = np.reshape(img, (IMAGE_HEIGHT, IMAGE_WIDTH, 3))

    cv2.imshow("",img);

    k = cv2.waitKey(1)
    if k== 13 :
        break

cv2.destroyAllWindows()
