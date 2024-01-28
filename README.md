# Basic server-client chat program
This program simulates a basic chat program between a client and a server. 

To run the program:  
* open two terminals, one for the server and one for the client
* install the Pycryptodome library for AES implementation using the command **pip install pycryptodome**
* on one terminal, run **python3 server.py** and enter your name
* on the other terminal, run **python3 client.py** and enter your name
* once the client connects, the server and client can now send alternating messages (server sends the first message)
* **[e]** can be entered to leave the chat  

Limitations:
* one user (client/server) cannot send consecutive messages, only alternating
* server has to initiate the messaging  

Future improvements:
* users can send consecutive messages
* users can exit the chat at any time, rather than exiting during their turn to send a message
* multiple clients can join the chat

