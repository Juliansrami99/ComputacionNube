from socket import *
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ("192.168.10.13", 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    recibido=''
    recibido=sock.recv(1024).decode()
    print(recibido)
    str = input("S: ")
    sock.send(str.encode());
    resultado=''
    resultado=sock.recv(1024).decode()
    if resultado=="cant":
        print("mencione cuanto desea debitar de su cuenta:")
        str = input("S: ")
        sock.send(str.encode());
        resul=''
        resul=sock.recv(1024).decode()
        if resul=='corr':
            print("debito realizado")
    else:        
        print(resultado)
finally:
    print('closing socket')
    sock.close()
