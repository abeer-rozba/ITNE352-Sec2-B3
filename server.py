import socket
import threading
import json

server_address = ("127.0.0.1", 49158)

def handle_client(client_socket, client_address):
    client = client_socket.recv(1024).decode("ascii")
    print(f"New connection accepted from: {client}")
    while True:
        data = client_socket.recv(1024).decode("ascii")
        if not data:
            break
        response = handle_request(request)
        print (f"Incoming request from {client} : {request}")
        client_socket.send(json.dumps(response).encode("ascii"))
    print(f"{client} disconnected.")
    client_socket.close()

def handle_request(request):
    if request == '1':
        print()
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
