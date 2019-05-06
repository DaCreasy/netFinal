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

from socket import *
import threading
from datetime import datetime

welcome = "You've successfully connected to the room! Welcome!"

def newClient(client, addr):

    userName = "User["+ addr[0] +"]"
    
    # Welcome the newly connected client
    client.send(str.encode(welcome))
    print(userName + " has received welcome message.")
    
    # Begin looping for receiving client messages
    while 1:
        try:
            clientMSG = client.recv(1024)
            clientMSG = clientMSG.decode()

            # This checks if the message is not empty as a result of a closed connection
            if clientMSG:
                # Log the client message and the time at which it is received
                logMSG = userName + " @ ["+ str(datetime.now())+"] : " + clientMSG
                print(logMSG)

                # Broadcast the message to all clients other than the one who sent the message
                userMSG = userName + " says: " + clientMSG
                for user in users:
                    if user != client:
                        try:
                            user.send(str.encode(userMSG))
                        except:
                            user.close()
                            users.remove(user)
                    

            # if the message is a result of a closed connection, remove the user from the list of active clients and end this thread by breaking from the while loop
            else:
                print("Removing " + userName)
                endConn(client)
                break
        # Something unexpected occurred and the client must be removed from the list
        except:
            print("Removing " + userName)
            endConn(client)
            break


def endConn(client):
    users.remove(client)
    client.close()
    
serverPort = 12000
server = socket(AF_INET, SOCK_STREAM)
server.bind(('',serverPort))

users = []
server.listen(50)
print("Server is ready and listening for connections...")

while 1:

    # Accept a connection with a new client
    client, addr = server.accept()

    # Add the client to the list of active users
    users.append(client)

    # Log the new user
    print("User["+ addr[0] +"] has joined...")
    
    # Start a new thread for the new user and begin listening for messages
    clientThread = threading.Thread(target = newClient, args = (client,addr,), daemon = True)
    clientThread.start()
    
client.close()
server.close()
