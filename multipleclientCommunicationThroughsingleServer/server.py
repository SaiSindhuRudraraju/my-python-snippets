import socket
from threading import Thread

dictOf_AllClients = {}
clientNo = 0

class ChildThread(Thread):
    def run(self):
        while True:
            for key in list(dictOf_AllClients.keys()):
                try:
                    dictOf_AllClients[key].settimeout(0.1)
                    '''
                        settimeout(seconds) is a method in Python's socket module that sets a maximum amount of time (in seconds) that a socket operation like recv() or send() can block (wait).
                        if you don't set a timeout, this line will wait forever for a client to send something. That would block your thread, and other clients would not get checked in that loop.
                        So by setting a short timeout:
                        You're telling Python: "If the client hasn't sent anything in 0.1 seconds, skip and move on to the next client."
                        This keeps the server responsive and fair to all connected clients.
                    '''
                    
                    data = dictOf_AllClients[key].recv(1024).decode()
                    if data:
                        if(data == 'exit'):
                            del dictOf_AllClients[key]
                            print(f"Client {key} exited. Current available Clients: {list(dictOf_AllClients.keys())}")
                            for clientId in iter(dictOf_AllClients.keys()):
                                try:
                                    dictOf_AllClients[clientId].send(
                                        f"Client {key} exited. Current available Clients: {list(dictOf_AllClients.keys())}".encode()
                                    )
                                except:
                                    pass
                        else:
                            info = data.split(",", 1)
                            if len(info) == 2:
                                client_tosend_message = int(info[0].strip())
                                message = info[1].strip()
                                if client_tosend_message in dictOf_AllClients:
                                    dictOf_AllClients[client_tosend_message].send(f"From Client {key} : {message}".encode())
                                else:
                                    dictOf_AllClients[key].send(f"Client {client_tosend_message} not available.".encode())

                    dictOf_AllClients[key].settimeout(None)
                    '''
                        resets the socket to blocking mode (the default mode), which means:
                            "From now on, wait forever for data — no timeout.”
                        it's good practice to clean up and not leave sockets in a modified state (e.g., in timeout mode).
                    '''
                except:
                    continue

server_socketObj = socket.socket()
server_socketObj.bind(("localhost", 8080))
server_socketObj.listen()

print("Server started. Waiting for Clients to Connect...")

child = ChildThread()
child.start()

while True:
    client_socketObj, addr = server_socketObj.accept()
    clientNo += 1
    dictOf_AllClients[clientNo] = client_socketObj
    print(f"Client {clientNo} connected from {addr}")
    for clientId in iter(dictOf_AllClients.keys()):
        try:
            dictOf_AllClients[clientId].send(
                f"Client {clientNo} connected. Current available Clients: {list(dictOf_AllClients.keys())}".encode()
            )
        except:
            pass