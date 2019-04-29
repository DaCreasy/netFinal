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

from socket import *
serverName = '172.25.43.182' #IP address of Damian's computer acting as our server
serverPort = 12000 #arbitrary port #
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input("Input lowercase sentence:")
clientSocket.send(sentence)
echo = clientSocket.recv(1024)
print('From Server:', echo)
clientSocket.close()
