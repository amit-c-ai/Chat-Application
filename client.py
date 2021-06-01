import socket
import threading
import time

#entering nickname
nickname = input("Choose your nickname: ")

#connecting to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = input("Enter exact address at which server is running: ")
port = int(input("Enter exact port at which server is running: "))
client.connect((address, port))

#listening to server and sending nickname
def receive():
    while(True):
        try:
            # recieve message from server
            # if 'NICK' then send nickname
            message = client.recv(2048).decode('ascii')
            if(message == "NICK"):
                client.send(nickname.encode('ascii'))
            else:
                print('\r{}\n{} : '.format(message, nickname))
        except:
            #close connection when error
            print("An error occured!")
            client.close()
            break

# sending messages to server
def write():
    while(True):
        time.sleep(0.5)
        message = input('')
        client.send('{} : {}'.format(nickname, message).encode('ascii'))

#starting threads for listening and writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
