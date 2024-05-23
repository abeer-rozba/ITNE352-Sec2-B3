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
num = input("Enter The Option Number : ")

while True:
    if num=="1":
        Client_socket.send("1".encode())
        print_headliens_menu()
        num=input("Enter Option Number: ")
        while True:
            if choess=="1":
                Client_socket.send("1".encode())
                key_word= input("Enter Keyword: ")
                Client_socket.send(key_word.encode())
                respon=Client_socket.recv(1024).decode()
                print(respon)
            elif choess=="2":
                Client_socket.send("2".encode())
                categories=["business","emtertainment","general","health","technology","sport","science"]
                print("categories: business, emtertainment, general, health, technology, sport, science ")
                category=input("Enter the category: " ).lowe()
                if category not in categories:
                    print(" Category does not exist")
                else:
                    Client_socket.send(category.encode())
                    print(Client_socket.recv(1024).decode())
            elif num=="3":
                Client_socket.send("3".encode())
                countries=["ma","us","sa","eg","nz","au","ae","gb","ca"]
                print("Available countries: ma, us, sa, eg, nz, au, ae, gb, ca")
                country=input("Enter the country code: " ).lower()
                if country not in countries:
                    print(" Countriy does not exist ")
                else:
                    Client_socket.send(country.encode())
                    print(Client_socket.recv(1024).decode())
           
            elif num=="4":
                Client_socket.send("4".encode())
                print(Client_socket.recv(1024).decode())
            elif num=="5":
                Client_socket.send("5".encode())
                break
            time.sleep(1)
            print_headliens_menu()
            num=input("Enter Option Number: ")
            
                
                 





    
           


    
    
                
                    
            

