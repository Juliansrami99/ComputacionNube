from socket import *
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
host=socket.gethostbyaddr("34.201.174.108")[0]
server_address = (host, 10000)
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
            print("OK")
        elif resul=='incorr':
            print("Saldo insuficiente")
    elif resultado=="credito":
        print("mencione el credito que desea aumentar a su cuenta:")
        str = input("S: ")
        sock.send(str.encode());
        resul = ''
        resul=sock.recv(1024).decode()
        if resul == 'corr':
            new_saldo = sock.recv(1024).decode()
            print("Nuevo saldo: ",new_saldo)
    else:        
        print(resultado)
finally:
    print('closing socket')
    sock.close()
