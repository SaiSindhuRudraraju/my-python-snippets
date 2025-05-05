import socket
import pickle
from product import Product

socket_obj = socket.socket()
socket_obj.connect(('localhost', 8080))
print("Connected to the server")

while True:
    pid = int(input("Enter pid: "))
    name = input("Enter name: ")
    price = float(input("Enter price: "))
    
    product = Product(pid, name, price)
    socket_obj.send(pickle.dumps(product))
    ch = input("Do you want to continue: y/n: ")
    if(ch == 'n'):
        print("Exiting the chat.")
        break

socket_obj.close()