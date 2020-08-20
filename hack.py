import sys
import socket
import re

def main():
    _, ip, port, msg = sys.argv

    client_socket = socket.socket()  # creating the socket

    client_socket.connect((ip, int(port)))  # Connect to the server
    client_socket.send(msg.encode())  # sending data converting to bytes through socket

    response = client_socket.recv(1024).decode()  # decoding received response from bytes to string

    print(response)
    client_socket.close()  # Close the connection


if __name__ == '__main__':
    main()
