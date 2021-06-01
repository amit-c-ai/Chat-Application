#!/usr/bin/env python3

import threading
import socket
import argparse
import os


class Server(threading.Thread):
    
    # data for connection
    def __init__(self, host, port):
        super().__init__()
        self.clients = []
        self.host = host
        self.port = port

    # starting the server
    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.host, self.port))

        server.listen(1)
        print('Listening at', server.getsockname(), '.....')

        while True:

            # Accept new connection
            client, address = server.accept()
            print('Accepted a new connection from {} to {}'.format(client.getpeername(), client.getsockname()))

            # Create new thread
            server_socket = ServerSocket(client, address, self)
            
            # Start new thread
            server_socket.start()

            # Add thread to active connections
            self.clients.append(server_socket)
            print('Ready to receive messages from', client.getpeername())

    def broadcast(self, message, source):
        for client in self.clients:
            # Send to all connected clients except the source client
            if client.address != source:
                client.send(message)
    
    def remove_client(self, client):
        self.clients.remove(client)


class ServerSocket(threading.Thread):
    def __init__(self, client, address, server):
        super().__init__()
        self.client = client
        self.address = address
        self.server = server
    
    def run(self):
        while True:
            message = self.client.recv(2048).decode('ascii')
            if message:
                print('{} says {!r}'.format(self.address, message))
                self.server.broadcast(message, self.address)
            else:
                # Client has closed the socket, exit the thread
                print('{} has closed the connection'.format(self.address))
                self.client.close()
                server.remove_client(self)
                return
    
    def send(self, message):
        self.client.sendall(message.encode('ascii'))


def exit(server):
    while True:
        ipt = input('')
        if ipt == 'A':
            print('Closing all connections...')
            for client in server.clients:
                client.client.close()
            print('Shutting down the server...')
            os._exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Chatroom Server')
    parser.add_argument('host', help='Interface the server listens at')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()

    # Create and start server thread
    server = Server(args.host, args.p)
    server.start()

    exit = threading.Thread(target = exit, args = (server,))
    exit.start()
