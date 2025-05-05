'''
    networking: communication between one or more systems/software.

    Server: is a software which takes request and gives response.

    types:
        Os servers,. this will help you to operate systems ovewr the network.
            Ex: win-2000, win-2008, linux, ubuntu etc
        database servers: ussed to store data in a structured format. over the network.
            Oracle, sql server, mysql, postgresql, mongodb.
        web servers/ application server used to host web applications over the network.
            apache, nginx, websphere, tomcat, weblogic, IIS

    Client: is a software which sends request and gets response.

    IP Address:  is a unique address asigned to each system over the network.
    (Ip address will be assigned by router)

    Protocol: is a set of rules which helps in transfering the data over the network.
        Http, HTTPS, FTP, SFTP, SMTP, POP3, IMAP, SNMP, DHCP, tcp/ip, UDP

    Port Number: is a unique number to identify the server/client software over the network.

'''

import socket

socket_obj = socket.socket()
socket_obj.bind(('localhost', 8080))
socket_obj.listen(5)
print("server is listining on port 8080")

while True:
    client_socket ,  addr = socket_obj.accept()
    print(f"Connection from {addr} has been established.")
    client_socket.send(bytes("Welcome to the server!", "utf-8"))
    while True:
        data = client_socket.recv(1024)
        str = data.decode("utf-8")
        print(str)
        if str.lower() == "exit":
            print("Client has exited the chat.")
            break

socket_obj.close()

"""
"Question : two way communication. client -> sends 'hello' to server. server have to send 'hello from server' -


2) send read product detaiuls in the client and send product object to the server and server should display the product details. this should be continuous. 
"""