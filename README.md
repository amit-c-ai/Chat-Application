# Chat-Application #

![alt text](https://github.com/amit-c-ai/Chat-Application/blob/main/images/demo.png)

_This is an implementation of server-client [Chat-Application](https://github.com/amit-c-ai/Chat-Application) using socket programming and some concepts
of multi-threading.
Basic idea of creating a chat-room is that create a [server](https://github.com/amit-c-ai/Chat-Application/blob/main/server.py) script and a [client](https://github.com/amit-c-ai/Chat-Application/blob/main/client.py) script. Server will act as a mediator, all clients will send messages to server and then
server will send messages to all clients connected to it._

_At this point everything works fine but on localhost. We can't send messages to person whose ip-address is not in out network.
Reason:_

    To connect to an ip-address, it should be a public ip for example google, amazon, etc. 
    But our ip-address is local provided by our ISP(Internet Service Provider). So we to
    connect to the server you created it should be hosted on public domain.
   
_This problem is solved by using ngrok, it basically gives us a public ip and tunnels the traffic at this ip to the post number we mention.
We host the server at our localhost and some port (you'll understand after the example) and ngrok will tunnel the clients at its public ip
to our localhost and mentioned port. We just need to share public ip and port (given by ngrok) to our friends._
   
* __installation:__ 
  * _clone this repository_
  * _install python for linux from [here](https://docs.python-guide.org/starting/install3/linux/)_
  * _open terminal and write "sh install.sh" without quotes_
  * _download ngrok from [here](https://ngrok.com/download) and follow the procedure as mentioned on the page_
  
* __get public ip:__
  * _first complete the procedure mentioned [here](https://ngrok.com/download)_
  * _go to ngrok directory and write "./ngrok tcp 1060" without quotes_

After this you'll see screen like [this](https://github.com/amit-c-ai/Chat-Application/blob/main/images/ngrok.png)

highlighted line in image is the public domain and port(seperated by ':') you got and it is directed to localhost port 1060.
Now server should be hosted at localhost 1060 and client should connect at ngrok-domain and port.

* __hosting server:__
  * _open a new terminal in cloned directory_
  * _command: python3 server.py 0.0.0.0 1060_
  * _server will start listening, [ex](https://github.com/amit-c-ai/Chat-Application/blob/main/images/server.png)_
 
* __join server as client:__
  * _open a new terminal in cloned directory_
  * _command: python3 client.py ngrok-domain port nickname_
  * _[Example](https://github.com/amit-c-ai/Chat-Application/blob/main/images/client.png)_
  
* __features:__
  * _large number of peope can join the server_
  * _as it uses tcp to connect, it is guaranteed that no messages will be lost
  * _emogi supported texts using some commands (type "emogi -help" without quotes)_
  * _supports some exciting linux commands, use following commands in chat:_
    * /train/
    * /cowsay?Hello/
    * cowsay -help
    * /xcowsay?hello/  (cowsay and xcowsay have same commands just use xcowsay in place of cowsay)
    * /cowthink?hello/ (cowsay and cowthink have same commands just use cowthink in place of cowsay)
    * /xeyes/
 
 * __bugs:__
   * _if only one client is connected and sends message, then it will go in infinite loop and server is crashed_
   * _if we write message on out terminal and someone's message comes then is get printed on the line we were writing_
   
 * __to prevent 2nd bug:_
   * _open two terminal and redirect output of 1st terminal to 2nd
   * run client script on 1st terminal and write your messages there
   * see others messages on 2nd terminal
   * you can achieve this using [tty command](https://unix.stackexchange.com/questions/261531/how-to-send-output-from-one-terminal-to-another-without-making-any-new-pipe-or-f)
  
  
