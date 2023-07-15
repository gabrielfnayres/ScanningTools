import socket

target = input("Target:")

ports = [22, 80, 443, 53, 21, 23, 8080]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    sock.close()
    if (result == 0):
        print(port)