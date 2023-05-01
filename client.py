import settings
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

import socket
import threading

HOST = '127.0.0.1'
PORT = 12000
   
KEY = settings.KEY
cipherE = AES.new(KEY, AES.MODE_EAX)
nonceE = cipherE.nonce
   
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
    client.send(nonceE)
    nonceD = client.recv(1024)
    cipherD = AES.new(KEY, AES.MODE_EAX, nonce=nonceD)
    print(f"{server_name} has joined the chat")
    print("Send [e] to exit the chat")

    while 1:
        message = client.recv(1024)
        message = cipherD.decrypt(message)
        print(f"{server_name}: {message.decode()}")
        message = input(f"{client_name}: ")
        if message == "[e]":
            print("You have left the chat.")
            message = "Left the chat."
            message = cipherE.encrypt(message.encode())
            client.send(message)
            break
        message = cipherE.encrypt(message.encode())
        client.send(message)
    