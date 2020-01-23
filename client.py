import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('192.168.170.58', 51452))
    s.sendall(b'TERUMICHI UNKO')

    data = s.recv(1024)
    if data:
        print(data)
