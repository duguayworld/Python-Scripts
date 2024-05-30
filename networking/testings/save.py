from scapy.all import Ether, IP, TCP, Raw, wrpcap

# Construct the packet (same as before)
ether = Ether(src="00:00:00:00:00:00", dst="00:00:00:00:00:00")
ip = IP(version=4, ihl=5, tos=0x0, len=0, id=4660, flags="DF", frag=0, ttl=64, proto=6, chksum=0xa570, src="192.168.1.1", dst="192.168.1.2")
tcp = TCP(sport=12336, dport=80, seq=0, ack=0, dataofs=5, reserved=0, flags="S", window=65280, chksum=None, urgptr=0)
payload = "Invoke-Expression -Command \"Write-Host 'Hello, World!'\""
packet = ether / ip / tcp / Raw(load=payload)

# Save the packet to a pcap file
pcap_file = "crafted_packet.pcap"
wrpcap(pcap_file, packet)

print(f"Packet saved to {pcap_file}")
