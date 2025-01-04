import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 55555)
server_socket.bind(server_address)

print("listening on port 55555...")

while True:
    data, address = server_socket.recvfrom(4096)
    print(f"received {data.decode()} from: {address}")