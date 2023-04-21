import threading
import socket
host = '127.0.0.1'
port = 54450
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
Aliases = []

# How to send message to all the clients that are connected

def broadcast(message):
    for client in clients:
       client.send(message)


# Functions to handle clients connection
def handle_client(client):
         while True:
             try:
               message = client.recv(1024)
               broadcast(message)
             except:
                index = clients.index(client)
                clients.remove(client)
                alias = Aliases[index]
                broadcast(f'{alias} has left the connection!'.encode('utf-8'))
                Aliases.remove(alias)
                break

# Main function to receive the clients connection

def receive():
        while True:
           print('Server is running and listening for connections..')
           client, address = server.accept()
           print(f'Connection is established with {str(address)}')
           client.send('alias?'.encode('utf-8'))
           alias = client.recv(1024)
           Aliases.append(alias)
           clients.append(client)
           print(f'The alias of this client is {alias}'.encode('utf-8'))
           broadcast(f'{alias} has connected to the game'.encode('utf-8'))
           client.send('You are now connected!'.encode('utf-8'))
           thread = threading.Thread(target = handle_client, args=(client,))
           thread.start()
if __name__ == "__main__":
    receive()
