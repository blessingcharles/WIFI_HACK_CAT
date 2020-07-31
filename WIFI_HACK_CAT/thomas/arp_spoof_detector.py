import scapy.all as scapy
def get_mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast = ether/arp_req
    answered = scapy.srp(broadcast,timeout=1,verbose=False)[0]
    mac = answered[0][1].hwsrc
    return mac

def process_packets(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op ==2:
        ip = packet[scapy.ARP].psrc
        given_mac = packet[scapy.ARP].hwsrc
        org_mac = get_mac(ip)
        if given_mac != org_mac :
            print("[+]YOU ARE UNDER ARP_SPOOFING[+]")
            print(f"SPOOFED BY \n\t\t\t\t\t\t\t ip : {ip} mac : {org_mac} "*3)
            flag = int(input("\nif you want to check again press 1 orelse press 0: "))

        else :
            print("not under attack...")
            flag = int(input("if you want to check again press 1 orelse press 0: "))
        if flag:
            print("checking again.........")
            main()
        else:
            exit(0)


def main():
    scapy.sniff(iface=interface,store=False,prn=process_packets)

def start():
    global interface
    interface = input("enter your network interface [eg: wlan0 , eth0 ]: ")
    main()