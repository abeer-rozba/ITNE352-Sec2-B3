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

while True:
    print_main_menu()
    option = input("Enter your option number: ")
    if option == "1":
        print_headlines_menu()
        option = input("Enter the letter that represents your choice: ").lower()
        while True:
            if option == "a":
                keyword = input("Enter headlines keyword: ")
                request = "1a " + keyword 
                client_socket.send(request.encode())
                response = client_socket.recv(6000).decode()
                print(response)
            elif option =="b":
                categories = ["business","entertainment","general","health","technology","sports","science"]
                category = input("Enter the category " + categories + ": ").lower()
                if category not in categories:
                    print(" Category does not exist.")
                else:
                    request = "1b " + category
                    client_socket.send(request.encode())
                    print(client_socket.recv(6000).decode())
            elif option == "c":
                countries = ["Morocco (ma)","United States (us)","Saudi Arabia (sa)","Egypt (eg)","New Zealand (nz)","Australia (au)",
                             "United Arab Emirates (ae)","United Kingdom (gb)","Canada (ca)"]
                country=input("Enter the country code " + countries + ": " ).lower()
                if country not in countries:
                    print(" Country is not included. Try again.")
                else:
                    request = "1c " + country
                    client_socket.send(request.encode())
                    print(client_socket.recv(6000).decode())
            elif option == "d":
                client_socket.send("1d".encode())
                print(client_socket.recv(6000).decode())
            if option == "e":
                client_socket.send("1e".encode())
                print(client_socket.recv(6000).decode())
                break
            time.sleep(1)
            print_headlines_menu()
            option = input("Enter the letter that represents your choice: ").lower()
            
    elif option == "2":
        client_socket.send("2".encode())
        print_sources_menu()
        option = input("Enter option Number:  ")

        while True:
            if option == "1":
                client_socket.send("1".encode())
                countries = ["ma","us","sa","eg","nz","au","ae","gb","ca"]
                print("Available countries:  ma , us , sa , eg , nz , au ,ae , gb, ca")
                country = input("Enter the country code : ").lower()
                if country not in countries:
                    print("Countriy does not exist")
                else:
                    client_socket.send(country.encode())
                    print(client_socket.recv(1024).decode())
            elif option == "2":
                client_socket.send("2".encode())
                languages = ["ar", "en"]
                print("Available languages: ar, en")
                Language = input("Enter the language code : ").lower()
                if Language not in languages:
                    print("This Language Does Not Exist")
                else:
                    client_socket.send(Language.encode())
                    print(client_socket.recv(6000).decode())
            elif option == "3":
                client_socket.send("3".encode())
                print(client_socket.recv(6000).decode())
            elif option == "4":
                client_socket.send("4".encode())
                break
            
            print_sources_menu()
            option = input("Enter option Number: ")

    elif option == "3":
        print("QUIT" )
        break
    else:
        print("Invalid option")
    
    print_main_menu()
    option = input("ENTER OPTION NUMBER: ")

client_socket.close()
