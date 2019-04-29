# -*- coding: utf-8 -*-
"""
 author Damian Creasy
 author Tim Yarosh
 version 1.0
 section CS475
 
 Basic TCP client class. 
 Source: Computer Networking a Top Down Approach 6th Edition 
"""

import socket
import threading
import sys

isConnected = False
serverIP = '172.25.43.182' #IP address of Damian's computer acting as our server
portNum = 12003 #arbitrary port #

def sendMsg(clientSocket):
        msg = input('Enter message: ')
        encoded_msg = str.encode(msg)
        clientSocket.send(encoded_msg)

def receiveMsg(clientSocket):
        msg = clientSocket.recv(1024)
        print(msg.decode())


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    clientSocket.connect((serverIP,portNum))
    print('Connection successful')
    isConnected = True
    
    sendMsg(clientSocket)
    receiveMsg(clientSocket)
    
    clientSocket.close()
    
except Exception as e:
    print('Failed to connect:' + ' ' + str(e))
    sys.exit(0)
    
