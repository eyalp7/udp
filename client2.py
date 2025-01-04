from scapy.layers.inet import IP, UDP
from scapy.sendrecv import send

message = input("input message: ")
num_fragments = int(input("number of fragments: "))

server_address = ('10.0.0.4', 55555)

fragment_size = len(message) // num_fragments
remainder = len(message) % num_fragments

for i in range(num_fragments):
    start_idx = i * fragment_size
    end_idx = (i + 1) * fragment_size
    if i == num_fragments - 1:
        end_idx = len(message)

    fragment = message[start_idx:end_idx]

    udp_packet = IP(dst=server_address[0]) / UDP(dport=server_address[1]) / fragment
    send(udp_packet)
    print(f"sent: {fragment}")

print("message sent successfully")