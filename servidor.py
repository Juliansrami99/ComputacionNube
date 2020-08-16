import socket                   # Import socket module


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyaddr("34.201.174.108")[0]
port = 10000
serversocket.bind((host, port))

print ('Server listening....')


serversocket.listen(5)
print ('server started and listening')
while 1:
    (clientsocket, address) = serversocket.accept()
    try:
        f = open("saldo.txt", "r")
        a=f.read()
        saldo=int(a)
        print ("connection found!")
        r='para cosultar saldo escriba: saldo \n para debitar escriba: debitar \n para acreditar escriba: acreditar'
        clientsocket.send(r.encode())        
        data = clientsocket.recv(1024).decode()
        print (data)
        if str(data)=="saldo":
            sal=str(saldo)
            sal="su saldo es igual a: "+sal
            clientsocket.send(sal.encode())
        elif str(data)=="debitar":
            sal="cant"
            clientsocket.send(sal.encode())
            data = clientsocket.recv(1024).decode()
            if int(data)<=saldo:
                nuevo=saldo-int(data)
                with open("saldo.txt", "w") as text_file:
                    text_file.write(str(nuevo))
                bb="corr"
                clientsocket.send(bb.encode())
            else:
                bb="incorr"
                clientsocket.send(bb.encode())
        elif str(data)=="acreditar":
            credito = "credito"
            clientsocket.send(credito.encode())
            data = clientsocket.recv(1024).decode()
            nuevo = saldo + int(data)
            nuevo=str(nuevo)
            with open("saldo.txt","w") as text_file:
                text_file.write(str(nuevo))
            clientsocket.send(nuevo.encode())
        else:
            sal="mal"
            clientsocket.send(sal.encode()) 
    finally:
        clientsocket.close()
