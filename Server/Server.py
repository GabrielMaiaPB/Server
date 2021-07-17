from socket import *
from threading import *

# Addresses and ports that can be listened.
ip_address = ""
port = 1500

server = socket(AF_INET, SOCK_STREAM)  # Starting socket that accepts TCP IPv4 connections.
server.bind((ip_address, port))  # Informing the server the addresses and ports.
server.listen(5)  # Number of simultaneous connections.
clients = []


def communication(_client: socket) -> None:
    while True:
        data = _client.recv(2048).decode()
        print(data)
        for client in clients:
            client.sendall(data.encode())


while True:
    client_name, address = server.accept()
    print(f"{address} conectou-se")
    clients.append(client_name)
    thread_receive = Thread(target=communication, args=(client_name, )).start()
