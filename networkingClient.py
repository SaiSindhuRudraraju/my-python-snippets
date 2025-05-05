import socket

socket_obj = socket.socket()
socket_obj.connect(('localhost', 8080))
print("Connected to the server")

data = socket_obj.recv(1024)
print(data.decode("utf-8"))

while True:
    message = input("Enter message to send to server (type 'exit' to quit): ")
    socket_obj.send(bytes(message, "utf-8"))
    if message.lower() == 'exit' : 
        print("Exiting the chat.")
        break

socket_obj.close()