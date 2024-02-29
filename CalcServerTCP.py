import socket
import datetime
import sys

now = datetime.datetime.now()
#   Take a port number as a command line argument
PORT_NUMBER = int(sys.argv[1])
#   Create a socket for the server
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_IP = '192.168.1.120'
serversocket.bind((SERVER_IP, PORT_NUMBER))
while True:
    #   Listen for TCP connection on the port specified
    serversocket.listen(5)
    cSocket, cIP = serversocket.accept()
    #   Receive data from socket
    data = cSocket.recv(1024)
    #   Print the IP address and port of the connected client
    print(cSocket.getpeername())

    while True:
        #   Exit inner loop if no data
        if not data:
            break
        #   Receive data from the client
        message = data.decode()
        print(message)

        try:
            message = eval(str(message))
        #   Check if sentinel value has been given, and terminate connection if true

            if message == "terminate":
                print("ERROR: Client terminated connection")
                cSocket.close()
                break
        #   Reply with “Message Received, <time>, thank you!”
            sendBack = "Message Received, " + "THE ANSWER IS: " + str(message) + \
                now.strftime(" %m/%d/%Y, %H:%M:%S") + \
                ", thank you!"
        #   Send the message with the time received back to the client.
            cSocket.sendall(str.encode(sendBack))

        except (SyntaxError, NameError, ZeroDivisionError) as e:
            error_message = "Error" + \
                str(e) + ". Please provide a valid arithmetic."
            cSocket.sendall(str.encode(error_message))

        #   Continue to receive data from socket

        data = cSocket.recv(1024)
