import socket

HOST, PORT = '127.0.0.1', 8000
clientMessage = 'Hello!'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(clientMessage.encode())
    serverMessage = str(client.recv(1024), encoding='utf-8')
    print('Server:', serverMessage)
