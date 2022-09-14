import socket

clients = []

def main():

    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 5000
    orig = (HOST, PORT)
    try:
        udp.bind(orig)
    except:
        return print("Algo deu errado!")

    while True:
        client, addr = udp.recvfrom(1024)
        print("Conexão recebida de", addr)
        clients.append(client)

def manageMsg(client):
    while True:
        try:
            msg = client.recvfrom(1024)
            streaming(msg, client)
        except:
            deleteClient(client)
            break
 
def streaming(msg, client):
    for numClient in clients:
        if numClient != client:
            try:
                numClient.sendto(msg)
            except:
                deleteClient(client)

def deleteClient(client):
    clients.remove(client)

main()

## By Luiz1nn