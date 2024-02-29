import socket
import sys

#   Take a server IP and a port number as command-line arguments
SERVER_IP = sys.argv[1]
PORT_NUMBER = int(sys.argv[2])
#   Create socket and get client's IP
cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
CLIENT_IP = socket.gethostbyname(hostname)
#   Connect to the server at the given IP and port using TCP
cSocket.connect((SERVER_IP, PORT_NUMBER))
#   Print the IP address and port of the server
print(cSocket.getpeername())
#   Ask the user for a message to send
message = input("CLIENT: Enter Message to send to Server: ")
while True:
    #   Send the message to the server
    cSocket.sendall(str.encode(message))
    #   Read the answer from the server
    recvData = cSocket.recv(1024)
    recvMessage = recvData.decode()
    #   Display the response to the client
    print(recvMessage)
    #   Terminate connection if sentinel value given
    if message == "terminate":
        #   Close the socket when sentinel value has been given
        cSocket.close()
        #   Terminate client program
        sys.exit()
    #   Ask the user for another message to send
    message = input("CLIENT: Enter Message to send to Server: ")



