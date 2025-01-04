from scapy.all import sniff
from scapy.layers.inet import IP, UDP

received_message = {}

def handle_packet_with_index(pkt):
    """Processes UDP packets, extracts characters, and reconstructs the message."""
    if UDP in pkt and IP in pkt:
        dport = pkt[UDP].dport
        index = pkt[UDP].sport

        if 32 <= dport <= 126:  # Ensure the destination port corresponds to a printable ASCII character.
            received_message[index] = chr(dport)  # Store the character in the dictionary with its index.

            # Reconstruct the message by sorting indices and joining characters.
            message = ''.join(received_message[i] for i in sorted(received_message))
            print(f"Current message: {message}")  # Print the reconstructed message.

def start_sniffing():
    """Starts listening for UDP packets and processes them."""
    print("Waiting for messages...")
    # Capture UDP packets and pass them to the handle_pkt_with_index function for processing.
    sniff(filter="udp", iface=None, prn=handle_packet_with_index)

if __name__ == "__main__":
    start_sniffing()
