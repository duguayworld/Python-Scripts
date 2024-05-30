import socket
import struct


# Function to convert ASCII MAC address to binary
def mac_to_binary(mac_address):
    return bytes.fromhex(mac_address.replace(':', ''))


# Function to convert ASCII IP address to binary
def ip_to_binary(ip_address):
    return socket.inet_aton(ip_address)


# Function to convert ASCII port number to binary (16-bit)
def port_to_binary(port):
    return struct.pack('!H', int(port))


# Function to convert ASCII Ethernet type to binary
def ethertype_to_binary(ethertype):
    return bytes.fromhex(ethertype)


# Get user input for MAC addresses, IP addresses, port numbers, and Ethernet type
dest_mac_ascii = input("Enter destination MAC address: ")
source_mac_ascii = input("Enter source MAC address: ")
source_ip_ascii = input("Enter source IP address: ")
dest_ip_ascii = input("Enter destination IP address: ")
source_port_ascii = input("Enter source port number: ")
dest_port_ascii = input("Enter destination port number: ")
ethertype_ascii = input("Enter Ethernet type: ")

# Convert ASCII inputs to binary
dest_mac = mac_to_binary(dest_mac_ascii)
source_mac = mac_to_binary(source_mac_ascii)
source_ip = ip_to_binary(source_ip_ascii)
dest_ip = ip_to_binary(dest_ip_ascii)
source_port = port_to_binary(source_port_ascii)
dest_port = port_to_binary(dest_port_ascii)
eth_type = ethertype_to_binary(ethertype_ascii)

# Create an Ethernet packet
eth_packet = struct.pack('!6s6s2s', dest_mac, source_mac, eth_type)

# Print the generated values for demonstration
print("Destination MAC address:", dest_mac)
print("Source MAC address:", source_mac)
print("Ethernet type:", eth_type)
print("Source IP address:", source_ip)
print("Destination IP address:", dest_ip)
print("Source Port:", struct.unpack('!H', source_port)[0])
print("Destination Port:", struct.unpack('!H', dest_port)[0])
