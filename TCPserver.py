from socket import *
from datetime import datetime

welcome = "You've successfully connected to the room! Welcome!"

def newClient(client, addr):
    
    # Welcome the newly connected client
    client.send(str.encode(welcome))
    
    # Begin looping for receiving client messages
    while 1:
        try:
            clientMSG = client.recv(1024)
            if clientMSG:
                # Log the client message and the time at which it is received
                logMSG = "User["+ addr[0] +"] @ ["+datetime.now()+"] " + clientMSG.decode()
                print(logMSG)
                
                for user in users:
                    if user != client:
                        try:
                            user.send(str.encode(logMSG))
                        except:
                            user.close()
                            users.remove(user)
            else:
                users.remove(client)
        except:
            continue
                            
serverPort = 12010
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
    clientThread = Thread(target = newClient, args = (client,addr,), daemon = True)
    clientThread.start()
    
client.close()
server.close()
