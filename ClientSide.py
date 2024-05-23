import socket
import threading
import time

Client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREA)
Client_socket.connect(("127.0.0.1",49158))
Client_socket.send("ClientSide".encode()) #Establish a connection with the server

def print_main_menu():
    print("1. Serch Headlines")
    print("2. List Of the Sources ")
    print("3. QUIT")

def print_headlines_menu():
    print("1. Search For Keyword")
    print("2.Search By Catogry")
    print("3. Search By Country")
    print("4. List All New Headliens")
    print("5. Back To The Main Menu")

def print_sources_menu():
    print("1 Search By Country")
    print("2 Search By Language")
    print("3 List All")
    print("4 Back To The Main Menu")

print_main_menu()
choess = input("Enter The Option Number : ")

