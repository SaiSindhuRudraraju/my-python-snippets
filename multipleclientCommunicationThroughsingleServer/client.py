import socket
import sys
from threading import Thread

class Childthread(Thread):
    def __init__(self, socket_Obj):
        Thread.__init__(self)
        self.socket_Obj = socket_Obj

    def run(self):
        while True:
            try:
                data = self.socket_Obj.recv(1024).decode()
                if data.lower() == "exit":
                    break
                print("\n", data)
            except:
                break

socket_Obj = socket.socket()
socket_Obj.connect(("localhost", 8080))

threadObj = Childthread(socket_Obj)
threadObj.start()

while True:
    msg = input("Enter message (client id, message): ")
    if msg.strip().lower() == "exit":
        socket_Obj.send("exit".encode())
        break
    socket_Obj.send(msg.encode())

sys.exit()