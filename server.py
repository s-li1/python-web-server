#import socket module
from socket import *
server_port = 6789
server_ip = '127.0.0.1'
#Prepare a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((server_ip, server_port))
serverSocket.listen()
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()   
    try:
        message =  connectionSocket.recv(2048).decode()          
        filename = message.split()[1]                 
        f = open(filename[1:])                        
        outputdata = f.read()
        connectionSocket.send(('HTTP/1.1 200 OK\r\n').encode())
        connectionSocket.send(message.encode())
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send(('HTTP/1.1 404 Not Found\r\n\r\n').encode())
        connectionSocket.send(("<html><body><h1> 404 Not Found </h1></body></html>\r\n\r\n").encode())
        connectionSocket.close()
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data   
