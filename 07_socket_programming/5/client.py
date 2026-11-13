import socket
from multiprocessing import Process

HOST = '127.0.0.1'
PORT = 14005
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.connect((HOST, PORT))

def recv():
    while True:
        data = tcpSocket.recv(1024)
        print("server send for you: ", data.decode())
    
p = Process(target=recv)
p.start()

while True:
    msg = input()
    if msg == "~":
        tcpSocket.send("!".encode())
        break
    try:
        tcpSocket.send(msg.encode())
    except:
        print("connection lost!")
        break
    
    if msg == "!":
        p.terminate()
    
tcpSocket.close()
p.terminate() 