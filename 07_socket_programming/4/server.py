import socket

HOST = '127.0.0.1'
PORT = 6523
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.bind((HOST , PORT))
tcpSocket.listen(5)
connection, client = tcpSocket.accept()
print("Got connection from {}".format(client))

while True:
    data = connection.recv(1024).decode()
    print("Received: ", data)
    if data == "!":
        break

connection.close()