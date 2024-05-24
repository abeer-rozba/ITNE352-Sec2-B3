import socket
import threading
import time

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 49158))
client_socket.send("ClientSide".encode()) #Establish a connection with the server

def print_main_menu():
    print("1. Search headlines")
    print("2. List of sources")
    print("3. Quit")

def print_headlines_menu():
    print("1. Search for keywords")
    print("2.Search by category")
    print("3. Search by country")
    print("4. List all new headlines")
    print("5. Back to the main menu")

def print_sources_menu():
    print("1. Search by category")
    print("2. Search by country")
    print("3. Search by language")
    print("4. List all")
    print("5. Back to the main menu")

print_main_menu()
option = input("Enter The Option Number : ")

while True:
    if option == "1":
        Client_socket.send("1".encode())
        print_headliens_menu()
        num=input("Enter Option Number: ")
        while True:
            if choess=="1":
                Client_socket.send("1".encode())
                key_word= input("Enter Keyword: ")
                Client_socket.send(key_word.encode())
                respon=Client_socket.recv(6000).decode()
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
                    print(Client_socket.recv(6000).decode())
            elif num=="3":
                Client_socket.send("3".encode())
                countries=["ma","us","sa","eg","nz","au","ae","gb","ca"]
                print("Available countries: ma, us, sa, eg, nz, au, ae, gb, ca")
                country=input("Enter the country code: " ).lower()
                if country not in countries:
                    print(" Countriy does not exist ")
                else:
                    Client_socket.send(country.encode())
                    print(Client_socket.recv(6000).decode())
           
            elif num=="4":
                Client_socket.send("4".encode())
                print(Client_socket.recv(6000).decode())
            elif num=="5":
                Client_socket.send("5".encode())
                break
            time.sleep(1)
            print_headliens_menu()
            num=input("Enter Option Number: ")
            
                
                 





    
           


    
    
                
                    
            

