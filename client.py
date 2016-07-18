import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('chitturi', 80))
print("i got output")
print sock.recv(100) # 100 is bytes of data

sock.close()