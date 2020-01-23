import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'TERUMICHI UNCHI', ('192.168.170.58', 51452))
