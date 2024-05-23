import socket
import threading
import json
import requests

server_address = ("127.0.0.1", 49158)

def handle_client(client_socket, client_address):
    client = client_socket.recv(1024).decode("ascii")
    print(f"New connection accepted from: {client}")
    while True:
        request = client_socket.recv(1024).decode("ascii")
        if not request:
            break
        response = handle_request(request)
        print (f"Incoming request from {client} : {request}")
        client_socket.send(json.dumps(response).encode("ascii"))
    print(f"{client} disconnected.")
    client_socket.close()

def handle_request(request):
    if request.startswith('1'):
        sub_option = request[1]
        if sub_option == 'a':
            keyword = input("Enter the keyword to search the headlines: ")
            return ()
        elif sub_option == 'b':
            category = input("Enter the category to search the headlines. Choose from business, entertainment, general, health, science, sports, technology.")
            return ()
        elif sub_option == 'c':
            country = input("Enter the country to search the headlines. Choose from Australia, New Zealand, Canada, Saudi Arabia, United Kingdom, United States, Egypt, or Morroco.")
            return()
        elif sub_option == 'd':
            return fetch_all_h()
        elif sub_option == 'e':
            return {"Back to the main menu."}
        else:
            return {"Invalid. Please try again."}
    elif request == '2':
        print()
    elif request == '3':
        return {"response" : "Quitting. Good bye."}
    else:
        return {"response" : "Invalid request. Please try again."}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(6)

while True:
    client_socket, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()
