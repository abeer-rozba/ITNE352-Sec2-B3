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

def h_by_keyword(keyword):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey=9a1f549ac51d44f1af17ea18ca78656b"
    response = requests.get(url)
    if response.status_code == 200:
        headlines = response.json()
        return {"response" : headlines}
    else:
        return {"response" : "Error. Please try again."}

def handle_request(request):
    if request.startswith('1'):
        sub_option = request[1]
        if sub_option == 'a':
            keyword = input("Enter the keyword to search the headlines: ")
            return h_by_keyword(keyword)
        elif sub_option == 'b':
            category = input("Enter the category to search the headlines. Choose from business, entertainment, general, health, science, sports, technology.")
            return h_by_category(category)
        elif sub_option == 'c':
            country = input("Enter the country to search the headlines. Choose from Australia, New Zealand, Canada, Saudi Arabia, United Kingdom, United States, Egypt, or Morroco.")
            return h_by_country(country)
        elif sub_option == 'd':
            return fetch_all_h()
        elif sub_option == 'e':
            return {"response" : "Back to the main menu."}
        else:
            return {"response" : "Invalid. Please try again."}
    elif request.startswith('2'):
        sub_option = request[1]
        if sub_option == 'a':
            category = input("Enter the category to search the sources. Choose from business, entertainment, general, health, science, sports, technology.")
            return s_by_category(category)
        elif sub_option == 'b':
            country = input("Enter the country to search the headlines. Choose from Australia, New Zealand, Canada, Saudi Arabia, United Kingdom, United States, Egypt, or Morroco.")
            return s_by_country(country)
        elif sub_option == 'c':
            language = input("Enter the language to search the sources. Choose either Arabic or English.")
            return s_by_language(language)
        elif sub_option == 'd':
            return fetch_all_s()
        elif sub_option == 'e':
            return {"response" : "Back to the main menu."}
        else:
            return {"response" : "Invalid. Please try again."}
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
