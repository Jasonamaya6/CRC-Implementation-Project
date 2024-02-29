import socket
import sys

# Take a server IP and a port number as command-line arguments
SERVER_IP = sys.argv[1]
PORT_NUMBER = int(sys.argv[2])

# Create a socket for the client (UDP)
cSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ask the user for a message to send
while True:
    # Get user input
    message = input(
        "CLIENT: Enter your arithmetic you want solved (or type 'terminate' to exit): ")

    # Send the message to the server
    cSocket.sendto(message.encode(), (SERVER_IP, PORT_NUMBER))

    if message == "terminate":
        # Close the socket and exit if the sentinel value is given
        cSocket.close()
        sys.exit()

    # Receive data from the server
    recvData, server_address = cSocket.recvfrom(1024)
    recvMessage = recvData.decode()

    # Display the response from the server
    print(recvMessage)
