from scapy.all import Ether, IP, TCP, Raw
import socket

def craft_packet():
    # Ethernet header
    src_mac = "00:00:00:00:00:00"  # Replace with random MAC address
    dst_mac = "00:00:00:00:00:00"  # Replace with random MAC address
    ether = Ether(src=src_mac, dst=dst_mac)

    # IP header
    version = 0b100
    ihl = 0b101  # Header length in 32-bit words (5 * 4 = 20 bytes)
    tos = 0x0  # Manually set Type of Service (leave as None to use random)
    total_length = 0x0  # Manually set Total length of packet (leave as None to use random)
    identification = 0x1234  # Manually set Identification (leave as None to use random)
    flags = 0b10  # Manually set Flags (leave as None to use random)
    frag = 0b0  # Manually set Fragment Offset (leave as None to use random)
    ttl = 0x40  # Manually set Time to Live (TTL) (leave as None to use random)
    proto = 0x6  # Manually set Protocol (e.g., 6 for TCP, 17 for UDP) (leave as None to use random)
    checksum = 0xa570  # Manually set Checksum (leave as None to calculate automatically)
    src_ip = 0xc0a80101  # Manually set Source IP Address (leave as None to use random)
    dst_ip = 0xc0a80102  # Manually set Destination IP Address (leave as None to use random)

    ip = IP(version=version, ihl=ihl, tos=tos, len=total_length, id=identification,
            flags=flags, frag=frag, ttl=ttl, proto=proto, chksum=checksum,
            src=src_ip, dst=dst_ip)

    # Transport Layer header (TCP)
    sport = 12336  # Source Port
    dport = 80  # Destination Port
    seq = 0  # Sequence Number
    ack = 0  # Acknowledgment Number
    dataofs = 5  # Data Offset (5 * 32-bit words)
    reserved = 0  # Reserved (3 bits)
    window = 65280  # Window Size
    urgptr = 0  # Urgent Pointer

    tcp = TCP(sport=sport, dport=dport, seq=seq, ack=ack, dataofs=dataofs,
              reserved=reserved, window=window, urgptr=urgptr)

    # Payload (PowerShell command)
    payload = "Invoke-Expression -Command \"Write-Host 'Hello, World!'\""

    # Construct the packet
    packet = ether / ip / tcp / Raw(load=payload)
    return packet

# Example usage:
packet = craft_packet()
print(packet.show())  # Display packet details
