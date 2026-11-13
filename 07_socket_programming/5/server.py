import socket

HOST = '127.0.0.1'
PORT = 8521
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.bind((HOST , PORT))
tcpSocket.listen(5)
connection, client = tcpSocket.accept()
print("Got connection from {}".format(client))

while True:
    data = connection.recv(1024).decode()
    if data == "!":
        break
    
    print("Received: ", data)
    connection.send("operations successfully".encode())

print("Goodbye")
connection.close()