import socket
import threading
import time
import subprocess
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[39m'
    
def help():
    print("Usage : python3 client.py address port")
    print("Ex: python3 client.py 192.168.5.103 5555")

def getDefaultName():
    nickname=subprocess.check_output(['whoami']).decode('ascii')[:-1]
    return nickname

#entering nickname
nickname=''
if(len(sys.argv)==4):
    nickname = sys.argv[3]
elif(len(sys.argv)==3):
    nickname=getDefaultName()
else:
    help()

subprocess.run(["cat", "file.txt"])

'''print("\n\n\n" + bcolors.HEADER + "Hello")
print("\n\n\n" + bcolors.OKBLUE + "Hello")
print("\n\n\n" + bcolors.OKCYAN + "Hello")
print("\n\n\n" + bcolors.OKGREEN + "Hello")
print("\n\n\n" + bcolors.WARNING + "Hello")
print("\n\n\n" + bcolors.FAIL + "Hello")
print("\n\n\n" + bcolors.ENDC + "Hello")
print("\n\n\n" + bcolors.BOLD + "Hello")
print("\n\n\n" + bcolors.UNDERLINE + "Hello")'''

#connecting to server
address = sys.argv[1]
port = int(sys.argv[2])
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((address, port))

#list of special commands
commands = {
  " /train/": "sl",
  " /cowsay": "cowsay",
  " /xcowsay": "xcowsay",
  " /cowthink": "cowthink"
}

#list of emogis
emogis = {
    "$grinning face$": "\U0001F600",
    "$grinning face with big eyes$": "\U0001F603",
    "$grinning face with smiling eyes$": "\U0001F604",
    "$beaming face with smiling eyes$": "\U0001F601",
    "$grinning squinting face$": "\U0001F606",
    "$grinning face with sweat$": "\U0001F605",
    "$rolling on the floor laughing$": "\U0001F923",
    "$face with tears of joy$": "\U0001F602",
    "$slightly smiling face$": "\U0001F642",
    "$upside-down face$": "\U0001F643",
    "$winking face$": "\U0001F609",
    "$smiling face with smiling eyes$": "\U0001F60A",
    "$smiling face with halo$": "\U0001F607",
    "$smiling face with 3 hearts$": "\U0001F970",
    "$smiling face with heart-eyes$": "\U0001F60D",
    "$star-struck$": "\U0001F929",
    "$face blowing a kiss$": "\U0001F618",
    "$kissing face$": "\U0001F617",
    "$smiling face$": "\U0000263A",
    "$kissing face with closed eyes$": "\U0001F61A",
    "$kissing face with smiling eyes$": "\U0001F619",
    "$face savoring food$": "\U0001F60B",
    "$face with tongue$": "\U0001F61B",
    "$winking face with tongue$": "\U0001F61C",
    "$zany face$": "\U0001F92A",
    "$squinting face with tongue$": "\U0001F61D",
    "$money-mouth face$": "\U0001F911",
    "$hugging face$": "\U0001F917",
    "$face with hand over mouth$": "\U0001F92D",
    "$shushing face$": "\U0001F92B",
    "$thinking face$": "\U0001F914",
    "$zipper-mouth face$": "\U0001F910",
    "$face with raised eyebrow$": "\U0001F928",
    "$neutral face$": "\U0001F610",
    "$expressionless face$": "\U0001F611",
    "$face without mouth$": "\U0001F636",
    "$smirking face$": "\U0001F60F",
    "$unamused face$": "\U0001F612",
    "$face with rolling eyes$": "\U0001F644",
    "$grimacing face$": "\U0001F62C",
    "$lying face$": "\U0001F925",
    "$relieved face$": "\U0001F60C",
    "$pensive face$": "\U0001F614",
    "$sleepy face$": "\U0001F62A",
    "$drooling face$": "\U0001F924",
    "$sleeping face$": "\U0001F634",
    "$face with medical mask$": "\U0001F637",
    "$face with thermometer$": "\U0001F912",
    "$face with head-bandage$": "\U0001F915",
    "$nauseated face$": "\U0001F922",
}

#emogi help
def emogihelp():
    print(" ","\t",end='')
    for i in range(46):
        print(bcolors.OKGREEN+"-", end='')
    print("")
    for emogi in emogis:
        print("\t", bcolors.OKGREEN+"|", bcolors.WHITE+' {:<33}'.format(emogi),": ", emogis[emogi], bcolors.OKGREEN +" |")
    print(" ", "\t",end='')
    for i in range(46):
        print(bcolors.OKGREEN+"-", end='')
    print("")

#modify message with emogis
def modify(message):
    for emogi in emogis:
        if(message.find(emogi)!=-1):
            message = message.replace(emogi, emogis[emogi], message.count(emogi))
    return message

#listening to server and sending nickname
def receive():
    while(True):
        try:
            # recieve message from server
            # if 'NICK' then send nickname
            message = client.recv(2048).decode('ascii')
            modify(message)
            if(len(message.split(':'))==2):
                msg = message.split(':')[1]
                if(msg in commands):
                    subprocess.run([commands[msg]])
                elif(msg.split('?')[0] in commands):
                    subprocess.run([commands[msg.split('?')[0]], msg.split('?')[1][:-1]])
                if(msg == " emogi -help"):
                    emogihelp()
                    
            if(message == "NICK"):
                client.send(nickname.encode('ascii'))            
            else:
                final = str(bcolors.OKBLUE + '\r-----[' + bcolors.OKGREEN + '{}'.format(message) + bcolors.OKBLUE + ' ]-----\n-----[' + bcolors.WARNING + ' {} : '.format(nickname))
                print("{:>120}".format(final), end='')
        except KeyboardInterrupt:  
            #close connection when error
            #client.send("{} left!".format(nickname).encode('ascii'))
            print("Thanks for Using the Application!")
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
