import socket
import threading

#data for connection
host = input("Enter host address: ")
port = int(input("Enter port(unreserved) number: "))

#Starting the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

#Lists for clients and nicknames
clients = []
nicknames = []

#Sending messages to all connected clients
def broadcast(message, index):
    for client in clients:
        if(clients.index(client)!=index):
            client.send(message)

#Handling messages from clients
def handle(client):
    while(True):
        try:
            #broadcasting messages
            message = client.recv(1024)
            index = clients.index(client)
            broadcast(message, index)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'), index)
            nicknames.remove(nickname)
            break

#receive or listening function
def receive():
    while(True):
        #accept connection
        client, address = server.accept()
        print("connected with {}".format(str(address)))

        #request and store nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        #print and broadcast nickname
        print("your nickname is {}".format(nickname))
        index = clients.index(client)
        broadcast("{} joined the server!".format(nickname).encode('ascii'), index)
        client.send("Successfully connected to server!".encode('ascii'))

        #start handling thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening.....")
receive()
            

        
