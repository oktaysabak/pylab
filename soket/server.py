import socket
import urllib.request
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#test client-server start
""" print(socket.gethostname())
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("welcome to the server.", "utf-8"))
    clientsocket.close() """
# test client-server end
print("Lets Find the site IP address!")
s.connect(('google.com',80))

my_local_ip = s.getsockname()[0]
print(f"Your Local IP: {my_local_ip}")
print(f"Your External IP: {external_ip}")
print("Write website name to resolve Ip address!")


try:
    web_site = input("For Example: (www.google.com): ")
    web_site_ip = socket.gethostbyname(web_site)
    print(f"Web site: {web_site} ip address: {web_site_ip}")
except socket.gaierror:
    print("Wrong web site name...")
