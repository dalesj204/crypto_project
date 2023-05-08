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
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # connect to the server
    try:
        client.connect((HOST, PORT))
        print("Successfully connected to server")
    except:
        print(f"Unable to connect to server {HOST} {PORT}")

    client_name = input("Enter your name: ")
    #send and recieve names
    client.send(client_name.encode())
    server_name = client.recv(1024).decode()
    #send and receieve public keys
    client.send(str(n).encode())
    nE = int(client.recv(1024).decode())
    client.send(str(e).encode())
    eE = int(client.recv(1024).decode())
    #send personal AES key, decode to convert from bytes to int
    client.send(str(settings.rsaEncrypt(nonceE, nE, eE)).encode())
    #client.send(settings.rsaEncrypt(nonceE.decode(), nE, eE).encode())
    #recieve AES key for decryption, encode to convert from int to bytes
    #nonceD = settings.rsaDecrypt(client.recv(1024).decode(), n, p, q, d).encode()
    nonceD = settings.rsaDecrypt(client.recv(1024).decode(), n, p, q, d)
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
    