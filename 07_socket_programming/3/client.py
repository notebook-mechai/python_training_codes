import socket
ip = "127.0.0.1"
port = 5230
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((ip , port))
    data = s.recv(1024)
    print(data.decode('ascii'))
    s.close()
except:
    print("cannot connect to server, please try another time.")

