from socket import *
import threading


cliente2 = socket(AF_INET, SOCK_STREAM)
cliente2.connect(("192.168.56.1", 1500))


def receive_messages(client: socket) -> None:
    while True:
        result = input()
        client.sendall(result.encode())
        message_received = client.recv(2048).decode()
        print(message_received)



thread_receive_message = threading.Thread(target=receive_messages, args=(cliente2,))
thread_receive_message.start()
