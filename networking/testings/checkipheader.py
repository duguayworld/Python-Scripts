# Import necessary modules
import struct

# Function to get the protocol value based on the protocol name
def get_protocol_value(protocol_name):
    protocols = {"TCP": 0x06, "ICMP": 0x01}
    return protocols.get(protocol_name, None)

# Function to calculate the IP header checksum
def calculate_checksum(ip_header):
    # Convert each field to 16-bit words
    fields = [
        (ip_header.version << 12) + (ip_header.ihl << 8) + ip_header.tos,
        ip_header.total_length,
        ip_header.identification,
        (ip_header.flags << 13) + ip_header.frag,
        (ip_header.ttl << 8) + ip_header.protocol,
        ip_header.src_ip,
        ip_header.dst_ip
    ]

    # Sum all the 16-bit words
    checksum = sum(fields)

    # Handle any carry over
    while checksum >> 16:
        checksum = (checksum & 0xFFFF) + (checksum >> 16)

    # Take the one's complement to get the checksum
    checksum = 0xFFFF - checksum

    return checksum

# Example IPHeader class to store IP header fields
class IPHeader:
    def __init__(self, version, ihl, tos, total_length, identification, flags, frag, ttl, protocol, src_ip, dst_ip):
        self.version = version
        self.ihl = ihl
        self.tos = tos
        self.total_length = total_length
        self.identification = identification
        self.flags = flags
        self.frag = frag
        self.ttl = ttl
        self.protocol = protocol
        self.src_ip = src_ip
        self.dst_ip = dst_ip

# Define the fields of the IP header
version = 0b0100  # Version (4 bits)
ihl = 0b0101  # IHL (4 bits)
tos = 0x00  # Type Of Service (8 bits)
total_length = 0x0000  # Total Length (16 bits) - Filled later
identification = 0x1234  # Identification (16 bits) - Random value
flags = 0b010  # Flags (3 bits) - Do not fragment
frag = 0b0000000000000  # Fragment Offset (13 bits)
ttl = 0x40  # Time To Live (8 bits) - Example: 64
protocol_name = "TCP"  # Protocol name
src_ip = "192.168.1.1"  # Source Address (32 bits)
dst_ip = "192.168.1.2"  # Destination Address (32 bits)
checksum = 0x0000  # Header Checksum (16 bits) - Filled later

# Get the protocol value
protocol = get_protocol_value(protocol_name)

# Convert IP addresses to binary
src_ip_binary = int("".join(format(int(x), '08b') for x in src_ip.split(".")), 2)
dst_ip_binary = int("".join(format(int(x), '08b') for x in dst_ip.split(".")), 2)

# Create an instance of IPHeader
ip_header = IPHeader(version, ihl, tos, total_length, identification, flags, frag, ttl, protocol, src_ip_binary, dst_ip_binary)

# Calculate the checksum
checksum = calculate_checksum(ip_header)

# Update the IP header with calculated checksum
ip_header.checksum = checksum

# Print the IP header fields
print("Version:", bin(ip_header.version))
print("IHL:", bin(ip_header.ihl))
print("TOS:", hex(ip_header.tos))
print("Total Length:", hex(ip_header.total_length))
print("Identification:", hex(ip_header.identification))
print("Flags:", bin(ip_header.flags))
print("Fragment Offset:", bin(ip_header.frag))
print("TTL:", hex(ip_header.ttl))
print("Protocol:", hex(ip_header.protocol))
print("Checksum:", hex(ip_header.checksum))
print("Source IP:", hex(ip_header.src_ip))
print("Destination IP:", hex(ip_header.dst_ip))
