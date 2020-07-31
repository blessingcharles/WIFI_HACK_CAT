import scapy.all as scapy

def sniff(interface):
    scapy.sniff(iface=interface , prn=analyze_packets , store=False)
def analyze_packets(packet):
    packet.drop()
def start():
    iface = input("\n\nENTER THE INTERFACE : ")
    sniff(iface)


