import socket
import threading
import json
import requests

server_address = ("127.0.0.1", 49158)

def handle_client(client_socket, client_address):
    client = client_socket.recv(1024).decode()
    print(f"New connection accepted from: {client}")
    while True:
        request = client_socket.recv(1024).decode()
        if not request:
            break
        response = handle_request(request, client)
        print (f"Incoming request from {client} :")
        if request.startswith("1"):
            print (f"Looking for {request[3:]} headlines.")
        if request.startswith("2"):
            print (f"Looking for {request[3:]} sources.")
        client_socket.send(json.dumps(response).encode())
    print(f"{client} disconnected.")
    client_socket.close()

def h_by_keyword(keyword, client):
    api_key = "9a1f549ac51d44f1af17ea18ca78656b"
    url = f"https://newsapi.org/v2/everything?q={keyword}"
    params = {
        "apiKey" : api_key,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        headlines = response.json()
        file = f"B3_{client}_keyword_headlines.json"
        with open(file, "w") as f:
            json.dump(headlines, f, indent=4)
        print (f"{keyword} headlines have been saved to {file}")
        return headlines
    else:
        return {"response" : "Error."}

def h_by_category(category, client):
    api_key = "9a1f549ac51d44f1af17ea18ca78656b"
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey" : api_key,
        "category" : category
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        headlines = response.json()
        file = f"B3_{client}_{category}_headlines.json"
        with open(file, "w") as f:
            json.dump(headlines, f, indent=4)
        print (f"{category} headlines have been saved to {file}")
        return headlines
    else:
        return {"response" : "Error."}

def h_by_country(country, client):
    api_key = "9a1f549ac51d44f1af17ea18ca78656b"
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey" : api_key,
        "country" : country
    }
    response = requests.get(url, params=params)
    country_codes = {"ma": "Morocco", "us": "United States", "sa": "Saudi Arabia", "eg": "Egypt", "nz": "New Zealand", 
                    "au": "Australia", "ae": "United Arab Emirates", "gb": "United Kingdom", "ca": "Canada"}
    country_name = country_codes.get(country)
    if response.status_code == 200:
        headlines = response.json()
        file = f"B3_{client}_{country_name}_headlines.json"
        with open(file, "w") as f:
            json.dump(headlines, f, indent=4)
        print (f"{country_name} headlines have been saved to {file}")
        return headlines
    else:
        return {"response" : "Error."}

def fetch_all_h(client):
    api_key = "9a1f549ac51d44f1af17ea18ca78656b"
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey" : api_key,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        headlines = response.json()
        file = f"B3_{client}_all_headlines.json"
        with open(file, "w") as f:
            json.dump(headlines, f, indent=4)
        print (f"All headlines have been saved to {file}")
        return headlines
    else:
        return {"response" : "Error."}
    
def handle_request(request, client):
    if request.startswith('1'):
        sub_option = request[1]
        if sub_option == 'a':
            keyword = request[3:]
            return h_by_keyword(keyword, client)
        elif sub_option == 'b':
            category = request[3:]
            return h_by_category(category, client)
        elif sub_option == 'c':
            country = request[3:]
            return h_by_country(country, client)
        elif sub_option == 'd':
            return fetch_all_h(client)
        elif sub_option == 'e':
            return {"response" : "Back to the main menu."}
        else:
            return {"response" : "Invalid. Please try again."}
    elif request.startswith('2'):
        sub_option = request[1]
        if sub_option == 'a':
            category = request[3:]
            return s_by_category(category, client)
        elif sub_option == 'b':
            country = request[3:]
            return s_by_country(country, client)
        elif sub_option == 'c':
            language = request[3:]
            return s_by_language(language, client)
        elif sub_option == 'd':
            return fetch_all_s(client)
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

try:
    while True:
        client_socket, client_address = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()
except KeyboardInterrupt:
    print("The server has been interrupted. Closing.")
    server_socket.close()
