import socket

HOST = '127.0.0.1'
PORT = 6523
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.connect((HOST, PORT))
while True:
    msg = input()
    if msg == "~":
        break
    try:
        tcpSocket.send(msg.encode())
    except:
        print("connection lost!")
        break
    
tcpSocket.close()