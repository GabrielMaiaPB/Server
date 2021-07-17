from socket import *
import threading


cliente = socket(AF_INET, SOCK_STREAM)
cliente.connect(("192.168.0.103", 1500))


def receive_messages(client: socket) -> None:
    while True:
        message = input("Client: ")
        client.sendall(message.encode())
        message = client.recv(2048).decode()
        print(message)



thread_receive_message = threading.Thread(target=receive_messages, args=(cliente,)).start()
