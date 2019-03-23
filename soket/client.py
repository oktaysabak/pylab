import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    s.connect((socket.gethostname(), 1234))

    all_msg = ''
    while True:
        msg = s.recv(8)
        if len(msg)<=0:
            break
        all_msg += msg.decode("utf-8")
    print(all_msg)
except ConnectionRefusedError:
    print("Server is closed...")