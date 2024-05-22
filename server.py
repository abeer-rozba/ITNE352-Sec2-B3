import socket
import threading

server_address = ("127.0.0.1", 49158)

def handle_client(client_socket, client_address):
    client = client_socket.recv(1024).decode("ascii")
    print("New connection accepted from: ", client)
    while True:
        data = client_socket.recv(1024).decode("ascii")
        if not data:
            print(client, " disconnected.")
            break
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(6)

while True:
    client_socket, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()
