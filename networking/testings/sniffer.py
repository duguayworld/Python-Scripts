from scapy.all import *

def packet_callback(packet):
    # Write the packet details to a text file
    with open("captured_packets.txt", "a") as f:
        f.write(str(packet.show(dump=True)) + '\n')

    # Check if the packet matches the specific IP and MAC address
    if (IP in packet and packet[IP].dst == "192.168.0.1") or (Ether in packet and packet[Ether].dst == "92:AA:C3:A7:2D:B1"):
        if packet.haslayer(TCP):
            print("TCP packet detected:")
            print(packet.show())
        elif packet.haslayer(UDP):
            print("UDP packet detected:")
            print(packet.show())
        elif packet.haslayer(HTTP):
            print("HTTP packet detected:")
            print(packet.show())
        elif packet.haslayer(SSL):
            print("HTTPS packet detected:")
            print(packet.show())

        # Write the packet to the pcap file
        wrpcap("captured_packets.pcap", packet, append=True)

def capture_packets(interface):
    print(f"Capturing packets on interface {interface}...")
    # Adjust the filter to capture packets for the specific IP and MAC address
    sniff(iface=interface, filter="tcp or udp or port 80 or port 67", prn=packet_callback)

if __name__ == "__main__":
    interface = "wlan0"  # Change this to the appropriate network interface
    capture_packets(interface)
