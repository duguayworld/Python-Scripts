import socket
import struct
import binascii

# Creating a rawSocket for communications
# PF_PACKET (packet interface), SOCK_RAW (Raw socket) - htons (protocol) 0x0800 = IP Protocol
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

# Read a packet with recvfrom method
pkt = rawSocket.recvfrom(2048)  # Tuple return

# Ethernet Header tuple segmentation
eHeader = pkt[0][0:14]

# Parsing using unpack
eth_hdr = struct.unpack("!6s6s2s", eHeader)  # 6 dest MAC, 6 host MAC, 2 ethType

# Using hexlify to convert the tuple value NBO into Hex format
dest_mac = binascii.hexlify(eth_hdr[0]).decode()
src_mac = binascii.hexlify(eth_hdr[1]).decode()
eth_type = binascii.hexlify(eth_hdr[2]).decode()

print("Destination MAC address:", dest_mac)
print("Source MAC address:", src_mac)
print("Ethernet type:", eth_type)

ipHeader = pkt[0][14:34]
ip_hdr = struct.unpack("!12s4s4s", ipHeader)  # 12s represents Identification, Time to Live, Protocol | Flags, Fragment Offset, Header Checksum

print("Source IP address:", socket.inet_ntoa(ip_hdr[1]))  # Network to ASCII conversion
print("Destination IP address:", socket.inet_ntoa(ip_hdr[2]))  # Network to ASCII conversion

# Unpack the TCP header (source and destination port numbers)
tcpHeader = pkt[0][34:54]
tcp_hdr = struct.unpack("!HH16s", tcpHeader)

print("Source Port:", tcp_hdr[0])
print("Destination Port:", tcp_hdr[1])
