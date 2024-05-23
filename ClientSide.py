import socket
import threading
import time

Client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREA)
Client_socket.connect(("127.0.0.1",49158))
Client_socket.send("ClientSide".encode()) #Establish a connection with the server

def send_receive(command, data=None):
    Client_socket.send(command.encode())
    if data:
        Client_socket.send(data.encode())
    return Client_socket.recv(1024).decode()    