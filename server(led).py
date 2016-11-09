import socket
import RPi.GPIO as GPIO
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)

    state = True

    # endless loop, on/off for 1 second
    while True:
     GPIO.output(4,True)
     time.sleep(1)
     GPIO.output(4,False)
     time.sleep(1)
    if len(buf) > 0:
        print buf
        break
