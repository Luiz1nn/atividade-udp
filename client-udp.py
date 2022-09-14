from base64 import encode
import socket
import string

def main():
    HOST = '192.168.1.6'
    PORT = 5000
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST, PORT)
    print ('\n...Para sair digite "exit"...\n')
    
    print("Digite 'connect' para conectar")
    
    while True:
        connectionString = input("--> ")
    
        if connectionString != 'connect':    
            print("Digitação errada, digite 'connect' para continuar!")
        else:
            username = input('User --> ')
            udp.sendto(username.encode(), dest)
            print('\nConectado')
            break

    print("\nDigite 'register' para entrar na lista\n")
    while True:
        passw = input("--> ")
        if passw != 'register':
            print("Palavra errada! Digite a palavra 'register' para entrar na lista!")
            
        else:
            print("Você entrou na lista!")
            break

    print("\nDigite 'unsubscribe' para sair da lista\n")
    while True:
        passw = input("--> ")
        if passw != 'unsubscribe':
            print("Palavra errada! Digite a palavra 'unsubscribe' para sair da lista!")
            
        else:
            print("Você saiu da lista!")
            break
    
    while True:
        sendMsg(udp, username)   

def receiveMsg (udp):
    while True:
        try: 
            
            msg = udp.recv(1024).decode('utf-8')
            print(msg+'\n')
        except:
            udp.close()
            print("\n Obrigado! volte sempre.")
            break

def sendMsg (udp, username):
    while True:
        try:          
                msg = input("\n")
                if msg != 'exit':
                    msg = udp.sendto(f'<{username}> {msg}'.encode('utf-8'))
                else:
                    udp.close()
                    break
        except:
            return
main()

## By Luiz1nn