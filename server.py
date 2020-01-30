import socket
import numpy as np
import cv2
import time
import configparser

config = configparser.ConfigParser()
config.read("./config.ini")

FPS = 30
INDENT = '    '

SERVER_HOST = config.get('server', 'ip')
SERVER_PORT = int(config.get('server', 'port'))

HEADER_SIZE = int(config.get('packet', 'header_size'))
IMAGE_WIDTH = int(config.get('packet', 'image_width'))
IMAGE_HEIGHT = int(config.get('packet', 'image_height'))
IMAGE_QUALITY = 30


# camera settings
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, FPS)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, IMAGE_WIDTH)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, IMAGE_HEIGHT)

print('Camera {')
print(INDENT + 'FPS   : {},'.format(cam.get(cv2.CAP_PROP_FPS)))
print(INDENT + 'WIDTH : {},'.format(cam.get(cv2.CAP_PROP_FRAME_WIDTH)))
print(INDENT + 'HEIGHT: {}'.format(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('}')


# server listening
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(1)

# connecting
soc, addr = s.accept()

print('Server {')
print(INDENT + 'HOST : {},'.format(SERVER_HOST))
print(INDENT + 'PORT : {}'.format(SERVER_PORT))
print('}')

print('Client {')
print(INDENT + 'IP   : {},'.format(addr[0]))
print(INDENT + 'PORT : {}'.format(addr[1]))
print('}')

while True:
    loop_start_time = time.time()
    flag, frame = cam.read()

    resized_img = cv2.resize(frame, (IMAGE_WIDTH, IMAGE_HEIGHT))
    (status, encoded_img) = cv2.imencode('.jpg', resized_img, [int(cv2.IMWRITE_JPEG_QUALITY), IMAGE_QUALITY])

    try:
        soc.sendall(encoded_img)
    except socket.error as e:
        print('Connection closed.')
        break

soc.close()
