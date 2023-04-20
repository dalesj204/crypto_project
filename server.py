import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
    
    
if __name__ == '__main__':
    # creating the server socket class object
    # AF_INET: we're using IPv4 addresses
    # SOCK_STREAM: we're using TCP packets for communication
    # to use UDP: replace SOCK_STREAM with SOCK_DGRAM
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # provide the server with an address in 
        # the form of host IP and port
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    server_name = input("Enter your name: ")
    # set server limit (how many clients can connect at the same time)
    server.listen(1)
    client, address = server.accept()
    # address[0] is the host of the client
    # address[1] is the port of the client
    print(f"Successfully connected to client {address[0]} {address[1]}")

    client_name = client.recv(1024).decode()
    print(f"{client_name} has joined the chat")
    print("Send [e] to exit the chat")
    client.send(server_name.encode())
        
    while 1:
        message = input(f"{server_name}: ")
        if message == "[e]":
            print("You have left the chat.")
            message = "Left the chat."
            client.send(message.encode())
            break
        client.send(message.encode())
        message = client.recv(1024).decode()
        print(f"{client_name}: {message}")
    