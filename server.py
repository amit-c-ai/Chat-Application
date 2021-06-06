import socket
import threading
import sys

#list of special commands
commands = {
  " /train/": "sl",
  " /cowsay": "cowsay",
  " /xcowsay": "xcowsay",
  " /cowthink": "cowthink"
}

def help():
    print("Usage: python3 server.py host port")
    print("Ex: python3 server.py 127.0.0.1 1060")
    exit()


#data for connection
if(len(sys.argv)==3):
    host = sys.argv[1]
    port = int(sys.argv[2])
else:
    help()

#Starting the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

#Lists for clients and nicknames
clients = []
nicknames = []

#Sending messages to all connected clients except the one sent message
def broadcast(message, index):
    if(len(message.decode('ascii').split(':')) == 2):
        msg = message.decode('ascii').split(':')[1]
    
        if(msg in commands or msg.split('?')[0] in commands or msg=="emogi -help"):
            for client in clients:
                client.send(message)
        else:
            for client in clients:
                if(clients.index(client)!=index):
                    client.send(message)

    else:
        for client in clients:
            if(clients.index(client)!=index):
                client.send(message)

#Handling messages from clients
def handle(client):
    while(True):
        try:
            #broadcasting messages
            message = client.recv(2048)
            index = clients.index(client)
            broadcast(message, index)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'), index)
            print('{} left the server'.format(nickname))
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
        nickname = client.recv(2048).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        #print and broadcast nickname
        print("Joined person's nickname is {}".format(nickname))
        index = clients.index(client)
        broadcast("{} joined the server!".format(nickname).encode('ascii'), index)
        #client.send("Successfully connected to server!".encode('ascii'))

        #start handling thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening.....")
receive()
            

        
