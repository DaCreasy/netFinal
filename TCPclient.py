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
#serverIP = '127.0.0.1' Local host IP for individual debugging purposes
serverIP = '172.25.47.216' #IP address of Damian's computer acting as our server
portNum = 12000 #arbitrary port #



def sendMsg(clientSocket):
    #print('Send Listener has begun.')
    while True:
        #print('Top of send while...')
        msg = input('')
        #print('Encoding msg...')
        encoded_msg = str.encode(msg)
        #print('Msg encoded...')
        try:
            clientSocket.send(encoded_msg)
            #print('Msg sent...')
        except:
            print('Error sending msg... closing connection...')
            clientSocket.close()
            break

def receiveMsg(clientSocket):
    #print('Receive Listener has begun...')
    while True:
        #print('Top of rcv while...')
        try:
            msg = clientSocket.recv(2048)
            #print('Msg received...')
            msg = msg.decode()
            #print('Msg decoded...')

            if msg:
                #print('Msg valid, printing...')
                print(msg)
            else:
                print('Connection lost... exiting program')
                clientSocket.close()
                break
        except:
            print('Connection lost... exiting program')
            clientSocket.close()
            break

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    clientSocket.connect((serverIP,portNum))
    print('Connection successful')
    
    MSL = threading.Thread(target = sendMsg, args=(clientSocket,), daemon = False)
    MSL.start()
    
    MRL = threading.Thread(target = receiveMsg, args=(clientSocket,), daemon = False)
    MRL.start()

    ''' 
    This main thread will fall through after the listener threads begin, but they will continue to run in the background
    '''
    
except Exception as e:
    print('Failed to connect:' + ' ' + str(e))
    sys.exit(0)
            
