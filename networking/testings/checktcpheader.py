# Import necessary modules
import struct

# Function to calculate checksum
def calculate_checksum(data):
    checksum = 0
    # Sum up 16-bit words
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i+1]
        checksum += word
    # Add carry-over
    while checksum >> 16:
        checksum = (checksum & 0xFFFF) + (checksum >> 16)
    # Take one's complement
    checksum = ~checksum & 0xFFFF
    return checksum

# Define source and destination IP addresses
source_ip = 0xC0A80201  # Converted from "192.168.2.1"
destination_ip = 0xC0A802C9  # Converted from "192.168.2.201"

# TCP Header
source_port = 12336  # Source Port
destination_port = 80  # Destination Port
sequence_number = 0x0000  # Sequence Number
ack_number = 0x0000  # Acknowledgement Number
data_offset = 0b0101  # Data Offset (4 bits)
reserved_flags = 0b000000010  # Reserved (3 bits) + Flags (9 bits) - SYN bit set to 1
window_size = 0xFF00  # Window Size
checksum = 0x0000  # Checksum (filled later)
urgent_pointer = 0x0000  # Urgent Pointer

# Convert values to bytes for checksum calculation
tcp_header = [
    (source_port >> 8) & 0xFF, source_port & 0xFF,
    (destination_port >> 8) & 0xFF, destination_port & 0xFF,
    (sequence_number >> 24) & 0xFF, (sequence_number >> 16) & 0xFF,
    (sequence_number >> 8) & 0xFF, sequence_number & 0xFF,
    (ack_number >> 24) & 0xFF, (ack_number >> 16) & 0xFF,
    (ack_number >> 8) & 0xFF, ack_number & 0xFF,
    ((data_offset << 4) + (reserved_flags >> 8)) & 0xFF, reserved_flags & 0xFF,
    (window_size >> 8) & 0xFF, window_size & 0xFF,
    (checksum >> 8) & 0xFF, checksum & 0xFF,
    (urgent_pointer >> 8) & 0xFF, urgent_pointer & 0xFF
]

# Calculate checksum
pseudo_header = [
    (source_ip >> 24) & 0xFF, (source_ip >> 16) & 0xFF,
    (source_ip >> 8) & 0xFF, source_ip & 0xFF,
    (destination_ip >> 24) & 0xFF, (destination_ip >> 16) & 0xFF,
    (destination_ip >> 8) & 0xFF, destination_ip & 0xFF,
    0, 6,  # Protocol (TCP)
    len(tcp_header) >> 8, len(tcp_header) & 0xFF  # TCP length
]

tcp_checksum_data = pseudo_header + tcp_header
checksum = calculate_checksum(tcp_checksum_data)
tcp_header[16] = (checksum >> 8) & 0xFF
tcp_header[17] = checksum & 0xFF

# Print TCP header
print("TCP Header:")
print("Source Port:", source_port)
print("Destination Port:", destination_port)
print("Sequence Number:", sequence_number)
print("Acknowledgment Number:", ack_number)
print("Data Offset:", data_offset)
print("Reserved Flags:", reserved_flags)
print("Window Size:", window_size)
print("Checksum:", hex(checksum))
print("Urgent Pointer:", urgent_pointer)
