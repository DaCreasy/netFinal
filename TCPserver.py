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
            print("Listening to " + userName)
            clientMSG = client.recv(1024)
            if clientMSG:
                # Log the client message and the time at which it is received
                logMSG = userName + " @ ["+datetime.now()+"] " + clientMSG.decode()
                print(logMSG)
                
                for user in users:
                    if user != client:
                        try:
                            user.send(str.encode(logMSG))
                        except:
                            user.close()
                            users.remove(user)
            else:
                # TODO: Thread has to be killed here or handled in some way...
                # This part loops infinitely if a user disconnects
                print("Removing " + userName)
                users.remove(client)
        except:
            continue
                            
serverPort = 12011
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
