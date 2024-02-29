import socket
import datetime
import sys

now = datetime.datetime.now()
# Take a port number as a command line argument
PORT_NUMBER = int(sys.argv[1])

# Create a socket for the server (UDP)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address (IP and port)
SERVER_IP = '192.168.1.120'
server_address = (SERVER_IP, PORT_NUMBER)

# Bind the server socket to the server address (UDP doesn't establish connections)
serversocket.bind(server_address)

while True:
    try:
        # Receive data from the client
        data, client_address = serversocket.recvfrom(1024)
        # Print the client's address
        print(client_address)

        # Receive data from the client
        message = data.decode()
        print(message)

        try:
            message = eval(message)

            # Check if sentinel value has been given, and terminate the connection if true
            if message == "terminate":
                print("ERROR: Client terminated connection")
                # No need to close the socket in UDP

            # Reply with “Message Received, <time>, thank you!”
            sendBack = "Message Received, " + "THE ANSWER IS: " + \
                str(message) + now.strftime(" %m/%d/%Y, %H:%M:%S") + ", thank you!"

            # Send the message with the time received back to the client
            serversocket.sendto(sendBack.encode(), client_address)

        except (SyntaxError, NameError, ZeroDivisionError) as e:
            error_message = "Error: " + \
                str(e) + ". Please provide a valid arithmetic expression."
            serversocket.sendto(error_message.encode(), client_address)

    except KeyboardInterrupt:
        # Handle Ctrl+C for graceful termination
        print("Server terminated by the user")
        serversocket.close()
        break
