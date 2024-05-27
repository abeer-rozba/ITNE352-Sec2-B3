import socket
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
                category_str = ",".join(categories)
                category = input("Enter the category [" + category_str + "]: ").lower()
                if category not in categories:
                    print(" Category does not exist.")
                else:
                    request = "1b " + category
                    client_socket.send(request.encode())
                    print(client_socket.recv(6000).decode())
            elif option == "c":
                country_codes = {"Morocco": "ma", "United States": "us", "Saudi Arabia": "sa", "Egypt": "eg", "New Zealand": "nz", 
                                 "Australia": "au", "United Arab Emirates": "ae", "United Kingdom": "gb", "Canada": "ca"}
                for country in country_codes:
                    print(country)
                country_name = input("Enter the country: " ).title()
                if country_name not in country_codes:
                    print(" Country is not included. Try again.")
                else:
                    country_code = country_codes[country_name]
                    request = "1c " + country_code
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
        print_sources_menu()
        option = input("Enter the letter that represents your choice: ").lower()
        while True:
            if option == "a":
                categories = ["business","entertainment","general","health","technology","sports","science"]
                category_str = ",".join(categories)
                category = input("Enter the category [" + category_str + "]: ").lower()
                if category not in categories:
                    print(" Category does not exist.")
                else:
                    request = "2a " + category
                    client_socket.send(request.encode())
                    print(client_socket.recv(6000).decode())
            if option == "b":
                country_codes = {"Morocco": "ma", "United States": "us", "Saudi Arabia": "sa", "Egypt": "eg", "New Zealand": "nz", 
                                "Australia": "au", "United Arab Emirates": "ae", "United Kingdom": "gb", "Canada": "ca"}
                for country in country_codes:
                    print(country)
                country_name = input("Enter the country: " ).title()
                if country_name not in country_codes:
                    print(" Country is not included. Try again.")
                else:
                    country_code = country_codes[country_name]
                    request = "2b " + country_code
                    client_socket.send(request.encode())
                    print(client_socket.recv(6000).decode())
            elif option == "c":
                language_code = {"arabic":"ar", "english": "en"}
                language_name = input("Choose your desired language (Arabic or English): ").lower()
                if language_name not in language_code:
                    print("This language is not available.")
                else:
                    language = language_code[language_name]
                    request = "2c " + language
                    client_socket.send(request.encode())
                    print(client_socket.recv(6000).decode())
            elif option == "d":
                client_socket.send("2d".encode())
                print(client_socket.recv(6000).decode())
            elif option == "e":
                client_socket.send("2e".encode())
                break
            print_sources_menu()
            option = input("Enter the letter that represents your choice: ").lower()

    elif option == "3":
        client_socket.send("3".encode())
        print(client_socket.recv(6000).decode())
        break
    else:
        print("Invalid option.")

client_socket.close()
