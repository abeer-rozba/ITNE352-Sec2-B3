import socket
import threading
import time

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 49158))
client_name = input("Enter client name: ")
client_socket.send(client_name.encode())

def print_main_menu():
    print("1. Search headlines")
    print("2. List of sources")
    print("3. Quit")

def print_headlines_menu():
    print("a. Search for keywords")
    print("b.Search by category")
    print("c. Search by country")
    print("d. List all new headlines")
    print("e. Back to the main menu")

def print_sources_menu():
    print("a. Search by category")
    print("b. Search by country")
    print("c. Search by language")
    print("d. List all")
    print("e. Back to the main menu")

print_main_menu()
option = input("Enter your option number: ")

while True:
    if option == "1":
        print_headlines_menu()
        option = input("Enter your option number: ")
        while True:
            if option == "a" or option == "A":
                keyword = input("Enter keyword: ")
                request = "1a " + keyword 
                client_socket.send(request.encode())
                response = client_socket.recv(6000).decode()
                print(response)
            elif option =="2":
                Client_socket.send("2".encode())
                categories=["business","emtertainment","general","health","technology","sport","science"]
                print("categories: business, emtertainment, general, health, technology, sport, science ")
                category=input("Enter the category: " ).lowe()
                if category not in categories:
                    print(" Category does not exist")
                else:
                    Client_socket.send(category.encode())
                    print(Client_socket.recv(6000).decode())
            elif option =="3":
                Client_socket.send("3".encode())
                countries=["ma","us","sa","eg","nz","au","ae","gb","ca"]
                print("Available countries: ma, us, sa, eg, nz, au, ae, gb, ca")
                country=input("Enter the country code: " ).lower()
                if country not in countries:
                    print(" Countriy does not exist ")
                else:
                    Client_socket.send(country.encode())
                    print(Client_socket.recv(6000).decode())
           
            elif option =="4":
                Client_socket.send("4".encode())
                print(Client_socket.recv(6000).decode())
            elif option =="5":
                Client_socket.send("5".encode())
                break
            time.sleep(1)
            print_headlines_menu()
            num=input("Enter Option Number: ")
            
                
                 





    
           


    
    
                
                    
            

