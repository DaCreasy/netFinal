# -*- coding: utf-8 -*-
"""
 author Damian Creasy
 author Tim Yarosh
 version 1.0
 date 4/29/19
 section CS475
 
 Basic TCP client class. 
 Source: Computer Networking a Top Down Approach 6th Edition 
"""

import socket
serverName = '172.25.43.182' #IP address of Damian's computer acting as our server
serverPort = 12001 #arbitrary port #

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
    
sentence = input("Input lowercase sentence:")
encoded = str.encode(sentence)

try:
    clientSocket.send(encoded)
except Exception:
    clientSocket.close()

echo = clientSocket.recv(64)
print('From Server:', echo.decode())
clientSocket.close()
