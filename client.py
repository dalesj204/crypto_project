import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
   
   
if __name__ == '__main__':
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # connect to the server
    try:
        client.connect((HOST, PORT))
        print("Successfully connected to server")
    except:
        print(f"Unable to connect to server {HOST} {PORT}")

    client_name = input("Enter your name: ")
    client.send(client_name.encode())
    server_name = client.recv(1024).decode()
    print(f"{server_name} has joined the chat")
    print("Send [e] to exit the chat")

    while 1:
        message = client.recv(1024).decode()
        print(f"{server_name}: {message}")
        message = input(f"{client_name}: ")
        if message == "[e]":
            print("You have left the chat.")
            message = "Left the chat."
            client.send(message.encode())
            break
        client.send(message.encode())
    