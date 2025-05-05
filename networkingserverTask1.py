import socket

socket_obj = socket.socket()
socket_obj.bind(('localhost', 8080))
socket_obj.listen(5)
print("Server is listening on port 8080")

while True:
    client_socket, addr = socket_obj.accept()
    print(f"Connection from {addr} has been established.")
    client_socket.send(bytes("Welcome to the server!", "utf-8"))

    while True:
        data = client_socket.recv(1024)
        message = data.decode("utf-8")
        print(f"Client said: {message}")
        if message.lower() == "exit":
            print("Client has exited the chat.")
            break
        response = message + " from server"
        client_socket.send(bytes(response, "utf-8"))