import socket

target = input("Target:")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect_ex((target, 22))
print(sock.recv(2048))
sock.close()
