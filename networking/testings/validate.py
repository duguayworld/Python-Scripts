from scapy.all import rdpcap

def validate_packet(packet):
    # Add your validation logic here
    # For example, you can check packet fields, headers, etc.
    # Return True if the packet is valid, False otherwise
    return True

def main():
    # Load the pcap file containing the packet
    pcap_file = "/home/paulgrey/PycharmProjects/packet_injector/crafted_packet.pcap"
    packets = rdpcap(pcap_file)

    if len(packets) == 0:
        print("No packets found in the pcap file.")
        return

    # Assuming you want to validate the first packet in the file
    packet_to_validate = packets[0]

    # Validate the packet
    if validate_packet(packet_to_validate):
        print("Packet validation successful.")
    else:
        print("Packet validation failed.")

if __name__ == "__main__":
    main()
