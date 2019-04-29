from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Server is ready and listening for connections...")
while 1:
    connectionSocket, addr = serverSocket.accept()
    print("Connection established...")
    sentence = connectionSocket.recv(1024)
    print("Message received: ", sentence)
    print("Sending echo...")
    connectionSocket.send(sentence)
    print("Echo sent. Closing connection...")
    connectionSocket.close()
    print("Connection closed...")
