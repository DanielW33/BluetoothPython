import socket
CSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CSocket.connect((socket.gethostname(), 1234))

while True:
    Message = CSocket.recv(8)
    print(Message.decode("utf-8"))
