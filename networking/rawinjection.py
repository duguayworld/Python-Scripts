import socket
import struct

# Creating a rawSocket for communications
# PF_PACKET (packet interface), SOCK_RAW (Raw socket) - htons (protocol) 0x0800 = IP Protocol
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

# Deciding interface - packet sniffing and then injection
rawSocket.bind(("wlan1", socket.htons(0x0800)))

# Create an Ethernet packet
packet = struct.pack("!6s6s2s", b'\x00\xbc\x8d\x15', b'\x9e\xdc\x88\xf0', b'\x08\x00')
# 6 dest address, 6 source address, and 2 for ethertype = IP

# Inject a random string after the header
rawSocket.send(packet + b"Hello fucking world")
