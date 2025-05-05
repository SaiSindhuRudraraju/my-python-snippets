import socket
import pickle

socket_obj = socket.socket()
socket_obj.bind(('localhost', 8080))
socket_obj.listen(5)
print("Server is listening on port 8080")

while True:
    client_socket, addr = socket_obj.accept()
    print(f"Connection from {addr} has been established.")

    while True:
        try:
            data = client_socket.recv(4096)
            product = pickle.loads(data)
            print("Product: ", product)
        except:
            print("Client exited the chat.")
            break
client_socket.close()