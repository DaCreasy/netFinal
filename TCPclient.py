# -*- coding: utf-8 -*-
"""
author Damian Creasy
author Tim Yarosh
version 1.0
section CS475
 
Project Description: We wanted to simulate, using a standard TCP connection 
between a client and a server, the functionalities of a chat room. 
 
Basic TCP client class. 
Adapted from Computer Networking a Top Down Approach 6th Edition code in ch 2
Source:  
"""

import socket
import threading
import sys

#define mock global variables
isConnected = False
serverIP = '172.25.43.182' #IP address of Damian's computer acting as our server
portNum = 12002 #arbitrary port #



def sendMsg(clientSocket):
    while True:
        msg = input('Enter message: ')
        encoded_msg = str.encode(msg)
        clientSocket.send(encoded_msg)

def receiveMsg(clientSocket):
    while True:
        msg = clientSocket.recv(2048)
        print('Received from the Server: '+ msg.decode())

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    clientSocket.connect((serverIP,portNum))
    print('Connection successful')
    isConnected = True
    
    MSL = threading.Thread(target = sendMsg, args=(clientSocket,), daemon = True)
    MSL.start()
    
    MRL = threading.Thread(target = receiveMsg, args=(clientSocket,), daemon = True)
    MRL.start()
    
    MSL.join()
    MRL.join()
    
    print('Closing connection')
    clientSocket.close()
    print('Connection closed')
    
except Exception as e:
    print('Failed to connect:' + ' ' + str(e))
    sys.exit(0)
            
