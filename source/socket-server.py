import socket

HOST, PORT = '192.168.50.130', 8000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)

try:
    while True:
        conn, addr = server.accept()
        clientMessage = str(conn.recv(1024), encoding='utf-8')
        print('Client message is:', clientMessage)
        serverMessage = 'reply from server.'
        conn.sendall(serverMessage.encode())
        conn.close()
except KeyboardInterrupt as e:
    print('Server Close.')
finally:
    server.close()
