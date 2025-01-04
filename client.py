from scapy.layers.inet import IP, UDP
from scapy.sendrecv import send
import time

SERVER_IP = "10.0.0.7"

def send_message(msg):
    """Sends each character of the message as a UDP packet with its ASCII value and position."""
    for index, char in enumerate(msg):
        ascii_value = ord(char)  # Convert the character to its ASCII value.
        udp_pkt = IP(dst=SERVER_IP) / UDP(dport=ascii_value, sport=index)

        send(udp_pkt) 
        time.sleep(0.1)

if __name__ == "__main__":
    user_msg = input("Enter your message: ")
    send_message(user_msg)
