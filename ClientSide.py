import socket
import threading
import time

Client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREA)
Client_socket.connect(("127.0.0.1",49158))
Client_socket.send("ClientSide".encode()) #Establish a connection with the server

while True:
    print("1.Server Heading")
    print("2.List of Source")
    print("3.Quit")
    num=input("Enter Option Number: ")

    if num =="1":
        search_headliens(Client_socket) 

    elif num =="2":
        list_of_source(Client_socket)

    elif num=="3":
        print(" QUIT ")
        break
    else:
        print("Invalid option.")
def search_headlines(client_socket):
    client_socket.send("1".encode())

    print("1 SEARCH FOR KEYWORDS")
    print("2 SEARCH BY CATEGORY")
    print("3 SEARCH BY COUNTRY")
    print("4 LIST ALL NEW HEADLINES")
    print("5 BACK TO THE MAIN MENU")
    num = input("ENTER OPTION NUMBER: ")

    