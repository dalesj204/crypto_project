import settings
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

import socket
import threading

HOST = '127.0.0.1'
PORT = 12000


#RSA keys
n, e, p, q, d = settings.generateKeys()

#AES keys
KEY = settings.KEY
cipherE = AES.new(KEY, AES.MODE_EAX)
nonceE = cipherE.nonce
    
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
    #send name
    client.send(server_name.encode())
    #recieve and send public keys
    nE = int(client.recv(1024).decode())
    client.send(str(n).encode())
    eE = int(client.recv(1024).decode())
    client.send(str(e).encode())
    #recieve AES key, encode to convert from int to byte
    nonceD = settings.rsaDecrypt(client.recv(1024).decode(), n, p, q, d)
    print(nonceD)
    print(nonceD.encode())
    #send personal AES key, decode to convert from byte to int
    #client.send(settings.rsaEncrypt(nonceE.decode(), nE, eE))
    client.send(str(settings.rsaEncrypt(nonceE, nE, eE)).encode())
    cipherD = AES.new(KEY, AES.MODE_EAX, nonce=nonceD)
        
    while 1:
        message = input(f"{server_name}: ")
        if message == "[e]":
            print("You have left the chat.")
            message = "Left the chat."
            message = cipherE.encrypt(message.encode())
            client.send(message)
            break
        message = cipherE.encrypt(message.encode())
        client.send(message)

        message = client.recv(1024)
        message = cipherD.decrypt(message)
        print(f"{client_name}: {message.decode()}")