## Python Socket Communication README


## Overview

This repository contains Python scripts demonstrating client-server communication using sockets, implemented for both TCP and UDP protocols. The scripts provide a basic framework for establishing communication between a client and a server, facilitating message exchange.


## TCP Client (tcp_client.py):

Takes the server's IP address and port number as command-line arguments.
Creates a TCP socket for communication with the server.
Connects to the server using the provided IP address and port number.
Sends a message to the server and receives a response.
Communication continues until the user inputs the "terminate" message, which closes the connection and terminates the client program.


## UDP Client (udp_client.py):

Similar to the TCP client, it takes the server's IP address and port number as command-line arguments.
Creates a UDP socket for communication with the server.
Sends a message to the server using the UDP protocol.
Receives a response from the server.
Communication continues until the user inputs the "terminate" message, which closes the socket and terminates the client program.


## TCP Server (tcp_server.py):

Takes a port number as a command-line argument.
Creates a TCP server socket and binds it to the specified port.
Listens for incoming connections from clients.
Accepts client connections and receives data from them.
If the received message is "terminate," it closes the connection. Otherwise, it sends a confirmation message back to the client.


## UDP Server (udp_server.py):

Similar to the TCP server, it takes a port number as a command-line argument.
Creates a UDP server socket and binds it to the specified port.
Listens for incoming datagrams (messages) from clients.
Receives data from clients and sends a response back.
The server continues running until terminated by the user.


## Usage
Clone the repository to your local machine.
Open a terminal and navigate to the directory containing the Python scripts.
Run the desired script(s) using Python, providing necessary command-line arguments as described in the script's overview.
